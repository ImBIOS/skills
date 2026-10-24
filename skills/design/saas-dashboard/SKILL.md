---
name: saas-dashboard
description: Build a dense, realistic SaaS product screen (KPIs, chart, data table) as one self-contained HTML file. Use when asked to mock, prototype, or demo an admin panel, analytics dashboard, billing page, settings screen, or any logged-in product UI.
---

# SaaS Dashboard

Produce one self-contained HTML file that reads as a real product screen: sidebar nav, top bar with search and user, KPI cards, a chart drawn with inline SVG, a data table with sort or filter, and one detail affordance (drawer, modal, or expandable row). All CSS inline, all data plausible and product specific, no placeholder text.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/saas-dashboard). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: plain language brief (product name, audience, core features, or even a vague idea). Derive the screen from it: pick the single most representative view (overview, invoices, users, runs, campaigns) and name the 4 to 6 entities the data describes.

### 2. Fix the data model first

Define 3 KPIs with values and deltas, 6 to 10 table rows with consistent fields, and one time series of 12 to 24 points for the chart. Values must be internally consistent (totals match rows, deltas match direction). Write these down before coding so the mock does not contradict itself.

### 3. Write the file

Single file, one `<style>` block, one small `<script>` block for sort/filter plus one interaction (tab switch, row expand, modal open). Rules:

- Chrome: sidebar with active state, top bar, breadcrumbs or page title, consistent spacing scale.
- Chart: inline SVG line or bars generated from the series, with axis labels. No chart library.
- Table: sortable by at least one column or filterable by one control, with status pills and right aligned numbers.
- Density: real product density (12px to 14px body, compact rows), not marketing whitespace.
- Responsive: sidebar collapses under 860px, table scrolls horizontally inside its card.
- No external requests. System font stack or one inline font fallback.

### 4. Verify

Screenshot at 1440x900 and 390x844. Check: no overflow, numbers align, sort or filter works, chart renders with labels, active nav matches the page. Fix and re-shoot until all pass.

## Boundaries

Front-end mock only: no persistence, no API, no auth. For the marketing page around the product, use `landing-page`. For a grid of feature cells rather than one dense screen, use `bento-features`. For a skeleton with placeholder blocks, use `low-res-mockup`.
