---
name: landing-page
description: Build a polished hero landing page plus an interactive mock of the product UI, delivered as one self-contained HTML file. Use when asked to build, mock, or prototype a SaaS landing page, hero section, or product homepage with an interactive product preview.
---

# Landing Page

Produce a complete landing page as one self-contained HTML file: hero with headline and CTA, a working visual demo of the product interface (static mock with hover states or small JS interactions, no backend), plus supporting sections (logos, features, pricing teaser, footer). No external assets except system fonts or inline SVG. Everything inline so the file opens directly in a browser.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/landing-page). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: product description (one paragraph, or name plus feature list). Optional: color scheme (dark or light). If the scheme is missing, pick based on product mood (dev tools lean dark, SMB SaaS leans light) and state the choice.

Invent every word on the page: headline, subhead, CTAs, feature names, metrics, testimonial, prices. Reference screenshots or galleries may inform layout only; their words are never reused, not even headlines or button labels.

### 2. Draft the page plan

Before writing code, fix: headline (outcome, not feature list), subhead (one sentence), primary CTA plus secondary CTA, 3 proof elements (metric, logo row, testimonial), demo block contents (the 3 or 4 UI elements the fake product shows), and section order. Keep total under 6 sections so the file stays reviewable.

### 3. Write the file

Single file, semantic HTML, one `<style>` block, one small `<script>` block only if the demo needs interaction (tabs, toggles, fake live data). Rules:

- Type: Inter first (local `@font-face` when the runner provides it; system stack fallback), display headline 600 to 800 weight with tight tracking (-0.02em), scale that dwarfs body copy. Headline quality decides the page.
- Hero visual: layer the product UI with depth, not a flat screenshot box. Compose 2 or 3 overlapping panels (main window plus a floating notification, alert, or detail card offset over a corner), soft shadows, subtle backdrop glow. The demo interaction lives in the main panel.
- Layout: max width 1120px, generous whitespace, one accent color plus neutrals.
- Demo block: build it from divs that look like the product (sidebar, table, chart drawn with SVG or CSS bars). Add at least one interaction (switch tabs, filter rows, animate a number on load).
- CTA buttons pair an icon with the label (inline SVG: terminal, arrow, play). The secondary button always carries one; the primary may too. Text-only button pairs are rejected.
- Window chrome is never empty: traffic lights, product or repo icon plus breadcrumb path, a right-aligned search field with kbd hint, and an avatar stack (initials on varied hues with +N overflow). Every region of the demo window shows product content.
- Depth through layering: main panel plus at least two floating cards overlapping its edges (alert, assign, cause, forecast) plus one card clipped by the viewport bottom edge. Soft shadows and a backdrop glow sell the depth; a single flat panel does not ship.
- Responsive: single column under 720px, no horizontal scroll.
- Accessibility: real buttons and links, alt text on meaningful images, contrast that passes AA for body text.
- No lorem ipsum. Every string reads like the product team wrote it.
- No emoji anywhere in the page. Icons are inline SVG only.

### 4. Verify

Open the file in a browser (or screenshot it) and check: hero fits first viewport, CTA visible without scroll, demo interaction works, no overflow at 390px width, no console errors. Fix and re-screenshot until all pass. Save next to the file as `landing-preview.png` when the caller wants evidence.

## Boundaries

This skill produces a front-end mock, not a production site. No framework scaffolding, no backend, no analytics wiring. For a stripped skeleton with placeholder blocks instead of copy, use `low-res-mockup`. For a dashboard screen rather than a marketing page, use `saas-dashboard`.
