# waha-compose

## What it does

Turns a messaging intent into a WAHA-ready WhatsApp message: plain draft, native formatting pass, anti-ban compliance check, and the exact `POST /api/sendText` payload (plus `sendSeen` and typing sequence, `reply_to`, `linkPreview`, and `mentions` where they apply). Covers text, image captions, replies, group mentions, and short broadcasts. WAHA only, not Meta Cloud API templates.

## When to reach for it

Reach for it when you are writing, rewriting, or reviewing any message that leaves through a WAHA session gateway and you care about rendering, restriction risk, or scanability. Typical triggers: "draft this WA message", "rewrite for WhatsApp", "is this WAHA-safe", "format this broadcast", "why did WAHA return 463 or 475".

## Common questions

**Does this submit Meta templates?** No. WAHA has no template review; the risk is session restriction, so the skill enforces reply-first behavior, opt-in, human pacing, and the 463 and 475 playbooks.

**What formatting works?** WhatsApp native marks (`*bold*`, `_italic_`, `~strike~`, code ticks, `> quote`, `- ` and `1. ` lists) plus WAHA fields like `linkPreview` and `mentions`. Full table in `references/formatting.md`.

**How long should a message be?** Opener under 200 characters, one idea and one ask per message, break after 4 to 6 lines. Patterns in `references/readability.md`.

**What does the compliance pass check?** Opt-in, short link-free first touch, labeled HTTPS links, opt-out line on promo, sender profile completeness, and human-like send pacing. Checklist in `references/compliance.md`.

## It's working if

Messages render with at most two bold spans, links carry labels and correct preview flags, first touches are short and link-free, promo sends include an opt-out, and every send follows the seen plus typing sequence with randomized gaps. Restriction errors map to pausing new-contact outreach, never to session restarts.
