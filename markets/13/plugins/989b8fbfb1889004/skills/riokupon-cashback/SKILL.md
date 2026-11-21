---
name: riokupon-cashback
description: Estimate Riokupon cashback (RP points) for a Shopee or TikTok Shop Vietnam product link and explain how to claim it (Lazada: claim instructions only).
---

# Riokupon cashback

Use the `riokupon` MCP server when the user shares a Shopee, TikTok Shop or Lazada Vietnam product link and asks how much cashback (hoàn tiền) they can get, or whether buying through Riokupon is worth it.

## Tool
- `check_riokupon_cashback(url)` — product name, shop, price, units sold, estimated cashback in RP (base + bonus) and how to claim it.

## Rules
- Cashback is an estimate at the current price; the final amount is set when the order completes and is 0 if the order is cancelled or returned. Always say so.
- The user only receives cashback by buying from the Riokupon app/web while logged in. Repeat the claim instructions from the tool; never suggest buying directly on the marketplace for cashback.
- If the tool says the link or platform is not supported, relay that message; do not invent numbers.
- Riokupon RP points are Riokupon's reward unit; do not convert them to VND unless the user's Riokupon account terms say so.
