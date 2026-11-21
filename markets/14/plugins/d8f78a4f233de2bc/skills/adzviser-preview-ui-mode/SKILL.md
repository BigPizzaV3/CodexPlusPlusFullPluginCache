---
name: adzviser-preview-ui-mode
description: Open an interactive Microsoft Ads report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, ordinary analysis, or previewing and applying account changes.
---

# Microsoft Ads Preview UI

Use this workflow only for an explicit interactive report-preview request. Use
`adzviser-data-mode` for answers requiring inspection of reporting rows.

1. Call `list_workspace` and select the named Microsoft Ads workspace. The
   account type may be labeled Bing Ads. Ask when multiple suitable workspaces
   remain and none is named; do not substitute an inaccessible account.
2. Call `list_metrics_and_breakdowns_bing_ads` for exact fields. Cost represents
   spend. Request Currency code for money values and only compatible fields.
3. Resolve relative dates from the current date and user's timezone. Pass
   inclusive ISO pairs; N days ending two days ago means `[D-(N+1), D-2]`.
   Honor explicit historical dates. For daily reporting use a contiguous range
   with `time_granularity=Date`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and only `assorted_requests.bing_ads_request` containing
   `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once and let the user inspect,
   edit, and run the report in the component. A preview is not final reporting
   data; do not invent answers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Do not call `set_reporting_mode` from the conversation.
Let the component handle Run and mode controls. Analyze only model-visible
rows; if the user switches to analysis and no rows are available, use
`retrieve_reporting_data` through Data Mode.

Preserve currencies, actual dates, report scopes, and metric meanings. Do not
sum ratios, mix currencies, duplicate metrics across report tables, or interpret
missing data and authentication errors as zero activity. The plugin cannot
identify individual ad clickers.

For current account settings, Search campaign renames, pauses, daily budget
changes, permissions, or change receipts, use `adzviser-account-management`
and `source=bing_ads` for resource discovery. `preview_changes` previews an
account edit; `preview_and_retrieve_reporting_data` previews a report. Running
a report or changing its presentation mode does not approve an account edit.
