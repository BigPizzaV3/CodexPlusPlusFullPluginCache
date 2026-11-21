---
name: adzviser-data-mode
description: Retrieve and analyze reporting from the user's connected Shopify stores with Adzviser. Use for sales, orders, items, product rankings, channel comparisons, trends, raw rows and Data Mode. This plugin does not modify stores, process refunds, place orders or send messages.
---

# Shopify Data Mode

Use `retrieve_reporting_data` for reporting and analysis. Open an interactive
preview only when the user explicitly requests one. Do not follow a successful
direct retrieval with a widget merely to display the same request.

## Build a minimal report

1. Call `list_workspace` and select the user's named Shopify workspace. If access
   is unavailable, explain that rather than substituting another store. If no
   workspace is named and several choices remain, ask which to use.
2. Call `list_metrics_and_breakdowns_shopify` and use exact returned field names,
   including capitalization. Request only the fields necessary for the question.
3. Resolve inclusive YYYY-MM-DD date pairs from the current date. Last month is
   the previous complete calendar month; last week is the previous complete
   Monday-Sunday week unless otherwise specified. Use the store's reporting
   timezone. Put comparison periods in separate date-range pairs in one request.
4. Send `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.shopify_request` containing `metrics`
   and optional `breakdowns`. No other source keys are supported by this plugin.
5. Inspect `structuredContent.reportingData.Shopify.data`, a header row followed
   by data rows, and surface relevant `note_of_assumption` values. Use the actual
   headers and shape returned, not hard-coded column positions from an example.
6. Answer from the rows with the requested figures, exact dates and material
   limitations. Reuse successful results instead of repeating identical queries.

Never send conversation history, the raw user prompt, unrelated context,
credentials, session tokens or arbitrary destinations as reporting inputs.
`reporting_mode=data` selects this workflow; it is not a tool argument. Do not
send `client_id`, `reporting_mode` or `_widget_action`. `set_reporting_mode` is an
app-only preference control. Do not invent report filters, sorting or limits;
sort and aggregate the returned rows when required.

## Interpret sales carefully

- Gross sales, Net sales and Total sales are different metrics. Use the measure
  requested and name it explicitly. If "revenue" is ambiguous, clarify or state
  the sales measure used. Do not describe sales as profit or cash collected.
- The connector defines Net sales as Gross sales minus Discounts and Returns;
  Total sales also incorporates Shipping, Tax and Duties. These component columns
  may be returned automatically. Preserve their signs and the returned derived
  metric; do not subtract a return twice or add components to Total sales again.
- Include Currency for monetary reports and keep currencies separate. Literal
  "None", null and blank values mean missing currency. Label those amounts as
  currency unspecified, show them separately, and do not assume USD or include
  them in a currency-labelled grand total. Explain that a named-currency subtotal
  is not necessarily the complete store total. Negative sales values can occur.
- Product ID with Product title distinguishes products. For a top-products
  question by quantity, request Items and these identifiers, aggregate by ID,
  and sort the returned item counts. Do not request money or customer fields
  unless needed. Explain ties, and distinguish reported Items from Orders.
- Missing product IDs/titles form an unidentified group; do not invent a product
  name or silently merge them into a named product. Show that group separately
  from a ranking of identifiable products. Preserve unknown channel groups too.
- Orders is a count, not the number of line items. An order can contain several
  products, so summing order counts across product groups can double count.
  Customer count is not interchangeable with Orders or Items.
- Report grouping can affect which adjustments are attributable to a product or
  channel. Do not assume independently grouped reports reconcile; compare the
  actual rows and disclose a discrepancy instead of altering numbers to fit.
- Use `time_granularity` for Date, Week, Month or Quarter. Do not add time labels
  to breakdowns. Keep missing dates distinct from returned zero values.
- Calculate percentage changes only when the earlier period is a meaningful
  nonzero baseline. Separate missing-currency amounts; do not calculate a
  currency-specific change from rows whose currency is unknown. Round displayed
  money only after calculations.
- Historical inventory must not be inferred merely from a report's date range.
  Describe inventory according to what the actual tool response establishes.
- Avoid customer emails, names, phone numbers, addresses, order notes and other
  personal fields for aggregate sales reports. Request any sensitive field only
  when necessary for the user's specific authorized reporting task.

For unsupported fields, refresh discovery, correct the request once and retry.
Explain authentication, timeout or access errors without inventing a successful
report. A successful empty report means no returned rows, not proven zero sales.

This connector retrieves reports; it cannot refund or cancel orders, change
prices or stock, edit or delete products/customers, place purchases, or send
marketing emails. Explain unsupported actions without pretending a report
performed them or invoking unrelated tools to simulate success.
