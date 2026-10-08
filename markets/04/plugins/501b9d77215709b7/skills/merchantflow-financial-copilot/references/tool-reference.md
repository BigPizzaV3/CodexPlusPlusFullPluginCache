# MerchantFlow MCP tool reference

Generated from the live tool registry. 64 tools are registered.

This file is rendered from the server's own `tools/list` response at download time,
so it cannot drift from the running server. It is still a snapshot: the tools your
connection actually sees depend on your plan tier and on per-tenant feature flags,
so trust the live `tools/list` over this file when the two disagree.

Every tool is read-only. There is no write scope, so no tool here can create, modify
or delete anything in the store.

## Index

| Tool | Scope | Purpose |
| --- | --- | --- |
| `fetch` | `mcp:products:read` | Retrieve the full record for an opaque document id from MerchantFlow's retrieval results. Returns id, title, text, URL, and metadata. |
| `find_cogs_gaps` | `mcp:products:read` | Find products or variants with missing or stale COGS data that are affecting P&L accuracy. Returns product titles, SKUs, and the gap reason. |
| `find_duplicate_customers` | `mcp:orders:read` | Group orders by customer email hash to find customers under multiple names or phone numbers. |
| `generate_report` | `mcp:reports:read` | Generate the data for any report over a date range - the same numbers the dashboard shows. The report selector is exactly one of report_id (a saved or custom report identifier) and template_key (a built-in template such as pnl or product_performance). Dates default to the report's own default timeframe ending today; narrower ranges reduce truncation. |
| `get_ad_performance` | `mcp:ads:read` | Get paid and owned channel performance for a date range across Meta, Google, Snapchat, TikTok, Pinterest and Klaviyo, with spend, clicks, impressions, conversions and the revenue each platform reports for itself. Group by platform, campaign, or country. Klaviyo is an owned channel billed as a flat fee, so its spend is 0 by design and it is marked is_owned_channel. |
| `get_anomalies` | `mcp:activity:read` | Get recent anomalies detected by MerchantFlow (profit drops, spend spikes, missing sync data, attribution issues). |
| `get_attribution_breakdown` | `mcp:ads:read` | Get attributed revenue by channel using MerchantFlow's attribution rules, including organic, paid, email, referral, and direct. |
| `get_bank_balance` | `mcp:pnl:read` | Get the current bank balance, burn rate over the last 30/60/90 days, and projected runway in days. |
| `get_bottom_products` | `mcp:products:read` | Get the bottom N products ranked by profit or margin. Useful for finding SKUs that are losing money. Supports a minimum units filter to drop low-volume noise. |
| `get_cac_payback` | `mcp:customers:read` | Get customer acquisition cost payback period per channel, showing how long it takes to recoup CAC via customer first-order profit. |
| `get_channel_roas` | `mcp:ads:read` | Get blended MER (Marketing Efficiency Ratio) and per-platform spend over a date range, with optional comparison to the previous period. Each row also carries platform_reported_revenue and platform_reported_roas - the ad platform’s own self-attributed claim. These figures are non-additive across platforms because Meta and Google may claim the same order; MerchantFlow-attributed revenue remains null in this result. |
| `get_cogs_coverage` | `mcp:cogs:read` | Report how much of the store's catalogue, units sold, and revenue is covered by COGS data over a date range (default: last 30 days), including margin distribution and the top products still missing costs. |
| `get_cohort_analysis` | `mcp:customers:read` | Get customer cohort analysis showing LTV, repeat purchase rate, and revenue by cohort month/week over time. |
| `get_combined_pnl` | `mcp:pnl:read` | Combined profit and loss across every linked store for a date range (default: last 30 days), converted into one reporting currency. Set per_store to also get the per-store breakdown. Requires a plan covering more than one store. |
| `get_customer_detail` | `mcp:customers:read` | Get lifetime value detail for a single customer: net profit, revenue, CAC, tenure, and order history (most recent 200 orders). Customer name and email in the response are partially redacted. The customer identifier is the id returned in the customer lifetime value list. |
| `get_date_range_summary` | `mcp:pnl:read` | Get a high-level summary of revenue, profit, orders, ad spend, and top metrics for an arbitrary date range, suitable for quick time-period comparisons. |
| `get_discount_code_performance` | `mcp:marketing:read` | Get per-discount-code margin metrics: uses, revenue, discount cost, COGS, allocated ad spend, gross profit, and margin percent, ranked by any column. Pre-aggregated rolling timeframes provide the fastest results, while an explicit start_date/end_date produces a custom range computed live. |
| `get_expenses_breakdown` | `mcp:pnl:read` | Get OPEX and CAPEX expenses broken down by category and vendor over a date range, including recurring expenses and CAPEX amortisation. |
| `get_integration_status` | `mcp:activity:read` | Get the connection status of all integrations (Shopify, WooCommerce, GA4, ad platforms, SpeedFulfill) including last sync time and any errors. |
| `get_item_cogs` | `mcp:cogs:read` | Get the current cost of goods sold and full cost history for one item, identified by sku, product_id (internal product id), or variant_id (the commerce platform's variant id, e.g. the Shopify variant id - not an internal uuid). Optional on_date returns the cost effective on that date. |
| `get_ltv_summary` | `mcp:customers:read` | Get customer lifetime value summary including average LTV, LTV by acquisition channel, and LTV:CAC ratio. |
| `get_market_products` | `mcp:pnl:read` | Get the Markets country drilldown for a date range, ranked by variant and bundle contribution margin using the same service as the dashboard. |
| `get_markets` | `mcp:pnl:read` | Get the Markets dashboard table for a date range, including real geo ad spend, blended fallback spend, revenue, net profit, margins, ROAS, POAS, CAC, and spend-without-orders markets. |
| `get_mca_status` | `mcp:pnl:read` | Get active revenue-based funding (MCA) agreements, repayment schedule, and impact on current period P&L. |
| `get_north_star_status` | `mcp:north-star:read` | Get the current status of all configured North Star KPIs with target, actual, delta, and trend direction. |
| `get_organic_revenue` | `mcp:pnl:read` | Get organic vs paid vs direct revenue for a date range, classified from order-level UTM parameters and referrer data captured at checkout - NOT from Google Analytics 4 sessions, pageviews, or traffic data. Includes an attribution-confidence score, optional period-over-period growth, a channel breakdown, and an optional daily trend. Requires the attribution feature flag to be enabled for the tenant; returns attribution_disabled otherwise. |
| `get_pnl_summary` | `mcp:pnl:read` | Get a profit and loss summary for the tenant's store over a date range, broken down by revenue, COGS, ad spend, expenses, fees, and net profit. Optionally compare to the previous period or previous year for percentage deltas. |
| `get_product_detail` | `mcp:products:read` | Get detailed profitability for a specific product including current catalogue price, variant-level pricing breakdown, COGS, and 90-day trend from the analytics snapshots. |
| `get_recent_activity` | `mcp:activity:read` | Get a chronological feed of recent tenant activity: syncs, large orders, and integration events. |
| `get_revenue_breakdown` | `mcp:pnl:read` | Get revenue broken down by source (organic, paid, direct, email, referral), by channel, or by country over a date range. |
| `get_store_list` | `mcp:store:read` | List the stores linked to this account, with each store's platform, currency, timezone, connection state and last sync time. The result defines the store set available for combined figures. |
| `get_tax_insights` | `mcp:pnl:read` | Get period tax totals and the blended effective tax rate over a trailing N-day window, plus a per-country split. Tax figures combine tax the platform reported on orders with tax computed from active manual TaxRule entries where the platform reported none (or a fixed-amount rule applies). Mirrors the dashboard tax settings page tiles. |
| `get_top_products` | `mcp:products:read` | Get the top N products ranked by revenue, profit, margin, or units sold over a date range using the same order-based product profit math as the dashboard. |
| `get_unattributed_revenue` | `mcp:ads:read` | Get revenue that MerchantFlow couldn't attribute to a known channel, with order count, percentage of total revenue, and recent examples. |
| `list_capabilities` | `mcp:activity:read` | Report this connection's plan tier, available history, cross-store availability, current rate-limit headroom, and known data limits. |
| `list_cogs` | `mcp:cogs:read` | List cost-of-goods-sold entries for all items and variants in this store, newest effective date first, enriched with the matching product and variant. Paginate with page/page_size; filter by SKU substring or effective-date range. |
| `list_customers` | `mcp:customers:read` | List customers ranked by lifetime value (net profit after allocated overhead, summed across each customer's full order history) - the same source as the dashboard Customers page. start_date/end_date filter WHICH customers appear, by their first-order date; they do NOT clamp a customer's lifetime totals to that window. Customer name and email in the response are partially redacted. Each returned id identifies a customer record whose detail includes up to 200 recent orders. |
| `list_reports` | `mcp:reports:read` | List every report available to this store: saved template reports, custom reports, and the built-in template catalogue. Each returned report id or template key identifies a report available for generation. |
| `lookup_order` | `mcp:orders:read` | Look up a single order by number and return its line items, margin, fulfillment state, and refund history. |
| `query_order_basket_analytics` | `mcp:pnl:read` | Analyse orders filtered by what is IN the basket (which products, and how many units), broken down by region, channel or month. Answers questions the pre-computed dashboard context cannot, such as 'orders containing two chairs, average shipping cost per region'. Returns order counts, net revenue, and BOTH shipping figures: what customers were charged (revenue) and what fulfilment actually cost the merchant, with an explicit coverage percentage for the cost side. |
| `resolve_products` | `mcp:products:read` | Resolve a product name, category word or SKU (e.g. 'chairs', 'oak desk', 'CHR-01') to concrete product IDs in this store's catalog. Each match includes a similarity score and supports disambiguation of natural-language product references for product-level basket analysis. |
| `run_abandoned_cart_identifier` | `mcp:marketing:read` | Recent abandoned checkouts with recoverable value. Read-only - does not send messages. |
| `run_business_valuation` | `mcp:valuation:read` | Run the SDE-multiple business valuation for the tenant based on current P&L data, growth, margin, MER, and risk scoring. Returns valuation range with sensitivity analysis. |
| `run_collection_membership_audit` | `mcp:store:read` | Collections in the store with product count and last-updated date, flagging empty collections. Returns the first "limit" collections and reports how many matched in total. The result covers collection hygiene, empty collections, and potentially stale collections. |
| `run_customer_spend_tier_classifier` | `mcp:marketing:read` | Classify customers into VIP / regular / casual / one-time tiers based on lifetime spend and order count. |
| `run_dead_stock_report` | `mcp:inventory:read` | Identify products with zero sales in the window and (when Shopify is connected) their current on-hand inventory. |
| `run_fulfillment_digest` | `mcp:orders:read` | Digest of open orders by fulfillment status and age. Surfaces orders stuck for more than 3 days. |
| `run_gift_card_balance_report` | `mcp:store:read` | Outstanding gift card balance grouped by currency plus redemption percentage against initial issuance. |
| `run_high_risk_order_report` | `mcp:orders:read` | Shopify-flagged orders with medium or high fraud risk in the recent window. Read-only. |
| `run_inventory_valuation` | `mcp:inventory:read` | Total dollar value of inventory currently on hand (on-hand quantity x recorded COGS per SKU). |
| `run_multi_location_inventory_audit` | `mcp:inventory:read` | Find variants that are out of stock at some locations but available at others - candidates for transfers. |
| `run_page_content_audit` | `mcp:store:read` | Store pages flagged by content thinness, unpublished status, or staleness. |
| `run_product_completeness_score` | `mcp:store:read` | Scores every product on a 0-100 scale based on images, SEO fields, description length, and taxonomy. |
| `run_product_image_audit` | `mcp:store:read` | Products without a featured image or fewer than N total images. |
| `run_product_viability` | `mcp:products:read` | Run a product viability simulation: given a proposed selling price, COGS, and expected ad spend, compute break-even ROAS, contribution margin, and sensitivity analysis against store averages. |
| `run_repeat_purchase_rate` | `mcp:orders:read` | Percentage of customers in the selected window who placed two or more orders. |
| `run_sales_by_channel_report` | `mcp:marketing:read` | Revenue, orders, profit, and AOV broken down by acquisition channel. Requires the attribution feature flag to be enabled for the tenant. |
| `run_seo_metadata_audit` | `mcp:store:read` | Products missing SEO title or with SEO description shorter than threshold. |
| `run_stock_velocity` | `mcp:inventory:read` | Rank products by units sold in the selected timeframe and classify them as fast, steady, slow, or dead. |
| `run_url_redirect_audit` | `mcp:store:read` | URL redirects in the store, flagging loops, empty targets and redirect chains. Returns the first "limit" redirects and reports the total matched. The result covers broken links, redirect loops, and SEO risks from redirect chains after a replatform. |
| `run_win_back_candidates` | `mcp:marketing:read` | Identify valuable customers who haven't purchased in the last N days. |
| `run_wismo_digest` | `mcp:marketing:read` | Where Is My Order digest - in-flight orders with tracking status, age, and destination. |
| `search` | `mcp:products:read` | Search this MerchantFlow store for products and orders matching a query. Returns retrieval documents with an id, title, and URL; each id resolves to its full record. This endpoint provides record retrieval rather than profit, ad, cohort, or valuation analytics. |
| `search_orders` | `mcp:pnl:read` | Search orders by date range, customer email, order number, or product SKU. Returns a summary of matching orders with profit per order. Hard-capped at 100 results. |

## Tools

### `fetch`

**Fetch Record** - scope `mcp:products:read`

Retrieve the full record for an opaque document id from MerchantFlow's retrieval results. Returns id, title, text, URL, and metadata.

Parameters:

- `id` (string, required) - An opaque document id returned by `search` (formatted like `product:<id>` or `order:<id>`). Do not construct this id manually.

### `find_cogs_gaps`

**Products Missing COGS** - scope `mcp:products:read`

Find products or variants with missing or stale COGS data that are affecting P&L accuracy. Returns product titles, SKUs, and the gap reason.

Parameters:

- `include_zero_cost` (boolean, optional) - Include products whose latest COGS entry is exactly zero as a gap (default true); set to false to only flag products with no COGS entry at all.
- `stale_older_than_days` (number, optional) - Also flag products whose latest COGS entry is older than this many days as stale (omit to skip the staleness check entirely).

### `find_duplicate_customers`

**Duplicate Customers** - scope `mcp:orders:read`

Group orders by customer email hash to find customers under multiple names or phone numbers.

Parameters:

- `min_orders` (integer, optional) - Minimum number of orders under the same email hash for a customer to be reported as a possible duplicate (default 2, 2 to 20).
- `limit` (integer, optional) - Maximum number of duplicate-customer groups to return (default 50, 5 to 200).

### `generate_report`

**Generate Report** - scope `mcp:reports:read`

Generate the data for any report over a date range - the same numbers the dashboard shows. The report selector is exactly one of report_id (a saved or custom report identifier) and template_key (a built-in template such as pnl or product_performance). Dates default to the report's own default timeframe ending today; narrower ranges reduce truncation.

Parameters:

- `report_id` (string, optional) - The internal MerchantFlow id of a saved or custom report from list_reports. Pass exactly one of report_id or template_key.
- `template_key` (string, optional, one of `pnl`, `product_performance`, `marketing_overview`, `order_summary`, `expense_breakdown`, `month_over_month`, `week_over_week`, `year_over_year`) - The key of a built-in report template (e.g. pnl, product_performance) from list_reports. Pass exactly one of report_id or template_key.
- `start_date` (string, optional) - Start of the report date range as YYYY-MM-DD, resolved in the tenant's timezone. Defaults to the report's own default timeframe measured back from end_date.
- `end_date` (string, optional) - End of the report date range as YYYY-MM-DD, resolved in the tenant's timezone. Defaults to today in the tenant's timezone.
- `comparison_mode` (string, optional, one of `none`, `previous_period`, `previous_year`) - How to compute the comparison_rows: "none" for no comparison, "previous_period" for the immediately preceding period of equal length, or "previous_year" for the same period one year earlier.

### `get_ad_performance`

**Ad Performance** - scope `mcp:ads:read`

Get paid and owned channel performance for a date range across Meta, Google, Snapchat, TikTok, Pinterest and Klaviyo, with spend, clicks, impressions, conversions and the revenue each platform reports for itself. Group by platform, campaign, or country. Klaviyo is an owned channel billed as a flat fee, so its spend is 0 by design and it is marked is_owned_channel.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `platforms` (array, optional) - Restrict results to these ad platforms (meta, google, snapchat, tiktok, pinterest, klaviyo); omit to include every platform with synced spend in the period.
- `group_by` (string, optional, one of `platform`, `campaign`, `country`) - How to bucket ad spend rows: by platform (default), by campaign name, or by country.

### `get_anomalies`

**Anomalies and Alerts** - scope `mcp:activity:read`

Get recent anomalies detected by MerchantFlow (profit drops, spend spikes, missing sync data, attribution issues).

Parameters:

- `since_days` (number, optional) - How many days back to look for anomalies (1-30, default 7).
- `severity` (string, optional, one of `low`, `medium`, `high`) - Only return anomalies at this severity level; omit to return anomalies of every severity.

### `get_attribution_breakdown`

**Attribution Breakdown** - scope `mcp:ads:read`

Get attributed revenue by channel using MerchantFlow's attribution rules, including organic, paid, email, referral, and direct.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `attribution_model` (string, optional, one of `first_click`, `last_click`, `rule_based`) - Attribution model to apply: 'first_click' credits the first touch, 'last_click' credits the most recent touch before purchase (default), 'rule_based' applies the tenant's configured attribution rules.

### `get_bank_balance`

**Bank Balance** - scope `mcp:pnl:read`

Get the current bank balance, burn rate over the last 30/60/90 days, and projected runway in days.

Parameters:

- `runway_periods` (array, optional) - Day windows to compute burn rate over, e.g. [30, 60, 90] (default [30, 60, 90] when omitted); the largest value also sets how far back the burn history is aggregated, and the 30-day figure drives the runway projection.

### `get_bottom_products`

**Bottom Products by Profit** - scope `mcp:products:read`

Get the bottom N products ranked by profit or margin. Useful for finding SKUs that are losing money. Supports a minimum units filter to drop low-volume noise.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `rank_by` (string, required, one of `profit`, `margin_pct`) - Metric to rank products by, lowest first: net profit after overhead allocation, or net margin percentage.
- `limit` (number, optional) - Maximum number of products to return (default 10, hard-capped at 50).
- `exclude_below_units` (number, optional) - Drop products that sold fewer than this many units in the period, to filter out low-volume noise (default 0, meaning no filter).

### `get_cac_payback`

**CAC and Payback** - scope `mcp:customers:read`

Get customer acquisition cost payback period per channel, showing how long it takes to recoup CAC via customer first-order profit.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).

### `get_channel_roas`

**Channel ROAS** - scope `mcp:ads:read`

Get blended MER (Marketing Efficiency Ratio) and per-platform spend over a date range, with optional comparison to the previous period. Each row also carries platform_reported_revenue and platform_reported_roas - the ad platform’s own self-attributed claim. These figures are non-additive across platforms because Meta and Google may claim the same order; MerchantFlow-attributed revenue remains null in this result.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `compare_to` (string, optional, one of `previous_period`) - Set to 'previous_period' to also compute the same metrics for the immediately preceding period of equal length and return the percentage change in blended MER; omit for no comparison.

### `get_cogs_coverage`

**COGS Coverage** - scope `mcp:cogs:read`

Report how much of the store's catalogue, units sold, and revenue is covered by COGS data over a date range (default: last 30 days), including margin distribution and the top products still missing costs.

Parameters:

- `start_date` (string, optional) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (default: 30 days before end_date).
- `end_date` (string, optional) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (default: today).

### `get_cohort_analysis`

**Customer Cohort Analysis** - scope `mcp:customers:read`

Get customer cohort analysis showing LTV, repeat purchase rate, and revenue by cohort month/week over time.

Parameters:

- `cohort_start_date` (string, required) - Start of the cohort acquisition window in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `cohort_end_date` (string, required) - End of the cohort acquisition window in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `metric` (string, required, one of `ltv`, `repeat_rate`, `revenue`) - Metric to track per cohort period: 'ltv' and 'revenue' both show accumulated revenue per customer over time, 'repeat_rate' shows the repurchase rate.
- `period` (string, required, one of `monthly`, `weekly`) - Cohort grouping granularity: group customers by acquisition month or acquisition week.

### `get_combined_pnl`

**Combined P&L Across Stores** - scope `mcp:pnl:read`

Combined profit and loss across every linked store for a date range (default: last 30 days), converted into one reporting currency. Set per_store to also get the per-store breakdown. Requires a plan covering more than one store.

Parameters:

- `start_date` (string, optional) - Start of the date range, in YYYY-MM-DD format, resolved in the tenant's timezone. Defaults to 30 days before end_date.
- `end_date` (string, optional) - End of the date range, in YYYY-MM-DD format, resolved in the tenant's timezone. Defaults to today.
- `reporting_currency` (string, optional) - ISO 4217 code to convert every store into. Defaults to the primary store currency.
- `per_store` (boolean, optional) - Include the per-store breakdown alongside the combined totals.

### `get_customer_detail`

**Customer Detail** - scope `mcp:customers:read`

Get lifetime value detail for a single customer: net profit, revenue, CAC, tenure, and order history (most recent 200 orders). Customer name and email in the response are partially redacted. The customer identifier is the id returned in the customer lifetime value list.

Parameters:

- `customer_id` (string, required) - Customer id, from list_customers.

### `get_date_range_summary`

**Date Range Summary** - scope `mcp:pnl:read`

Get a high-level summary of revenue, profit, orders, ad spend, and top metrics for an arbitrary date range, suitable for quick time-period comparisons.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).

### `get_discount_code_performance`

**Discount Code Performance** - scope `mcp:marketing:read`

Get per-discount-code margin metrics: uses, revenue, discount cost, COGS, allocated ad spend, gross profit, and margin percent, ranked by any column. Pre-aggregated rolling timeframes provide the fastest results, while an explicit start_date/end_date produces a custom range computed live.

Parameters:

- `timeframe` (string, optional, one of `today`, `7d`, `30d`, `90d`, `1y`) - Pre-aggregated rolling window: 'today', '7d', '30d' (default), '90d', or '1y'. Ignored when start_date and end_date are both provided.
- `start_date` (string, optional) - Custom range start (YYYY-MM-DD, tenant timezone). Requires end_date. Overrides timeframe.
- `end_date` (string, optional) - Custom range end (YYYY-MM-DD, tenant timezone). Requires start_date.
- `sort_by` (string, optional, one of `code`, `uses`, `grossRevenue`, `discountCost`, `totalCOGS`, `adSpendAllocated`, `grossProfit`, `marginPercent`) - Sort field, default 'grossProfit'.
- `sort_order` (string, optional, one of `asc`, `desc`) - Sort direction, default 'desc'.
- `page` (integer, optional) - Page number, 1-based (default 1).
- `page_size` (integer, optional) - Rows per page, 1 to 100 (default 25).

### `get_expenses_breakdown`

**Expenses Breakdown** - scope `mcp:pnl:read`

Get OPEX and CAPEX expenses broken down by category and vendor over a date range, including recurring expenses and CAPEX amortisation.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `category` (string, optional) - Filter to a single expense category, matched exactly against the recorded Expense category; omit to include every category.
- `include_capex` (boolean, optional) - Include CAPEX expenses alongside OPEX in the by_category/by_vendor breakdown (default true); set to false to return only OPEX.

### `get_integration_status`

**Integration Status** - scope `mcp:activity:read`

Get the connection status of all integrations (Shopify, WooCommerce, GA4, ad platforms, SpeedFulfill) including last sync time and any errors.

No parameters.

### `get_item_cogs`

**Item Cost of Goods** - scope `mcp:cogs:read`

Get the current cost of goods sold and full cost history for one item, identified by sku, product_id (internal product id), or variant_id (the commerce platform's variant id, e.g. the Shopify variant id - not an internal uuid). Optional on_date returns the cost effective on that date.

Parameters:

- `sku` (string, optional) - The item's SKU. Provide at least one of sku, product_id, or variant_id.
- `product_id` (string, optional) - The internal MerchantFlow product id (Product.id), not the commerce platform's own product id. Provide at least one of sku, product_id, or variant_id.
- `variant_id` (string, optional) - The commerce platform's own variant id (e.g. the Shopify variant id), not the internal ProductVariant.id. Provide at least one of sku, product_id, or variant_id.
- `on_date` (string, optional) - Return the cost effective on this date, in YYYY-MM-DD format, resolved in the tenant's timezone (default: today).

### `get_ltv_summary`

**Lifetime Value Summary** - scope `mcp:customers:read`

Get customer lifetime value summary including average LTV, LTV by acquisition channel, and LTV:CAC ratio.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `segment_by` (string, optional, one of `channel`, `first_product`, `country`) - How to segment LTV: 'channel' groups by acquisition channel (only available when attribution is enabled for the tenant), 'country' groups by shipping country, 'first_product' is not supported in this MCP release and returns no segment rows. Defaults to 'channel' when attribution is enabled for the tenant, otherwise 'country'.

### `get_market_products`

**Products by Market** - scope `mcp:pnl:read`

Get the Markets country drilldown for a date range, ranked by variant and bundle contribution margin using the same service as the dashboard.

Parameters:

- `country_code` (string, required) - ISO 3166-1 alpha-2 shipping country code to drill into, e.g. 'US' or 'AU'.
- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive); clamped forward to the plan's history window if it reaches further back than allowed.
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `limit` (integer, optional) - Maximum number of variants (and bundles, if included) to return, ranked by contribution margin (default 50, hard-capped at 100).
- `include_bundles` (boolean, optional) - Include product bundle rows alongside individual variants (default true).

### `get_markets`

**Markets Overview** - scope `mcp:pnl:read`

Get the Markets dashboard table for a date range, including real geo ad spend, blended fallback spend, revenue, net profit, margins, ROAS, POAS, CAC, and spend-without-orders markets.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive); clamped forward to the plan's history window if it reaches further back than allowed.
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `country_codes` (array, optional) - Restrict results to these ISO 3166-1 alpha-2 shipping country codes (up to 50); omit to return every market with activity in the period.
- `include_spend_without_orders` (boolean, optional) - Include markets that had ad spend but no orders in the period (default true); set to false to hide spend-without-orders markets.
- `sort_by` (string, optional, one of `dashboard`, `net_profit`, `revenue`, `orders`, `spend`, `net_margin_pct`, `roas`, `poas`, `cac`) - Metric to sort markets by, highest first. 'dashboard' (default) uses the dashboard's own net-profit-based ordering; other values sort directly by that metric: net_profit, revenue, orders, spend, net_margin_pct, roas, poas, cac.
- `limit` (integer, optional) - Maximum number of markets to return after sorting (default 50, hard-capped at 100).

### `get_mca_status`

**Revenue-Based Funding Status** - scope `mcp:pnl:read`

Get active revenue-based funding (MCA) agreements, repayment schedule, and impact on current period P&L.

No parameters.

### `get_north_star_status`

**North Star Metrics** - scope `mcp:north-star:read`

Get the current status of all configured North Star KPIs with target, actual, delta, and trend direction.

Parameters:

- `period` (string, optional, one of `today`, `week`, `month`, `quarter`) - Comparison window for the KPIs: 'today', 'week' (last 7 days), 'month' (last 30 days), or 'quarter' (last 90 days). Defaults to 'month' when omitted.

### `get_organic_revenue`

**Organic Revenue Split** - scope `mcp:pnl:read`

Get organic vs paid vs direct revenue for a date range, classified from order-level UTM parameters and referrer data captured at checkout - NOT from Google Analytics 4 sessions, pageviews, or traffic data. Includes an attribution-confidence score, optional period-over-period growth, a channel breakdown, and an optional daily trend. Requires the attribution feature flag to be enabled for the tenant; returns attribution_disabled otherwise.

Parameters:

- `start_date` (string, required) - Range start (YYYY-MM-DD, tenant timezone).
- `end_date` (string, required) - Range end (YYYY-MM-DD, tenant timezone).
- `compare_previous` (boolean, optional) - Include a comparison against the immediately preceding period of equal length (default true).
- `include_channels` (boolean, optional) - Include a per-channel breakdown (Organic Search, Organic Social, Email, Referral, Direct, Other Organic) (default true).
- `include_trend` (boolean, optional) - Include a daily organic-vs-paid revenue trend for the range (default false - can be large for long ranges; capped at 100 days by the response formatter).

### `get_pnl_summary`

**Profit and Loss Summary** - scope `mcp:pnl:read`

Get a profit and loss summary for the tenant's store over a date range, broken down by revenue, COGS, ad spend, expenses, fees, and net profit. Optionally compare to the previous period or previous year for percentage deltas.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `compare_to` (string, optional, one of `previous_period`, `previous_year`) - Optional comparison window - 'previous_period' compares to the immediately preceding range of equal length; 'previous_year' compares to the same date range last year

### `get_product_detail`

**Product Detail** - scope `mcp:products:read`

Get detailed profitability for a specific product including current catalogue price, variant-level pricing breakdown, COGS, and 90-day trend from the analytics snapshots.

Parameters:

- `product_id` (string, required) - The internal MerchantFlow product id (Product.id, the same value returned as product_id by get_top_products/get_bottom_products/find_cogs_gaps), not the commerce platform's own product id.

### `get_recent_activity`

**Recent Activity** - scope `mcp:activity:read`

Get a chronological feed of recent tenant activity: syncs, large orders, and integration events.

Parameters:

- `since_hours` (number, optional) - How many hours back to look for activity (1-168, default 24).
- `activity_types` (array, optional) - Only include these activity types in the feed (e.g. 'sync', 'large_order', 'integration_event'); omit to include every type.

### `get_revenue_breakdown`

**Revenue Breakdown** - scope `mcp:pnl:read`

Get revenue broken down by source (organic, paid, direct, email, referral), by channel, or by country over a date range.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `group_by` (string, required, one of `source`, `channel`, `category`, `country`) - How to bucket revenue: 'source' groups by the order's attribution source (organic, paid, direct, email, referral), 'channel' groups by the named ad or marketing channel, 'country' groups by the ISO 3166-1 alpha-2 shipping country code, and 'category' currently returns no rows in this MCP release (use get_top_products for per-product revenue instead). 'source' and 'channel' require attribution to be enabled for the tenant.

### `get_store_list`

**Connected Stores** - scope `mcp:store:read`

List the stores linked to this account, with each store's platform, currency, timezone, connection state and last sync time. The result defines the store set available for combined figures.

No parameters.

### `get_tax_insights`

**Tax Insights** - scope `mcp:pnl:read`

Get period tax totals and the blended effective tax rate over a trailing N-day window, plus a per-country split. Tax figures combine tax the platform reported on orders with tax computed from active manual TaxRule entries where the platform reported none (or a fixed-amount rule applies). Mirrors the dashboard tax settings page tiles.

Parameters:

- `days` (integer, optional) - Trailing window in days, 1 to 365 (default 30).

### `get_top_products`

**Top Products by Profit** - scope `mcp:products:read`

Get the top N products ranked by revenue, profit, margin, or units sold over a date range using the same order-based product profit math as the dashboard.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `rank_by` (string, required, one of `revenue`, `profit`, `margin_pct`, `units`) - Metric to rank products by, highest first: gross revenue, net profit after overhead allocation, net margin percentage, or units sold.
- `limit` (number, optional) - Maximum number of products to return (default 10, hard-capped at 50).

### `get_unattributed_revenue`

**Unattributed Revenue** - scope `mcp:ads:read`

Get revenue that MerchantFlow couldn't attribute to a known channel, with order count, percentage of total revenue, and recent examples.

Parameters:

- `start_date` (string, required) - Start of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).
- `end_date` (string, required) - End of the date range in YYYY-MM-DD format, resolved in the tenant's timezone (inclusive).

### `list_capabilities`

**Account Capabilities** - scope `mcp:activity:read`

Report this connection's plan tier, available history, cross-store availability, current rate-limit headroom, and known data limits.

No parameters.

### `list_cogs`

**Cost of Goods List** - scope `mcp:cogs:read`

List cost-of-goods-sold entries for all items and variants in this store, newest effective date first, enriched with the matching product and variant. Paginate with page/page_size; filter by SKU substring or effective-date range.

Parameters:

- `sku_contains` (string, optional) - Case-insensitive substring match against the SKU; omit to return entries for every SKU.
- `effective_from` (string, optional) - Only include entries effective on or after this date, in YYYY-MM-DD format, resolved in the tenant's timezone.
- `effective_to` (string, optional) - Only include entries effective on or before this date, in YYYY-MM-DD format, resolved in the tenant's timezone.
- `page` (number, optional) - Page number to return, 1-indexed (default 1).
- `page_size` (number, optional) - Number of entries per page (default 50, hard-capped at 100).

### `list_customers`

**Customer Lifetime Value List** - scope `mcp:customers:read`

List customers ranked by lifetime value (net profit after allocated overhead, summed across each customer's full order history) - the same source as the dashboard Customers page. start_date/end_date filter WHICH customers appear, by their first-order date; they do NOT clamp a customer's lifetime totals to that window. Customer name and email in the response are partially redacted. Each returned id identifies a customer record whose detail includes up to 200 recent orders.

Parameters:

- `start_date` (string, optional) - Only include customers whose first order falls on or after this date (YYYY-MM-DD, tenant timezone). Omit for all-time.
- `end_date` (string, optional) - Only include customers whose first order falls on or before this date (YYYY-MM-DD, tenant timezone). Omit for all-time.
- `sort` (string, optional, one of `marginLtv`, `revenueLtv`, `orderCount`, `firstOrderAt`) - Sort key: 'marginLtv' (net profit, default), 'revenueLtv', 'orderCount', or 'firstOrderAt'.
- `dir` (string, optional, one of `asc`, `desc`) - Sort direction, default 'desc'.
- `page` (integer, optional) - Page number, 1-based (default 1).
- `limit` (integer, optional) - Rows per page, 1 to 50 (default 25).

### `list_reports`

**List Reports** - scope `mcp:reports:read`

List every report available to this store: saved template reports, custom reports, and the built-in template catalogue. Each returned report id or template key identifies a report available for generation.

Parameters:

- `type` (string, optional, one of `template`, `custom`) - Restrict the listing to "template" (the built-in report catalogue) or "custom" (saved custom reports); omit to list both.
- `include_archived` (boolean, optional) - Include archived saved reports in the listing (default false, archived reports are hidden).

### `lookup_order`

**Look Up Order** - scope `mcp:orders:read`

Look up a single order by number and return its line items, margin, fulfillment state, and refund history.

Parameters:

- `order_number` (string, required) - Order number as shown in the store, with or without a leading "#" (for example "1001" or "#1001").

### `query_order_basket_analytics`

**Order Basket Analytics** - scope `mcp:pnl:read`

Analyse orders filtered by what is IN the basket (which products, and how many units), broken down by region, channel or month. Answers questions the pre-computed dashboard context cannot, such as 'orders containing two chairs, average shipping cost per region'. Returns order counts, net revenue, and BOTH shipping figures: what customers were charged (revenue) and what fulfilment actually cost the merchant, with an explicit coverage percentage for the cost side.

Parameters:

- `start_date` (string, required) - Inclusive start of the window, YYYY-MM-DD, in the store's timezone.
- `end_date` (string, required) - Inclusive end of the window, YYYY-MM-DD, in the store's timezone.
- `product_ids` (array, optional) - Only count orders whose basket contains these products. Get IDs from resolve_products. Omit to analyse all orders in the window.
- `min_quantity` (integer, optional) - Order must contain at least this many units across product_ids. Use for 'two or more chairs'. Mutually exclusive with exact_quantity.
- `exact_quantity` (integer, optional) - Order must contain exactly this many units across product_ids. Use for 'orders with two chairs'. Mutually exclusive with min_quantity.
- `region_codes` (array, optional) - Restrict to these ISO 3166-1 alpha-2 shipping country codes, e.g. ['AU','NZ'].
- `sales_channel` (string, optional) - Restrict to a single sales channel value.
- `group_by` (string, optional, one of `none`, `shipping_country`, `sales_channel`, `month`) - Dimension to break results down by. Defaults to 'none' (one total row).
- `limit` (integer, optional) - Maximum groups to return, highest order count first. Defaults to 50.

### `resolve_products`

**Resolve Product Names** - scope `mcp:products:read`

Resolve a product name, category word or SKU (e.g. 'chairs', 'oak desk', 'CHR-01') to concrete product IDs in this store's catalog. Each match includes a similarity score and supports disambiguation of natural-language product references for product-level basket analysis.

Parameters:

- `query` (string, required) - Product name, category word, or SKU to look up.
- `limit` (integer, optional) - Maximum matches to return. Defaults to 10.

### `run_abandoned_cart_identifier`

**Abandoned Cart Candidates** - scope `mcp:marketing:read`

Recent abandoned checkouts with recoverable value. Read-only - does not send messages.

Parameters:

- `days` (integer, optional) - How many days back to look for abandoned checkouts, from 1 to 30 (default 7).

### `run_business_valuation`

**Business Valuation** - scope `mcp:valuation:read`

Run the SDE-multiple business valuation for the tenant based on current P&L data, growth, margin, MER, and risk scoring. Returns valuation range with sensitivity analysis.

Parameters:

- `lookback_months` (number, optional) - How many months of P&L history to use for the valuation (1-36, default 12). 6 or fewer switches the calculation to 6-month mode; more uses 12-month mode, matching the dashboard valuation page.

### `run_collection_membership_audit`

**Collection Membership Audit** - scope `mcp:store:read`

Collections in the store with product count and last-updated date, flagging empty collections. Returns the first "limit" collections and reports how many matched in total. The result covers collection hygiene, empty collections, and potentially stale collections.

Parameters:

- `limit` (integer, optional) - Maximum number of matching rows to return, sorted worst-first (default 50, hard-capped at 100). The response reports the total number of rows that matched even when more were found than were returned.

### `run_customer_spend_tier_classifier`

**Customer Spend Tiers** - scope `mcp:marketing:read`

Classify customers into VIP / regular / casual / one-time tiers based on lifetime spend and order count.

Parameters:

- `vip_spend_threshold` (number, optional) - Lifetime spend, in the tenant currency, at or above which a customer is classified VIP (default 1000).
- `regular_spend_threshold` (number, optional) - Lifetime spend, in the tenant currency, at or above which a customer is classified regular rather than casual (default 300).
- `window_days` (integer, optional) - How many days of order history to consider when computing lifetime spend and order count, from 30 to 1825 (default 365).

### `run_dead_stock_report`

**Dead Stock Report** - scope `mcp:inventory:read`

Identify products with zero sales in the window and (when Shopify is connected) their current on-hand inventory.

Parameters:

- `timeframe` (string, optional, one of `30d`, `90d`, `1y`) - Window to check for zero sales activity before a product counts as dead stock (default 90d).

### `run_fulfillment_digest`

**Fulfilment Digest** - scope `mcp:orders:read`

Digest of open orders by fulfillment status and age. Surfaces orders stuck for more than 3 days.

Parameters:

- `days` (integer, optional) - How many days back to look for open orders (default 30, 1 to 180).

### `run_gift_card_balance_report`

**Gift Card Balances** - scope `mcp:store:read`

Outstanding gift card balance grouped by currency plus redemption percentage against initial issuance.

No parameters.

### `run_high_risk_order_report`

**High-Risk Orders** - scope `mcp:orders:read`

Shopify-flagged orders with medium or high fraud risk in the recent window. Read-only.

Parameters:

- `days` (integer, optional) - How many days back to scan for flagged orders (default 7, 1 to 30).
- `min_level` (string, optional, one of `LOW`, `MEDIUM`, `HIGH`) - Minimum Shopify fraud risk level to include: LOW includes every flagged order, MEDIUM (the default) excludes LOW-risk orders, HIGH returns only the highest-risk orders.

### `run_inventory_valuation`

**Inventory Valuation** - scope `mcp:inventory:read`

Total dollar value of inventory currently on hand (on-hand quantity x recorded COGS per SKU).

Parameters:

- `top_n` (integer, optional) - Maximum number of highest-value SKUs to include in the returned breakdown (default 50).

### `run_multi_location_inventory_audit`

**Multi-Location Inventory Audit** - scope `mcp:inventory:read`

Find variants that are out of stock at some locations but available at others - candidates for transfers.

Parameters:

- `min_locations` (integer, optional) - Minimum number of distinct stock locations a variant must be tracked at to be considered for a transfer candidate (default 2).

### `run_page_content_audit`

**Page Content Audit** - scope `mcp:store:read`

Store pages flagged by content thinness, unpublished status, or staleness.

Parameters:

- `stale_days` (integer, optional) - Number of days since a page was last updated before it is flagged as stale (default 180).
- `min_body_chars` (integer, optional) - Minimum body content length in characters required to avoid being flagged as thin content (default 100).
- `limit` (integer, optional) - Maximum number of matching rows to return, sorted worst-first (default 50, hard-capped at 100). The response reports the total number of rows that matched even when more were found than were returned.

### `run_product_completeness_score`

**Product Completeness Score** - scope `mcp:store:read`

Scores every product on a 0-100 scale based on images, SEO fields, description length, and taxonomy.

Parameters:

- `limit` (integer, optional) - Maximum number of lowest-scoring products to return, sorted worst-first (default 50, minimum 10, hard-capped at 100).

### `run_product_image_audit`

**Product Image Audit** - scope `mcp:store:read`

Products without a featured image or fewer than N total images.

Parameters:

- `min_images` (integer, optional) - Minimum number of images a product must have to pass the audit; products with fewer (or no featured image) are flagged (default 1).
- `limit` (integer, optional) - Maximum number of matching rows to return, sorted worst-first (default 50, hard-capped at 100). The response reports the total number of rows that matched even when more were found than were returned.

### `run_product_viability`

**Product Viability Score** - scope `mcp:products:read`

Run a product viability simulation: given a proposed selling price, COGS, and expected ad spend, compute break-even ROAS, contribution margin, and sensitivity analysis against store averages.

Parameters:

- `price` (number, required) - Proposed selling price per unit, in the tenant's currency; must be greater than 0.
- `cogs` (number, required) - Proposed cost of goods sold per unit, in the tenant's currency.
- `expected_ad_spend_per_unit` (number, required) - Expected ad spend required to sell one unit, in the tenant's currency (this is what break_even_roas is measured against).
- `expected_volume_per_month` (number, optional) - Expected units sold per month; when provided, the response includes a monthly_projection of contribution and ad spend (omitted otherwise).
- `shipping_cost` (number, optional) - Shipping cost per unit not already covered by COGS, in the tenant's currency (default 0).

### `run_repeat_purchase_rate`

**Repeat Purchase Rate** - scope `mcp:orders:read`

Percentage of customers in the selected window who placed two or more orders.

Parameters:

- `days` (integer, optional) - Size of the trailing window in days used to compute the repeat purchase rate (default 90, 7 to 730).

### `run_sales_by_channel_report`

**Sales by Channel** - scope `mcp:marketing:read`

Revenue, orders, profit, and AOV broken down by acquisition channel. Requires the attribution feature flag to be enabled for the tenant.

Parameters:

- `days` (integer, optional) - How many trailing days to summarize by channel, from 7 to 365 (default 30).

### `run_seo_metadata_audit`

**SEO Metadata Audit** - scope `mcp:store:read`

Products missing SEO title or with SEO description shorter than threshold.

Parameters:

- `min_description_length` (integer, optional) - Minimum SEO description character length required to pass; products with a shorter or missing SEO description are flagged (default 50).
- `limit` (integer, optional) - Maximum number of matching rows to return, sorted worst-first (default 50, hard-capped at 100). The response reports the total number of rows that matched even when more were found than were returned.

### `run_stock_velocity`

**Stock Velocity** - scope `mcp:inventory:read`

Rank products by units sold in the selected timeframe and classify them as fast, steady, slow, or dead.

Parameters:

- `timeframe` (string, optional, one of `7d`, `30d`, `90d`, `1y`) - Lookback window used to compute units sold and velocity classification (default 30d).
- `limit` (integer, optional) - Maximum number of ranked products to return (default 50, hard-capped at 100).

### `run_url_redirect_audit`

**URL Redirect Audit** - scope `mcp:store:read`

URL redirects in the store, flagging loops, empty targets and redirect chains. Returns the first "limit" redirects and reports the total matched. The result covers broken links, redirect loops, and SEO risks from redirect chains after a replatform.

Parameters:

- `limit` (integer, optional) - Maximum number of matching rows to return, sorted worst-first (default 50, hard-capped at 100). The response reports the total number of rows that matched even when more were found than were returned.

### `run_win_back_candidates`

**Win-Back Candidates** - scope `mcp:marketing:read`

Identify valuable customers who haven't purchased in the last N days.

Parameters:

- `inactive_days` (integer, optional) - Minimum days since a customer last purchased to count as inactive, from 30 to 730 (default 90).
- `min_lifetime_spend` (number, optional) - Minimum lifetime spend a customer must have to be considered valuable enough to win back, in the tenant currency (default 100).
- `limit` (integer, optional) - Maximum number of candidates to return, from 10 to 500 (default 100).

### `run_wismo_digest`

**Where Is My Order Digest** - scope `mcp:marketing:read`

Where Is My Order digest - in-flight orders with tracking status, age, and destination.

Parameters:

- `days` (integer, optional) - How many trailing days of in-flight orders to include in the digest, from 1 to 90 (default 14).

### `search`

**Search MerchantFlow** - scope `mcp:products:read`

Search this MerchantFlow store for products and orders matching a query. Returns retrieval documents with an id, title, and URL; each id resolves to its full record. This endpoint provides record retrieval rather than profit, ad, cohort, or valuation analytics.

Parameters:

- `query` (string, required) - Free-text search string matched against product names/SKUs and order numbers (truncated to 200 characters).

### `search_orders`

**Search Orders** - scope `mcp:pnl:read`

Search orders by date range, customer email, order number, or product SKU. Returns a summary of matching orders with profit per order. Hard-capped at 100 results.

Parameters:

- `start_date` (string, optional) - Start of the date range, in YYYY-MM-DD format, resolved as the start of that day in the tenant's timezone. At least one of start_date, end_date, customer_email, order_number, or sku is required.
- `end_date` (string, optional) - End of the date range, in YYYY-MM-DD format, resolved as the end of that day in the tenant's timezone.
- `customer_email` (string, optional) - Customer email to search for; it is hashed before querying so no plaintext email is used as a lookup key, and the customer_email field on each returned order is redacted.
- `order_number` (string, optional) - The store's own order number, with or without a leading '#', not the internal MerchantFlow order id.
- `sku` (string, optional) - Product SKU to match against any line item on the order.
- `limit` (number, optional) - Maximum number of orders to return (default 20, hard-capped at 100).
