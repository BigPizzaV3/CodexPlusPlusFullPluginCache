---
name: adzviser-preview-ui-mode
description: Open an interactive Matomo report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Matomo Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires inspection of reporting rows.

1. Call `list_workspace` and select the named Matomo workspace. Ask when none is
   named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_matomo` for exact field names. Match metrics
   to breakdown families: Device visits with Device type, Channel visits with
   Channel type, and Location visits with Country. Keep report families separate
   when necessary. Request only fields needed for the user's report.
3. Resolve relative dates from the current user date and timezone. Pass inclusive
   ISO date pairs. For N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and only `assorted_requests.matomo_request`, containing
   `metrics` and optional `breakdowns`. For a daily report, use one contiguous
   range and `time_granularity=Date`.
5. Call `preview_and_retrieve_reporting_data` once and let the user inspect,
   edit, and run the report in the component. A preview is not the final data;
   do not invent values or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Do not call `set_reporting_mode` from the conversation.
Let the component handle Run and mode controls. Analyze rows only when they
become model-visible. If the user switches to analysis and rows are absent,
use `retrieve_reporting_data` through Data Mode. Inspect every named Matomo table.

Preserve units and source labels, keep Actions distinct from pageviews, do not
sum unique visitors across periods, and disclose incomplete row coverage. The
plugin cannot install tracking, edit the website, delete analytics, or identify
visitors by name or email. Explain errors and missing access accurately.
