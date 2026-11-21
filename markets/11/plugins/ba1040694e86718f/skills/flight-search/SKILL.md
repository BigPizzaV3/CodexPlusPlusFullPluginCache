---
name: flight-search
description: Search WAYA flights and hand the traveller a booking link.
---

Use the WAYA flight search tools in this order:

1. `find_airports` when the traveller names a city or airport rather than an IATA code. Confirm the code before searching.
2. `cheapest_dates` when the dates are flexible. It returns the lowest known one-way fare per day for a month. These prices are indicative, not bookable.
3. `search_flights` for a chosen date. It returns the cheapest offers first.

Each offer has a `booking_url` to the WAYA fare page for that offer. The traveller can view the fare there and use WAYA's options to continue or manage a flight. The MCP app itself cannot book or change flights, and no seat is held.

Only economy fares are sold. Children are aged 2 to 12, infants are under 2, and there must be at least one adult per infant.
