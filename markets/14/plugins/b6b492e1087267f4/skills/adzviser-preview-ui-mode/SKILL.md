---
name: adzviser-preview-ui-mode
description: Open an interactive Mailchimp report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Mailchimp Preview UI

Use only for an explicit interactive-preview request. Use `adzviser-data-mode`
when the answer requires actual reporting rows.

1. Call `list_workspace` and select the named workspace with Mailchimp access.
   Ask when none is named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_mailchimp` for exact field names and
   request only necessary fields. Avoid contact-level information unless the
   user explicitly requests a report that needs it.
3. Resolve inclusive dates from the current date and user's timezone. For
   N days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`,
   optional `time_granularity`, and `assorted_requests.mailchimp_request`
   containing `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run
   the report. A preview alone contains no final reporting rows; do not invent
   numbers or claim to analyze hidden component data.

Campaign dates select send dates in UTC. Engagement values are accumulated
campaign results, not events occurring only inside the selected period.
Current audience counts and returned growth-history statistics are not filtered
by the request's date range. Keep CampaignReports and AllTimeListReports
separate. Rates marked (%) are already percentages. Do not average percentages
or sum per-campaign unique counts to claim a unique cross-campaign audience.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in time_granularity, not breakdowns. Do not add
unsupported filters or other sources.

Let the component handle Run and mode controls. Analyze only model-visible rows.
If the user switches to analysis and rows are absent, use `retrieve_reporting_data`
through Data Mode. Explain errors and missing access accurately. This plugin
cannot send or schedule campaigns, change contacts, unsubscribe members, or
delete audiences.
