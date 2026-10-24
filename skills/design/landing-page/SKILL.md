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

### 2. Draft the page plan

Before writing code, fix: headline (outcome, not feature list), subhead (one sentence), primary CTA plus secondary CTA, 3 proof elements (metric, logo row, testimonial), demo block contents (the 3 or 4 UI elements the fake product shows), and section order. Keep total under 6 sections so the file stays reviewable.

### 3. Write the file

Single file, semantic HTML, one `<style>` block, one small `<script>` block only if the demo needs interaction (tabs, toggles, fake live data). Rules:

- Layout: max width 1120px, generous whitespace, one accent color plus neutrals.
- Demo block: build it from divs that look like the product (sidebar, table, chart drawn with SVG or CSS bars). Add at least one interaction (switch tabs, filter rows, animate a number on load).
- Responsive: single column under 720px, no horizontal scroll.
- Accessibility: real buttons and links, alt text on meaningful images, contrast that passes AA for body text.
- No lorem ipsum. Every string reads like the product team wrote it.

### 4. Verify

Open the file in a browser (or screenshot it) and check: hero fits first viewport, CTA visible without scroll, demo interaction works, no overflow at 390px width, no console errors. Fix and re-screenshot until all pass. Save next to the file as `landing-preview.png` when the caller wants evidence.

## Boundaries

This skill produces a front-end mock, not a production site. No framework scaffolding, no backend, no analytics wiring. For a stripped skeleton with placeholder blocks instead of copy, use `low-res-mockup`. For a dashboard screen rather than a marketing page, use `saas-dashboard`.
