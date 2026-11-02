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

Produce exactly 25 names: 5 product briefs (different categories, e.g. fintech, AI devtool, wellness, travel, developer SaaS), 5 names per brief, generated fresh per brief (never one generation reused across briefs). Methods across at least 4 construction types per brief:

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

Deliver 5 product briefs, each with its own 5-name shortlist (25 names total). Structure every name as product name plus its best available domain plus verified-free handles, and require at least 1 AVAILABLE domain per name: names need not be identical across slots (industry standard is prefix/suffix variants like get, use, try, join, hey, hq, app, labs when the exact .com is taken, e.g. useemberline.com for Emberline). Handle variants follow the same rule (get/try/use prefixes, app/hq suffixes).

Recommend every example only with handles VERIFIED free on GitHub and X (LIKELY FREE via script, re-run at delivery time). Platforms the script cannot verify (Instagram, TikTok, YouTube, Dribbble rate walls) are analyzed only where checkable: skip unknowns silently instead of listing them as caveats. Rejected also-rans go in one line at the bottom. State the first pick with reasoning (shortest clean domain plus most verified handles).

## Verify

Re-run both scripts on the shortlist before delivering. Confirm: every recommended name has at least 1 AVAILABLE domain and verified-free GitHub + X handles, every TAKEN claim has an RDAP 200 or profile 200 behind it, every AVAILABLE domain has a registry 404, report shows 5 briefs with 5 names each. Read the report yourself before handing it over.

## Boundaries

Screening only, not legal clearance: RDAP proves registration status, not trademark safety; recommend a trademark search before filing. For the mark and lockups of the chosen name, call `saas-logo`. For share cards and pages under the new name, use `og-image` and `landing-page`.
