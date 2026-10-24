#!/usr/bin/env bash
# Capture hero sections for website-screenshot-reel using agent-browser.
# Original helper, no third party code. Requires agent-browser and ffmpeg.
# Usage: ./reel.sh --width 1440 --height 900 --scale 2 --out ./reel <url>...
set -euo pipefail

WIDTH=1440
HEIGHT=900
SCALE=2
OUT="./reel"
URLS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --width) WIDTH="$2"; shift 2 ;;
    --height) HEIGHT="$2"; shift 2 ;;
    --scale) SCALE="$2"; shift 2 ;;
    --out) OUT="$2"; shift 2 ;;
    --help) echo "Usage: $0 [--width 1440 --height 900 --scale 2 --out ./reel] <url>..."; exit 0 ;;
    *) URLS+=("$1"); shift ;;
  esac
done

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "Give at least one URL." >&2
  exit 1
fi

export PATH="$HOME/.bun/bin:$HOME/.local/bin:$PATH"
i=0
for url in "${URLS[@]}"; do
  shot=$(printf "%s-%02d.png" "$OUT" "$i")
  agent-browser open "$url"
  agent-browser set viewport "$WIDTH" "$HEIGHT" "$SCALE"
  agent-browser snapshot -i | grep -iE "dialog|banner|cookie|accept" || true
  agent-browser wait 1500
  agent-browser screenshot "$shot"
  echo "captured $shot"
  i=$((i + 1))
done
echo "Review each PNG before encoding. Encode per SKILL.md step 3."
