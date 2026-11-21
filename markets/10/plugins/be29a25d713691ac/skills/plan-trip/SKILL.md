---
name: plan-trip
description: "Plan a trip with TravelYalla: round-trip flights plus a hotel that matches the dates, an estimated total against the budget, and booking links. Use when the user asks to plan a trip, holiday, getaway or Umrah stay, or wants flights and a hotel together (خطط رحلة، رحلة، إجازة، طيران وفندق)."
---

# Plan a trip

Tools: `search-flights`, `search-destinations`, `search-hotels` and, if useful, `get-hotel-details`. Follow the `find-flights` and `find-hotels` skills for how to call each tool and how to build links.

Explicit user instructions take priority over the defaults here.

## 1. Collect the trip

You need:

- where the user is travelling from and to
- the dates, or a month plus the trip length
- the number of travellers.

The budget and preferences (hotel stars, area, non-stop flights) are optional but useful. If a required item is missing, ask for everything missing in one short question.

If the user gives only a month and a length ("5 days in November"), choose specific dates and state them. Use the `flexible-dates` skill only if the user wants the cheapest dates.

## 2. Flights first

Search round-trip flights with `search-flights` as in `find-flights`. Pick a recommended option, the cheapest reasonable one unless the user prefers otherwise, and note its arrival and return departure times.

## 3. Hotel matching the flights

- Check-in is the outbound arrival date in local time. If the arrival is after midnight, mention that the room for the night before may be needed.
- Check-out is the return flight's departure date.
- Use the same `nationality` and **the same `currency`** as the flight search so the total adds up. If the flight search returned a currency, pass it to `search-hotels`.
- Size the rooms for the group: by default up to 2 adults per room, with children in their parents' room.

Search with `search-destinations`, then `search-hotels`, as in `find-hotels`. Pick 2–3 hotels across price levels.

## 4. Summary

Present:

1. **Flights:** the recommended option with times, airline, stops and price.
2. **Hotels:** 2–3 options with stars, guest score, nightly price and stay total.
3. **Estimated total:** flights plus each hotel option, in one currency, compared with the budget if one was given. If you can't make it fit, say what would (other dates, fewer stars, a stop).
4. **A light day-by-day outline**, clearly labelled as suggestions from general knowledge rather than TravelYalla data. Keep it short.
5. **Booking links** for the flight search and each hotel.

Prices are live and change until booked. Booking and payment happen on travelyalla.com, never in the chat.
