---
name: ga4-insights
description: Report, rank, compare, and trend the user's own Google Analytics 4 (GA4) website and app data through Windsor.ai - sessions, users, new users, engagement rate, bounce rate, pageviews, average session duration, event count, conversions (key events), and revenue, broken down by date, default channel group, source and medium, campaign, landing page, device category, or country. Use when the user asks how their site, app, traffic, channels, or conversions are doing. Read-only - do not use to change property settings, for advertising cost or ROAS, to connect a property, or to schedule exports.
---

# GA4 insights

Read live Google Analytics 4 report data for the user's connected properties through Windsor.ai and turn it into a clear report, ranking, comparison, or trend. The connector id is `googleanalytics4`. This app is read-only and has no advertising cost data.

## Resolve scope and time
- Call get_connectors first to see which properties are connected. If none is, hand off to $ga4-connect. If several properties match, ask which one.
- Read field ids from get_fields for `googleanalytics4`: GA4 splits into dimensions (date, sessionDefaultChannelGroup, source and medium, campaign, landing page, device category, country) and metrics (sessions, users, engagement rate, conversions, revenue). Use the exact ids returned, never the examples. Call get_options for date-filter columns and connector options.
- Use the date range the user gave. If none, use a sensible preset (last_30d, this_month, last_7d) and state which one you used. Append T to a preset to include today.

## Choose the smallest useful read
- Traffic overview or trend -> date plus sessions and users over the preset; report direction and magnitude.
- By channel -> sessionDefaultChannelGroup plus sessions and conversions; rank in the answer and name the metric used.
- Top source, campaign, or landing page -> that dimension plus the metric asked for, ranked. If "best" or "top" has no metric, ask which one.
- Period comparison -> two get_data calls with the same fields and different ranges; show absolute and relative change.
- Keep field sets small, request only the properties you need, and check for truncated or paginated results before claiming complete coverage.

## Accuracy guardrails
- GA4 "conversions" are key events. Cost per conversion and ROAS need ad spend, which this connector does not have; say so and point to the ad-platform listing instead of estimating.
- Sampling, thresholding, and the property time zone can shift numbers; when the range includes today or yesterday, say the data may still be incomplete.
- If a field the user wants is not in get_fields, say so rather than substituting a different metric.
- Public data about other websites is not available: this app reads only the user's connected properties.

## Answer with evidence
Lead with the requested result, then state the property, the time window, and the numbers behind the conclusion. Keep internal ids and raw JSON out of the answer unless the user asks for them.

## Route the request
- Reports, rankings, comparisons, trends -> $ga4-insights
- Connecting, reconnecting, adding a property, or asking what is connected -> $ga4-connect
- Recurring exports and syncs -> $ga4-export
- What the app covers and does not -> $ga4-help
Never offer plans, upgrades, or pricing.
