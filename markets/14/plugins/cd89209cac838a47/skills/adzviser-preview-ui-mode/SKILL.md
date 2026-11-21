---
name: adzviser-preview-ui-mode
description: Open an interactive Merchant Center report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, rankings, comparisons, audits, or ordinary analysis.
---

# Merchant Center Preview UI

Use only for explicit interactive-preview requests. Use `adzviser-data-mode`
when the answer requires actual reporting rows.

1. Call `list_workspace` and choose the named workspace with Merchant Center
   access. Ask when none is named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_merchant_center` for exact fields.
   Request only necessary fields. Keep product detail and issue reports
   separate from performance analysis.
3. Resolve inclusive dates using the current date and user's timezone. For
   N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.merchant_center_request`
   containing `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run
   it. A preview alone contains no final reporting rows; do not invent values
   or claim to analyze hidden component data.

CTR is a fractional ratio, displayed as a percentage after multiplying by 100.
Numeric counts may be strings; preserve Product ID as text. Current product
details and issues are not historical date-filtered performance. Repeated issue
rows do not represent additional products. Customer country and target country
are different fields. Keep currencies and reporting scopes separate.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in time_granularity, not breakdowns. Do not add
unsupported filters or other sources.

Let the component handle Run and mode controls. Analyze only model-visible rows.
If the user switches to analysis and rows are absent, use `retrieve_reporting_data`
through Data Mode. Explain errors and missing access accurately. This plugin
cannot edit or delete products, fix disapprovals, or change ad bids and budgets.
