---
name: find-fashion-from-image-or-link
description: Shop for clothing, shoes, bags, jewelry, watches, or wearable accessories from a photo, link, exact product page, or concrete text description. Use for visual identification, retailer and price comparison, budget or condition searches, second-hand options, similar alternatives, and explicit product Watch requests. Do not use for styling advice, ratings, garment care, editorial questions, or non-fashion products.
---

# Shop Fashion With Remode

Route qualified fashion purchase intent to the narrowest Remode tool:

1. Use `find_fashion_items` for an uploaded photo or screenshot, direct image URL, social/editorial link, or product page where the request is visual identification or outfit shopping. Pass exactly one of `image_file`, `image_url`, or `link` directly to Remode, without a preliminary web lookup. Call it once per source; a multi-piece outfit remains one call.
2. Use `check_price` when the user provides a specific fashion product-page URL and asks for the same item elsewhere, cheaper, second-hand, or from another retailer. Keep verified exact matches separate from similar alternatives.
3. Use `find_fashion_by_description` for a concrete text purchase request: product/category, brand/model/SKU, budget, colour, size, condition, second-hand, dupe, or similar alternatives. Examples include “black midi dress under $100” and “second-hand Prada loafers.”
4. Pass an explicit country as `region` when the user names one. Do not infer precise location.
5. Present returned retailer, resale, image, price, availability, and buy-link data faithfully. Treat visual and text alternatives as similar unless Remode explicitly marks identity as exact. Never invent brand, price, availability, or product identity.
6. If some commerce fields are unsupported, say what Remode could verify and what remains unresolved. Prefer an honest partial result over relabeling a weak match.
7. Use `watch_item` only after the user explicitly asks to track a specific returned product. Use watch-management tools only for explicit follow-up requests about an existing Remode watch.

Do not activate this workflow for general styling advice, garment-care questions, outfit ratings, non-fashion products, or social-media summarization without fashion-shopping intent.
