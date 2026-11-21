---
name: inspect-listing
description: >-
  Deepen on one Karta listing: catalog details and/or live room rates. Use when
  the user already has a listing_page_url (or listing_url) and asks what the
  place is like, amenities, house rules, or comparable rates for dates. Do not
  use for destination-wide search (use find-stays) or to invent booking links.
---

# Inspect one Karta listing

## Goal

Answer questions about a single stay using Karta tools, then send the user to the site to book.

## Steps

1. If unsure which tool fits, call `mcp_guide` first (no args).
2. Catalog / “what is this place?” → `listing_details` with `url` = `listing_page_url` or `listing_url`.
3. Live rooms / board / cancellation / prices for dates → `listing_rates` with the same `url` (optional `arrival` / `departure` / `adults` / `child_ages` if not already on the URL).
4. Compare rates in chat. For booking or browsing, open `listing_page_url` in the browser.
5. Do not invent amenities, rates, or booking links.

## Output

- Separate catalog facts from live rates (different tools).
- Summarize board and cancellation briefly when rates are shown.
- End with a clear site link to continue on karta.com.
