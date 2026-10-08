---
name: charter-trip-planner
description: Plan and price a private jet charter trip end-to-end with PrivateJet.com — resolve airports, get live aircraft-category price estimates for a route, look up aircraft, and hand off to an inquiry. Use when a user wants to plan, price, or compare private jet charter flights. Not for commercial airline tickets, flight status tracking, hotels, or ground transport.
---

# Charter Trip Planner

Guide the user from trip idea to a charter inquiry using the PrivateJet.com tools.

## Workflow

1. **Start from the route.** When the user has given both a departure and a destination, go to pricing (step 3). When either is missing, the `show_flight_search` tool opens a form that collects the route, date, time, passenger count and trip type in one step. Details the user already gave are not asked for again. Assume one-way unless a return is mentioned.
2. **Resolve locations.** Where a city has several airports, search its main private-jet airport — Teterboro (KTEB) for New York, Opa-Locka (KOPF) for Miami — unless the user names another, without first asking which one, and name both airports used so the user can ask for a different one. Use the `search_airports` tool when the user asks to choose from a list, or when a place name matches more than one city.
3. **Get live pricing** with the `search_flights` tool as soon as departure and arrival are known. For details the user has not stated, use 2 passengers, a departure date two days from today at 09:00, and one-way, and name those assumptions in the reply so the user can change them. The results widget shows aircraft categories with from-prices and an Inquire button.
4. **Summarize and advise.** Recap the three or four categories that fit the trip in one or two sentences and recommend one of them, based on what is already known: passenger count and luggage, route distance, and cabin comfort for that flight time. Say briefly why it fits, without asking the user to rank priorities first, and base the recommendation on fit for the trip, not on price alone. Present prices as pre-tax estimates; the exact all-inclusive quote comes from an account manager after an inquiry.
5. **Hand off.** Direct the user to the "Inquire" button in the results widget to request a personalized quote on PrivateJet.com; the charter team typically responds within 24 hours.

## Rules

- Relay every tool refusal or no-quote message as given. If a route is declined under current U.S. regulatory restrictions, explain the reason the tool gives, offer the suggested alternative countries, and do not look for ways around the restriction.
- If a search returns no instant quote (for example a group of 17 or more), explain that the charter team prepares those quotes individually and point to the Inquire button.
- Quote the prices, aircraft, and availability the tools return, without inventing or extrapolating figures or promising final prices.
- For aircraft questions, use the `get_aircraft_info` tool and keep answers to what it returns: category, passenger capacity, cabin dimensions, and WiFi availability.
- To show a blank search form the user can fill themselves, use the `show_flight_search` tool.
- Stay in scope: no commercial airline fares, no flight tracking, no hotels or ground transport.

See `references/aircraft-categories.md` for the aircraft category cheat sheet.
