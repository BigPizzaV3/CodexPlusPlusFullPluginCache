---
name: diagnose-metric-change
description: Use when the user asks why a marketing metric went up or down, whether a change is real or normal, or when something changed, for example "why did my cost per lead jump?", "is this weekend dip normal?", "when did our CPCs go up?" or "revenue looks low this month, should I worry?".
---

# Diagnose a metric change

Work from evidence to explanation. Follow the data and accuracy rules in the `analyze-marketing-data` skill throughout.

## 1. Pin down the change

- Confirm the metric, the platform or platforms, and the two periods being compared. If the user is vague ("last week"), state the dates you used.
- Quantify it with `pma_get_date_range_comparison`. If the change is small, say so before going further.
- If the current period is still in progress, run `pma_forecast` first. A partial month often looks like a drop; report the projected total and its range instead.

## 2. Is it real or normal?

- `pma_detect_seasonality` tells you whether the movement matches a regular weekday pattern, such as weekend dips.
- `pma_detect_significant_anomalies` flags days that are unusual after removing the weekly pattern, with a confidence for each. "No significant anomalies" is a valid answer.
- Check for data gaps and freshness: zero days, an old `last_sync`, or a `data_through` date before the end of the period. Use `pma_get_token_health_summary` when a connection may be broken.
- Use `pma_list_available_analyses` first when unsure whether the data supports these analyses.

## 3. When did it change?

Use `pma_detect_changepoints` to find the date the metric stepped to a new level and the before and after averages. Ask the user what happened around that date (budget changes, new campaigns, site changes, promotions).

## 4. What drove it?

Use `pma_analyze_drivers`:

- For an additive metric (spend, revenue, clicks, conversions), pass the metric and a dimension. Start with `campaign_name`, then try others the report supports, such as country or device.
- For a rate, pass the rate name with `rate_numerator` and `rate_denominator`. Examples: CTR = clicks / impressions, conversion rate = conversions / clicks, ROAS = conversion value / spend. For cost per result, analyse the conversion rate and CPC separately, or analyse spend and conversions as two additive metrics. The result splits the change into efficiency (segments performing differently) and mix (volume moving between segments). That split usually is the answer.

## 5. Check across platforms

- For cost or conversion questions, run the same check on every ad platform that is connected.
- If conversions fell on every ad platform at the same moment while orders or revenue in Shopify, Stripe or GA4 held steady, the likely cause is tracking or attribution, not performance. Say so as a hypothesis to verify.

## 6. Write it up

1. **What changed:** the metric, the size of the change and the dates.
2. **Real or normal:** what the seasonality, anomaly and freshness checks showed.
3. **When:** the changepoint date, if one was found.
4. **Why:** the main drivers, naming campaigns or segments, and whether the cause was efficiency or mix.
5. **Next steps:** what to check or change.

Keep facts and hypotheses apart. Present anything the data does not directly show as a possible cause to check, not as a finding.
