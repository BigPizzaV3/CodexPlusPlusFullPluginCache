---
name: get-started
description: Search private jet empty leg flights with PrivJet and show details and booking links. Use when the user asks for empty legs, one-way private jet deals or repositioning flights between cities, airports or dates.
---

Use the PrivJet tools to answer questions about private jet empty legs (repositioning flights that are sold at a discount).

1. Call `search_empty_legs` with what the user gave you: `origin` and `destination` (city name, IATA or ICAO code), a date window (`earliestDeparture`, `latestDeparture` as ISO dates) and `pax` for the number of passengers. Leave out filters the user did not mention.
2. If there is no exact match, the tool returns the closest alternatives with a note. Show them and say clearly that they are alternatives.
3. When the user wants more about one flight, call `get_empty_leg` with the `id` from the search result.
4. Prices are totals including the PrivJet service fee (the same amount the link shows on privjet.net) and are subject to operator confirmation. Repeat them exactly as the tool returns them. Bookings happen on privjet.net through the link in each result; never claim that a flight is booked or reserved.

PrivJet covers only private jet empty legs. For airline tickets, flight status, trains or hotels, tell the user that PrivJet cannot help with that.
