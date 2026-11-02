---
name: brand-name
description: Ideate a product name from the brief, then screen each candidate with live domain and social handle checks. Use when naming a product, company, or feature, or when asked for available domains, handles, naming options, or brand-name ideas with proof they can be registered.
---

# Brand Name

Generate name candidates from the product brief, then verify each one against reality: live RDAP domain checks across extensions and live handle checks across social platforms. A name without proof of availability is a suggestion; this skill delivers names with receipts.

Original skill. No Paralect counterpart exists; this fills the gap before `saas-logo` in the brand pipeline.

## Workflow

### 1. Collect inputs

Need: product description (what it is, verb users perform, audience), naming constraints (tone, length, must-avoid words, required TLD if any). Optional: seed words, competitor names to differ from, preferred extensions (default: com, io, co, ai, dev, app), platforms to check (default: GitHub, X, Instagram, YouTube, TikTok, Dribbble).

### 2. Generate candidates

Produce 12 to 20 candidates across at least 4 construction methods (never one method for the whole list):

1. Compound: two product words fused or clipped (Northwind, Fieldkit).
2. Evocative: mood or outcome word adjacent to the category (Beacon, Lantern).
3. Invented: pronounceable coinage from product syllables (Meridian, Cadence).
4. Verb-derived: the user action nominalized (Pulse from beat, Relay from pass on).
5. Shortener: clipped or suffixed form (Tally, Meterline).

Each candidate: 4 to 12 characters, pronounceable on first read, no hyphens, no numbers, spellable after hearing once. Drop lookalikes of top-1000 brands and of direct competitors before screening.

### 3. Screen domains live

Use `scripts/check-domains.py` (stdlib only, IANA RDAP bootstrap cached in `rdap-servers.json`, per-TLD fallbacks for registries without RDAP such as .io and .co). It reports TAKEN (RDAP 200 with registration status), AVAILABLE (registry 404), or UNKNOWN (timeout, rate limit, no RDAP path) per domain. Never present UNKNOWN as available. Rate limit: 1 request per second per registry, one retry on 5xx.

```
python3 scripts/check-domains.py --tlds com,io,co,ai,dev,app Meridian Beacon Relay
```

### 4. Screen handles live

Use `scripts/check-handles.py`. Method per platform: GitHub and X return 404 for free names (GET the profile URL, follow one redirect at most, accept 200 as taken and 404 as likely free). Instagram, TikTok, YouTube, Dribbble are checked best-effort the same way, but all three rate-limit aggressively: any 429 or login wall becomes UNKNOWN, never a verdict. Label each handle TAKEN, LIKELY FREE, or UNKNOWN with the reason. One request per second, browser User-Agent.

### 5. Deliver the shortlist

One HTML or markdown report: the top 5 names ranked, each with its method, the domain matrix (extension by status), the handle matrix (platform by status), and the recommended first pick with reasoning (shortest clean .com or the required TLD, plus most handles free). Candidates that fail everywhere are listed once at the bottom as rejected, not hidden. UNKNOWN-heavy names are flagged for manual re-check, never recommended.

## Verify

Re-run both scripts on the shortlist before delivering. Confirm: every TAKEN claim has an RDAP 200 or profile 200 behind it, every AVAILABLE domain has a registry 404, no UNKNOWN is presented as a verdict, report shows at most the top 5 plus rejects. Read the report yourself before handing it over.

## Boundaries

Screening only, not legal clearance: RDAP proves registration status, not trademark safety; recommend a trademark search before filing. For the mark and lockups of the chosen name, call `saas-logo`. For share cards and pages under the new name, use `og-image` and `landing-page`.
