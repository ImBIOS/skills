#!/bin/bash
# Record a tight tab demo with per-step screenshots.
# Usage: record-tab.sh <url> <out-base> [scrolls]
# Example: record-tab.sh https://forkhub.imbios.dev /tmp/demo 3
set -e
export PATH="$HOME/.bun/bin:$HOME/.local/bin:$PATH"
URL="${1:?url required}"
OUT="${2:?out base required}"
SCROLLS="${3:-3}"
WEBM="${OUT}.webm"
MP4="${OUT}.mp4"
agent-browser --session-name x-auto --args "--no-sandbox" open "$URL" >/dev/null
agent-browser --session-name x-auto --args "--no-sandbox" wait 800 >/dev/null
agent-browser --session-name x-auto --args "--no-sandbox" record start "$WEBM" --cursor --fps 30
agent-browser --session-name x-auto --args "--no-sandbox" screenshot "${OUT}-00.png"
for i in $(seq 1 "$SCROLLS"); do
  agent-browser --session-name x-auto --args "--no-sandbox" scroll down 600
  agent-browser --session-name x-auto --args "--no-sandbox" wait 700 >/dev/null
  agent-browser --session-name x-auto --args "--no-sandbox" screenshot "${OUT}-0${i}.png"
done
agent-browser --session-name x-auto --args "--no-sandbox" record stop
ffmpeg -i "$WEBM" -c:v libx264 -pix_fmt yuv420p "$MP4" -y
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 "$MP4"
ls -lh "$WEBM" "$MP4" "${OUT}"-*.png
