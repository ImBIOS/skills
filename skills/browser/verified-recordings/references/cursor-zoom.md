# Cursor and zoom

## Cursor in tab recordings

`record start` takes `--cursor`. With it, an inert overlay renders pointer plus page together (drags stay synced, hidden from snapshots, removed on stop). Without the flag, no cursor. There is no toggle mid-record.

```bash
agent-browser record start ./demo.webm --cursor --fps 30
```

## Cursor in desktop recordings

`ffmpeg -f x11grab` captures no cursor. When the pointer matters, record the tab with `--cursor` instead of the desktop. No post overlay is documented here.

## Zoom during recording

No zoom command exists. Two paths, both verified live:

- Smooth animated zoom (recommended): CSS transform with a transition, captured at 30fps. Verified frames show the zoom mid flight plus cursor plus scroll in one 2.6s take:

```bash
agent-browser eval "document.body.style.transition='transform 1.2s ease-in-out'; document.body.style.transformOrigin='50% 35%'; document.body.style.transform='scale(1.4)'"
agent-browser wait 1500
```

Reset with transition none plus transform none plus zoom 1 before the next take.

- Headed or focused window only: `press ctrl+plus` steps and `press ctrl+0` reset. Does nothing headless.

## Zoom in post

`zoompan` adds a zoom move to finished mp4. Example, 3s push into center on a 1280x1024 clip:

```bash
ffmpeg -i out.mp4 -vf "zoompan=z='1+0.3*on/90':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=90:s=1280x1024:fps=30" -c:v libx264 -pix_fmt yuv420p zoom.mp4 -y
```

Verify with `ffprobe` duration plus reading frame screenshots.
