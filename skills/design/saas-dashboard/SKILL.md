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

Single file, one `<style>` block, one small `<script>` block for search, sort, filter, and row actions. Follow the standard SaaS console layout (shadcn-style): fixed left sidebar, top header bar, scrollable content. Rules:

- Type: Inter first (local `@font-face` when provided; system stack fallback), 13px body, semibold section titles, tabular numbers.
- Sidebar: workspace switcher button at the top (product mark plus name plus chevron), nav section with one consistent inline SVG icon set (uniform 16px stroke icons, never mixed styles), active item highlighted, and a user card pinned at the bottom (avatar initials, name, plan). Nav, user, and workspace placement is fixed by convention, not invented per page.
- Header: breadcrumbs (Workspace / Section / View) on the left, search field and primary action on the right.
- Chrome: KPI cards with delta and sparkline, one inline SVG chart with axis labels, then the data table.
- Table: text search input that filters rows, at least one status or category filter, sortable column headers with direction indicators, checkbox column, and a per-row actions menu (View, Edit, Delete as real menu items). Numbers right aligned with status pills.
- Density: real product density (compact rows), not marketing whitespace.
- Responsive: sidebar collapses under 860px, table scrolls horizontally inside its card.
- No external requests. No emoji anywhere; icons are inline SVG only.

### 4. Verify

Screenshot at 1440x900 and 390x844. Check: no overflow, numbers align, sort or filter works, chart renders with labels, active nav matches the page. Fix and re-shoot until all pass.

## Boundaries

Front-end mock only: no persistence, no API, no auth. For the marketing page around the product, use `landing-page`. For a grid of feature cells rather than one dense screen, use `bento-features`. For a skeleton with placeholder blocks, use `low-res-mockup`.
