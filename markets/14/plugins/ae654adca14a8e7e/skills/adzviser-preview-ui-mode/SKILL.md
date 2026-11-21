---
name: adzviser-preview-ui-mode
description: Open an interactive HubSpot report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# HubSpot Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires actual reporting rows.

1. Call `list_workspace` and select the named HubSpot workspace. Ask when none
   is named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_hubspot` for exact supported field names.
   Request only fields needed for the report. CRM dates filter record creation
   with UTC day boundaries; current stages and amounts are not historical
   snapshots. Include `Deal Currency` for deal amounts and separate currencies.
3. Resolve dates from the user's current date and timezone. Pass inclusive ISO
   date pairs. For N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and an `assorted_requests` object containing only
   `hubspot_request`, with `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run the
   report in the component. A preview alone does not contain final reporting
   rows; do not invent numbers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in `time_granularity`, not breakdowns. Do not add
unsupported filters or other sources. Do not substitute record creation dates
for a requested close-date analysis without explaining the difference.

Let the component handle its Run and mode controls. Analyze rows only when they
become model-visible. If the user switches to analysis and rows are absent, use
`retrieve_reporting_data` through Data Mode. Explain access errors and pending
reports accurately. The plugin cannot modify CRM records, send emails, or enroll
contacts in workflows. Request personal fields only when needed for the report.
