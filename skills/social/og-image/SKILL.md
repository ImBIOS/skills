---
name: og-image
description: Compose the static OpenGraph link preview for a product out of screenshots of its actual UI, then wire up the meta tags. Use when asked to create, fix, or preview a link share card, og:image, Twitter card, or social preview.
---

# OG Image

Produce a 1200x630 share card composed from the product's real UI (screenshot the running app, never redraw it from memory), plus a headline, and wire it into the site's meta tags. The card must survive small sizes: legible at 300px wide, since that is how it appears in feeds.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/og-image). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Optional: a headline to use verbatim (otherwise derive the pitch from the homepage hero), and which page the card is for if not the site-wide one. Read the repo directly: routes, existing meta tags, brand color, logo file.

### 2. Capture the real interface

Screenshot the running app or production page at 2x with banners and overlays dismissed (see `website-scroll` tidy habits and `verified-recordings` screenshot loop). Crop to the most recognizable UI region. Never fabricate a UI in an image model and call it the product.

### 3. Compose the card

One HTML file at exactly 1200x630, then screenshot it at 2x for the PNG. Rules:

- Left: headline (5 to 8 words), optional one line subhead, logo or wordmark.
- Right or behind: the real UI capture, cropped hard, at an angle only if text stays legible.
- Background: brand color or dark neutral, subtle texture at most. Contrast AAA for the headline.
- Text occupies at most 40 percent of the area. No small print, no URLs on the card.
- Type: Inter first (local `@font-face` when provided; system stack fallback). No emoji anywhere on the card.

### 4. Wire the meta tags

Set on the target route (absolute URLs, card file served from the site):

```html
<meta property="og:image" content="https://example.com/og/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="https://example.com/og/og-image.png" />
```

### 5. Verify

Check the PNG at full size and at 300px wide, confirm headline legibility in both, confirm file under 1MB, fetch the route and confirm tags resolve to absolute URLs, and run one social card validator or local preview. Fix and re-shoot until all pass.

## Boundaries

Static card only. For a short animated reveal of this card, use `og-image-animated`. For a card with live product motion inside, use `og-image-live`. For slideshows of page screenshots, use `website-screenshot-reel`.
