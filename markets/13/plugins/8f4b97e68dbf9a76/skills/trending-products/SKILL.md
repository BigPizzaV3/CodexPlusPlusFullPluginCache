---
name: trending-products
description: Show which products are trending on PriceCheck in South Africa right now. Use when the user asks what's popular, trending, hot or getting a lot of attention on PriceCheck.
---

# Show trending products

1. Call `trending-products-tool`. Use `window: 24h` for "today" or "right now" and `window: 7d` for "this week".
2. Show the products it returns (up to 10), each with its name, category, lowest price, number of shops and PriceCheck link. The links are the Product URLs in `product_details`.
3. The list can be short and mixed (for example a graphics card next to groceries). Show it as it is; don't pad it with other products.
4. If the user asked about one type of product (e.g. "trending TVs") and none of the trending products match, say so and offer to search for that type with `search-products-tool` instead.

Trending means a quick rise in interest on PriceCheck, not best-selling or best-reviewed. Don't describe it as either. Prices are in ZAR.
