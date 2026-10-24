# website-scroll

## What it does

Scrolls a public page section by section the way a reader does and records it as MP4 plus a poster frame, using eased tweens with rests on each section. Shared primitives (sessions, verify loop, convert, X upload) live in verified-recordings.

## When to reach for it

Reach for it when showing a full landing page read-through as video. Typical triggers: "scroll reel of this page", "record the page top to bottom", "landing page read-through video".

## Common questions

**Full-page tween or section beats?** Section beats: tween to each section, rest, continue. A single full-page tween reads relentlessly.

**How are banners handled?** Snapshot for dialogs and cookie banners first and dismiss before recording, so the take starts clean at the top.

**How does this relate to the Paralect catalog?** Functional scope matches their website scroll skill (https://www.paralect.com/skills/website-scroll). This is an original implementation built on agent-browser, not affiliated, with no shared text or code.

## It's working if

First, middle, and last frames show hero top, mid content, and footer; the poster shows the hero; and the take starts at the very top with no static frames.
