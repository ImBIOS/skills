# og-image

## What it does

Builds the static 1200x630 share card from a real screenshot of the product UI plus a headline, exports the PNG, and wires `og:image` and Twitter card meta tags into the route with absolute URLs.

## When to reach for it

Reach for it when asked to create or fix a link preview, share card, or social image. Typical triggers: "og image", "share card", "link preview looks wrong", "Twitter card".

## Common questions

**Is the UI redrawn or captured?** Captured from the running app at 2x. Never fabricated, so the card matches the product.

**What do you need from me?** Optionally a verbatim headline and the target page. Otherwise the skill derives both from the repo.

**How does this relate to the Paralect catalog?** Functional scope matches their OpenGraph image skill (https://www.paralect.com/skills/og-image). This is an original implementation, not affiliated, with no shared text or code.

## It's working if

The PNG is exactly 1200x630 under 1MB, the headline reads at 300px wide, meta tags use absolute URLs, and a validator or local preview renders the card.
