---
name: website-scroll
description: Record a top-to-bottom scroll reel of any public page with poster frame. Use when showing a full landing page read-through as MP4 plus poster, for launch posts or page reviews.
---

# Website Scroll

Scroll a page top to bottom the way a reader does, as MP4 plus poster. Shared primitives (sessions, verify loop, convert, X upload) live in verified-recordings.

## Pattern (proven live)

```bash
agent-browser open <url>
agent-browser eval "document.body.scrollHeight"   # total px, plan flicks
agent-browser snapshot -i | grep -iE "dialog|banner|cookie|accept"  # dismiss if present
agent-browser eval "window.scrollTo(0,0)"          # verify top with screenshot
agent-browser record start ./scroll.webm --fps 30
agent-browser wait 1000                            # settle: capture starts late, first scroll would be missed
for i in $(seq 1 11); do agent-browser scroll down 700; agent-browser wait 400; done
agent-browser record stop
ffmpeg -y -i scroll.webm -c:v libx264 -pix_fmt yuv420p scroll.mp4
ffmpeg -y -ss 0.5 -i scroll.mp4 -frames:v 1 poster.png
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 scroll.mp4
```

700px flicks with 400ms waits read naturally; 11 flicks covered 7431px. No cursor flag for a clean reel. No `networkidle` inside record.

## Verify

Read first, middle, last frames: hero top, mid content, footer. Poster must show the hero. If the take starts mid page, the settle wait was missing. Reshoot, never ship static frames.
