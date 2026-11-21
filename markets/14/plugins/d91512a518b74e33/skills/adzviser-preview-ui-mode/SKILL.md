---
name: adzviser-preview-ui-mode
description: Open an interactive Salesforce report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Salesforce Preview UI

Use this workflow only when the user explicitly requests an interactive preview.
For questions requiring inspection of actual results, use `adzviser-data-mode`.

1. Call `list_workspace` and select the named Salesforce workspace. If multiple
   suitable workspaces remain and none was named, ask the user to choose.
2. Call `list_metrics_and_breakdowns_salesforce` for exact supported field names.
   Request only fields needed for the user's report.
3. Resolve dates from the current date in the user's timezone. Pass inclusive
   ISO date pairs. For N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and an `assorted_requests` object containing only
   `salesforce_request`, with `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once and allow the user to edit or
   run the report in the component. The preview response alone is not a report
   result; do not invent numbers or claim to have analyzed hidden component data.

Salesforce date ranges select records by CreatedDate using UTC calendar-day
boundaries. Stage and status are current values, not historical snapshots. Do
not present this as filtering records by close date. Explain an unsupported date
interpretation before constructing a misleading report.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Never call `set_reporting_mode` from the conversation. Put
Date/Week/Month/Quarter in `time_granularity`, never in breakdowns. Do not add
unsupported filters or other data sources.

Let the component handle its own Run and mode controls. Analyze rows only when
they become model-visible. If the user switches to analysis and no rows are
available, use `retrieve_reporting_data` through the Data Mode workflow. Report
missing workspace access or tool errors accurately. This plugin cannot modify
Salesforce records or send messages.
