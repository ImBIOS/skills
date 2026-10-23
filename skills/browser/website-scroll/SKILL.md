---
name: website-scroll
description: Record a top-to-bottom scroll reel of any public page with poster frame. Use when showing a full landing page read-through as MP4 plus poster, for launch posts or page reviews.
---

# Website Scroll

Scroll a page section by section the way a reader does, as MP4 plus poster. Shared primitives (sessions, verify loop, convert, X upload) live in verified-recordings.

## Pattern (proven live)

Eased tween per section with a rest on each, paced to page height. Beats read; glides connect:

```bash
agent-browser open <url>
agent-browser eval "JSON.stringify({h: document.body.scrollHeight, secs: Array.from(document.querySelectorAll('h2')).map(e => [Math.round(e.getBoundingClientRect().top + scrollY), (e.innerText||'').trim().slice(0,34)])})"
agent-browser snapshot -i | grep -iE "dialog|banner|cookie|accept"  # dismiss if present
agent-browser eval "window.scrollTo(0,0)"          # verify top with screenshot
agent-browser eval "window.__tween = (y1, D) => { const y0 = scrollY, t0 = performance.now(); const step = (t) => { const k = Math.min(1, (t - t0) / D), e = k < .5 ? 4*k*k*k : 1 - Math.pow(-2*k+2,3)/2; scrollTo(0, y0 + (y1 - y0) * e); if (k < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }"
agent-browser record start ./scroll.webm --fps 30
agent-browser wait 800                              # settle: capture starts late
agent-browser eval "window.__tween(1500, 900)"; agent-browser wait 1100
agent-browser eval "window.__tween(2400, 900)"; agent-browser wait 1100
agent-browser eval "window.__tween(5000, 1000)"; agent-browser wait 1100
agent-browser eval "window.__tween(6582, 1000)"; agent-browser wait 1200
agent-browser record stop
ffmpeg -y -i scroll.webm -c:v libx264 -pix_fmt yuv420p scroll.mp4
ffmpeg -y -ss 0.5 -i scroll.mp4 -frames:v 1 poster.png
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 scroll.mp4
```

Pick tween targets from the h2 map so each rest lands on a section. Scale durations plus rests to budget. Single full-page tween (no rests) works but reads relentlessly; section beats match the Paralect clipwing/linear rhythm. No cursor flag for a clean reel. No `networkidle` inside record.

## Verify

Read first, middle, last frames: hero top, mid content, footer. Poster must show the hero. If the take starts mid page, the settle wait was missing. Reshoot, never ship static frames.
