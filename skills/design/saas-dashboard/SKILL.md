---
name: saas-dashboard
description: Build a dense, realistic SaaS product screen (KPIs, chart, data table) as one self-contained HTML file. Use when asked to mock, prototype, or demo an admin panel, analytics dashboard, billing page, settings screen, or any logged-in product UI.
---

# SaaS Dashboard

Produce one self-contained HTML file that reads as a real product screen: sidebar nav, top bar with search and user, KPI cards, a chart drawn with inline SVG, a data table with sort or filter, and one detail affordance (drawer, modal, or expandable row). All CSS inline, all data plausible and product specific, no placeholder text.

Original implementation. Functional scope is inspired by the Paralect skills catalog (https://www.paralect.com/skills/saas-dashboard). Not affiliated with Paralect. No Paralect text, prompts, or code are reused here.

## Workflow

### 1. Collect inputs

Need: plain language brief (product name, audience, core features, or even a vague idea). Derive the screen from it: pick the single most representative view (overview, invoices, users, runs, campaigns) and name the 4 to 6 entities the data describes. Match the view to the product's core object: pipeline products show a kanban, queue products show an inbox or list, metric products show KPIs plus chart.

Brand first: same rule as `landing-page`. When no brand exists yet, call `saas-logo` first; sidebar wordmark and avatars use its outputs.

Invent every name, company, figure, and label on the page. References inform layout only; their words and numbers are never reused.

### 2. Fix the data model first

Define 3 KPIs with values and deltas, 6 to 10 table rows with consistent fields, and one time series of 12 to 24 points for the chart. Values must be internally consistent (totals match rows, deltas match direction). Write these down before coding so the mock does not contradict itself. Match the view to the product's core object, never defaulting to one template: pipeline products show kanban columns with cards, queue or inbox products show a split list plus detail pane, metric products show KPIs plus chart plus table, time products show a timeline. Vary the module lineup per product (KPI count, chart type, table versus cards); two outputs for different products must not share the same skeleton.

### 3. Write the file

Single file, one `<style>` block, one small `<script>` block for search, sort, filter, and row actions. Follow the standard SaaS console layout (shadcn-style): fixed left sidebar, top header bar, scrollable content. Rules:

- Type: Inter for UI and body (local `@font-face` when provided; system stack fallback), 13px body, tabular numbers. Headline, KPI numerals, and sidebar workspace name may use the display face when one is in use on the page (same pairing rule as `landing-page`); body, table, and labels stay Inter. Tracking: display -0.02em to -0.03em, body 0, uppercase micro-labels +0.08em to +0.12em with 11 to 12px size.
- Spacing scale: one 4px base unit, section rhythm 16/24/32, card padding 20 to 24, table rows 12 to 14px vertical. Hierarchy by size and weight only: one display size, one title size, body, micro. Never two adjacent sizes within 2px of each other.
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
