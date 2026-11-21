---
name: product-descriptions
description: Write or rewrite WooCommerce product names, descriptions, short descriptions and SEO titles. Use when the owner asks to improve, refresh, shorten or write product text, or to fix thin descriptions.
---

1. Call `get_brand_voice`. If the owner has a saved style, follow it. If they have none, ask one question about tone and length, then offer to save it with `save_brand_voice`.
2. Find the products: `find_products` with `max_description_words` (for example 50) or `missing: ["description"]`, or the specific products the owner named.
3. Draft the new text yourself. Keep facts to what is already in the store (name, category, existing description). Do not invent specifications, materials, certifications or claims.
4. Call `apply_product_content` WITHOUT `confirm` to preview before/after for each product. Optionally include `meta_title` (about 60 characters) and `meta_description` (about 150 characters).
5. Show the owner the previews and wait for approval. Only then call it again with `confirm: true` and the `preview_id`.
6. Mention the change number and that "undo change N" restores the old text.
