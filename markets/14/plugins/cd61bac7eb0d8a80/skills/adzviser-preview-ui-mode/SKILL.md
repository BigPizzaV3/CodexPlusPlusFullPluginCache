---
name: adzviser-preview-ui-mode
description: Open an interactive Zoho CRM report preview with Adzviser only for an explicit Preview UI, UI Mode, embedded report, or interactive report builder request. Do not use for ordinary reporting, raw rows, calculations, comparisons, or audits.
---

# Zoho CRM Preview UI

1. Call `list_workspace` and select an authorized Zoho CRM workspace.
2. Discover exact supported fields with `list_metrics_and_breakdowns_zoho`.
3. Resolve inclusive dates from today's date in the user's timezone and order
   date pairs chronologically. Follow the sibling Data Mode skill's rules for
   creation dates, current field values, separate modules and currency context.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.zoho_request` containing `metrics`
   and optional `breakdowns`. Request only fields needed for the report.
5. Call `preview_and_retrieve_reporting_data` once. Briefly say the preview is
   ready; preview configuration is not completed reporting data.

Ordinary requests such as "show my lead count" use Data Mode. Never send
`client_id`, `reporting_mode`, `_widget_action`, conversation history or unrelated
context. Never invoke `set_reporting_mode` from the conversation; the component
owns its Run and preference controls.

Do not duplicate component requests or immediately ask the user to rerun. Analyze
subsequent model-visible rows without another retrieval unless the question changes.
Hidden `_meta` is unavailable for analysis. Explain missing access or provider
errors honestly. This plugin cannot create, edit or delete CRM records.
