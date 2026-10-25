---
name: bento-features
description: Build a bento-style feature overview in HTML where each tile contains a small live mock demonstrating that feature. Use when asked to show a feature overview, bento grid, or features section where each tile demonstrates the feature instead of describing it.
---

# Bento Features

Produce one self-contained HTML file: a bento grid (mixed large and small cells) where each cell contains a miniature working mockup of one feature (toggle that flips, mini chart, fake inbox row, progress ring, kanban snippet), plus a one line caption per cell. The grid as a whole reads as the product at a glance.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/bento-features). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: product description, or a list of feature names plus what each does. Six features make the best grid (one hero cell, two wide cells, three small cells). If more arrive, group them; if fewer, split the richest one into two aspects.

Write every headline, caption, and miniature label from the input brief in your own words. References inform composition only; their words are never reused.

### 2. Assign cells

Give each feature a cell size by demo value: the most visual feature gets the double cell, status or metric features get small cells, workflow features get wide cells. Each cell gets: a mockup (the working miniature), a 3 to 6 word label, and one line of caption. No cell may contain only text.

### 3. Write the file

Single file, CSS grid, one `<style>` block, one small `<script>` block. Rules:

- Type: Inter first (local `@font-face` when provided; system stack fallback), semibold cell titles, small quiet captions.
- Card finish: each cell carries a soft radial light, but the anchor varies by size class and never repeats uniformly: small cells anchor top-right, hero and large cells anchor top-center, wide cells anchor top-left, with slight intensity variation. Miniatures sit layered against that light: either in front of it (slightly translucent surfaces catching the glow) or set back so the light washes over them. Flat opaque cards with no light are rejected.
- Grid rhythm: deliberately varied spans, never a uniform table, and never a mechanical big-small-big-small alternation. Compose asymmetric mosaics: two smalls stacked, a tall 1x2 against wides, an offset hero. Hero cell spans 2x2, mixed wide (2x1), tall (1x2), and small cells so the mosaic feels composed, not gridded. Caption sits bottom-left of each cell, miniature fills the rest.
- Every mockup has at least one live element: animated counter, toggleable switch, hoverable row, playable mini timeline, or auto cycling tabs.
- Miniatures use the same design tokens (radius, accent, font scale) so cells feel like one product.
- Motion is subtle and pauses on `prefers-reduced-motion`.
- Responsive: 3 columns to 2 to 1 as width shrinks, hero cell spans first at each breakpoint.
- No external assets, no real product copy beyond names the caller supplied. No emoji anywhere; icons are inline SVG only.

### 4. Verify

Screenshot full grid plus each cell at 2x. Check: every cell shows a mockup (not a paragraph), each interaction responds, grid has no gaps or overlaps at 1280px and 390px. Fix and re-shoot until all pass.

## Boundaries

One overview grid, not full screens per feature. For a complete dense screen, use `saas-dashboard`. For a marketing page that embeds one demo, use `landing-page`. For skeleton placeholders, use `low-res-mockup`.
