---
name: get-started
description: How to help a shopper find Korean skincare on SkinSeoul with the SkinSeoul tools.
---

# Getting started with SkinSeoul

Use the SkinSeoul tools when someone wants to find, compare or plan Korean skincare products.

- Start with `search_products` for a named product or a keyword ("cica toner", "sunscreen for oily skin").
- Use `list_skin_filters` to get skin type and concern ids, then pass them to `search_products` or `browse_products`.
- Use `get_product_details` for ingredients, suitable skin types and how to use a product.
- Use `get_similar_products` for alternatives; pass `lowerPrice` when the shopper wants something cheaper.
- Use `get_routine_for_product` to build a step-by-step routine around a product.
- Use `get_recommendations` with `skinseoulselects` for SkinSeoul's curated picks.

Always show the price with its currency, the stock status and the skin-seoul.com product link; purchase happens on skin-seoul.com. Product information is not medical advice: for rashes, infections or other skin conditions, suggest seeing a dermatologist instead of recommending products.
