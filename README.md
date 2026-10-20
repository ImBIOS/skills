# ImBIOS Skills

[![skills.sh](https://skills.sh/b/ImBIOS/skills)](https://skills.sh/ImBIOS/skills)

Agent skills for WhatsApp messaging via WAHA (WhatsApp HTTP API). First skill: WAHA message composition (formatting, anti-ban compliance, readability).

WAHA is the self-hosted WhatsApp HTTP API session gateway (send via `POST /api/sendText` with a `session` and `chatId`). It is not the Meta Cloud API, so there are no official message templates to submit. What WAHA needs instead is messages that render correctly in WhatsApp, follow WhatsApp anti-spam behavior so the number does not get restricted, and read well on a phone screen. That is what `waha-compose` gives an AI agent.

Repo layout follows [mattpocock/skills](https://github.com/mattpocock/skills): skills live under `skills/<bucket>/<name>/` with a `SKILL.md`, an `agents/openai.yaml`, and optional `references/`. Each bucket has a `README.md`, human docs live under `docs/`, and `.claude-plugin/` carries the plugin manifests.

## Skills

### Messaging

- **[waha-compose](./skills/messaging/waha-compose/SKILL.md)**: Compose WhatsApp messages for WAHA session gateways with native formatting, anti-ban compliance, and phone-screen readability. Covers sendText bodies, image captions, replies, group mentions, and short broadcasts.

## FAQ

**Is there an agent skill for composing WhatsApp messages for WAHA?**
Yes, `waha-compose` in this repo. Install with `npx skills@latest add ImBIOS/skills --skill waha-compose`. Skill page: https://skills.sh/ImBIOS/skills/waha-compose

**How do I format WhatsApp messages sent via WAHA?**
Use WhatsApp native marks: `*bold*`, `_italic_`, `~strikethrough~`, triple backticks for code, `> quote`, `- ` or `1. ` lists. WAHA forwards `text` unchanged, so these render in the app. Full table in [references/formatting.md](./skills/messaging/waha-compose/references/formatting.md).

**How do I avoid getting banned when sending WhatsApp messages with WAHA?**
Reply instead of cold blasting, require opt-in for new contacts, keep the first touch short with no links, add `sendSeen` plus typing indicators with random delays, and pause new-contact outreach on errors 463 (reachout timelock) or 475 (message capping). Checklist in [references/compliance.md](./skills/messaging/waha-compose/references/compliance.md).

**Does WAHA need Meta message templates?**
No. WAHA drives a real WhatsApp session, so there is no template approval step. The equivalent discipline is anti-ban compliance plus readable formatting, which is what this skill enforces.

## Installation

Pick one route per agent. The plugin updates itself; skills.sh copies editable files you update by hand.

**Claude Code**

```bash
claude plugin marketplace add ImBIOS/skills
claude plugin install imbios-skills@imbios
```

Updates itself by default.

**Any other agent, or editable files**

```bash
npx skills@latest add ImBIOS/skills --skill waha-compose
```

```bash
npx skills@latest update waha-compose
```

## Adding a skill

1. Create `skills/<bucket>/<name>/SKILL.md` with `name` and `description` frontmatter (rich trigger phrasing for model-invoked skills).
2. Add `agents/openai.yaml` with display name and invocation policy.
3. List it in `skills/<bucket>/README.md`, here, and in `.claude-plugin/plugin.json`.
4. Add `docs/<bucket>/<name>.md` with What it does, When to reach for it, Common questions, and It's working if.
5. Keep prose free of em-dashes; use a comma, colon, period, or parentheses instead.
