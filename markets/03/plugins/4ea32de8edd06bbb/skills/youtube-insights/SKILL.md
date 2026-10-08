---
name: youtube-insights
description: Report, rank, compare, and trend the performance of the user's own YouTube channels and videos through Windsor.ai - views, watch time, average view duration, subscribers gained and lost, likes, comments, shares, and traffic sources, per channel, per video, and by day, week, or month. Use when the user asks how their channel or videos are doing. Read-only - do not use to change channel settings, publish videos, connect a channel, or schedule exports.
---

# YouTube insights

Read live analytics for the user's connected YouTube channels through Windsor.ai and turn them into a clear report, ranking, comparison, or trend. The connector id is `youtube`. This app is read-only: it never changes anything on the channel.

## Resolve scope and time
- Call get_connectors first to see which channels are connected. If none is, hand off to $youtube-connect. If several channels match, ask which one.
- Read field ids from get_fields for `youtube`, and get_options for date-filter columns and connector options. Never guess field names, channel ids, or video ids.
- Use the date range the user gave. If none, use a sensible preset (last_30d, this_month, last_7d) and state which one you used. Append T to a preset to include today.

## Choose the smallest useful read
- Top videos -> fields [video title or id, views, watch time], rank in the answer and name the metric used. If "best" or "top" has no metric, ask which one.
- Channel trend -> fields [date, views, subscribers gained] over the preset; report direction and magnitude, and net subscribers if lost is available.
- Traffic sources -> fields [traffic source, views]; share of views per source.
- Engagement -> likes, comments, shares against views; say when views are zero.
- Keep field sets small and check for truncated or paginated results before claiming complete coverage.

## Accuracy guardrails
- Watch time units come from the field definition; state minutes or hours explicitly.
- Analytics for the most recent day or two can still be incomplete; say so when the range includes today or yesterday.
- If a field the user wants is not in get_fields, say so rather than substituting a different metric.
- Public data about other channels is not available: this app reads only the user's connected channels.

## Answer with evidence
Lead with the requested result, then state the channel, the time window, and the numbers behind the conclusion. Keep internal ids and raw JSON out of the answer unless the user asks for them.

## Route the request
- Reports, rankings, comparisons, trends -> $youtube-insights
- Connecting, reconnecting, adding a channel, or asking what is connected -> $youtube-connect
- Recurring exports and syncs -> $youtube-export
- What the app covers and does not -> $youtube-help
Never offer plans, upgrades, or pricing.
