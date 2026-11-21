---
name: forthclear-buy
description: Find wholesale surplus inventory on ForthClear, compare lots, request and track bulk quotes, or manage the connected buyer's orders and saved searches.
---

Use the ForthClear MCP connection for current inventory and account information.
Search and product lookup work anonymously. Account tools prompt for linking;
never ask the user to paste a password, API key, or delegated token into chat.

Search with `search_inventory`; use `search_inventory_semantic` for descriptive
queries. Prices in tool inputs and most outputs are integer minor units (cents).
Respect each returned currency. Use actual product IDs returned by search, then
`get_product_details` for condition, available quantity, minimum order quantity,
bulk tiers, shipping, and purchase guidance. Do not invent stock or present
pricing guidance as a binding seller offer. Explain empty results and offer
relevant broader filters without claiming unavailable stock exists.

For a bulk quote, collect the chosen product, quantity, buyer email, and any
requested target price or message. `request_quote` contacts a real seller;
submit when the user authorizes sending those details. It works anonymously
with a buyer email, subject to five requests per hour per IP. An existing
account may require linking to prove ownership. Keep the returned quote ID and
`status_token` private; use them with `get_quote_status` to read seller replies.
A quote request is not a completed order or guaranteed reservation.

`quick_buy` is available only where product details explicitly allow instant
checkout. Confirm the chosen product, quantity, current total and currency,
and available shipping information before starting a purchase. Use a returned
checkout link for payment; never collect card details or imply payment or funds
release succeeded without a successful server response. Bulk thresholds may
require a seller quote. A connection with buyer read/write permissions does
not include purchase permission; follow the account-linking prompt if needed.

Use `get_order_status` only for the connected buyer's order. `open_dispute`
changes a real order and notifies administrators; obtain the user's reason and
authorization to submit it. `subscribe_to_query` persists a saved search and
can dispatch notifications. Honor the user's chosen filters and delivery
method; do not invent a webhook or use a third party's address.

On an authentication error, let the host open account linking and retry the
same requested operation after connection. On a scope error, request only the
permission needed by that operation. Manage or revoke connections at
https://app.forthclear.io/oauth/connections. On a timeout after a write, check
its status or use the tool's supported idempotency key before retrying; do not
submit a duplicate quote, dispute, or purchase blindly.
