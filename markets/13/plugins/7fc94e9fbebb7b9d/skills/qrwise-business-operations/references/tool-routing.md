# QRWise tool routing

Choose the narrowest tool that directly answers the user's question.

## Identity and stores

| Tool           | Use for                                                                  | Important behavior                                          |
| -------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| `get_merchant` | Identify approved merchants, environment, currency, and read-only access | Use the merchants list to establish connection scope.       |
| `list_stores`  | List authorized merchant stores                                          | Paginated; follow `next_offset` when all stores are needed. |

## Sales and tax

These tools accept ranges of up to 366 QRWise business dates except
`get_daily_payment_method_sales`, which accepts up to 31. Missing dates are not
automatically zero-sales dates.

| Tool                             | Use for                                                                                                                                                                | Important behavior                                                                                                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_transaction_sales`          | Finalized sales totals, transaction statuses, payment methods, channels, monthly totals, and optional daily totals                                                     | Uses paid, closed transactions and deduplicates current data with authorized backups. Cancelled, returned, and refunded transactions are excluded from paid sales.                                |
| `get_daily_payment_method_sales` | Complete date-by-payment-method tax classes, service charge, statutory discounts, audience-classified voucher discounts, net sales, and transaction counts in one call | Use for up to 31 business dates instead of paginating raw transactions. Take-out charge is already in net sales. Split-tender money is allocated proportionally and totals reconcile to the cent. |
| `get_category_sales`             | Category sales, item sales, quantities, and best sellers                                                                                                               | Allocates transaction gross sales, discounts, net sales, service charge, and payable totals across line items with cent reconciliation. `item_sales_amount` equals net sales.                     |
| `get_menu_item_hourly_sales`     | One menu item's quantity, transactions, and reconciled sales amounts by Manila clock hour                                                                              | Uses invoice-entry time with transaction creation time as fallback. Check `unbucketed`; do not infer missing timestamps or rebuild the report from raw records.                                   |
| `get_tax_sales_summary`          | Recorded VAT and other transaction tax classifications                                                                                                                 | A transaction summary, not a replacement for finalized X/Z readings. Legacy classifications may be incomplete.                                                                                    |
| `get_sales_channel_activity`     | Grab, Foodpanda, kiosk, walk-in, or other channel performance                                                                                                          | Uses paid, closed transactions. Item rows use the same reconciled allocation as category sales. Apply an exact channel filter only when the user specifies one.                                   |

### Receipt and product detail

| Tool                     | Use for                                                                     | Important behavior                                                                                                                                                                                                                                                                    |
| ------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `find_receipt`           | Saved item rows, tenders, totals, and statuses for a single receipt         | Provide one exact printed invoice number, QR Wise transaction number or order reference as `receiptNumber`, or use `transactionId`. Preserve leading zeros. If the result is ambiguous, ask the user to select a matching ID or supply a business date or POS. Current receipts only. |
| `list_product_mix`       | Sold product quantities and gross sales by exact product, SKU, and category | Up to 90 inclusive business dates from current paid sales, with optional receipt POS filtering. Use the page and total fields to complete the report.                                                                                                                                 |
| `get_product_option_mix` | Complete option and add-on combinations sold for a product                  | Reuse exact product, SKU, and category labels from `list_product_mix` with the same dates and POS. Omit SKU or category only when its row value is null. The added price is already included in gross sales.                                                                          |

For a found receipt, preserve the saved statuses and totals. Item or tender rows
can include cancellations, refunds, or pending payments. An empty tender list
can still have a saved payment method on the receipt. If a truncation flag is
set, state that the corresponding list is partial.

## Readings, registers, and exceptions

| Tool                                 | Use for                                                                            | Important behavior                                                                                                                                                                           |
| ------------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_reading_activity`               | Current X/Z-reading counts and totals                                              | Up to 366 business dates; the detail list is bounded and missing readings are not reconstructed.                                                                                             |
| `get_end_of_day_status`              | Oldest overdue Z-reading, scheduled close, and open-bill and active-order blockers | Omit `posDeviceId` for shared fiscal registration. Supply the active POS device ID for an independent registration. A null business date means no overdue close was reported for that scope. |
| `get_register_activity`              | Drawer opens, manual opens, reversed cash transactions, and net cash               | Up to 366 business dates. It does not infer over/short from transactions.                                                                                                                    |
| `get_shift_reconciliation`           | Expected versus counted cash, over/short, and reconciliation status                | Current X-reading data only; no variance is inferred for an uncounted shift.                                                                                                                 |
| `get_transaction_exception_activity` | Refunded, returned, cancelled, and legacy void activity                            | Up to 366 business dates. Older reason text may be unavailable.                                                                                                                              |
| `get_store_activity`                 | Sanitized store audit activity                                                     | Maximum 31-date range and paginated. Detailed metadata and changed values are intentionally excluded.                                                                                        |

## Menu, inventory, integrations, and orders

| Tool                        | Use for                                                                                                | Important behavior                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `get_menu_health`           | Inactive or low-stock items, empty categories, unassigned options/add-ons, and missing delivery prices | Current read-only health check with bounded issue lists.                                                                         |
| `get_inventory_activity`    | Restocks, deductions, adjustments, low stock, and out-of-stock items                                   | Up to 366 Asia/Manila calendar dates; current-system history only.                                                               |
| `get_integration_health`    | Safe enablement and configuration status for supported integrations                                    | Never returns credentials, tokens, external merchant IDs, payloads, or provider errors.                                          |
| `get_order_operations`      | Open/completed/cancelled orders, preparation state, delays, tables, and completion time                | Up to 366 business dates; current workflow records only.                                                                         |
| `get_store_operating_hours` | Weekly store hours and automatic closing Z-reading setting                                             | Manila local times. Monday is 1 and Sunday is 7. Use the closed-day flag and check actual blockers with `get_end_of_day_status`. |

## Promotions, payments, people, and experience

| Tool                            | Use for                                                                                       | Important behavior                                                                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_discount_voucher_activity` | Actual discounts and voucher use recorded on paid transactions                                | Up to 366 business dates. Do not confuse configured voucher allowance with recorded usage.                                                                 |
| `list_promotions`               | Find active, scheduled, expired, or inactive promotions by name                               | Campaign status and linked menu item availability are separate. Use the promotion ID for the reports below.                                                |
| `get_promotion_performance`     | Recorded redemptions, promotion-attributed net sales, and available Kitavo AI comparison      | Supply both business dates to limit recorded sales, or omit both for all tracked sales. Kitavo AI measures the full campaign separately.                   |
| `get_promotion_redemptions`     | Individual paid promotion uses with business dates, transaction IDs, and attributed net sales | A bundle counts once per recorded use. Follow `next_offset`, then use `find_receipt` with a returned transaction ID to reconcile an individual redemption. |
| `get_payment_activity`          | Payment methods, statuses, failures, refunds, cancellations, and recorded discrepancies       | Up to 366 business dates. Provider credentials and references are excluded.                                                                                |
| `get_staff_activity`            | Staff sales, discounts, exceptions, and manual drawer opens                                   | Up to 366 business dates. Returns display names only, not employee numbers or contact details.                                                             |
| `get_kiosk_experience`          | Ratings, response/skip rates, positive ratings, and star distribution                         | Up to 366 Asia/Manila calendar dates and no customer identity.                                                                                             |

For “How many bundles sold this week?”, select the store and promotion, then
report the recorded count and attributed net sales for the requested business
dates. A promotion can be active while a linked menu item is inactive.

## Settlements, business records, and backups

| Tool                          | Use for                                                                                                             | Important behavior                                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_settlements`            | Netbank payout amounts, statuses, references, and dates                                                             | Uses Asia/Manila payout creation dates, not business dates. Paginated and excludes bank account details.                                                                |
| `list_store_business_records` | Approved catalog, inventory, settings, order, payment, discount, and voucher fields not covered by a focused report | Use only an enumerated dataset. Dated datasets accept at most 31 Asia/Manila creation dates. Pages are not snapshots, and raw rows must not be summed indiscriminately. |
| `list_store_data_backups`     | List authorized automatic and manual Store Data backups                                                             | Paginated. Backups are historical snapshots, not current live data.                                                                                                     |
| `read_store_data_backup`      | Read a bounded page of privacy-filtered records from a listed backup                                                | Use only a path returned by `list_store_data_backups`. Follow `next_offset`; sensitive fields are excluded.                                                             |
