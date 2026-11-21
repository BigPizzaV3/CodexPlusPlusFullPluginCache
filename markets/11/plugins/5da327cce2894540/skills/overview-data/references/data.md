# Fields and provenance

## Search envelope

- `data`: the complete JSON representation of the existing app market-reaction response, without plugin filtering, ranking or pagination. Its product adapter currently caps cards at 100; this is existing app behavior.
- `data.productsEntries`: dashboard product cards. Common fields are `title`, `productUrl`, `country`, `ad_title`, `ad_body`, `ad_start_date`, `ad_image_urls`, `ad_video_urls`, `ads_count`, `avg_creatives`, `ads_per_unique_url`, `active_ads`, `actualPrice`, `priceHistory`, `productAge` and a card-local `id`.
- `data.adaptedResult`: existing deterministic app market aggregates. Their timeline is based on stored batch/job fields, not necessarily consecutive calendar weeks. Do not interpret them as measured transactions or complete historical coverage.
- `data.ress`: the existing response field; its market-reaction AI report is currently disabled and normally returns an empty object.
- `data.adLibrarydata`: separately fetched Meta ad-library data, not the proprietary stored product observations. The existing market-reaction app request uses the first two title words and Meta's **DZ** country filter even when other countries were selected for proprietary search. These sources must remain distinct.
- Empty search currently returns `{a: null, b: null, c: null}` in `data`. No products/estimates are synthesized.

Media strings use semicolon-separated references. Source links can be unavailable, expired or inaccessible in a host. Counts of links do not establish unique creative content or continued advertising.

`active_ads` is a stored/adapter flag, not a live verification. `productAge` uses batch differences and may contain Arabic text; it is not an authoritative elapsed-time measurement. The raw search currently filters for Overview-hosted video URL prefixes, so search coverage is not an exhaustive set of static-only products.

Historical scraped prices were retired in August 2025. Current search data can contain zero `actualPrice` and empty/zero price history. Do not present these as a current free offer or a current pricing trend. Inspect a current public page independently if price matters.

## Dashboard estimates

`estimates` pairs an exact `productUrl` with the output of the existing `estimateSalesAndSpend` helper, computed at retrieval/render time. A null estimate indicates that the helper did not yield valid finite output.

- `daily_units_sold`: heuristic low/high daily unit range.
- `total_units_sold`: heuristic low/high total units, derived from daily ranges and estimated ad age.
- `ad_spend_usd`: heuristic low/high **total** advertising spend in USD, not daily spend or observed billing.
- `ad_days_live`: elapsed time from recorded ad start to calculation time, clamped to 0–70 days. This extrapolation is an estimator input; it does not prove continuous ad activity.
- `store_tier`, `ad_performance_multiplier`, `notes`: model assumptions/classification outputs, not measured quality or performance.

The helper uses shop ad-count tiers, referenced image/video counts, average creative count, ad age, baseline unit ranges and country cost-per-sale assumptions. It applies minimum daily ranges (20 low / 60 high). Missing start dates default to calculation time; malformed dates can produce an unavailable estimate. This is not a calibrated probability interval, transaction dataset, margin estimate or proof of traction. Negative sentinel ranges mean unavailable.

## Ad activity

`data` is the existing ad-activity row array: `ad_start_date`, `ad_end_date`, `ad_video_urls`. It reads stored rows by exact `product_url`, with no separate search, plugin caching, ordering, deduplication or country filter. Duplicate observations and null values can occur. Captured end dates do not imply a verified stop date; missing end dates do not prove continuing spend. `productUrl` identifies the requested product; `retrievedAt` records retrieval time.

Current collection is described by the owner as weekly. Neither tool adds a new collection timestamp or invents freshness guarantees where the app output lacks those fields.
