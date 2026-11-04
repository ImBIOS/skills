---
name: website-screenshot-reel
description: Capture hero sections for a list of URLs and cut them into a short slideshow as GIF or MP4. Use when asked to make a screenshot reel, hero slideshow, competitor hero comparison, or multi-site showcase clip.
---

# Website Screenshot Reel

Purpose: a crisp still slideshow of hero sections for comparing or showcasing sites (competitor scan, inspiration board, launch post). Still frames with quick crossfades; no camera motion, no zoom. Motion would fight the purpose, which is reading each hero.

Capture the hero section of each given URL at 2x with consent dialogs and popups dismissed, then cut them into a short slideshow (each hero held ~1.2s with a 0.25s crossfade) as MP4 plus GIF.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/website-screenshot-reel). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: the URL list (3 to 8 works best) plus output format (MP4, GIF, or both). Public pages only; pages behind login capture their login screen, so confirm that is acceptable before proceeding.

### 2. Capture each hero

For each URL, open at 1440x900 with deviceScaleFactor 2, dismiss consent dialogs and popups (click accept inside the notice only, hide the rest), wait for fonts and hero images, screenshot the first viewport only. Save as `reel-00.png`, `reel-01.png`, and so on. Helper script [scripts/reel.sh](scripts/reel.sh) drives this loop with agent-browser; read it before running.

```bash
./scripts/reel.sh --width 1440 --height 900 --out ./reel "https://a.example" "https://b.example"
```

Review every capture yourself: hero fully rendered, no banner visible, no blank font flash. Re-shoot failures individually.

### 3. Encode the slideshow

Hold 1.2s per hero with 0.25s crossfades, 1280 wide output. No zoom, pan, or Ken Burns drift: frames stay perfectly still so text stays readable and heroes can be compared frame to frame.

```bash
ffmpeg -y -framerate 1/1.2 -i reel-%02d.png -vf "scale=1280:-2" -c:v libx264 -pix_fmt yuv420p reel.mp4
ffmpeg -y -i reel.mp4 -vf "fps=12,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=256[p];[s1][p]paletteuse" reel.gif
```

### 4. Verify

Check: every URL appears once in order, no banner in any frame, text crisp at full size, GIF under 8MB, MP4 H264 yuv420p. Drop or re-shoot any hero that fails rather than shipping it.

## Boundaries

Hero-only slideshow of given URLs. For scrolling a full page top to bottom, use `website-scroll`. For recording interaction with a running app, use `product-demo` or `verified-recordings`.
