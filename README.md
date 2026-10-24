# ImBIOS Skills

[![skills.sh](https://skills.sh/b/ImBIOS/skills)](https://skills.sh/ImBIOS/skills)

Agent skills for WhatsApp messaging via WAHA (WhatsApp HTTP API) and verified browser demo recordings (agent-browser tab capture, OCU desktop capture, X video posts).

WAHA is the self-hosted WhatsApp HTTP API session gateway (send via `POST /api/sendText` with a `session` and `chatId`). It is not the Meta Cloud API, so there are no official message templates to submit. What WAHA needs instead is messages that render correctly in WhatsApp, follow WhatsApp anti-spam behavior so the number does not get restricted, and read well on a phone screen. That is what `waha-compose` gives an AI agent.

Repo layout follows [mattpocock/skills](https://github.com/mattpocock/skills): skills live under `skills/<bucket>/<name>/` with a `SKILL.md`, an `agents/openai.yaml`, and optional `references/`. Each bucket has a `README.md`, human docs live under `docs/`, and `.claude-plugin/` carries the plugin manifests.

## Skills

### Messaging

- **[waha-compose](./skills/messaging/waha-compose/SKILL.md)**: Compose WhatsApp messages for WAHA session gateways with native formatting, anti-ban compliance, and phone-screen readability. Covers sendText bodies, image captions, replies, group mentions, and short broadcasts.

### Browser

- **[verified-recordings](./skills/browser/verified-recordings/SKILL.md)**: Record correct demo videos with agent-browser tab capture or OCU plus ffmpeg desktop capture, verified by screenshots. Covers tab demos, TigerVNC :1 desktop, and X compose video upload.
- **[website-scroll](./skills/browser/website-scroll/SKILL.md)**: Record a top-to-bottom scroll reel of any public page with poster frame.

### Design

- **[landing-page](./skills/design/landing-page/SKILL.md)**: Generate a polished hero landing page with a layered product visual and working demo as a single self-contained HTML file.
- **[saas-dashboard](./skills/design/saas-dashboard/SKILL.md)**: Generate a standard SaaS console (workspace sidebar, breadcrumbs, KPIs, chart, searchable and sortable table with row actions) as a single HTML file.
- **[bento-features](./skills/design/bento-features/SKILL.md)**: Generate an HTML bento grid of glow-finished cards where every cell is a working miniature of one feature.
- **[saas-logo](./skills/design/saas-logo/SKILL.md)**: Design flat geometric logo concepts in SVG and export the pick as transparent mark plus app-icon PNGs.
- **[low-res-mockup](./skills/design/low-res-mockup/SKILL.md)**: Generate a stripped-back skeleton wireframe of a screen before copy and visuals exist.

### Social

- **[og-image](./skills/social/og-image/SKILL.md)**: Generate the static 1200x630 share card from the real product UI and wire its meta tags.
- **[og-image-animated](./skills/social/og-image-animated/SKILL.md)**: Turn the static share card into a short looping reveal as MP4 and GIF.
- **[og-image-live](./skills/social/og-image-live/SKILL.md)**: Make a 5 second share clip with scripted product motion inside the card.
- **[website-screenshot-reel](./skills/social/website-screenshot-reel/SKILL.md)**: Turn a list of URLs into a crisp hero slideshow as MP4 and GIF.
- **[product-demo](./skills/social/product-demo/SKILL.md)**: Record a polished guided demo of the running app as MP4 with a poster frame.

### Content

- **[article-image](./skills/content/article-image/SKILL.md)**: Turn a paragraph into the blog illustration it runs with, in a chosen house style.

## Paralect catalog parity and license note

The design, social, and content buckets above cover the same use cases as the Paralect skills catalog (https://www.paralect.com/skills): landing page, SaaS dashboard, bento features, SaaS logo, low res mockup, OpenGraph image, animated and live OG variants, screenshot reel, website scroll, product demo, and blog post image with its style variants. Paralect publishes no license grant for its skill text or scripts (site footer: 2026 Paralect, Inc, all rights default reserved), so every skill here is an original clean-room implementation: same functional scope, our own words, our own scripts, no copied prompts or code. Each skill page links back to the corresponding Paralect page for attribution. This repo is not affiliated with Paralect.

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
