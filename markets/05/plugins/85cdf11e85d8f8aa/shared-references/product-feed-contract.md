# Product Feeds

Use Planning Guidance for suitability, product-set organization, and launch-quality advice. Use Operational Rules for feed discovery, ownership resolution, and product-feed creates or updates. Read the sections relevant to the active task; the owning skill's allowed tools and write-safety workflow remain authoritative.

## Planning Guidance

### Choose Product Feeds For Catalog Complexity

Product-feed mode is best suited to retailers and ecommerce advertisers with broad or frequently changing catalogs, many SKUs, or product details that would be costly or error-prone to maintain manually.

Do not recommend product-feed mode solely because a feed exists. First connect the choice to the advertiser's catalog shape, update frequency, and need to create or maintain relevant product ads at scale. If a focused standard campaign better matches a small stable offering, explain that tradeoff instead of forcing a feed workflow.

### Build Focused Product Sets

Use product sets to keep each ad group coherent. Group products that share customer need, value, destination, and bidding economics.

When the user supplies useful feed metadata, or a live tool actually returns it, use it to propose focused sets such as product line, season, inventory tier, margin band, or another advertiser-supplied business grouping. Never invent metadata, infer a product set from a sibling ad group, or promise a filter operator or field that the live schema does not expose.

### Launch With Quality Inputs

Before recommending launch, ask the advertiser to review:

- product titles and descriptions for accuracy, clarity, and useful differentiation;
- images for relevance, legibility, and alignment with the product;
- landing pages for validity, availability, and consistency with the product and message;
- product-set filters and any product count actually returned by `list_product_feeds` when that read is allowed by the active skill; do not claim a post-filter eligible-product count;
- an existing feed-supplied ad preview only when the active skill exposes a live preview action that supports the exact ad; do not promise a new product-template preview before creation.

Ratings, review counts, price, availability, and other feed-driven details should be described only when the user supplies them or a live tool returns them. Do not invent catalog attributes or claim that a product is eligible, approved, or ready to serve without live evidence.

Route changing product-capability and launch-requirement questions to `$ads-manager-help`; within Help, use its Help Center guide directly. Use live tool descriptions for field support and limits. Advice does not authorize feed discovery, previews, or writes outside the active skill's allowed tools.

## Operational Rules

- Use only an account-linked `feed_id`, not `id`; paginate required reads and stop on failed, incomplete, missing, conflicting, or unlinked ownership.
- New product-feed campaigns require `mode=product_feed` and confirmed `product_feed_id`. Paginate `list_product_feeds`; stop on zero feeds, confirm one, and ask the user to choose when multiple remain.
- For an existing product-feed campaign, reuse its verified parent `product_feed_id`; any sent `product_set.product_feed_id` must match it. Omit `product_set` unless filters are needed. If the parent has no feed, stop; do not infer one from sibling ad groups. Never repair or retry with another feed.
- Never send `product_feed_id` or `product_set` for standard campaigns, or silently fall back if product-feed setup is unavailable.
