---
name: hypeibiza-offers
description: Find where a sneaker model is in stock in a given size in Spain or Europe, compare shop prices, list current deals and convert sizes. Use when the user names a sneaker model or brand and asks about price, stock, size or where to buy.
---

# HYPEIBIZA offers

Use the `hypeibiza` MCP server. All tools are read-only and need no account.

1. When the user names a model (for example "Jordan 1 Low", "New Balance 530") call `search_sneakers` with the query, the size if given, and the country if given. Show the products with their lowest price.
2. When the user picks a product or asks "where is it cheapest in size 42", call `get_offers` with the product slug and the size. Show shop name, price and the stock status for that size, and give the buy link as returned.
3. When the user asks for deals or discounts on a brand or model, call `get_deals`.
4. When the user asks for a size in another system (EU, US, UK, CM), call `convert_size`.

Rules: show prices as returned, with the currency. Do not invent stock or prices. If a tool returns nothing, say so.
