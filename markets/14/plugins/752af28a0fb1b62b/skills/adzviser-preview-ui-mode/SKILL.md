---
name: adzviser-preview-ui-mode
description: Open an interactive Campaign Manager 360 report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Campaign Manager 360 Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires inspection of actual reporting rows.

1. Call `list_workspace` and select the named CM360 workspace. Ask when none is
   named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_cm360` for exact, compatible field names.
   Request only fields needed for the report. Keep media cost, planned media
   cost and revenue distinct; preserve the reported currency.
3. Resolve dates from the user's current date and timezone. Pass inclusive ISO
   date pairs. For N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests` containing only `cm360_request`,
   with `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run
   the report in the component. A preview alone is not the final reporting data;
   do not invent numbers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in `time_granularity`. Do not add unsupported
filters or other data sources. Keep different campaign and placement IDs separate.

Let the component handle its own Run and mode controls. Analyze rows only when
they become model-visible. If the user switches to analysis and rows are absent,
use `retrieve_reporting_data` through Data Mode. Explain missing access or errors.
The plugin cannot pause campaigns, upload or assign creatives, change budgets,
or identify individual ad clickers.
