---
name: saas-logo
description: Design a flat geometric logo mark plus app-icon tile as SVG, then export transparent PNGs. Use when asked to create, concept, or iterate a SaaS logo, app icon, or brand mark with a geometric construction.
---

# SaaS Logo

Produce 3 or 4 logo concepts as hand authored SVG geometry, compare them on one sheet, then export the pick as transparent PNGs: the bare mark with no padding, and the rounded app-icon tile. The method is construction from primitives (circles, squares, strokes, grids), not tracing or image editing.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/saas-logo). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: one line on the product (what it is, the verb users perform). Optional: a brand to be like ("like Vercel's"), a hex brand color, or a preferred family. If no color arrives, propose one saturated tile color or black and say so. Read the repo README and landing copy when running inside the project.

### 2. Pick families and sketch concepts

Work across 2 or 3 of these construction families so the concepts differ structurally:

1. Solid primitive: one bold shape, possibly subtracted.
2. Repeated primitive: one shape tiled or rotated into rhythm.
3. Letterform: the initial reduced to geometry on a grid.
4. Faceted object: isometric or folded plane suggesting the product noun.
5. Soft stroke: one continuous rounded stroke, mono weight.

For each concept write one line: the symbol as geometry, its count and rhythm, the color, and what to leave out. Constrain every concept: flat, 2 colors max, legible at 16px, no gradients except a flat two stop facet at most.

### 3. Author SVG and compare

Hand write each concept as clean SVG on a grid (viewBox 0 0 256 256, strokes expanded or uniform). Render all concepts side by side on one comparison sheet (one HTML page embedding the SVGs at 64px, 32px, and 16px) and judge: silhouette distinctness, 16px legibility, single color version survival. Iterate the weakest concept once, then pick.

### 4. Export the pick

Deliverables, mark centered with optical (not mathematical) balance:

- `mark.png`: transparent background, no padding, 1024px on the long side.
- `icon.png`: rounded tile (22 percent radius) in brand color with the mark knocked out or overlaid, 1024x1024.
- Keep the source `mark.svg` and `icon.svg` next to the PNGs.

Rasterize with whatever is installed (`rsvg-convert`, Inkscape, ImageMagick, or a short Python PIL script that parses the SVG paths). Verify: open both PNGs over light and dark backgrounds, confirm clean edges and no clipping, confirm 16px favicon legibility from the sheet.

## Boundaries

Logo marks and app icons only. No full brand systems, no wordmarks with custom lettering beyond the initial, no copying of existing marks (being "like" a brand means sharing its family, never its shape). For share cards that use the logo, pair with `og-image`. For generated imagery in articles, use `article-image`.
