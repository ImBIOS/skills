#!/usr/bin/env python3
"""Live social handle screening. Stdlib only.

Checks a handle per platform by requesting the public profile URL and
reading the status: 200 means taken, 404 means likely free. Platforms
that rate-limit or wall off anonymous checks (Instagram, TikTok,
YouTube, Dribbble) report UNKNOWN instead of guessing.

Usage:
  python3 check-handles.py --platforms github,x,instagram,tiktok,youtube,dribbble handle1 handle2

Output: one JSON line per handle per platform:
  {"handle","platform","status","detail"}.
status: TAKEN | LIKELY FREE | UNKNOWN. UNKNOWN is never a green light.

Rate limit: 1 req/s per platform host. Browser User-Agent.
"""
import json
import sys
import time
import urllib.request
import urllib.error

UA = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}

PLATFORMS = {
    "github": "https://github.com/{h}",
    "x": "https://x.com/{h}",
    "instagram": "https://www.instagram.com/{h}/",
    "tiktok": "https://www.tiktok.com/@{h}",
    "youtube": "https://www.youtube.com/@{h}",
    "dribbble": "https://dribbble.com/{h}",
}

# Platforms where anonymous probing is unreliable: any non-200/404
# becomes UNKNOWN, and even 404 stays LIKELY FREE at most.
STRICT_UNKNOWN = {"instagram", "tiktok", "youtube", "dribbble"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url, host_last):
    wait = 1.0 - (time.time() - host_last.get(url.split("/")[2], 0))
    if wait > 0:
        time.sleep(wait)
    opener = urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, headers=UA)
    try:
        with opener.open(req, timeout=15) as r:
            host_last[url.split("/")[2]] = time.time()
            return r.status
    except urllib.error.HTTPError as e:
        host_last[url.split("/")[2]] = time.time()
        if e.code in (301, 302, 303, 307, 308):
            # One redirect followed manually (login walls redirect).
            loc = e.headers.get("Location", "")
            if not loc or "login" in loc or "signup" in loc:
                return "WALL"
            try:
                r2 = urllib.request.Request(loc, headers=UA)
                with opener.open(r2, timeout=15) as r:
                    return r.status
            except urllib.error.HTTPError as e2:
                return e2.code
            except Exception:
                return -1
        return e.code
    except Exception:
        host_last[url.split("/")[2]] = time.time()
        return -1


def check(handle, platform, host_last):
    url = PLATFORMS[platform].format(
        h=handle.lower().replace("_", "" if platform != "instagram" else "_")
    )
    if platform == "instagram" and "_" not in handle:
        url = PLATFORMS[platform].format(h=handle.lower())
    status = fetch(url, host_last)
    if status == 200:
        return "TAKEN", "profile resolves"
    if status == 404:
        if platform in STRICT_UNKNOWN:
            return "UNKNOWN", "anonymous check unreliable here"
        return "LIKELY FREE", "profile 404"
    if status == "WALL" or status in (429, 401, 403, -1):
        return "UNKNOWN", "rate limited or login walled (%s)" % status
    return "UNKNOWN", "unexpected HTTP %s" % status


def main(argv):
    platforms = ["github", "x", "instagram", "youtube", "tiktok", "dribbble"]
    handles = []
    i = 0
    while i < len(argv):
        if argv[i] == "--platforms":
            platforms = [p.strip().lower() for p in argv[i + 1].split(",")]
            i += 2
        else:
            handles.append(argv[i])
            i += 1
    if not handles:
        print("Usage: check-handles.py [--platforms ...] handle...", file=sys.stderr)
        return 2
    unknown = [p for p in platforms if p not in PLATFORMS]
    if unknown:
        print("Unknown platforms: %s" % ",".join(unknown), file=sys.stderr)
        return 2
    host_last = {}
    for handle in handles:
        slug = "".join(c for c in handle.lower() if c.isalnum() or c == "_")
        for platform in platforms:
            status, detail = check(slug, platform, host_last)
            print(
                json.dumps(
                    {"handle": slug, "platform": platform,
                     "status": status, "detail": detail}
                )
            )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
