---
name: flightpoints-award-search
description: Search and compare airline award-flight availability bookable with points or miles using FlightPoints, then inspect flight segments for a selected loyalty-program result. Use for award seats, mileage redemptions, cabin availability, points prices, taxes, flexible dates, direct routes, and loyalty-program filters. Do not use for cash-fare shopping, hotels, booking or purchasing tickets, payments, points transfers, or account and subscription management.
---

# FlightPoints Award Search

Use the connected FlightPoints tools to find award availability and inspect a selected result. Preserve the user's stated route, date, cabin, passenger count, and filters.

## Prepare the search

- Convert origins and destinations to uppercase three-letter airport codes. If a city has multiple plausible airports and the user has not expressed a preference, ask which airport they want before searching.
- Convert an unambiguous relative date to `YYYY-MM-DD`. Ask for clarification when the date or year is ambiguous.
- Use these cabin values: `economy`, `premium_economy`, `business`, or `first`.
- Default to one passenger and economy only when the user does not specify them.
- When the user requests multiple award seats, set both `passengers` and `minimum_seats` to that count.
- Express date flexibility with `delta`, the number of days on either side of the departure date.
- Map explicit preferences to implemented filters: `only_direct`, `max_fees`, `filter_cabin` for operating-airline codes, `programmes`, `alliances`, `max_points`, and `days_of_week`. Use the matching exclusion flag only when the user asks to exclude a named airline, program, or alliance. Do not add unstated filters.

## Search award availability

Call `search-flights` for requests to find or compare flights bookable with points or miles.

- For a new search, provide `origin`, `destination`, and `departure_date` plus the user's other constraints.
- Do not set or claim the search mode. FlightPoints chooses cached or live availability from the user's linked-account entitlement.
- Never request credentials, tokens, payment data, or subscription details. Authentication is handled by the connected FlightPoints account.
- If the result is still processing, let the widget poll. If no widget polling is available, poll `search-flights` using only the returned `search_key`; do not start a duplicate search.
- Treat `is_live`, `is_authenticated`, `is_premium`, and `search_mode` in the response as authoritative. Do not describe cached results as live.

## Inspect a result

Call `get-flight-details` when the user asks for segments, times, aircraft, duration, operating airlines, or a booking handoff for a specific result.

- Use the selected result's exact `departure_date`, `program`, `origin`, and `destination`.
- Set `direct_flight_only` only when the user requested a nonstop itinerary or selected a nonstop result.
- Never guess a loyalty-program code. If the selected result does not provide one, explain that details cannot be retrieved for that option.
- A booking URL is a handoff link only. Do not claim that FlightPoints can reserve, ticket, transfer points, accept payment, or complete a booking.

## Present results

- Lead with the options that satisfy the requested cabin and seat count.
- When the user says "best" without defining it, compare points price, taxes or fees, stops, and seat availability; identify the tradeoff instead of asserting a universal winner.
- Keep points or miles separate from cash taxes and fees.
- Report only fields returned by FlightPoints. Do not invent availability, transfer partners, aircraft, amenities, or booking rules.
- Describe an empty result as no matching award availability found, not proof that no flight operates.
- When useful, mention whether results are cached or live and include `last_seen` freshness information if returned.
- If no matching award is found, suggest widening dates, cabins, airports, programs, points limits, or routing filters. Run a broader search only when the user requests it.

## Boundaries

- Do not invoke FlightPoints for cash airfare, hotel awards, general travel planning, flight status, schedules without award intent, or loyalty-account administration.
- Do not invoke FlightPoints when the request is to purchase, book, or pay for a ticket. Explain that FlightPoints can search award availability and may provide a booking handoff link, but cannot complete the transaction.
- For mixed requests, perform only the supported award-search or detail-retrieval portion and clearly state the unsupported portion.
