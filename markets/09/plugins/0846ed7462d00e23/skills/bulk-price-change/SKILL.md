---
name: bulk-price-change
description: Use when the seller wants to raise, lower, round, or set prices across one or many listings or variants (e.g. "raise sweatshirts 10%", "make XXL $2 more"). Creates one approval request.
---

1. Resolve the target listings with `list_listings`; confirm the exact set back to the seller when the wording is ambiguous (e.g. which listings count as "sweatshirts").
2. Call `propose_price_update` once with all `listingIds`, the mode (`set`, `adjust_percent`, or `adjust_amount`), and a `where` variation filter when only some variants change.
3. Read the returned status. If pending, tell the seller to approve on the card; show the before → after pairs from the preview. If executed, say it was applied automatically and do not repeat it.
4. Mention that price changes can be undone exactly with the undo-a-change skill.
