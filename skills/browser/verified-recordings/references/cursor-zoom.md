# Cursor and zoom

## Cursor in tab recordings

`record start` takes `--cursor`. With it, an inert overlay renders pointer plus page together (drags stay synced, hidden from snapshots, removed on stop). Without the flag, no cursor. There is no toggle mid-record.

```bash
agent-browser record start ./demo.webm --cursor --fps 30
```

## Cursor in desktop recordings

`ffmpeg -f x11grab` captures no cursor. When the pointer matters, record the tab with `--cursor` instead of the desktop. No post overlay is documented here.

## Zoom during recording

No zoom command exists. Two paths, verified:

- Headed or focused window: `press ctrl+plus` steps and `press ctrl+0` reset are captured like any interaction.
- Headless: keyboard zoom does nothing. Zoom with CSS instead, stepped for visible motion:

```bash
agent-browser eval "document.body.style.zoom = 1.15"
agent-browser wait 1000
agent-browser eval "document.body.style.zoom = 1.3"
```

## Zoom in post

`zoompan` adds a zoom move to finished mp4. Example, 3s push into center on a 1280x1024 clip:

```bash
ffmpeg -i out.mp4 -vf "zoompan=z='1+0.3*on/90':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=90:s=1280x1024:fps=30" -c:v libx264 -pix_fmt yuv420p zoom.mp4 -y
```

Verify with `ffprobe` duration plus reading frame screenshots.
