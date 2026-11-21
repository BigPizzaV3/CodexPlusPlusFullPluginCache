---
name: allr-gear-guide
description: Use ALLR's tools to find motorcycle gear and compare retailer offers by landed cost for the rider's country.
---

When the rider asks about motorcycle gear (helmets, jackets, suits, pants, boots, gloves, protection, luggage):

1. Ask for or infer the rider's country (CA, US, EU or UK). Pass it as `country` on every tool call so prices are landed for that country.
2. Use `list_categories_and_brands` first when you need the exact category or brand slug for a filter.
3. Use `search_gear` to find the product, then `get_product_offers` for the per-retailer table. Quote prices together with the currency and the "as of" time the tool returns, and quote sizes only together with their colorway.
4. Use `get_size_recommendation` for size questions, and tell the rider to confirm against the retailer's own chart before buying.
5. Use `get_deals` for current price drops.
6. Link the product page on allr.io and use each retailer link exactly as the tool returned it. ALLR does not sell gear or take payment; the rider completes any purchase on the retailer's website.
7. If a tool reports an error or no result, say so plainly. Do not invent prices, stock or sizes.
