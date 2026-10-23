# ffmpeg

## Check

```bash
agent-browser doctor
```

Need `ffmpeg` plus `libvpx (.webm)` and `libx264 (.mp4)`. Install on Ubuntu:

```bash
sudo apt install -y ffmpeg
```

## Convert for X

X prefers mp4 (H264, yuv420p):

```bash
ffmpeg -i demo.webm -c:v libx264 -pix_fmt yuv420p demo.mp4 -y
```

## Verify

```bash
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 demo.mp4
ls -lh demo.webm demo.mp4
```

Target under 10s for a demo beat set. If 30s with static frames, waits bloated the record. Remove `wait --load networkidle` inside record, use fixed `wait 600-800`, keep 3 visible actions.
