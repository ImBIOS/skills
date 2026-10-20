# ImBIOS Skills

[![skills.sh](https://skills.sh/b/ImBIOS/skills)](https://skills.sh/ImBIOS/skills)

Agent skills maintained by ImBIOS. First skill: WAHA message composition.

Repo layout follows [mattpocock/skills](https://github.com/mattpocock/skills): skills live under `skills/<bucket>/<name>/` with a `SKILL.md`, an `agents/openai.yaml`, and optional `references/`. Each bucket has a `README.md`, human docs live under `docs/`, and `.claude-plugin/` carries the plugin manifests.

## Skills

### Messaging

- **[waha-compose](./skills/messaging/waha-compose/SKILL.md)**: Compose WhatsApp messages for WAHA session gateways with native formatting, anti-ban compliance, and phone-screen readability.

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
