#!/usr/bin/env python3
"""Live domain availability via RDAP. Stdlib only.

Reads the IANA RDAP bootstrap for DNS (cached in rdap-servers.json next to
this script; refreshed when older than 7 days), queries each candidate
domain at its authoritative RDAP server, and reports TAKEN / AVAILABLE /
UNKNOWN. Registries without an IANA RDAP entry (e.g. .io, .co) fall back
to their documented RDAP or WHOIS-over-HTTP endpoints where known.

Usage:
  python3 check-domains.py --tlds com,io,co,ai,dev,app Name1 Name2

Output: one JSON line per domain: {"domain","tld","status","detail"}.
status: TAKEN | AVAILABLE | UNKNOWN. UNKNOWN is never a green light.

Rate limit: 1 req/s per registry host, one retry on 5xx/network error.
"""
import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

HERE = Path(__file__).parent
SERVERS_CACHE = HERE / "rdap-servers.json"
IANA_BOOTSTRAP = "https://data.iana.org/rdap/dns.json"
UA = {"User-Agent": "imbios-skills brand-name/1.0", "Accept": "application/json"}

# Registries with no IANA RDAP entry but a known lookup path.
# .io: NIC.io has no public RDAP; availability via WHOIS is unreliable from
# scripts, so .io reports UNKNOWN with the reason instead of guessing.
FALLBACKS = {
    "io": ("unknown-no-rdap", None),
    "co": ("rdap", "https://rdap.nic.co/rdap/domain/"),
}


def load_servers():
    if SERVERS_CACHE.exists():
        try:
            data = json.loads(SERVERS_CACHE.read_text())
            if data.get("_fetched", 0) > time.time() - 7 * 86400:
                return data["servers"]
        except (ValueError, KeyError):
            pass
    req = urllib.request.Request(IANA_BOOTSTRAP, headers=UA)
    data = json.load(urllib.request.urlopen(req, timeout=20))
    servers = {}
    for tlds, urls in data["services"]:
        for t in tlds:
            servers.setdefault(t, urls[0])
    SERVERS_CACHE.write_text(
        json.dumps({"_fetched": int(time.time()), "servers": servers})
    )
    return servers


def query(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.read(2048)
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # timeout, DNS, reset
        return -1, str(e).encode()


def check(domain, tld, servers, last_hit):
    fb = FALLBACKS.get(tld)
    if fb and fb[0] == "unknown-no-rdap":
        return "UNKNOWN", "no public RDAP for .%s; check manually" % tld
    base = servers.get(tld)
    if fb and fb[0] == "rdap":
        base = fb[1]
    if not base:
        return "UNKNOWN", "no RDAP server known for .%s" % tld
    host = base.split("/")[2]
    wait = 1.0 - (time.time() - last_hit.get(host, 0))
    if wait > 0:
        time.sleep(wait)
    url = base.rstrip("/") + "/domain/" + domain
    status, body = query(url)
    last_hit[host] = time.time()
    if status == 200:
        try:
            st = json.loads(body.decode("utf-8", "ignore") or "{}").get(
                "status", []
            )
            return "TAKEN", ",".join(st[:3]) or "registered"
        except ValueError:
            return "TAKEN", "registered"
    if status == 404:
        # Retry once: some registries 404 on transient errors.
        time.sleep(1.0)
        status2, body2 = query(url)
        last_hit[host] = time.time()
        if status2 == 404:
            return "AVAILABLE", "registry 404"
        if status2 == 200:
            return "TAKEN", "registered (retry)"
        return "UNKNOWN", "inconsistent registry response"
    if status in (429, 500, 502, 503, 504, -1):
        time.sleep(2.0)
        status2, _ = query(url)
        last_hit[host] = time.time()
        if status2 == 404:
            return "AVAILABLE", "registry 404 (retry)"
        if status2 == 200:
            return "TAKEN", "registered (retry)"
        return "UNKNOWN", "registry error %s" % status
    return "UNKNOWN", "unexpected HTTP %s" % status


def main(argv):
    tlds = ["com", "io", "co", "ai", "dev", "app"]
    names = []
    i = 0
    while i < len(argv):
        if argv[i] == "--tlds":
            tlds = [t.strip().lower() for t in argv[i + 1].split(",")]
            i += 2
        else:
            names.append(argv[i])
            i += 1
    if not names:
        print("Usage: check-domains.py [--tlds com,io,...] Name...", file=sys.stderr)
        return 2
    servers = load_servers()
    last_hit = {}
    for name in names:
        slug = "".join(c.lower() for c in name if c.isalnum())
        for tld in tlds:
            domain = "%s.%s" % (slug, tld)
            status, detail = check(domain, tld, servers, last_hit)
            print(
                json.dumps(
                    {"domain": domain, "tld": tld, "status": status,
                     "detail": detail}
                )
            )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
