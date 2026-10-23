# verified-recordings

## What it does

Turns a demo intent into a proven short video: screenshot verified beats, agent-browser tab capture or OCU plus ffmpeg desktop capture on TigerVNC :1, webm to mp4 conversion, and X compose upload with Ready check. Covers forkhub style product tours that stay on site under 10 seconds.

## When to reach for it

Reach for it when recording, re-shooting, or reviewing any tab demo or desktop demo where correctness matters, or when posting video through X compose. Typical triggers: "record this demo", "video is static, iterate it", "screenshot verify the recording", "post this mp4 to X", "desktop capture on :1".

## Common questions

**Tab or desktop?** Tab for web product pages with agent-browser record. Desktop for native apps or terminal plus browser mixes with OCU driving and ffmpeg x11grab on :1. OCU has no recorder.

**How do I know the video is correct?** Read the per-step screenshots yourself. If the PNG sequence shows distinct on site beats with no dead air, the video matches. If not, tighten waits and actions and repeat.

**What breaks recordings?** Missing PATH entries, missing ffmpeg codecs, `networkidle` inside record (bloats 8s to 30s), stale refs after nav, and unauthed headless X (use x-auto session with loaded cookies).

**How does X upload work?** Fill textbox, upload mp4 via Choose Files, wait for Ready, click Post, capture status URL. Delete bad takes via More then Delete.

## It's working if

Videos run under 10 seconds with 3 visible beats, screenshots match the video frames, mp4 plays as H264 yuv420p, X shows Ready before Post and Your post was sent after, and bad takes are deleted before reposting.
