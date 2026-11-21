---
name: adzviser-preview-ui-mode
description: Open an interactive Instagram account or post report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# Instagram Insights Preview UI

Use only for an explicit interactive-preview request. Use `adzviser-data-mode`
when the answer requires actual reporting rows.

1. Call `list_workspace` and select the named workspace with Instagram access.
   Ask if none is named and multiple suitable workspaces remain.
2. Discover exact fields with `list_metrics_and_breakdowns_ig_profile` for account
   reports or `list_metrics_and_breakdowns_ig_post` for post reports.
3. Resolve inclusive dates from the user's current date and timezone. For N
   days ending two days ago, use `[D-(N+1), D-2]`.
4. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests` containing only necessary
   `ig_profile_insights_request` and/or `ig_posts_insights_request` entries
   with `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Let the user edit and run
   it. A preview alone contains no final reporting rows; do not invent numbers
   or claim to analyze component-only data.

Account insight totals cover the reporting period. Post dates select when posts
were published; their insight values are current/lifetime totals. Profile Views
is not profile visits or retired impressions. Followers, Follows and Media Count
are snapshots; Follows means accounts followed. Do not sum unique reach across
dates or posts, turn nulls into zeros, or label all activity organic-only.
Follow metric compatibility and returned notes.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history
or unrelated context. Never call `set_reporting_mode` from the conversation.
Date/Week/Month/Quarter belong in `time_granularity`, not breakdowns. Do not add
unsupported filters or other data sources.

Let the component handle Run and mode controls. Analyze only model-visible rows.
If the user switches to analysis and rows are absent, use `retrieve_reporting_data`
through Data Mode. Explain access errors accurately. This plugin cannot publish,
schedule, edit or delete content, send messages, or identify individual viewers.
