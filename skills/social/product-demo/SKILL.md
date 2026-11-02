---
name: product-demo
description: Record a 10 to 40 second polished demo of the running app (live UI in a staged frame with a guided cursor) as MP4 with a poster frame. Use when asked to record a product tour, feature demo, launch clip, or ScreenStudio-style app video.
---

# Product Demo

Record the real app driven for real: a browser on the local running instance, presented in a rounded frame over a soft gradient backdrop, with a smooth guided cursor that moves through one scripted flow. 10 to 40 seconds, square 1080x1080 by default, MP4 plus poster frame.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/product-demo). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: the one idea (page, modal, or flow plus what the cursor does in it) and the way in (local URL, plus demo credentials via environment for apps behind login; credentials never go into the take file). Optional: shape (default square 1080x1080, wide 1600x900, mobile 900x1600).

### 2. Write the take file

A take is a short ordered list of beats, 3 to 6 total: hover, click, type, wait, assert. Drive the real cursor through the real browser (see step 3); drawn or synthetic cursors are not used. Example shape:

```
1. Open <url>, settle, assert hero visible.
2. Hover primary CTA, click, assert modal open.
3. Type demo input, submit, assert success state.
4. Hold 1.5s on the end state for the poster.
```

Screenshot verify every beat with `verified-recordings` before recording: each PNG distinct, no dead air, no unwanted nav. Only the proven sequence gets recorded.

### 3. Stage and record

Framing is a presentation layer over the real UI: the app sits in a rounded window centered over a soft gradient backdrop (two brand-tinted radial glows on dark, never a flat void). Record with the real cursor flag on so the pointer behaves like a user's: hover states fire, buttons show their pressed state, text fields show focus rings, and the cursor shape changes over interactive elements. Drawn or injected cursors are rejected because they cannot trigger these states. Position from measured element boxes immediately before acting, then record the tab per `verified-recordings` (no URL in record start, no networkidle inside record), then convert and poster:

```bash
agent-browser record start ./demo.webm --cursor --fps 30
# play the verified beats
agent-browser record stop
ffmpeg -y -i demo.webm -c:v libx264 -pix_fmt yuv420p demo.mp4
ffmpeg -y -ss 1.0 -i demo.mp4 -frames:v 1 demo-poster.png
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 demo.mp4
```

Keep 10 to 40 seconds. The cursor must be the real one with its flag on: hover states fire, pressed states show, focus rings appear, and the pointer changes shape over interactive elements. Beat stills must show the real cursor on target at every click; a take where clicks land away from the cursor fails. The demo app itself must meet the design-skill bar: real data, icons in buttons, populated chrome, no empty regions. Build the demo app with the same skill that builds the product screen (`saas-dashboard` for console UIs, `landing-page` for marketing pages) instead of hand-rolling a one-off page, so its quality matches.

### 4. Verify

Read first, middle, last frames: entry state, mid flow action, resting end state matching the poster. If any frame is static, off site, or mid transition, tighten waits and actions and re-shoot. Never ship an unverified take.

## Boundaries

Polished demo of the real running app. For unstyled correctness-first captures, use `verified-recordings` directly. For full page scroll reads, use `website-scroll`. For scripted motion inside a share card rather than a real app session, use `og-image-live`.
