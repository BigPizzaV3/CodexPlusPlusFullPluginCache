---
name: find-stays
description: >-
  Find hotels and stays on Karta by place, dates, and guests. Use when the user
  asks for hotels, villas, or stays in a destination, wants a shortlist with
  from-prices, or needs listing_page_url links. Do not use for flights, cars,
  calendars, email, or booking payment inside chat.
---

# Find stays on Karta

## Goal

Return a short Karta shortlist for the user's trip (place + dates + guests).

## Steps

1. If the funnel or tool choice is unclear, call `mcp_guide` first (no args).
2. Call `stays_search` with:
   - `direction.text` for city / region / landmark (prefer text first)
   - `dates.arrival` / `dates.departure` as `YYYY-MM-DD` (UTC, future, departure after arrival)
   - `pax.adults` (and `pax.child_ages` if kids)
3. Present results as a shortlist: title, style, from-prices, `listing_page_url`.
4. Do not invent prices, amenities, or room inventories.
5. If the user wants more about one place or live rates, hand off to those tools using `listing_page_url` unchanged (see skill `inspect-listing`).

## Output

- Keep the list short and actionable.
- Include openable `listing_page_url` links.
- Do not invent stays, prices, amenities, or links.
