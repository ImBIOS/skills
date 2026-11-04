# saas-dashboard

## What it does

Turns a plain language brief into one self-contained HTML file that looks like a shipped SaaS console: workspace sidebar with switcher and user card, breadcrumbs, KPI cards, inline SVG chart, and a table with text search, status filter, sortable headers, and per-row actions. All data is plausible and internally consistent.

## When to reach for it

Reach for it when asked to mock or prototype a logged-in product UI: admin panel, analytics overview, billing, users, runs, campaigns. Typical triggers: "dashboard mock for X", "prototype the admin panel", "demo UI for the app".

## Common questions

**What do you need from me?** A sentence or two about the product and its users. The skill derives the screen, entities, and data from that.

**Does it connect to real data?** No. Data is invented but consistent (totals match rows, deltas match direction). No API or persistence.

**How does this relate to the Paralect catalog?** Functional scope matches their SaaS dashboard skill (https://www.paralect.com/skills/saas-dashboard). This is an original implementation, not affiliated, with no shared text or code.

## It's working if

The file opens with no build, KPIs plus chart plus table render with no overflow at desktop and phone widths, sort or filter responds, and every number in the mock agrees with every other number.
