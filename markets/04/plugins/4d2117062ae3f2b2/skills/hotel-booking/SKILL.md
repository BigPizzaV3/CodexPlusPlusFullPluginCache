---
name: hotel-booking
description: Search and book hotels on trip1 via MCP, paid per reservation in USDC on Base using x402. Covers 3M+ properties in 200+ countries.
---

# Booking hotels on trip1

trip1 exposes an MCP server that lets an AI agent search, price, and book hotels without a human browser session. Payment is handled inline via x402 on Base (USDC).

## Connect

- MCP endpoint: `https://trip1.com/api/mcp` (Streamable HTTP, spec 2025-06-18)
- Server card: https://trip1.com/.well-known/mcp.json
- x402 discovery: https://trip1.com/.well-known/x402.json
- Human docs: https://trip1.com/agents

Configure your MCP client with the endpoint above. No authentication is required to browse or search — payment is attached per booking via x402.

## Tools and order of calls

1. `search_hotels` — find hotels by destination name and dates. Returns properties with pricing, images, and a booking link.
2. `get_hotel_details` — fetch rooms, rates, and cancellation terms for one hotel from the search results.
3. `purchase_hotel` — create the reservation with a chosen rate id and guest details. Returns a `payment_url`. The URL returns an x402 challenge when fetched.
4. `get_order_details` — poll after payment until `ready` is `true` to confirm the booking has cleared.

On every remote MCP tool call (`https://trip1.com/api/mcp`), pass `context`: one short sentence on the user's goal (not the tool name; never names, emails, phones, or prices). Occupancy on that server is fixed at 2 adults — do not pass `guests` or `adults` there.

## Guest details

All guest fields are required: first name, last name, email, phone, title, nationality. Collect every field from the user. Never invent, guess, or default any of them. Show the full booking summary and get explicit confirmation before calling `purchase_hotel`.

## Payment

- Default scheme: x402, exact, USDC on Base (`eip155:8453`).
- Alternative: pass `payment_service: "coingate"` to `purchase_hotel` for a human-completed checkout URL (CoinGate supports USDC and 50+ other coins).
- Never cards. trip1 is crypto-only.

## When things go wrong

- If `get_order_details` returns `ready: false` after 60 seconds, keep polling — on-chain settlement can take longer during network congestion.
- If a rate becomes unavailable between `get_hotel_details` and `purchase_hotel`, re-run `get_hotel_details` for fresh rates.
