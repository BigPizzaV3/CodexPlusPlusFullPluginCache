---
name: adzviser-preview-ui-mode
description: Open an interactive X Ads report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# X Ads Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires inspecting reporting rows.

1. Call `list_workspace` and choose the named X Ads workspace. Ask if none is
   named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_x_ads` for exact fields. Use Cost for spend,
   Campaign for campaign names, and Campaign currency for monetary units.
   Request only fields needed for the report.
3. Honor explicit historical dates and resolve relative dates from the current
   user date and timezone. Pass inclusive ISO pairs. For N days ending two days
   ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` containing `workspace_name`, `date_ranges`,
   optional `time_granularity`, and only `assorted_requests.x_ads_request` with
   `metrics` and optional `breakdowns`. For daily reporting, use a contiguous
   range and `time_granularity=Date`.
5. Call `preview_and_retrieve_reporting_data` once and let the user inspect,
   edit, and run the report in the component. A preview is not the final data;
   do not invent answers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Do not call `set_reporting_mode` from the conversation.
Let the component handle its Run and mode controls. Analyze rows only when they
become model-visible; if the user switches to analysis and rows are absent,
use `retrieve_reporting_data` through Data Mode.

Inspect all returned tables, aggregate additive campaign rows correctly, keep
currencies and date ranges separate, and distinguish Clicks from URL clicks.
Explain errors, missing access, incomplete coverage, and rounding differences.
The plugin cannot publish posts, create or pause ads, change budgets, or identify
individual clickers by name or email.
