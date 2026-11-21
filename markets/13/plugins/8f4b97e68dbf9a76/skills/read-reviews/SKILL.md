---
name: read-reviews
description: Summarise customer reviews of a product, or of a South African shop, from PriceCheck. Use when the user asks whether a product is any good, what buyers think of it, or whether a shop or retailer is trustworthy.
---

# Read product and shop reviews

## Product reviews

1. Find the product with `search-products-tool` and take the product ID from the Product URL (the number after `/offers/`).
2. Call `product-reviews-tool` with the product ID. Use `sort: date` for recent opinions or `sort: score` to see the best and worst.
3. Summarise: the number of reviews, the average star rating, what reviewers like, and the most common complaints. Quote a short line or two if it helps.

## Shop reviews

1. Call `shop-reviews-tool` with the shop's `shop_id` if you have it, or without one to browse.
2. Summarise: the average rating, and what customers praise or complain about (delivery, returns, customer service).

## Both

- If there are no reviews, say so plainly. If there are only a few, say that a handful of reviews isn't a reliable picture.
- Product reviews come from South African retailers, and shop reviews from Google. Say where they come from.
- Report what reviewers said, without adding your own verdict on the product or shop.
