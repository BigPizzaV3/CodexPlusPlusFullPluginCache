---
name: tradehand
description: Find, message, price and book local UK tradespeople with Tradehand, then hand the customer a Stripe link to pay.
---

Tradehand's MCP server is `https://tradehand.com/api/mcp` (ChatGPT: `/api/mcp/chatgpt`), Streamable HTTP.

Find
- `browse_trades` lists the trades. `search_traders` finds public listings by trade and area. `get_trader` and `get_service_options` open one listing.

Talk to the trader (signed-in customer)
- `message_trader` passes the customer's own words to the trader's Assistant and returns its reply. With a `jobId` it continues that job's conversation (questions, moving a visit, access, extra work); with a `quoteToken` it continues a quote request; with neither it starts a new quote request and returns its `quoteToken`. If `replied` is false, read `get_job` shortly after.
- `list_my_jobs` and `get_job` (by `jobId` or `quoteToken`) show progress, price and the latest messages. Photos: `quote_uploadUrl`, then `quote_addPhoto`.

Book a fixed-price service
1. `prepare_booking` with the listing's reference, the service, the full address and postcode. It returns fixed-price services, live slots (each with a `slotReference`) and a `revision`.
2. `confirm_booking` with that `revision` as `expectedRevision` and the chosen `slotReference`. The first call returns the live total and books nothing. Show it.
3. Only after the customer says yes, call `confirm_booking` again with that exact `confirmedTotalAmount`. It books the visit and returns `checkoutUrl`.
- `get_payment_link` returns the payment link for money due on a job or an accepted quote.
- A link is never payment. Say it is paid only when `get_job` says so.
- `SLOT_UNAVAILABLE` or `STALE_REVIEW`: call `prepare_booking` again and offer the new times or price.
