# X upload

Compose refs change every load, so re-snapshot each run.

## Fill then upload

```bash
agent-browser --session-name x-auto --args "--no-sandbox" open https://x.com/compose/post
# snapshot -i, note textbox @eTEXT and Choose Files @eFILES and Post @ePOST
agent-browser --session-name x-auto --args "--no-sandbox" fill @eTEXT "forkhub catalog is live
one command to re-derive, verify, and PR your fork patches
no more merge hell
forkhub.imbios.dev"
agent-browser --session-name x-auto --args "--no-sandbox" upload @eFILES /tmp/demo.mp4
```

Wait for `Ready` (example: `forkhub-v3.mp4: Ready`), then:

```bash
agent-browser --session-name x-auto --args "--no-sandbox" click @ePOST
```

Confirm `Your post was sent`, capture the `/status/` URL.

## Delete a bad take

Open the status URL, click `More`, `Delete`, confirm `Delete`. Expect `Your post was deleted`. Reshoot tighter before reposting.
