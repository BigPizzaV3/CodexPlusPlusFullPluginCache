---
name: compare-products
description: Compare 2 to 5 products sold in South Africa side by side on price and features using PriceCheck. Use when the user asks "X vs Y", which product to choose, or for a comparison table of shortlisted products.
---

# Compare products

1. Find each product with `search-products-tool`. Put the brand in `brands` and the model in `search` (e.g. `search: "Galaxy S24"`, `brands: "Samsung"`). Take the product ID from each Product URL: the number after `/offers/`.
2. If a search returns several versions (sizes, storage, colours), use the one the user named, or ask which they mean.
3. Call `comparison-data-tool` with 2 to 5 `product_ids`. It returns each product's lowest and highest price (`price_min`, `price_max`), number of shops (`num_offers`), rating, number of reviews, brand, model number and product link.
4. For features and specs, use the product descriptions from the search results. Only list specs that are actually stated there; if a spec isn't given for a product, show it as "not listed".
5. Answer with a short table: one column per product, rows for the lowest price, the number of shops, rating (if any) and the specs that matter most for this kind of product.
6. Finish with one or two sentences on the main trade-off (for example, "the S24 is R2 000 cheaper; the iPhone has more storage"). Don't pick a winner unless the user asks; if they do, base it on what they said matters to them.

Only use data the tools return. Prices are in ZAR. Link to each product's PriceCheck page.
