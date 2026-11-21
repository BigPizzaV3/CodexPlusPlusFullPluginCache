# Workflows

All tools accept an optional `store_id` (from `list_stores`); omit it to use the connected store. Use `list_stores` if the merchant mentions a store you can't match, or to explain `store_not_ready`.

## 1. Quick status

`get_store_health` with `detail: "brief"`.
Answer: "Eskopia status: **ok / limited_data / insufficient_data / attention / critical**" plus up to three `priorities` in order. For `limited_data` or `insufficient_data`, name the checks in `checks_without_enough_data` and say they couldn't check anything, which is not the same as healthy. If `ok`, add one line of today's numbers vs normal (`today_vs_recent_same_weekdays`). Under 80 words unless asked.

## 2. Detailed health report

`get_store_health` with `detail: "full"`; add `get_performance` (`period: "today"`, `compare_to: "last_4_same_weekdays"`) if the merchant wants numbers.
Sections: overall status and why (cite `overall_status_rule`), active anomalies, pipeline checks (pixel and order webhook), each detector's current state (including "not enough data"), today vs normal (`position`: below/within/above range), rule-based insights.

## 3. Live activity

`get_live_activity`, with `window_minutes` matching the question (10, 60, ...).
Report `live_now` (visitors by activity, top countries), the recent window (visitors, event counts, orders), recent orders (no customer details), open checkouts, and `compared_with_recent_same_weekdays` position. "Cart" means the visitor's latest action was cart-related, not Shopify's saved carts.

## 4. Performance and comparisons

`get_performance` with:
- "today vs yesterday": `period: "today"`, `compare_to: "same_time_yesterday"`
- "vs same day last week": `compare_to: "same_weekday_last_week"`
- "normal for this time of day", "better or worse than normal": `compare_to: "last_4_same_weekdays"` (report `position` and the min/average/max range; never call it statistically significant)
- "this week vs last week": `period: "this_week"`, `compare_to: "previous_period"`
- "last Wednesday" or a specific span: `start`/`end` with offsets, plus `compare_to` as needed
- "when did it start deteriorating": `series: "hourly"` (windows up to 72h), or `investigate_store_change` for an onset

## 5. Anomalies

`get_anomalies` (default last 7 days; widen with `period: "last_30_days"`).
Order: active critical, active warning, resolved most recent. For each: detector label, title, severity, detected at, last confirmed or resolved at, `previous_occurrences` ("has this happened before"), and `retroactive` (found in Eskopia's historical review). "Is it still happening?" = `status: active` and `last_confirmed_at`.

## 6. Investigation ("why")

See the playbook in SKILL.md. Typical sequence: `get_anomalies` (if the merchant didn't name one) → `investigate_store_change` → optionally `get_funnel` or `get_product_engagement` for the same window → answer with labels.
"Traffic or conversion problem?": `revenue_decomposition.dominant_factor` and `share_of_change_percent`.
"Before or during checkout?": `funnel.largest_worsening` (visitor funnel steps up to `reached_checkout` are before checkout; checkout funnel steps are during).

## 7. Alerts

`get_alerts` → `get_alert_details` for one alert → `investigate_store_change` with `alert_id` for "what happened around then". Only anomaly alerts have severity; rule alerts are "unclassified". "Is it still happening?" applies to anomaly alerts only (`condition_still_active`). A regular user sees only alerts delivered to them.

## 8. Breakdowns ("by" and "from" questions)

`get_breakdown` with a `dimension` and, when the merchant names a segment, a filter.
- "How many visitors from Saudi Arabia today?": `dimension: "country"`, `country: "Saudi Arabia"`, `period: "today"`; read `totals.visitors`.
- "Which countries buy the most?": `dimension: "country"`, `sort_by: "revenue"`.
- "Which cities in the UAE?": `dimension: "city"`, `country: "UAE"`.
- "Where does my traffic come from?" / "Does Instagram convert?": `dimension: "traffic_source"`.
- "Mobile vs desktop": `dimension: "device"`; also `browser`, `operating_system`.
- "Top landing pages" / "most viewed pages": `landing_page` / `page`.
- "New vs returning": `visitor_type` (visitors) or `customer_type` (orders).
- "Saudi visitors per day this month": `dimension: "day"`, `country: "Saudi Arabia"`, `period: "this_month"`.
- "Did Germany drop versus last week?": `dimension: "country"`, `compare_to: "previous_period"`, read the row's `comparison.change_percent`.
State which location a number uses (visitors: IP; orders: the order's address), mention `truncated` when more rows exist, and flag groups under 30 visitors.

## 9. Orders and checkouts

`get_orders`: lead with the `summary` (count, revenue, average, median, largest, first-time share), then list orders as time, amount, place and items. Never promise names, emails or order numbers: say those are in the Eskopia web app or Shopify admin.
`get_checkouts`: counts by status, `abandoned_cart_value`, `not_completed_by_furthest_stage` (where they stopped), then examples (`status: "abandoned"`, `sort: "largest"` for the biggest carts). "Abandoned" means no activity for 30 minutes; some shoppers return. For step conversion rates and comparisons use `get_funnel`.

## 10. Product sales

`get_product_sales` (`sort_by`: revenue, units_sold, orders; `product_query` for one product; `compare_to` for change).
Lead with the top products (units, revenue, share of product revenue). "Views but no sales": high `viewers` with low `orders_per_100_viewers` (ignore products under 30 viewers). Always read `coverage`: if fewer than all orders have product lines stored, say the figures cover only those orders. Product revenue excludes shipping and tax and does not subtract refunds, so it won't match total revenue.

## 11. Busy times, retention, settings

`get_busy_times` (`metric`: visits, orders, revenue, checkout_starts; `days`): busiest slots, then the weekday and hour pattern.
`get_visitor_retention`: week 1 return rate and the cohort table; say it is visit retention per browser, not repeat purchases.
`get_settings`: what rules, channels, anomaly alerts, digest and scheduled reports exist, and `where_to_change` for the place in the web app. It is read-only.

## 12. Executive summary / morning briefing / end of day

Morning: `get_store_health` (brief) + `get_performance` (`period: "yesterday"`, `compare_to: "same_weekday_last_week"`) + today so far.
End of day: `get_performance` (`period: "today"`, `compare_to: "last_4_same_weekdays"`) + `get_anomalies` (`period: "today"`).
Format: "The three things to know" (prioritized, labeled), then a compact numbers block. Skip metrics that didn't move.
