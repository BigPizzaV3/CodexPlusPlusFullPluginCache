---
name: get-started
description: How to shop Port66 from ChatGPT. Use when someone asks to find, price or buy authenticated luxury, streetwear or collectibles on Port66.
---

# Shopping Port66

1. Search with `search_listings`. One or two words in the query match best (a brand like "Chrome Hearts" or an item like "Jordan 1"); use `min_price` / `max_price` for budgets.
2. Open a result with `get_listing` for its description, condition, sizes and provenance record.
3. For crypto prices, use `price_in_crypto`; for what a buyer can pay with, `payment_options`. Sellers always receive USDC.
4. Offers go through `make_offer` and are tracked with `offer_status`.
5. Always include the port66.xyz link so the buyer can review the piece and complete checkout on the site.

Do not claim a piece is authentic beyond what its listing and provenance record state.
