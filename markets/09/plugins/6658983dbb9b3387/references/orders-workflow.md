# Orders, fulfillment and financial reads

Offline, analyze a supplied export as of its export timestamp and prepare a fulfillment worksheet. Connected, read live Etsy orders even if the MakeBox dashboard snapshot has not been refreshed. Never represent an export as current.

## Read and triage

Use `list_orders`/`get_order` for live MakeBox summaries or the exact direct receipt/transaction operations in the [index](etsy-operation-index.md). Paginate all requested records. State date range, timezone, capture time and whether the result is complete. Order, receipt, transaction, payment and listing IDs are not interchangeable.

Prioritize actual unpaid/payment issues, impending or overdue dispatch, missing customization, cancellations, tracking anomalies and explicit buyer requests. Do not call every unshipped order overdue; read the order's processing/deadline and current state. A personalized item may have multiple personalization values, including upload links; inspect all relevant line items. Collect only the buyer data needed for fulfillment.

## Fulfillment writes

Read the exact receipt and line items. Match seller-approved real carrier, tracking, dispatch information and any buyer-facing note. `etsy_create_receipt_shipment` can notify the buyer; obtain approval covering that consequence. “Create shipment” is not a purchased postage label. `etsy_update_shop_receipt` follows its own current fields; do not invent delivery confirmation or cancellation authority.

After acceptance reread the receipt and compare requested shipping/tracking/status. If ambiguous, do not repeat a buyer notification blindly. Drafting a message does not authorize sending it, and a note-to-buyer field is not a general messaging API.

## Reports

Payment and ledger endpoints are reads. Preserve money amount/divisor/currency, fees versus gross/net and settlement date versus order date. Do not aggregate different currencies without an explicitly sourced conversion. Distinguish order sales, payments, fees, deposits and refunds already recorded. These tools do not authorize a new refund, transfer or purchase.

Output `receipt | current status | item/quantity | dispatch deadline | issue | next action | source/time`. Include buyer identities only in the private operational view where necessary. Never reuse real buyer data in plugin examples or public reports.
