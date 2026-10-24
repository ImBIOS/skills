---
name: og-image-live
description: Produce a 5 second share clip where scripted activity plays inside the card while its chrome stays fixed, as MP4 and GIF. Use when asked for a live-feeling share clip, animated product moment, or motion version of the share card.
---

# OG Image Live

Produce a 5 second clip at share card aspect where the motion comes from the product itself: new rows arriving, statuses flipping, a chart extending, notifications landing. The card chrome (headline, logo, background) stays fixed; only the embedded product region moves. Deliver MP4 plus GIF with a poster frame.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/og-image-live). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Require the static card first

Run `og-image` first if no approved static card exists. The live version keeps its headline, palette, and layout, and swaps the static UI crop for a live region.

### 2. Script one product moment

Pick exactly one loopable moment suited to the product: a couple of records landing in a list, a status pill cycling through states and back, a chart extending by a few points, a counter ticking up. Write it as a tiny JS loop inside the card HTML that returns to its start state, so the 5 second clip loops. One moment only; two moments read as noise at feed size.

### 3. Record and encode

Build the card as one HTML page at 1200x630 with the scripted region, verify with screenshots, then record per `verified-recordings` and encode both formats:

```bash
agent-browser record start ./og-live.webm --fps 30
agent-browser wait 5200
agent-browser record stop
ffmpeg -y -i og-live.webm -t 5 -c:v libx264 -pix_fmt yuv420p og-live.mp4
ffmpeg -y -i og-live.mp4 -vf "fps=15,scale=1200:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse" og-live.gif
ffmpeg -y -ss 0.5 -i og-live.mp4 -frames:v 1 og-live-poster.png
```

### 4. Verify

Check: exactly one product moment, readable at 300px wide, loop restart invisible, 5 seconds, GIF under 8MB, poster shows the resting card state. If the motion stutters or the loop jumps, fix the script timing and re-record. Never ship a screen recording of manual clicking as the live clip.

## Boundaries

Scripted product motion inside the card. For a one-time reveal animation of the card itself, use `og-image-animated`. For an honest recording of a human driving the real app, use `product-demo`. For page scrolls, use `website-scroll`.
