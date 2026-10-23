# Screenshots

Every method below was used live on TigerVNC `:1` (shell `DISPLAY` often empty, `:1` exists). Pick by target, then verify each file (`ls -la`, `file`, read it yourself). Blank-page guard: a full-page PNG under ~50KB means the wrong tab.

## Viewport (exact)

`agent-browser screenshot` matches `snapshot`/`get box` coordinates 1:1:

```bash
agent-browser --args "--no-sandbox" screenshot ./view.png
agent-browser get box @e10
```

## Element crop

Crop the viewport PNG, no desktop coordinate mapping needed:

```bash
ffmpeg -y -v error -i view.png -vf "crop=333:90:462:590" signin-crop.png
```

Get `x:y:w:h` from `get box @eRef`, add padding, keep inside viewport bounds (1257x849 here).

## Whole desktop

```bash
DISPLAY=:1 scrot /tmp/opencode/desktop.png
```

## Active window only

Focus first (OCU click on the window), then:

```bash
DISPLAY=:1 xfce4-screenshooter -w -s /tmp/opencode/window.png
```

`scrot -u` also captures the focused window. Confirmed 1259x994 window-only PNG this way.

## Fixed area

```bash
DISPLAY=:1 scrot -a X,Y,W,H /tmp/opencode/area.png
```

Desktop coords equal window position plus viewport box. Prefer the ffmpeg crop above, it skips the mapping.

## OCU window capture

`get_app_state` returns the app window screenshot inline plus a11y tree. It saves no file. For files, focus via OCU then use the window/desktop methods above.

## Tab targeting

`tab list` first. Switch with the tab id, `get url` to confirm (never shoot `about:blank`), `wait 600-800` for settle. Never `wait --load networkidle` inside record.
