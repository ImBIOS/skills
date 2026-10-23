# OCU desktop

This host runs TigerVNC `:1` with Xfce at 1280x1024. The shell often has empty `DISPLAY`, but `:1` exists:

```bash
DISPLAY=:1 xdpyinfo | head
ls /tmp/.X11-unix/
```

## Drive with OCU

Use Computer Use tools: `list_apps`, `get_app_state`, click, type. It controls apps but has no recorder.

Verify desktop apps first:

```bash
# via execute: open-computer-use.list_apps
```

Expect Chrome, xfce4-panel, xfdesktop, xfwm4.

## Record with ffmpeg

Pair OCU control with x11grab capture:

```bash
DISPLAY=:1 ffmpeg -f x11grab -r 30 -s 1280x1024 -i :1.0 -c:v libx264 -pix_fmt yuv420p out.mp4
```

Stop with `q` or `timeout 8` for an 8s take. Check output with `ffprobe` and by reading screenshots taken during the run.
