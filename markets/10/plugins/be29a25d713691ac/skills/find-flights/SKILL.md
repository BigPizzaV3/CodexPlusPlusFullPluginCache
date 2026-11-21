---
name: find-flights
description: "Search and compare live TravelYalla flight prices (one-way, round-trip or multi-city) and give a travelyalla.com booking link. Use for any request for flights, airfare, plane tickets or the cheapest way to fly on known dates, in English or Arabic (طيران، رحلات طيران، تذاكر طيران، حجز طيران، أرخص طيران), especially to, from or within Egypt, Saudi Arabia and the Gulf."
---

# Find flights

Tools: `search-flights`, then `get-flight-details` when the user wants baggage or fare details for one option.

Explicit user instructions take priority over the defaults here.

## 1. Collect the trip

You need these before searching:

- **From and to.** Use 3-letter IATA airport codes (Cairo `CAI`, Dubai `DXB`, Riyadh `RUH`, Jeddah `JED`, London Heathrow `LHR`). For a city with several airports, use its main airport unless the user names another. Ask if you are not sure of the code.
- **Dates.** Resolve relative dates ("next weekend", "the 10th") against today's date. Never search a date in the past.
- **Trip type.** A return date or "round trip" means two legs. Otherwise search one-way.

If something required is missing, ask for all of it in one short question. Do not ask about anything that has a default:

- 1 adult, 0 children, 0 infants. Children are 2–11 years old and infants are under 2.
- Economy cabin. The other options are `business` and `first`.

## 2. Search

Call `search-flights` with:

- `itineraries`: one `{departure, arrival, date}` per leg, in travel order. A round trip has two legs, the second one reversed. Write dates as `DDMMMYYYY` in upper case, for example `16OCT2026`.
- `adults`, `children`, `infants`, `class`.
- `nationality`: the traveller's own country as an ISO-2 code (`EG`, `SA`, `AE`), never the destination's. It sets the fare and the default currency. Use it if you know it. If you don't, search anyway and offer to re-run for their nationality.
- `currency`: only if the user asked for one.
- `language`: `ar` when the user writes in Arabic.
- `limit`: 10 by default. Raise it, up to 50, when filtering by airline, stops or time leaves too few results.

The search takes about 20–30 seconds, so tell the user once that you are searching.

If the search fails or returns nothing, retry once. If it still fails, say so and suggest a nearby date or airport. Do not invent results.

## 3. Present the results

Show the 3–5 best options in a compact table. For each one, give:

- price and currency
- airline names (from `airlines`)
- departure and arrival times for each leg
- stops
- duration

Rules for the table:

- `price` is the total for all passengers in the search. With more than one passenger, also show the price per person.
- Work out each leg's duration from that trip's own `duration`. Do not use the itinerary-level `duration`.
- Label the **cheapest** option, the **fastest** one (shortest total of the trip durations) and, if it differs, the best balance of the two.
- Write times as local clock times. Mark a next-day arrival with "+1".
- Filter on the returned data for requests like "non-stop only" (`stops` = 0), "Emirates only" or "morning departures". Say how many options matched.

Prices are live and can change until the booking is paid. Say so once.

## 4. Details

When the user picks an option, call `get-flight-details` with that `search_id` and itinerary `id`. Report the checked and cabin baggage allowance per trip and passenger type.

## 5. Booking link

End with a travelyalla.com link built from the search, as described in [references/booking-links.md](references/booking-links.md). The user books and pays on the website. Never collect payment details in the chat.
