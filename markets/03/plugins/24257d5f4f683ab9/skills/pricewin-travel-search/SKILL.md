---
name: pricewin-travel-search
description: Search and compare live hotel and flight prices with the Pricewin MCP server, including hotel details and cancellation terms for OpenTravel direct listings. Use when the user asks to find hotels or flights for dates, compare travel prices, inspect an OpenTravel hotel or room, or check a selected rate's cancellation policy.
---

# Pricewin Travel Search

Use only the Pricewin MCP dependency declared in `agents/openai.yaml`. Do not
replace it with browser automation, shell commands, direct API calls, or
invented booking URLs.

## Collect the required trip details

For a hotel search, obtain:

- destination or city;
- check-in and check-out dates;
- number of adults, defaulting to 2 when the user does not specify;
- number of rooms, defaulting to 1.

For a flight search, obtain:

- origin and destination airport IATA codes;
- departure date and optional return date;
- number of adults, defaulting to 1;
- cabin, defaulting to economy.

Resolve unambiguous relative dates from the current date. Ask one concise
follow-up when a required date, destination, or airport is genuinely ambiguous.
Never invent a date or silently choose among multiple plausible airports.

Pass `language` matching the user's language when supported. Do not put
unrelated conversation or personal data in `queryText`.

## Search hotels

1. Call `search_hotels_live` with the destination, dates, occupancy, and only
   the filters the user actually requested.
2. Read `sessionId` and `nights` from the response.
3. Call `poll_search_results` with that `sessionId` and `nights`.
4. If the response is pending or partial with no useful results, poll again
   until results arrive, the search completes or fails, or the session expires.
5. Present a concise comparison of relevant results. Label the source and
   currency exactly as returned.

Use `hotelName`, `area`, `priceMin`, or `priceMax` only when the user supplied
that constraint. Do not claim that a result is the cheapest in the whole
market; describe it as the cheapest among the sources returned for this search.
A failed or missing source does not invalidate results from other sources.

## Inspect an OpenTravel direct hotel

Call `get_hotel_detail` only for a hotel identified as an OpenTravel direct
listing.

- Prefer its `propertyId` from `opentravelResults`.
- Reuse the user's dates and occupancy.
- Use `hotelName` plus `city` only when the property is already known to be an
  OpenTravel direct listing and no `propertyId` is available.
- Do not call this tool for an Agoda, Booking.com, or Traveloka-only result.

Present the returned photos, amenities, availability, room capacity, total
price, per-night price, and currency without changing their meaning. State
clearly when availability or a price is missing.

## Explain a cancellation policy

Call `get_cancellation_policy` only after `get_hotel_detail` supplies both:

- the property's `propertyId`; and
- the selected room's `ratePlanId`.

Pass the check-in date so the tool can compute an exact deadline. Report the
returned non-refundable status, refund percentage, free-cancellation window,
deadline, and summary. Never infer a policy or deadline when the tool does not
return one.

## Search flights

1. Call `search_flights_live` with IATA codes, departure date, optional return
   date, adults, and cabin.
2. Read the returned `sessionId`.
3. Use `poll_flight_results` when the host exposes it to the model; otherwise
   let the Pricewin flight widget perform its app-side polling.
4. Continue only until useful results arrive, the search completes or fails, or
   the session expires.
5. Present relevant options with source, carrier, times, stops, cabin, currency,
   and fare exactly as returned.

Keep outbound and return legs distinct. Do not combine unrelated one-way fares
into a round trip or imply that a fare is still available after the live result
expires.

## Safety and output rules

- Use only these six tools: `search_hotels_live`, `poll_search_results`,
  `search_flights_live`, `poll_flight_results`, `get_hotel_detail`, and
  `get_cancellation_policy`.
- Treat all prices as time-sensitive and avoid guarantees or unsupported
  "lowest price" claims.
- Use only outbound URLs returned by the tools. Never construct, append,
  rewrite, or guess a booking URL.
- Explain that booking and payment happen outside ChatGPT on Pricewin or the
  selected travel provider.
- Do not ask for or handle guest names, email addresses, booking references,
  card data, credentials, or other booking/payment information.
- Do not create, modify, cancel, or pay for a booking. Those actions are not
  exposed by this plugin.
- If a tool fails, state the limitation briefly and suggest a new search. Do
  not fabricate partial inventory, prices, availability, or policies.
