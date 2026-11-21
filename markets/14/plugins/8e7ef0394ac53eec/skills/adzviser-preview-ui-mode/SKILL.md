---
name: adzviser-preview-ui-mode
description: Open an interactive BigCommerce report preview with Adzviser only when the user explicitly requests Preview UI, UI Mode, an embedded report, or an interactive report builder. Do not use for ordinary reporting, raw data, audits, calculations, comparisons, or store-performance analysis.
---

# BigCommerce Preview UI

1. Call `list_workspace` and choose an authorized BigCommerce workspace.
2. Discover exact fields with `list_metrics_and_breakdowns_bigcommerce`.
3. Resolve inclusive dates using the current date in the user's timezone.
   Select only necessary fields and follow the sibling Data Mode skill's
   order-date, status, currency and order-versus-product interpretation rules.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.bigcommerce_request` containing
   `metrics` and optional `breakdowns`.
5. Call `preview_and_retrieve_reporting_data` once. Briefly say the preview is
   ready; do not describe preview configuration as completed report data.

A request such as "show my order total" normally calls for Data Mode. Only use
this workflow for an explicit interactive-preview request. Never send
`client_id`, `reporting_mode`, `_widget_action`, conversation history or unrelated
context. Never invoke `set_reporting_mode` from the conversation; the component
owns its Run and preference controls.

Do not duplicate component requests or ask the user to rerun immediately. If
model-visible rows are subsequently published, analyze them without another
retrieval unless the question changes. Hidden `_meta` is not available for
analysis. Report missing access or provider errors honestly. The plugin cannot
edit orders, issue refunds, or change products, prices and inventory.
