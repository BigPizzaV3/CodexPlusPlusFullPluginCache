---
name: analyze-marketing-data
description: Use whenever the user asks about marketing, advertising, web analytics, e-commerce, CRM or payments data connected to Power My Analytics, such as spend, clicks, conversions, revenue, ROAS, orders, sessions or campaigns on any connected platform. Covers finding the right connector and fields, choosing the right Power My Analytics tool, and reporting numbers accurately.
---

# Analyze marketing data with Power My Analytics

Power My Analytics (PMA) warehouses the user's data from 85+ marketing platforms. Every answer should come from the user's real numbers through the PMA tools, never from estimates.

## 1. Always start by finding the data

1. Call `pma_list_data_sources` unless you already have the connector types from earlier in this conversation.
   - Copy `connector_type` and `account_id` values exactly as returned. Never guess them: the stored type (for example `facebook`) can differ from the common name (`facebook_ads`).
   - When the user asks about one platform, pass `connector_type_filter` (for example `facebook` or `google`). Facebook and Google are stored as several connector types that can land on different pages.
   - When the user names a client, store, brand or account, pass `name_filter`. Client names often live on sub-accounts, so never conclude a client is missing without trying it.
   - If `has_more` is true, read every page before saying a platform is not connected.
2. Before passing explicit metric or dimension names, call `pma_describe_platform` for that connector and report type (once per conversation is enough). Use `field_search` to find a field quickly.
3. Choose the right report type. On ad platforms, `campaigns` holds settings only (name, status, budget). Performance metrics live on the insights level: `campaign_insights` for Facebook Ads, `campaigns_insights` for Google Ads. Common others: Shopify and WooCommerce `orders`, Stripe `transactions`, HubSpot `deals`, Salesforce `opportunities`, Amazon Ads `performance_campaigns`, GA4 `daily_insights`.

## 2. Pick the right tool

| The user wants | Use |
| --- | --- |
| Totals or a snapshot for one or more platforms | `pma_get_account_summary` (spend, conversions, revenue, ROAS only); `pma_query_custom` with `aggregate_only=true` for any other metric |
| Rankings, breakdowns, top N, grouping by campaign, account or date | `pma_query_custom` |
| One metric compared across 2 to 10 platforms | `pma_compare_sources` |
| This period vs a previous period (WoW, MoM, YoY, custom) | `pma_get_date_range_comparison` (use `custom` mode for calendar months) |
| A metric over many days, weeks or months | `pma_get_trend` |
| Why a metric moved, and which segments drove it | `pma_analyze_drivers` |
| Unusual days | `pma_detect_significant_anomalies` (seasonality-aware, with confidence); `pma_detect_anomalies` for a quick multi-metric scan |
| When a metric stepped to a new level | `pma_detect_changepoints` |
| Whether a pattern is normal for the day of week | `pma_detect_seasonality` |
| Pace for the month, or what comes next | `pma_forecast` |
| Repeat customers and retention | `pma_analyze_cohorts` (commerce and CRM data only, never ad platforms) |
| Individual records ("show me the last 20 orders") | `pma_query_performance` |
| A saved, blended report to reuse in Sheets, Data Studio or Power BI | `pma_list_datasets`, `pma_create_dataset` |

If you are unsure whether a statistical analysis can run on a metric, call `pma_list_available_analyses` first. When a tool says an analysis cannot run, pass its reason to the user as written.

## 3. Field names differ by platform

- Google Ads: spend is `cost`, revenue is `conversions_value`.
- Amazon Ads: spend is `cost`, conversions `attributedConversions14d`, revenue `attributedSales14d`.
- Shopify: revenue is `order_total_amount` on `orders`. Stripe: `transaction_amount` on `transactions`. These have no spend column, so ROAS does not apply to them on their own.
- If a metric comes back null, look up the right name with `pma_describe_platform` before telling the user the data is missing.

## 4. Accuracy rules

- **Never add or average rates.** CTR, CPC, CPA, ROAS, conversion rate and frequency must be computed from their component totals (for example ROAS = total conversion value / total spend), not by summing or averaging the rate.
- **Match the grain before combining.** Ad platform insights are stored per day; orders and transactions are stored per record. `max`, `min` and `avg` work at that natural grain. When combining sources, aggregate each to the same period first, then combine. Default to `sum` when in doubt.
- **Do not mix currencies.** Report amounts per currency rather than adding them together.
- **Platform conversions overlap.** Each ad platform reports conversions under its own attribution model, so adding conversions across platforms overstates the true total. Say this when you show combined conversions, and use a source of truth such as Shopify, Stripe or GA4 for actual orders or revenue when it is connected.
- **Respect data freshness.** `data_through` is the latest date the warehouse has; the most recent day may not be loaded yet. Do not present a partial month or week as a decline; use `pma_forecast` for pacing and label projections as projections, with their range.
- **Gaps are not drops.** Days with no data are sync gaps. Report them separately from real anomalies.

## 5. When data seems missing

An empty result does not mean no activity. Check, in order: the right `connector_type` and report type, the `has_data` and `last_sync` fields (widen the date range if the last sync is old), `pma_inspect_org_data` for that connector, and `pma_get_token_health_summary` for broken connections. If a connection needs attention, tell the user to reconnect the account in the Power My Analytics app.

## 6. Presenting results

- Lead with the answer, then the supporting numbers.
- State the date range and which platforms and accounts are included.
- Use platform names people recognize (Facebook Ads, Google Ads), never internal connector codes.
- Format currency and round sensibly; use a small table when comparing more than two items.
- When the user will run the same analysis again, suggest saving it as a dataset.

## 7. Limits

- The tools read data and can create datasets. They cannot change campaigns, budgets or ads.
- Connecting new accounts and billing happen in the Power My Analytics app, not in chat.
- `pma_create_dataset` needs the user to confirm the dataset name first. Show the proposed name, wait for approval, then create it.
