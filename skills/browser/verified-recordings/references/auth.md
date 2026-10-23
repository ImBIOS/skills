# Auth

Session file holds X login cookies. Treat as secret.

## Save (needs user Chrome approval once)

```bash
agent-browser --auto-connect state save ~/.agent-browser/x-imbios.json
chmod 600 ~/.agent-browser/x-imbios.json
agent-browser --session-name x-auto state load ~/.agent-browser/x-imbios.json
```

## Reuse (no approval needed)

```bash
agent-browser --session-name x-auto --args "--no-sandbox" open https://x.com/home
```

Unauthed headless gets `Access denied` or `ERR_HTTP_RESPONSE_CODE_FAILURE`. With loaded cookies it loads as the user.

## Rules

* Keep in `~/.agent-browser/` (600, outside repo).
* Never commit state files. They contain session tokens.
* Re-copy when X expires the cookies.
