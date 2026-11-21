---
name: find-best-price
description: Find products sold by South African retailers on PriceCheck and the cheapest shop for them. Use when the user wants to find, search for or buy a product in South Africa, find the cheapest option, or see products within a budget (prices in ZAR).
---

# Find a product and its best price

Use `search-products-tool`. Answer only from what it returns; don't make up products, prices or shops. Prices are in South African Rand (ZAR); write them like `R4 999`.

## Searching well

- **Put brands in `brands`, not only in the search text.** Product names often leave out the brand, so "Ninja air fryer" as plain text can return other brands. Use `search: "air fryer"` with `brands: "Ninja"`. List several brands with commas, e.g. `"Samsung,LG"`.
- **Be specific.** Use the product type plus model, series or key specs ("Galaxy S24 128GB", "gaming laptop RTX 4060"). A bare word like "laptop" also matches accessories.
- **Use `minPrice` and `maxPrice`** for budgets ("under R1 500" → `maxPrice: 1500`).
- **If results are poor,** search again with different words: drop extra words, use the model number, or move a brand into `brands`.

Each result has a product name, category, the shops selling it with their prices, and a Product URL. The number after `/offers/` in the URL is the product ID, e.g. `https://www.pricecheck.co.za/offers/258614062/...` → `258614062`.

## Answering

1. Pick the products that really match. Leave out accessories, books and loose matches unless the user asked for them.
2. Show the best 3 to 5. For each, give the name, the lowest price and the shop offering it, how many shops sell it, and the PriceCheck product link.
3. If the user asked for the cheapest, sort the matching products by their lowest price.
4. Remind the user that prices and stock change often, so they should confirm the price, stock and delivery on the shop's site before buying.
