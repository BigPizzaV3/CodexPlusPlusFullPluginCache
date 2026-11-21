---
name: manage-etsy-orders
description: Inspect current Etsy orders, customization, fulfillment needs, transactions and financial records; prepare action worksheets from exports without MCP or carry out exactly authorized fulfillment with real data.
---

# Orders and fulfillment

Read [order workflow](../../references/orders-workflow.md). Offline use a supplied export and label its capture time. Connected use live `list_orders`/`get_order` or direct receipt/transaction tools; do not require a dashboard refresh to read Etsy.

## Read before deciding

Choose date range/timezone and retrieve requested pages. Distinguish receipt, transaction, payment and listing IDs. Inspect paid/unshipped/deadline state and all line-item personalization, not just the first text value. Classify actual overdue dispatch, missing input, cancellations or tracking issues using recorded facts; an unshipped order is not automatically late.

Return receipt/status/item count/deadline/issue/next action with source/time, and only the buyer details necessary for the task. Keep private addresses and emails out of examples and general reports.

## Authorized fulfillment

Read exact receipt, collect real carrier/tracking/dispatch and approved buyer note. `etsy_create_receipt_shipment` can notify the buyer; it does not buy a label. Inspect current schema and obtain/reuse authorization for the actual shipment and notification. Never fabricate tracking, mark all orders shipped from a general read request, or resend uncertain buyer notifications. Read the receipt after acceptance and report unconfirmed outcomes honestly.

For payments/ledger reads preserve amount/divisor/currency and distinguish sales, fees, settlements and already-recorded refunds. Do not infer authority to issue refunds or transfers. General Etsy messaging, ad control and refund initiation are not available just because an order tool exists. See [index](../../references/etsy-operation-index.md) for exact supported methods.
