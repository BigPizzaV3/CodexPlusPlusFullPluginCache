# Flights

## Tool choice

- `find_destination`: inspiration when no destination is chosen. Current v5 accepts IATA airport or city codes in `origins`; a multi-airport city code covers its airports. It has no region parameter, so restrict a theme or region with known destination codes.
- `flight_calendar`: cached route/date discovery. Send `trip_type`; default to `roundtrip` unless the user explicitly requests one way. Use future `departure_dates` or `departure_date_ranges`, optional return equivalents, and `stay_days` or `stay_days_range` for flexible trips.
- `price_monitoring`: cache-only scheduled polling for an exact route and dates. It prices one adult; `traveler_counts` is echoed but does not change the fare or cap.
- `flight_search`: live search for one exact date pair or live re-price of a discovery `offer_token`. Send exactly one nested object: `search` or `price_check`.

## Cached discovery and live confirmation

Cached results from `find_destination`, `flight_calendar`, and `price_monitoring` are indicative one-adult fares. Label them as estimates. Before presenting a fare as bookable or adding it to a trip, confirm it with `flight_search` using the returned `price_check` or an exact-date `search`.

Read each cached response's `search_criteria` and `next`:

- For a non-empty calendar, use the chosen `next.args` price check with the real passenger party.
- For an empty calendar, inspect `next.reason`. Do not claim there are no flights from a cached empty result. Run suggested exact-date searches only when within the booking horizon and within the live-search budget.
- For `beyond_booking_horizon`, do not run live search. Explain that fares are likely not on sale and use `next.opens_on` when supplied.
- For stale monitoring, report the stale snapshot and offer the live next step. Do not run it silently.

Use at most three live `flight_search` confirmations after discovery per user request, unless the user explicitly asked to compare more than three exact dates. Apply one shared budget across routes/date windows and name candidates not checked live.

## Route, party, filters, and budgets

- Never invent an IATA code. Ask when the place cannot be mapped confidently.
- Send a city code when the user named a city and an airport code plus `origin_type` or `destination_type: "airport"` when they named an airport. This matters for codes such as `LAX`, `MIA`, and `LAS`, which default to city scope.
- Always send the real party as `traveler_counts` (adults 12+, children 2–11, infants under 2) to live search and price check: counts only, never a name or a date of birth. Never retry by dropping a child or infant. A party with anyone under 13 is booked on the Jinko page at the trip's `trip_link`; see Jinko Booking.
- Send `cabin_class` only when the user explicitly selected a cabin; otherwise omit it or send `null`.
- Use `max_stops: 0` for nonstop live searches. Preserve every stated live filter, including carriers, fare conditions, baggage, times, connections, duration, airports, and aircraft.
- A calendar `max_total` and monitoring `max_price` cap one adult. A live `flight_search.search.max_price` caps the whole trip for all passengers. Convert a per-person budget to a whole-party live cap; use a whole-trip budget unchanged for live search.
- A time window belongs only to the date and leg the user attached it to. On a round trip, apply a trip-wide departure window to both outbound and return departures unless the user says otherwise.

## Present and continue

- Compare all live results fetched for the request, not only the last call.
- A live result supersedes its cached estimate.
- Distinguish a successful empty result, an unavailable offer, a failed call, and an unperformed check.
- Do not silently relax filters. Ask which constraint to change when the live instruction says the filter combination produced no matches.
- Quote returned price display strings, local dates/times, durations, and fare rules. Do not calculate a display amount from raw money fields.
- If a price check returns `offer_unavailable`, present any returned alternatives and require a new selection. Do not add the old token.
- Add only the selected live fare's `trip_item_token` through `trip(add_item)`.

