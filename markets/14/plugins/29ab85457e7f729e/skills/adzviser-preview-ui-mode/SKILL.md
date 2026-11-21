---
name: adzviser-preview-ui-mode
description: Open an interactive ActiveCampaign report preview with Adzviser only for an explicit Preview UI, UI Mode, embedded report, or interactive report builder request. Do not use for ordinary reporting, raw rows, calculations, rankings, comparisons, or audits.
---

# ActiveCampaign Preview UI

1. Call `list_workspace` and select an authorized ActiveCampaign workspace.
2. Discover supported fields with `list_metrics_and_breakdowns_activecampaign`.
3. Resolve inclusive dates from today's date in the user's timezone. Follow the
   sibling Data Mode skill's send-date selection, cumulative-statistic, rate,
   count-scope and currency rules. Select only fields needed for the report.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.activecampaign_request` containing
   `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Briefly say the preview is
   ready; preview configuration is not completed reporting data.

Ordinary requests such as "show my campaign performance" use Data Mode. Never
send `client_id`, `reporting_mode`, `_widget_action`, conversation history or
unrelated context. Never invoke `set_reporting_mode` from the conversation;
the component owns its Run and preference controls.

Do not duplicate component requests or immediately ask the user to rerun.
Analyze subsequent model-visible rows without another retrieval unless the
question changes. Hidden `_meta` is unavailable for analysis. Explain access
or provider errors honestly. This plugin cannot send emails or modify campaigns,
automations, contacts or deals.
