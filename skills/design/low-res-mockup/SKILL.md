---
name: low-res-mockup
description: Build an early-stage layout wireframe in HTML using gray skeleton bars and labeled boxes, with no real copy. Use when exploring layout, information hierarchy, or component placement before copy and visuals exist.
---

# Low Res Mockup

Produce one self-contained HTML file that shows structure only: gray skeleton bars for text, boxes for images, labeled outlines for components. It must read as a layout proposal, never as finished design, so nobody mistakes it for the real page.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/low-res-mockup). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: the screen or component in a few words ("settings page", "checkout step 2", "mobile nav"). Optional: the 3 to 5 elements that must appear and their priority order. Nothing else is required; this skill explicitly avoids real copy.

### 2. Write the file

Single file, one `<style>` block, no JS unless the layout needs a tab switch to show two states. Rules:

- Skeletons: rounded gray bars sized like the text they stand for (short bars for labels, long bars for paragraphs), crossed or shaded boxes for media, dashed outlines with tiny labels for interactive components ("CTA", "table", "chart").
- Tokens: one gray scale, one accent used sparingly for the primary action outline only, monospace micro labels.
- Structure: real semantic regions (header, nav, main, aside, footer) so the mock maps onto implementation.
- Annotation: numbered callouts (1, 2, 3) for open questions, listed at the bottom of the file as HTML comments plus a visible legend.
- Responsive: show desktop and phone as two stacked frames in the same file when both matter.

### 3. Verify

Screenshot and check: no real sentences anywhere (labels like "Headline" are fine, prose is not), every region labeled, skeleton rhythm resembles the intended density, no overflow at 390px. If anyone could mistake it for final design, remove detail until it reads as a wireframe again.

## Boundaries

Layout exploration only. When copy exists and the page should look finished, use `landing-page` or `saas-dashboard`. When each tile should demo a feature, use `bento-features`.
