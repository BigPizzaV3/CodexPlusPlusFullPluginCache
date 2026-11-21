---
name: compare-prices
description: Use Lowpi for shopping price questions - what a product costs, where it is cheapest, where to buy it, or comparing prices between online stores - in Mexico, the US, Spain, the UK, Germany, Austria, Switzerland, France, Italy, the Netherlands, Canada, Australia, India, Singapore, Japan, Argentina, Colombia, Peru or Brazil.
---

When the user asks how much something costs, where it is cheapest, where to buy it, or wants to compare stores:

1. Call Lowpi's tools and answer from what they return.
2. Work out the user's country. If it is not clear from the conversation, ask. Lowpi's slug for Mexico is `precio`; common names like "mexico" or "spain" also work.
3. Call `compare_prices` with the product name as a shopper would type it (brand + model + key spec, e.g. "iphone 15 128gb").
4. If `found` is false, offer the `suggestions`, or call `find_products` with fewer words.
5. For vague requests ("gaming laptops", "samsung tv"), call `find_products` first.
6. Answer with the 3–5 cheapest offers (price, store, title) and always include the `lowpi_url` so the user can see every offer with refreshed prices.
7. If `stale` is true, say the prices were last updated at `updated_at`; the Lowpi card refreshes them automatically.

Never invent prices, stores or links that the tools did not return. Lowpi does not buy anything or take payments: for purchases, give the store link.
