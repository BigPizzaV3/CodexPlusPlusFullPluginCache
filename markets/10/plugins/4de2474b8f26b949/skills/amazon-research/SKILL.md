---
name: amazon-research
description: Search Amazon products or read a supplied ASIN, seller, seller catalog or product-review sample with HasData. Use for Amazon-specific data, not cross-store comparisons, checkout or seller administration.
---

# Research Amazon listings and sellers

Read `../hasdata-research/SKILL.md` and the Ecommerce section of `../hasdata-research/references/tool-catalog.md`.

Discovery uses `hasdata_amazon_search_getSearchResults` with q. Preserve the requested marketplace using an actual domain enum such as www.amazon.com. A product name without an ID is enough for one search; do not demand a fabricated ASIN. An unambiguous supplied /dp/ or /gp/product/ URL can supply its ASIN directly.

Details use `hasdata_amazon_product_getProductDetails` with asin; reviews use `hasdata_amazon_reviews_getProductReviews` with asin. For a seller ID from supplied or returned source data, use `hasdata_amazon_seller_getSellerDetails` or `hasdata_amazon_seller_products_getSellerProducts` as requested. Do not reuse product ASIN as sellerId.

Search, details, reviews and seller catalog are separate reads: call only the requested operation. otherSellers can incur an extra source request; do not enable it merely to inspect a product. Apply delivery, review and sort options only from the live schema.

Return a compact observed comparison with source links, currency, variant/pack wording, sponsored status and requested counters where provided. Missing shipping, tax, stock and ratings stay unavailable. For review themes, use `../review-insights/SKILL.md`; across stores, use `../product-research/SKILL.md`.
