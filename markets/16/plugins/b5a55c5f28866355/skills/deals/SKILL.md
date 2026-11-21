---
name: deals
description: "Find live deals on Deal.ai by search, store, category, discount or price. Use when the user asks for deals, sales or discounts on something, at a store, or in a category."
---

# Find live deals

## How to run it

1. Call `get_deals` with what the user asked: `query` for a kind of product ("air fryer"), `store` for a store ("Best Buy"), `category`, `min_discount_percent` or `max_price`, and a `limit` that suits the reply (5 is a good default).
2. List the deals: title, price, how much under the earlier price and what that earlier price is, the store with its link, and when it was checked. Keep any store-link notes at the end.
3. Offer the list page the answer links for more.

## Rules

- Say when each deal was checked; deals end and prices change.
- If nothing matches, say so and suggest a broader search.
