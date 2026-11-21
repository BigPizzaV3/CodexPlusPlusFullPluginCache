---
name: adzviser-preview-ui-mode
description: Open an interactive Omnisend report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Omnisend Preview UI

Use only for an explicit interactive-preview request. Use `adzviser-data-mode`
when the answer requires actual reporting rows.

1. Call `list_workspace` and select the named workspace with Omnisend access.
   Ask when none is named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_omnisend` for exact field names.
   Request only necessary fields from the live catalog.
3. Resolve inclusive dates from the current date and user's timezone. For
   N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.omnisend_request`
   containing `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run
   the report. A preview alone contains no final reporting rows; do not invent
   numbers or claim to analyze hidden component data.

Dates select campaigns by the date part of their startDate. Engagement values
are accumulated results for those campaigns, not date-filtered event counts.
Rates are fractional ratios using sends as denominator; multiply by 100 once
for percentage display. Device counts can have incomplete coverage. Keep
Campaigns and A/B Tests separate and do not double-count parent and variant
results. Automation reporting and revenue are not supported by this catalog.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in time_granularity, not breakdowns. Do not add
unsupported filters or other sources.

Let the component handle Run and mode controls. Analyze only model-visible rows.
If the user switches to analysis and rows are absent, use `retrieve_reporting_data`
through Data Mode. Avoid concurrent duplicate requests and immediate retry loops;
report provider errors accurately. The plugin cannot send or schedule campaigns,
edit automations, or change contact subscriptions.
