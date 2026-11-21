# Metrics and detectors

Authoritative definitions are also returned by the tools themselves (`data_quality.limitations`, the `detectors` list in `get_anomalies`, `evidence.rule` on each anomaly). If anything here disagrees with a tool result, trust the tool result.

## Metrics

- **Visitors**: distinct visitors seen by the Eskopia pixel in the window.
- **Orders / revenue**: from Shopify order webhooks (plus any CSV-imported history), by the time Eskopia received them. Mixed currencies are added without conversion (flagged in `data_quality`).
- **Conversion rate**: orders / visitors in the same window.
- **Average order value**: revenue / orders.
- **Checkout**: one checkout token, counted in the window it started. **Completed** if the pixel reported completion or an order webhook carried the same token.
- **Funnel**: distinct visitors who viewed a product, added to cart, reached checkout, completed. Step conversion is only given when at least 5 reached the previous step.
- **Product add-to-cart rate**: distinct visitors who added the product / distinct visitors who viewed it. No purchase data per product.
- **Comparisons**: concrete earlier windows in the store's timezone (previous period, same time yesterday, same weekday last week, or the last 4 same weekdays as min/average/max).

## Detectors (fixed rules, every 15 minutes, store timezone)

| Detector | Fires when | Severity |
|---|---|---|
| no_orders | Zero orders in the last 3h while the same 3h on recent same weekdays averaged 3+ orders | critical if that average is 6+ |
| revenue_drop | Revenue since local midnight is 30%+ below the average of the same window on the last 4 same weekdays AND below the lowest of them (an average of 50+ orders per comparison window, not a total; 2+ weeks of order history) | critical at 60%+ |
| traffic_drop | Visitors since local midnight are 50%+ below the average of the last 4 same weekdays (30+ visitors) | critical at 75%+ |
| checkout_completion_drop | Completed share of today's checkouts (100+) is below 60% of the pooled rate on recent same weekdays (300+) | critical below 30% |
| tracking_gap | 2+ webhook orders in the last hour but zero pixel events, with pixel activity in the prior week | always critical |
| abandoned_checkout_spike | 10+ checkouts started 30 min to 3h ago never completed, and at least 2x the usual number | critical at 4x |
| webhook_gap | 3+ checkouts reported completed by the pixel in 3h but zero order webhooks, with webhooks in the prior week | always critical |

**Not enough data**: a check below its minimum samples is `insufficient_data` (in `current_checks`, `checks_without_enough_data`, and the `limited_data` / `insufficient_data` overall statuses). It made no determination: never describe it as healthy, normal or "no anomaly".

Lifecycle: an anomaly is **active** while its rule keeps firing (`last_confirmed_at` updates), and **resolved** when the rule evaluates clear (`resolution: cleared`) or after 24h without confirmation (`stale`). Thresholds are Eskopia's initial defaults, not validated statistics.

**Onset** (from `investigate_store_change`): the first hour starting a run of 2+ consecutive hours each below 50% of the comparison; recovery is the first later hour back at or above it.
