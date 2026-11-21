---
name: adzviser-preview-ui-mode
description: Open an interactive LinkedIn Ads report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# LinkedIn Ads Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires actual reporting rows.

1. Call `list_workspace` and select the named workspace with LinkedIn Ads access.
   Ask when none is named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_linkedin_ads` for exact field names.
   Request only necessary fields. Keep USD spend and account-currency measures
   distinct. Use canonical Campaign, Ad set and Ad fields at their correct levels.
3. Resolve dates from the user's current date and timezone. Pass inclusive ISO
   date pairs. For N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and an `assorted_requests` object containing only
   `linkedin_ads_request`, with `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run the
   report in the component. A preview alone does not contain final reporting
   rows; do not invent numbers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in `time_granularity`, not breakdowns. Do not add
unsupported filters, other sources or organic company-page requests. Member
demographic reports allow one breakdown at a time and cannot identify individuals.

Let the component handle its Run and mode controls. Analyze rows only when they
become model-visible. If the user switches to analysis and rows are absent, use
`retrieve_reporting_data` through Data Mode. Explain missing access and errors
accurately. This plugin cannot change campaigns, bids or budgets, create ads,
send messages or identify individual ad clickers.
