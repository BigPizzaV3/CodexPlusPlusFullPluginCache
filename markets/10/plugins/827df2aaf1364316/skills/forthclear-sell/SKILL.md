---
name: forthclear-sell
description: Manage the connected ForthClear seller's listings, quote inbox, order exports, and shipping using its MCP tools.
---

Use the ForthClear MCP connection. Seller account tools require linking a
seller account; do not ask for secrets in chat. Public pricing recommendations
can run without connecting, but they are guidance rather than guaranteed sales.

Start inbox reviews with `seller_inbox_summarise` or `get_quote_requests`.
Describe the actual pending quotes, ship-by risks, and issues returned by the
server. Do not infer that an empty inbox means there are no active orders.
`bulk_export_orders` exports only the connected seller's orders; treat the
result as private account data.

For `create_listing`, collect required product facts from the seller: name,
category, condition, quantity, unit price, currency, minimum order quantity,
and any other required fields in the tool schema. Inputs use minor units where
specified. Do not invent provenance, condition, warranties, stock, or shipping
terms. Review the concrete listing details with the seller before publishing.
Use `get_pricing_recommendation` when requested and distinguish a recommendation
from the price the seller authorizes.

`respond_to_quote` accepts, counters, or declines a real quote. Identify the
quote and action; confirm price, quantity, shipping, and any applicable terms
before submitting a counteroffer or acceptance. Respect authorization already
provided by the user; do not add repeated confirmation for the same action.

`bulk_update_listings` overwrites price or minimum order quantity. Show the
specific listing IDs and proposed values before an authorized update; do not
interpret a general optimization request as permission to change all prices.
Batch limits come from the current tool schema (currently up to 200 items).
`bulk_mark_shipped` requires actual carrier/tracking details for the intended
orders. Do not mark goods shipped merely because a label was created.

Use supported idempotency keys for bulk operations. If a response is partial,
report successful and failed items and retry only failed items after resolving
their errors. If a write times out, verify its outcome before replaying it.
Never claim a listing, shipment, or quote changed without server confirmation.

Read permissions do not grant seller write permission. Follow host account
linking on authentication or scope errors. Connections can be revoked at
https://app.forthclear.io/oauth/connections.
