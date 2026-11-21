---
name: walmart-research
description: Search Walmart listings, inspect a product URL/item ID or read sampled product reviews with HasData. Use for Walmart-specific prices and products, not cross-store price comparisons or purchases.
---

# Research Walmart listings

Read `../hasdata-research/SKILL.md` and the Ecommerce section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_walmart_search_getSearchResults` with q for a named product or category text. Use catId only when an actual supplied or returned category ID is available. Preserve the source domain and actual requested filters; do not import Amazon's enums.

Use `hasdata_walmart_product_getWalmartProduct` or `hasdata_walmart_reviews_getWalmartReviews` with an actual itemId or supported product url. Although some required arrays are empty, a details/reviews request still needs a real product identifier. Do not invent aspectId for review filtering.

Retain and unwrap the response before displaying compact requested product fields. HTTP 200/ok can accompany a source-level no-matching-results message and no product records. Distinguish that absence from a failed request or local parsing error; no silent retry or fabricated comparison.

Keep title/model, variant, condition, seller, currency and original product URL where returned. Missing charges or availability are unknown. otherOffers is not a default. Review theme summaries follow `../review-insights/SKILL.md`; multi-store comparisons follow `../product-research/SKILL.md`.
