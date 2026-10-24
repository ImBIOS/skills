---
name: og-image-animated
description: Add motion to the approved static share card (headline entrance, UI settling into place) and export MP4 and GIF. Use when asked to animate a share card, make an OG video, or produce a looping social preview clip.
---

# OG Image Animated

Animate the static card from `og-image` into a 2 to 2.5 second reveal: headline drops in, product UI rises into place, one beat of rest, loop cleanly. Deliver MP4 plus GIF at share card aspect.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/og-image-animated). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Require the static card first

Run `og-image` first if no approved static card exists. The animation reuses its composition, headline, and assets, so the animated version is recognizably the same card.

### 2. Build the timeline

Default 2.4s at 30fps, three beats, all easing eased-out with full rest on the end frame so the loop point is invisible:

- 0.0 to 0.6s: background settles, headline drops in with a short overshoot.
- 0.5 to 1.4s: UI capture rises and fades into place.
- 1.4 to 2.4s: full card holds still (this hold is what loops and what feeds validate as the poster).

Accept a custom timing only if the caller gives one. Keep it under 3 seconds either way.

### 3. Render

Implement as one HTML page with CSS animations at 1200x630, then record with the `verified-recordings` pattern (screenshot verify first, record the tab, convert):

```bash
agent-browser record start ./og-anim.webm --fps 30
# play the animation once the recording settles, then hold
agent-browser record stop
ffmpeg -y -i og-anim.webm -c:v libx264 -pix_fmt yuv420p og-animated.mp4
ffmpeg -y -i og-animated.mp4 -vf "fps=15,scale=1200:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse" og-animated.gif
ffmpeg -y -ss 2.0 -i og-animated.mp4 -frames:v 1 og-animated-poster.png
```

Pure CSS animation keeps every frame deterministic, so the take records identically each run.

### 4. Verify

Check: total under 3s, first frame readable, last frame matches the static card, loop restart invisible, GIF under 5MB, MP4 plays as H264 yuv420p. Re-record on any animation jank, never ship a partial take.

## Boundaries

Motion applied to the static card only. For a card where the product itself moves (new items arriving, statuses changing), use `og-image-live`. For full page scroll recordings, use `website-scroll`.
