---
name: watch-prices
description: "Watch products for price drops with the user's Deal.ai wish list, which e-mails them when a price drops. Use when the user asks to be told when something gets cheaper, asks what they're watching, or wants to stop watching something."
---

# Watch prices

## How to run it

- **Watch:** find the product with `search_products` if you don't have its `product_id`, then call `watch_price`. Tell the user it's saved, its best price now, and whether price-drop e-mails are on for their account. If they're off, say so and give the link the answer includes to turn them on; never claim an e-mail will come when they're off.
- **What am I watching:** call `list_watched` and list each product with its price now.
- **Stop:** call `stop_watching` with the product. Confirm what was removed.

## Rules

- Only watch or stop watching when the user asks for it.
- If the wish list is full, tell the user and offer to remove something first.
