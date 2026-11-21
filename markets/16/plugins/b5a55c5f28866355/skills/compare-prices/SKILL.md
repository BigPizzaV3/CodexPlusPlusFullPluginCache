---
name: compare-prices
description: "Compare one product's price at every store Deal.ai tracks, with its price history. Use when the user asks how much something costs, where it's cheapest, or whether its price has been lower."
---

# Compare prices for a product

## How to run it

1. If the user gave a Deal.ai product link or a product_id, use it. Otherwise call `search_products` with the product's name (kind `product`) and pick the result that is the exact product (model, size, generation). If several fit, ask which one in a short question, listing them.
2. Call `get_product_prices` with its `product_id`.
3. Reply with the best store price first (the one marked best), then the next few stores, each with when it was seen and its store link. Mention marketplace sellers only as such. Add the lowest price Deal.ai has tracked when it's useful ("it was $179 on Black Friday").
4. End with the product's Deal.ai page, and keep any store-link notes the answer ends with.

For specs, a description or ratings, call `get_product_details`. To weigh two to four products against each other, call `compare_products`.

## Rules

- Quote prices exactly as returned, with the day they were seen.
- Don't call a price the best if the tool marked it as a marketplace seller's.
