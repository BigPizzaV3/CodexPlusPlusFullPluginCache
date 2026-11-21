---
name: adzviser-preview-ui-mode
description: Open an interactive Spotify Ads report preview with Adzviser only when the user explicitly requests Preview UI, UI Mode, an embedded report, or an interactive report builder. Do not use for ordinary reporting, raw data, audits, calculations, comparisons, or ad-performance analysis.
---

# Spotify Ads Preview UI

1. Call `list_workspace` and choose an authorized Spotify Ads workspace.
2. Discover exact fields with `list_metrics_and_breakdowns_spotify_ads`.
3. Resolve inclusive dates using the current date in the user's timezone.
   Request only necessary metrics and breakdowns. Preserve currency and report
   scope; use the reporting interpretation rules in the sibling Data Mode skill.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.spotify_ads_request` containing
   `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Briefly say the preview is
   ready; do not claim the preview configuration is final report data.

Use this workflow only for an explicit interactive-preview request. A request
such as "show spend" normally requires `retrieve_reporting_data` in Data Mode.
Never send `client_id`, `reporting_mode`, `_widget_action`, conversation history,
or unrelated context. Never call `set_reporting_mode` from the conversation;
the component owns its preference and Run controls.

Do not duplicate the component's requests or ask the user to rerun immediately.
If the component later publishes model-visible rows, analyze those rows without
another retrieval unless the question changes. Hidden `_meta` data is not
available for analysis. Report missing access or provider errors honestly.
This reporting plugin cannot create or modify ads, campaigns, bids or budgets.
