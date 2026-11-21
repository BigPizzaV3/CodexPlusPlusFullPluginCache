---
name: adzviser-preview-ui-mode
description: Open an interactive eBay report preview in ChatGPT so the user can inspect, edit, and run it. Use only for an explicit Preview UI, UI Mode, embedded report, or interactive report request. Do not use for raw rows, calculations, audits, or ordinary analysis.
---

# Adzviser eBay Preview UI

This plugin supports connected eBay accounts only. Discover fields with
`list_metrics_and_breakdowns_ebay` and use only `assorted_requests.ebay_request`.
For another source, explain the scope and suggest its corresponding connector.
This reporting plugin cannot buy items, edit or publish listings, change prices
or inventory, cancel orders, message buyers, or issue refunds. Do not use
reporting calls as a substitute for a requested mutation or claim it happened.

## Prepare the requested preview

1. Resolve the user's requested workspace with `list_workspace` and discover
   exact fields using `list_metrics_and_breakdowns_ebay`. Clarify ambiguous
   workspaces instead of silently switching accounts.
2. Resolve dates from the current date and use inclusive `YYYY-MM-DD` pairs.
   Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and an `assorted_requests` object containing only
   `ebay_request`, with `metrics` and optional `breakdowns`.
3. Call `preview_and_retrieve_reporting_data` once and let the user inspect,
   edit and run the component. The initial response is report configuration,
   not retrieved rows; do not invent a data summary from it.

Do not choose this mode merely because a user says "show me". Calculations,
comparisons and ordinary sales questions use `retrieve_reporting_data` through
Data Mode. Never send `client_id`, `reporting_mode`, or `_widget_action`, and do
not call the app-only `set_reporting_mode` control from the conversation.

## Select compatible eBay fields

- For order summaries, use `Orders`, `Order Total`, and `Quantity (Orders)`;
  an order count and a unit count are different measures. Keep monetary totals
  separated by `Order Currency`; do not invent a currency or convert amounts
  without an explicit conversion basis.
- For sold products, use `Quantity (Orders)` and `Product Revenue (Orders)`
  with order-line dimensions such as `Item ID (orders)`, `Item Name`, and
  `SKU (Orders)`. Include `Product Currency (Orders)` for product revenue.
  Do not sum order-level totals across item groups: a multi-item order can
  appear in several groups. Preserve distinct item IDs and missing SKUs.
- `Item Title`, `SKU (Items)`, listing and inventory fields describe current
  snapshots, not historical inventory for a supplied date range. Seller-standard
  fields describe the current returned evaluation. Inspect each report section
  and any assumptions; do not duplicate snapshots across comparison periods.
- `Total Marketplace Fees` and `Transaction Fees` refer to the same underlying
  fee. Do not add them together. Keep order value, product revenue, tax, fees,
  refunds and seller payout distinct; none alone establishes profit.
- Use supported field names from discovery. Listing views and category or
  marketplace dimensions are not currently in this connector's catalog.
  Request buyer names or notes only when needed for the user's question.

## Respect the component lifecycle

The component handles its Run and mode-toggle controls through the tool bridge.
Do not duplicate its requests or ask the user to rerun immediately after opening
it. If the component publishes model-visible rows in `structuredContent`, use
those rows for a requested analysis without repeating an identical call. `_meta`
is component-only; do not treat it as model-visible evidence.

Keep Date, Week, Month and Quarter in `time_granularity`, not breakdowns. Omit
time granularity for a total-only report. Multiple date ranges represent distinct
requested periods. Do not invent filters, sorting or limits in tool arguments.
If the workspace is missing, report the access issue. If a field is rejected,
refresh discovery and correct it once. If the user changes the task to analysis
or raw data, switch to `retrieve_reporting_data` rather than passing a mode flag.
