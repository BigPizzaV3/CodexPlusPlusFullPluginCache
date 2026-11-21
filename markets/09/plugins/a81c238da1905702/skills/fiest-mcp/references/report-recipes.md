# Reports and restaurant questions

Use the current tool schemas and returned evidence. These recipes describe
bounded MCP reads, not a complete payment-provider ledger or Fiest's official
export generator. Create custom files with the client's file tools. If a file
cannot be created, give the useful summary and state that limitation.

## Periods, rows, and totals

Resolve the restaurant first. Dates use its time zone and business-day start,
not the client's midnight. Summary, trend, filtered-order, refund, and movement
reads accept at most 31 inclusive dates. Split longer periods into consecutive
windows without gaps or overlaps. Keep returned bounds in the report.

Follow `nextCursor` until null where the tool provides it, keeping the exact
filters and dates for continuation. Other bounded tools may return truncation
without a cursor; never claim that their capped result is the complete dataset.
Keep `partial`, `review_required`, `legacy_cumulative`, unavailable fields, and
other evidence flags beside the affected rows. Do not discard them to balance
figures. A failed page leaves the report incomplete.

Amounts ending in `Minor` are integer minor units. Sum in cents, then format in
the returned currency. Do not mix currencies or estimate missing values. Use
totals and order counts to recompute a combined average, rather than averaging
daily averages. Reconcile matching periods and semantics; explain differences
instead of changing rows to make them agree.

## Sales and demand

Use `get_sales_summary` with `breakdown=day` for daily rows,
`breakdown=payment_method` for method totals, or `breakdown=none` for a summary.
Use `get_order_trends` only for the needed dimension: `hour_of_day`,
`day_of_week`, `order_type`, `item_type`, `item`, or `category`. Rankings have a
25-bucket cap. Label a top-item report as a ranking when coverage is incomplete.

Compare periods with the same business-date interpretation. Keep product sales,
discounts, refunds, tips, and deferred gift-card purchases distinct. Sales
figures already reflect their defined refund treatment; do not subtract the
refund headline again. Expired gift-card income is separate accounting income.

## Refunds

For "all refunds last month", call `find_refunds` for refund occurrence dates,
with up to 20 events per page, and follow every cursor. Include `refundId`,
`occurredAt`, `businessDate`, `kind`, the original order/date when available,
`amountMinor`, accounting impacts, and evidence flags. `items` is bounded;
retain `itemsTruncated` and `itemsEvidence` when reporting returned products.

`amountMinor` is the money returned in this event. `cumulativeAmountMinor` is
informational; never post that cumulative amount again. Signed `accounting`
impacts for sale refunds are separate from pending-payment, duplicate-capture,
and unfinished-payment returns, which do not create another sale credit.
Unresolved impacts stay unknown. Original-order details describe the current
cumulative state and cannot replace frozen incremental refund evidence.

Reconcile the complete period against `get_accounting_summary`, preserving
`totals.refundsMinor` and `refundBreakdown` for sales, tips, deferred gift cards,
non-sale payments, and unallocated amounts. Missing breakdowns remain unavailable.

If the user means refunds of sales made during a period, explain the difference:
the feed filters refund dates and cannot find all later refunds using only the
sale period. Confirm the refund search horizon or report the available scope.
Historical aggregates cannot reconstruct missing partial-refund dates. Voids
are found in order history and are not synthesized as refund events.

## Orders and payment questions

Use `find_orders` with its supported date, method, status, amount, item, or time
filters. Carry the returned opaque `orderId` into `get_order_details` when needed.
Both summaries and details have item/evidence caps. Do not infer customer
identity, notes, missing VAT, or provider settlement from omitted data.

An order's amount and effective payment-method label are not every individual
payment leg. For "card payments over 50 euros", clarify whether the user means
orders paid by card or individual tenders. `minTotalMinor` filters order totals;
never claim it filters a split's card leg. Payment references identify retained
provider records but do not prove provider settlement or refund execution.

## Accounting and payment allocations

Read `get_accounting_summary` and `get_payment_report` for the same restaurant,
currency, time zone, cutoff, and business dates. Payment reports use `scope=day`
or `scope=month`, at most 31 inclusive dates inside one calendar month. Split
cross-month requests at month boundaries. Do not invent an MCP range scope.

The accounting summary's method totals are raw. Keep `rawRows`,
`rawSourceBasis`, nullable `adjustedRows`, and status distinguishable. Use
adjusted method allocations only when the report is `ready`, accounting is
balanced, coverage matches, and VAT/tender evidence is complete. A
`review_required` or `blocked_stale` report stays out of a bookkeeping import;
show raw figures for review rather than silently using them as corrected rows.
Never add raw and adjusted methods together or change sales/VAT to match a
payment-only correction.

Present `giftCardExpiryIncome` separately from sales, VAT buckets, payment
methods, and reconciliation. It can be negative after reactivation reversals.
When null, report it unavailable. Repeat bookkeeping imports require retained
snapshots and correction IDs; an unchanged snapshot is not another posting.

## Stock and location comparisons

Use `get_inventory_status` for all, low, or out-of-stock items, up to 50 at a
time. It is current stock: its low-stock rule is the weekly purchasing
report's, and its quantities are in display units. Use
`get_inventory_movements` for selected stock IDs and a bounded period, up to
50 newest movements. These tools do not provide a complete supplier purchasing
history or authorize a purchase. Keep quantities in their returned units and
explain caps before calling a report complete.

For cost of goods sold, gross margin, waste (hävikki), count differences
(inventaarioerot) or stock value on a past date (varastoarvo), call
`get_inventory_report` for up to 93 days. Its figures are Fiest's inventory
report itself, computed by the same code as Inventory › Exports and the
monthly inventory email; quote them as returned and never recompute COGS,
margin or value from movements or stock rows. `trackedMarginPercent` covers
tracked sales only; `closingInventoryValue` is the value at the end of
`endDate`. When the restaurant does not use inventory, the tool says so.
The official files (inventory report workbook, low-stock list, stock items,
inventory value PDF) are downloaded from Inventory › Exports in Fiest; this
connector does not build them.

`get_scheduled_reports` says which automatic report emails are on (weekly and
monthly sales, low stock, monthly inventory), with recipient counts and the
last run. It needs sales access and returns no addresses; settings change in
Fiest.

For Management, use `get_management_context` and choose one organization.
`compare_restaurant_sales` compares 2 to 10 authorized restaurants over the
same bounded period. Preserve legal-identity warnings; one Management
organization is not necessarily one accounting entity. For row-level files,
run each restaurant's recipe with its authorized organization/restaurant pair
and add a Location column. Keep each location's own reporting boundaries.

## Deliver the requested report

For rows, create XLSX when supported, otherwise CSV. Choose a delimiter and
number format the user's spreadsheet can read. Preserve IDs and codes as text.
Include restaurant/location, period, currency, reporting basis, generation
time, source tools, totals, and coverage/evidence notes. Use period first, then
the restaurant in the file name. A custom MCP report is not an official Fiest
export or legal receipt. For a canonical receipt, use the separate file workflow.
Do not upload or email the report without the user's instruction.
