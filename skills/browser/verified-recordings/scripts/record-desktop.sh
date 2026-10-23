#!/bin/bash
# Record full desktop :1 with ffmpeg while OCU drives.
# Usage: record-desktop.sh <out-mp4> <seconds>
# Example: record-desktop.sh /tmp/desktop.mp4 8
set -e
OUT="${1:?out mp4 required}"
SECS="${2:-8}"
DISPLAY=:1 ffmpeg -f x11grab -r 30 -s 1280x1024 -i :1.0 -t "$SECS" -c:v libx264 -pix_fmt yuv420p "$OUT" -y
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUT"
ls -lh "$OUT"
