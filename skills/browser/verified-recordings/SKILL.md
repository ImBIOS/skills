---
name: verified-recordings
description: Record correct demo videos with agent-browser tab capture or OCU plus ffmpeg desktop capture, verified by screenshots. Use when recording any browser tab demo, desktop demo on TigerVNC :1, or posting video to X via compose upload for forkhub, sidekick, or similar product demos.
---

# Verified Recordings

Ship only videos proven by screenshots. Screenshot every step while recording, analyze the images, iterate until the sequence matches expected, then the video is correct.

## Workflow

### 1. Prep

Run once per shell:

```bash
export PATH="$HOME/.bun/bin:$HOME/.local/bin:$PATH"
agent-browser doctor
```

Require ffmpeg plus libvpx and libx264 pass. Headless Chrome needs `--args "--no-sandbox"`. Auth with `--session-name x-auto` plus `~/.agent-browser/x-imbios.json` (600, outside repo). Copy via `--auto-connect state save` when expired. See [auth.md](references/auth.md).

### 2. Screenshot verify loop (mandatory)

Do this before any final record:

1. `open <url>`, `snapshot -i` for refs.
2. `screenshot iter-00.png`, act, `screenshot iter-01.png`, act, `screenshot iter-02.png`.
3. Read each PNG yourself, confirm distinct beats with no dead air and no unwanted nav (example: stay on forkhub.imbios.dev, do not exit to GitHub).
4. If any frame is static or off site, tighten waits and actions, repeat.
5. Methods for other targets (desktop, window, area, element crop, OCU): [screenshots.md](references/screenshots.md).

Only record the sequence that screenshots prove.

### 2b. Beat-frame video QC (mandatory for staged clips)

Screenshots prove the plan; frames prove the take. After recording, extract one still per beat (`ffmpeg -ss <beat time> -i take.mp4 -frames:v 1 beat-NN.png`), read every still yourself, and confirm: the expected state is on screen, the cursor is visible where the beat needs it, no mid-transition blur, no banner intrusion. If any still fails, the take fails: adjust and re-shoot. A video is only done when its beat frames read like a storyboard of the intent.

### 3. Tab record

Pattern (no URL in `record start` so refs stay valid, no `networkidle` inside record):

```bash
agent-browser --session-name x-auto --args "--no-sandbox" record start ./demo.webm --cursor --fps 30
agent-browser --session-name x-auto --args "--no-sandbox" click @eX
agent-browser --session-name x-auto --args "--no-sandbox" wait 700
agent-browser --session-name x-auto --args "--no-sandbox" screenshot ./v-01.png
agent-browser --session-name x-auto --args "--no-sandbox" scroll down 600
agent-browser --session-name x-auto --args "--no-sandbox" wait 700
agent-browser --session-name x-auto --args "--no-sandbox" record stop
ffmpeg -i demo.webm -c:v libx264 -pix_fmt yuv420p demo.mp4 -y
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 demo.mp4
```

Keep under 10s, 3 beats, cursor on. Details in [ffmpeg.md](references/ffmpeg.md). Cursor include/exclude plus zoom (live keys and post zoompan) in [cursor-zoom.md](references/cursor-zoom.md). Script: [scripts/record-tab.sh](scripts/record-tab.sh).

### 4. Desktop record (OCU plus ffmpeg)

OCU drives, ffmpeg records. OCU has no recorder. See [ocu-desktop.md](references/ocu-desktop.md).

```bash
DISPLAY=:1 ffmpeg -f x11grab -r 30 -s 1280x1024 -i :1.0 -c:v libx264 -pix_fmt yuv420p out.mp4
```

Confirm `:1` with `DISPLAY=:1 xdpyinfo`. Script: [scripts/record-desktop.sh](scripts/record-desktop.sh).

### 5. Post video to X

Flow in [x-upload.md](references/x-upload.md): open compose, fill textbox, `upload @eFiles demo.mp4`, wait for `Ready`, click `Post`. If video is static, delete the post, tighten, reshoot. Evidence is `ffprobe` duration plus file sizes.

## Related work

- Paralect product-demo skill: ScreenStudio style, real Playwright browser driving the real UI, cursor plus chrome plus wallpaper drawn on top, take scripts. Staged and polished; this skill stays unstaged and screenshot verified instead.
- Tyler Germain screen-recordings skill (YouTube walkthrough): keyframed smooth zooms and pans, Screen Studio look, 60fps.
- Clipy / MCPBundles: recorder MCPs aimed at bug reports, timestamped narration plus frame links.
