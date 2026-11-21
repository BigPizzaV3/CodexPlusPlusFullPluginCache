---
name: get-started
description: Help the user connect GC Airport Transfers and run a first fixed-price quote.
---

# Get started with GC Airport Transfers

1. Confirm the user wants Gold Coast / Brisbane airport or Brisbane Cruise Terminal transfers (private, fixed-price, per vehicle).
2. If the MCP connection is not authorised yet, ask them to approve access when ChatGPT prompts for OAuth. Explain: approving lets the assistant get quotes, check availability, and lodge booking *requests*; a human confirms every booking; payment is only by emailed link.
3. Ask for pick-up, drop-off, passenger count, and optionally date/time.
4. Call `get_quote` — never invent a price. If `match` is not `fixed_route`, share the phone **0414 680 860** instead of guessing.
5. Offer `check_availability` when a date/time is known, then `request_booking` only after the user confirms name, email, phone, and trip details.
