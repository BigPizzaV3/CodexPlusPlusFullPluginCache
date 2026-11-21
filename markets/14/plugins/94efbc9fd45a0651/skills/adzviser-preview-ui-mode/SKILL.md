---
name: adzviser-preview-ui-mode
description: Open an interactive YouTube Analytics report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, comparisons, audits, or ordinary analysis.
---

# YouTube Preview UI

Use this workflow only for an explicit interactive-preview request. Use
`adzviser-data-mode` when the answer requires inspecting reporting rows.

1. Call `list_workspace` and choose the named YouTube workspace. Ask if none is
   named and multiple suitable workspaces remain.
2. Call `list_metrics_and_breakdowns_youtube` for exact fields. Use Video views
   for period views, Estimated minutes watched for watch time, and Gained
   subscribers / Lost subscribers for period subscriber changes. Include Video
   views when requesting video breakdowns; keep Video ID attached to Video title.
3. Resolve relative dates from the current user date and timezone. Pass inclusive
   ISO pairs. For N days ending two days ago, use `[D-(N+1), D-2]`. Honor explicit
   historical dates and explain source processing delays if recent data is absent.
4. Build one `adzviser_request` containing `workspace_name`, `date_ranges`,
   optional `time_granularity`, and only `assorted_requests.youtube_request` with
   `metrics` and optional `breakdowns`. For daily reporting, use a contiguous
   range and `time_granularity=Date`.
5. Call `preview_and_retrieve_reporting_data` once and let the user inspect,
   edit, and run the report in the component. A preview is not final data;
   do not invent answers or claim to analyze hidden component data.

Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Do not call `set_reporting_mode` from the conversation.
Let the component handle Run and mode controls. Analyze rows only when they
become model-visible; if the user switches to analysis and rows are absent,
use `retrieve_reporting_data` through Data Mode.

Preserve units, period boundaries, and actual values. Channel statistics snapshots
are not period activity. Video reports return at most 200 videos sorted by views
and can omit deleted videos; use channel aggregate reports for channel totals.
Disclose missing coverage and differences between daily and period estimates.
The plugin cannot publish, edit, or delete videos or identify individual viewers.
