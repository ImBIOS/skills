---
name: waha-compose
description: Compose WhatsApp messages for WAHA (WhatsApp HTTP API session gateway, not Meta Cloud API templates). Use when writing, rewriting, formatting, or reviewing any WAHA sendText body, sendImage caption, reply, group mention, or broadcast text for native formatting, anti-ban compliance, and readability.
---

# WAHA Compose

Write messages that render correctly in WhatsApp, respect WAHA and WhatsApp anti-spam rules, and are easy to scan on a phone screen.

This skill is for WAHA only: the self-hosted WhatsApp HTTP API where you send via `POST /api/sendText` with a `session` and `chatId`. It is not for Meta Cloud API template approval (`components[]`, utility versus marketing categories). If the task needs an official template, stop and use a WABA template skill instead.

## Workflow

### 1. Establish intent and audience

Collect: who receives this (one person, group, new contact, existing chat), why they expect it, the single action they should take, and whether they opted in. If there is no opt-in and no prior chat, the correct output is an opt-in invite (a `wa.me` link sent by SMS or another channel), not a WAHA cold message.

### 2. Draft for readability first

Write the plain text before adding any formatting. Rules live in [references/readability.md](references/readability.md). The short version: one idea per message, first message short, front-load the point, one clear ask, line breaks between blocks.

### 3. Apply native formatting

Formatting reference: [references/formatting.md](references/formatting.md). WAHA passes text through to WhatsApp, so use WhatsApp native marks:

- `*bold*` for the key fact or deadline
- `_italic_` for context or side notes, sparingly
- `~strike~` only for corrections
- triple backticks for codes or exact strings to copy
- `> quote` for replying context
- `- ` or `1. ` lists for steps or options

Bold at most two short spans per message. If everything is bold, nothing is.

### 4. Compliance pass

Checklist lives in [references/compliance.md](references/compliance.md). Blocking issues, not suggestions:

- Reply-first: WAHA sessions should reply, not cold blast. New contacts need prior opt-in.
- One short opener, no links or media in the first cold touch.
- No banned or spammy phrasing, no sensitive content, only HTTPS links, no shortener domains with bad reputation.
- Human pacing: `sendSeen`, `startTyping`, short random wait scaled to message length, `stopTyping`, then `sendText`. Random gaps between messages, no 24/7 blasting, batch with rest windows.
- Know errors `463` (reachout timelock, pause new contacts) and `475` (message capping, wait for cycle reset). Never logout or re-pair to clear them.
- Sender looks human: profile picture, name, status set.

### 5. Emit the WAHA payload

Base shape for `POST /api/sendText`:

```json
{
  "session": "default",
  "chatId": "6281234567890@c.us",
  "text": "Hi Andi, *order A-1042* has shipped.\n\nTrack it here: https://example.com/t/A-1042\n\nReply STOP to opt out."
}
```

Options:

- `reply_to`: message id being answered, keeps threads readable.
- `linkPreview`: set `false` to suppress previews on links that render badly; set `true` plus `linkPreviewHighQuality: true` when the preview matters.
- `mentions`: in groups, include both `@<number>` in text and the `chatId` in `mentions`, or `"all"` for everyone.
- `chatId` formats: `phone@c.us` for people, `id@g.us` for groups, `id@newsletter` for channels, `status@broadcast` for status.

Human-like send sequence before the text (per WAHA guidance):

1. `POST /api/sendSeen` with `session` and `chatId`
2. `POST /api/startTyping`, wait a random interval scaled to length
3. `POST /api/stopTyping`
4. `POST /api/sendText`

Image captions go through `POST /api/sendImage` with JPEG files and a short `caption` written with the same readability rules.

## Boundaries

Use this skill for message content: wording, formatting, compliance review, readability. Use a WAHA API or infra skill for sessions, webhooks, Docker, engines, or QR pairing. Use a WABA template skill for official template submission and category decisions.
