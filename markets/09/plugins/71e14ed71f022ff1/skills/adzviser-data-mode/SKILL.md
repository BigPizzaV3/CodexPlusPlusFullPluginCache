---
name: adzviser-data-mode
description: Retrieve and analyze model-visible eBay orders, sales, products, fees, inventory, and seller data with Adzviser. Use for Data Mode, raw rows, calculations, comparisons, trends, or answers requiring the underlying numbers. Do not use when the user explicitly wants only an interactive preview.
---

# Adzviser eBay Data Mode

This plugin supports connected eBay accounts only. Discover fields with
`list_metrics_and_breakdowns_ebay` and use only `assorted_requests.ebay_request`.
For another source, explain the scope and suggest its corresponding connector.
This reporting plugin cannot buy items, edit or publish listings, change prices
or inventory, cancel orders, message buyers, or issue refunds. Do not use
reporting calls as a substitute for a requested mutation or claim it happened.

## Retrieve rows for analysis

1. Resolve the user's workspace and reporting question. Call `list_workspace`;
   use a named workspace when available and clarify if several candidates remain.
   Do not switch away from a requested workspace after an access failure.
2. Discover valid fields with `list_metrics_and_breakdowns_ebay`. Resolve relative
   dates using today's date. Pass inclusive `[start_date, end_date]` pairs in
   `YYYY-MM-DD` format. Use complete calendar periods when the user says last
   month or last week; state the interpretation.
3. Call `retrieve_reporting_data` with `adzviser_request` containing
   `workspace_name`, `date_ranges`, and an `assorted_requests` object with only
   `ebay_request`. That source request contains `metrics` and optional
   `breakdowns`. For a time series, add `time_granularity`; otherwise omit it.
   Date, Week, Month and Quarter are not breakdown fields.
4. Read every relevant section of `structuredContent.reportingData`, its headers,
   rows, date ranges and `note_of_assumption`. Text/CSV is a fallback if structured
   content is absent. Answer from returned rows and preserve their units.

Use multiple date-range pairs in one request for comparisons. No arbitrary
filter, sort or limit arguments are supported; calculate and rank from returned
rows. Match currencies and entities before comparing periods. Calculate
percentage change only when the baseline is present and nonzero. Missing rows
are not proof of zero activity, and omitted days must not be fabricated.

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

## Keep Data Mode separate from the preview

Call `retrieve_reporting_data` for analysis. `preview_and_retrieve_reporting_data`
opens a component and is only for explicit interactive-preview requests.
`reporting_mode=data` is user intent, not a request field. Do not send
`client_id`, `reporting_mode`, or `_widget_action`, or call `set_reporting_mode`;
those are internal/app-only controls. If the user wants both analysis and a
preview, analyze rows first and open the preview as the separate requested step.

Use model-visible `structuredContent`, not component-only `_meta`. Do not repeat
an identical retrieval merely because a widget or follow-up message appears.
An empty successful result is a no-data result, not an invented zero total.
If a field is rejected, refresh discovery, correct the request once, and retry;
report a persistent error instead of adding unsupported parameters.
