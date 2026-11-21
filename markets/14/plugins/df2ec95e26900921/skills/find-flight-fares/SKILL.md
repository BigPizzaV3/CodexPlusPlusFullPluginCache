---
name: find-flight-fares
description: Use a2bflight to look up airports, explore cheap destinations, compare observed fares for a route, and find where a group from different cities can meet.
---

# a2bflight fare search

Use the connected a2bflight MCP tools when a user asks for flight prices, inexpensive destinations, or fares for a route. Resolve ambiguous city and airport names with `find_airports`; use `cheapest_routes` for open-ended destination discovery and `route_fares` for a particular origin and destination.

When several people fly from different cities, use `where_to_meet` with their home airports or city codes to find where they can meet cheapest: each place comes with a weekend, each person's round trip, the total, and a `meet_url` that opens the group's page on a2bflight.com with everyone filled in. When they already know where, use `meet_link` with their home airports and the meeting airport; without dates it picks a weekend that has fares for everyone. Give the user the `meet_url`. A `warning` means the option is poor (many stops, or far dearer than the cheapest place): say why, and offer the better pick it names.

Present prices as fares a2bflight has seen, for one adult in economy, with their `seen` date (or, when a fare has none, the `checked` date we last looked). They are not live quotes or guaranteed availability. Quote each price in the currency its row gives: never convert it or search the web for an exchange rate. Lead with the best few options in one short list or table and offer more on request, rather than every row. Keep one-way and return prices distinct. When both are available, show the one-way first, then return; on a return fare, stops and duration cover both directions. Do not infer missing dates, price, baggage, seller, or booking conditions.

Give the returned `page_url` for the route first, so the user can inspect the full route on a2bflight.com. A returned `book_url` goes to the seller for that observed fare; label it accordingly and never invent either link. If there is no cached fare, explain the gap and point to the returned route page when available. Answer in the user's language and keep recommendations aligned with their dates, budget, and route preferences.
