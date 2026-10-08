# Shared Ads Manager Insights Contract

This reference owns metric interpretation and reporting comparability. Skills own evidence collection and presentation; tool schemas own arguments, defaults, dependencies, and supported request shapes. Tool errors own recovery instructions. Recommendation thresholds belong to the review skill.

## Common Rules

- State the account or resource, reporting period, granularity, and applicable attribution settings. Use completed account-local periods and distinguish current configuration or delivery checks from historical performance.
- Compare matching scopes and report definitions. Inspect returned rows and pagination such as `has_more`; distinguish measured zero, missing or null values, empty results, partial coverage, and failed reads. Never infer missing metrics or turn unavailable data into zero.
- Corrections and split reports must preserve the requested dates, scope, aggregation, filters, and attribution settings. Cover the full requested report across splits; disclose any remaining gaps. Ask before changing an unsupported request rather than substituting a default or example window.
- Use backend values at the requested grain. Never calculate or reconstruct attributed sales, ROAS, CPA, or post-click CVR from other fields. A returned currency does not make a missing amount available.
- Monetary metrics use their returned currency or the resolved account currency where specified. Do not guess currencies, combine different currencies, or confuse reporting amounts with budget/bid micros.
- Label synthetic test values as synthetic. A successful empty response verifies neither metric values nor calculation accuracy.

### Metric Glossary

| Metric | Meaning and units | Attribution and availability |
| --- | --- | --- |
| `impressions`, `clicks` | Delivery counts | Requested scope and reporting period; absent values remain unavailable. |
| `spend`, `cpc`, `cpm` | Account-currency amount, cost per click, cost per 1,000 impressions | Backend delivery metrics; preserve returned zero or unavailable values. |
| `ctr` | Clicks per impression, a fraction (`0.04` displays as 4%) | Backend rate for the requested grain. |
| `order_created_attributed_sales` and its `_currency` | Attributed order-created sales value and currency | Not total business sales; zero is measured zero, null is unavailable. |
| `order_created_roas` | Attributed order-created ROAS, a dimensionless multiple | Backend ratio, unavailable when its required values are unavailable or spend is not positive. |
| `cpa`, `post_click_cvr` | Backend cost per attributed conversion in account currency; post-click conversion rate as a fraction | Use the performance tool's attribution contract; conversion-report settings do not customize these fields. |
| Conversion `conversions` | Goal-matched click-through plus selected view-through conversion counts | Selected click/view windows and date basis; not unique customers. Response `count` counts summary rows. |
| Nested attributed events | Event counts; optional value amount, value count, and currency | The same windows and date basis as the summary. Value count is separate from event count; missing or null values remain unavailable. |

## General Performance

Use `get_ad_account_insights` for account-wide comparisons or rankings and the matching campaign, ad-group, or ad insights tool for one resolved resource. Resource scope constrains the population; `aggregation_level` controls the rows within that population.

For a requested top-N by impressions, clicks, spend, CTR, CPC, or CPM, use entity aggregation, `time_granularity="none"`, the supported metric sort, and the requested limit. A backend-sorted top-N does not require every page unless the page is short, marked partial, or complete coverage was requested. Do not treat an arbitrary first page as a full-scope ranking.

If “best,” “top,” or “worst” has no defined metric, ask which supported metric or KPI should determine it. Do not choose a business objective from available data.

## Sales Efficiency

Request canonical performance fields on the matching general insights tool. Do not request deprecated `attributed_sales_amount`, `attributed_sales_count`, `attributed_sales_currency`, or `roas` aliases, or replace missing performance metrics with conversion-report values.

- Use one complete, completed account-local date range per call and `none`, `daily`, or `monthly` granularity. Prefer date-only intervals; partial days and hour-range requests are unsupported.
- Do not combine sales fields with hourly granularity, segments, product aggregation, segment group overrides, or filters/sorts on sales fields. Supported entity filters must match the aggregation level or an ancestor; product and segment filters are unsupported.
- Request `order_created_attributed_sales_currency` with `order_created_attributed_sales`. Compare amounts only when both currencies are present and equal. Describe the values as attributed order-created sales or attributed order-created ROAS.
- ROAS is a reference metric by default, alongside available spend, sales, and the period. Do not equate highest ROAS with best overall performance or recommend a change from ROAS alone. Rank by ROAS only when explicitly requested: fetch all relevant pages, require comparable scope and periods and reported ROAS for every candidate, then rank locally. Never send a ROAS sort to the API.
- If ranking coverage or values are incomplete, state the gap without declaring a full-scope winner or substituting another metric. Treat unavailable or gated metrics as data gaps. Do not assign a good/bad ROAS threshold without a user-supplied target or account evidence.

## Conversion Reporting

Use `get_conversion_insights` for goal totals and optional individual event details. Match `aggregation_level` to the supplied campaign, ad-group, or ad IDs. Omit IDs only for a combined account total with `group_by_entity=false`; comparisons use grouped rows. For conversion rankings, collect all candidates, request aligned batches of at most 1,000 IDs with aggregate granularity, and rank the returned goal counts. Disclose incomplete batching.

## Raw Diagnostics And Inventory

Use `list_conversion_sources` for connected sources and pixel IDs, and `list_conversion_event_settings` for current configured event types and source/campaign associations. This is configuration inventory, not historical performance.

Use `list_conversion_events` only for recent raw-event diagnostics after resolving the source `pixel_id`. It returns at most 50 sampled events from the latest 15 minutes. Do not present that sample as historical attributed conversions or complete received-event coverage.
