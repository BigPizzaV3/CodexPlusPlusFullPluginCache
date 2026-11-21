---
name: reteno-analytics
description: Analyze Reteno contact profiles and audiences with count_segment_contacts, or messaging performance and event volume with analytics exports. Count people matching fields, events, activity, time windows, and exclusions; explain population shares and supported breakdowns without saving segments.
---

# Reteno Analytics

## Overview

Use this skill for Reteno profile statistics, audience sizes, field completeness, country/language breakdowns, event-qualified contact counts, audience overlaps, or population shares, as well as campaign performance, workflow rankings, delivery/conversion rates, event volume, and event type lookup.

This skill does not modify contacts or save segments. Audience calculations return inline counts; analytics exports require downloading and inspecting their rows with `<plugin-root>/scripts/transfer.py`.

Default to a concise summary. Return exported files only when requested.

## Workflow

1. Identify the analytics question and choose the smallest Reteno MCP query that answers it.
   - Use `count_segment_contacts(schema)` for **contacts matching conditions**: profile/custom fields, missing values, events or activity (including occurrence thresholds and periods), AND/OR combinations, exclusions, and intersections supported by live definitions. Read `references/audience-counts.md` and use `$segment-designer` in `--mode count`; never create a segment merely to count it.
   - Use `get_segment_contacts(segment_id, limit=1, offset=0)` for the active-contact count of an already saved segment, after resolving its exact ID.
   - Use `get_messaging_analytics(group_by, date_from?, date_to?, workflow_ids?, message_ids?, media_types?, conversion_event?, order_by?)` for send, delivery, open, click, bounce, spam, unsubscribe, revenue, channel, media-type, or conversion metrics.
   - Use `get_events_analytics(date_from?, date_to?, event_type_ids?)` for event-count denominators or event-volume breakdowns.
   - Use `get_event_types(event_type_ids?, event_key?, search?)` first when the user provides an event name/key and you need to resolve the exact event type identifier before running analytics.
   - Event volume and matching-contact counts answer different questions. A contact with ten purchases contributes one contact to an audience count; it can contribute ten occurrences to event analytics. Do not infer one metric from the other.
2. Call the relevant MCP tool with the selected organization only.
   - Avoid exploratory loops. `get_messaging_analytics` and `get_events_analytics` are limited to 10 calls per 60 seconds per MCP client/tool.
   - Prefer one precise analytics query, then do filtering, ranking, and aggregation from the downloaded CSV.
3. If the tool returns a manifest with signed artifact URLs instead of inline rows, download the export through `python3 <plugin-root>/scripts/transfer.py download --url <ticket> --output <file>`.
   - Resolve `<plugin-root>` from this installed skill directory; use the transfer helper for signed tickets.
4. Save downloaded artifacts under `output/reteno-analytics/`.
   - Messaging exports: `output/reteno-analytics/messaging_<group_by>_<date_from>_<date_to>.csv`
   - Events exports: `output/reteno-analytics/events_<date_from>_<date_to>.csv`
   - If the export is JSON instead of CSV, keep the same basename and use `.json`.
5. Inspect the local file and answer from the downloaded rows.
   - Quote the exact `dateFrom`/`dateTo` resolved by the tool.
   - Reflect the manifest `timeRange` and `dataAvailability` in the answer when freshness, timezone, same-day data, or datetime precision matters.
   - Same-day analytics are available but values can change as new events arrive.
   - If the user asked for rankings, compute them from the local rows rather than from the manifest metadata.
6. Keep the response concise and clear.
   - Return files only when explicitly requested.
   - Do not move analytics exports into `saved/` unless the user later asks to keep them for reuse.

## Time Range Behavior

These export defaults do not apply to profile counts. Profile fields describe the current state; event/activity periods in an audience schema must express the requested window explicitly.

- `date_from` and `date_to` accept `YYYY-MM-DD` dates or ISO datetime strings.
- Date-only values cover the full organization-local day.
- Timezone-less datetimes are interpreted in the organization timezone.
- Timezone-aware datetimes use their explicit instant and are reported back in the organization timezone.
- When dates are omitted, the live API default is the last seven organization-local days, including today.
- A single `get_messaging_analytics` or `get_events_analytics` call must not exceed 185 days.

## Messaging Analytics Behavior

- `group_by` must be `organization`, `workflow`, or `message`.
- Allowed `media_types` are `email`, `sms`, `mobilepush`, `appinbox`, and `webpush`.
- When `media_types` is omitted, the MCP default is `email` and `mobilepush`; confirm the resolved channels from `filters.mediaTypes`.
- Every CSV row is separated by `media_type`; never merge channel rows unless the user explicitly asks for a cross-channel total and you label it as computed.
- `organization` rows include `media_type`, core metrics, `reach`, `frequency`, delivery/open/click/conversion rates, and `revenue`.
- `workflow` rows add `workflow_id`, `workflow_name`, and `launches`.
- `message` rows add `workflow_id`, `workflow_name`, `callout_id`, `callout_name`, `message_id`, and `message_subject`.
- Use `group_by="workflow"` for workflow totals and rankings. Message/callout rows describe
  message performance and are not additive workflow totals. Do not sum them to reconstruct
  workflow counts, even when their workflow IDs match. Read `metricScope.countsSource` when
  present and retain its meaning; compare like groupings, sources, channels and date windows.
- If `open_rate` is blank but same-row `opened` and `delivered` are valid nonnegative numbers
  with `delivered > 0`, calculate `100 * opened / delivered` and label it **derived open rate**.
  Preserve a supplied native rate. Missing counts or a zero denominator mean unavailable,
  not zero. Do not average row percentages or silently substitute message totals for workflow
  counts. Flag inconsistent counts instead of presenting an implausible rate as reliable.
- `spam`, `bounced`, and `unsubscribed` are message-level only.
- `conversions` is present only when `conversion_event` is supplied. `conversion_event` can be an integer `EventTypeID` or an exact case-insensitive event key/name match.
- Pass a supplied numeric conversion-event ID directly; resolve names through `get_event_types`.
  A lookup failure or unavailable event metadata does not prove the ID is invalid. Preserve the
  exact MCP error and report existence as unverified; do not guess another event or silently
  remove the conversion filter.
- `order_by` may use `sent`, `delivered`, `opened`, or `clicked` for all groups. `spam`, `bounced`, and `unsubscribed` are valid only for `group_by="message"`. `conversions` requires `conversion_event`.
- The finest available grouping level is callout/message. Recipient-domain, mailbox-provider, ISP, bounce-reason, recipient-level delivery errors, raw logs, and date-bucket splits are not available from this MCP analytics tool.
- Large `group_by="message"` exports can fail upstream for high-volume organizations. If a message-level export returns a 5xx/internal server error, do not keep retrying the same full-range call. Retry with smaller non-overlapping organization-local date shards, download each successful shard, and compute the requested result from local rows. For "unique message IDs and sends" over the last 7 days, use one shard per date, union non-empty `message_id` values for the unique count, and sum the CSV send metric (`sent`/`sends`, whichever column the export provides) across shards. Respect the 10 calls per 60 seconds limit. If any shard still fails, report a partial result and list the failed date shard(s).

## Event Analytics Behavior

- `get_events_analytics` groups only by event type.
- Do not pass or invent `split_by_date` or `source`; those filters are not available on the live API-backed tool.
- Event analytics CSV columns are `event_type_id`, `event_key`, `event_name`, `count`, `launched_workflows`, `stopped_workflows`, `contact_not_found`, and `parameter_errors`.
- Rows are ordered by `count` descending.
- Use `get_event_types` to resolve event keys, event names, conversion candidates, or event type IDs before querying analytics when the user provides a name rather than an ID.
- `get_event_types` returns metadata only. It does not return counts, trends, delivery metrics, or failure diagnostics.

## Active workflow count limitation

MCP `list_workflows` status alone does not establish the exact business count of active,
not-paused workflows with a valid launch condition. Report any available inventory as an
inventory/status count with that limitation. Do not infer missing launch-condition evidence,
use internal warehouse tables, or present an approximate count as exact. Individual workflow
exports can support inspection of named workflows but do not by themselves prove the complete
organization-wide business metric.

## Output Behavior

- Default: a concise summary
- Optional: provide CSV or JSON exports only when the user explicitly asks for the file
- Intermediate analytics artifacts stay under `output/reteno-analytics/`

## Constraints

- Read-only only; do not create, update, or delete Reteno entities.
- Stay within the selected organization unless the user explicitly asks for cross-organization comparison.
- Inspect the local downloaded artifact before answering whenever the MCP tool returns only an export manifest.

## Resources

- Read `references/audience-counts.md` for population semantics, safe calculation budgets, exact ranking requirements, and count reporting.
- Use the bundled helper `python3 <plugin-root>/scripts/transfer.py download --url <ticket> --output <file>` for every signed Reteno export download.

## Local export recovery

Use `<skill-dir>/scripts/shard_exports.py plan --from YYYY-MM-DD --to YYYY-MM-DD --output <manifest>` to plan non-overlapping inclusive date shards. Fetch sequentially within MCP limits; record each shard as `complete` with its local CSV `path`, or `failed` with a short error. Run `shard_exports.py summarize --manifest <manifest>` to union nonempty message IDs and sum additive `sent`/`sends`. Missing, pending or failed windows produce an explicit partial result. Do not sum unique reach, distinct users, rates or overlapping audience counts across shards. Keep organization/timezone, requested dates and excluded shards in the response. Viber and Telegram are unavailable in Reteno.
