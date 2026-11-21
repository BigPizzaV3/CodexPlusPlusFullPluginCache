---
name: plan-bus-trip
description: Use when the user wants a bus between two places where at least one is in Kosovo, Albania, North Macedonia or Montenegro, including routes to or from Austria, Germany or Switzerland. Finds departures with search_bus_lines and helps the user choose one.
---

# Plan a bus trip

What the user explicitly asks for always comes before these guidelines.

## 1. Get the route

You need an origin, a destination and a date.

- If the origin or the destination is missing, or could be more than one place, ask one short question before searching. Example: "Mitrovica" could be Mitrovicë in Kosovo or Sremska Mitrovica in Serbia.
- If the user gives no date, search today. Turn relative dates ("tomorrow", "next Friday", "të shtunën") into YYYY-MM-DD.
- A city is enough; you don't need a station. Use the station only when the user names one.
- If neither place is in the Balkans, don't search: say that Gjirafa Travel covers routes to and from the Balkans.

## 2. Search

Call `search_bus_lines` with `from`, `to`, `date` and `language`.

- Set `language` to the user's language: `en`, `sq`, `de`, `fr`, `es` or `it`. Use `en` for any other language.
- When `language` is `sq`, write the place names in Albanian (Prishtinë, Shkup, Tiranë). Otherwise write them in English with standard spelling (Pristina, Skopje, Tirana).

## 3. Answer

The widget already shows the routes, so don't repeat them as a list. In two to four sentences:

- Point out what helps the user choose: the earliest and latest departures, the fastest route, the cheapest fare, and whether a route has a change. Like the website, the results list the direct routes first, then the routes with a change (`via`).
- When `arrivalDayOffset` is 1 or more, say that the bus arrives the next day.
- If some routes aren't bookable online (`bookableOnline: false`), say that their tickets are bought at the station; those routes may have no price (0).
- End with the `searchUrl` link: all routes for the day are there, and tickets are bought there.

## 4. When nothing is found

- `NO_ROUTES`: when the result has `nextAvailable`, say that the next buses run on that date and offer to show them; otherwise offer a nearby bigger city (for example Prishtina instead of a village near it).
- `LOCATION_NOT_FOUND`: ask the user to check the spelling, or suggest the nearest city.
- `API_ERROR`: say the search isn't available right now and give https://travel.gjirafa.com/en (https://travel.gjirafa.com/sq in Albanian).

## 5. Questions about the route in general

- How many buses a day, the first and last bus, the usual price and travel time, the distance, which companies drive it, where the stations are or what travellers say: call `get_route_info`. Quote its numbers as "about" or "usually", and link the `routeUrl`.
- Which days buses run, or comparing days before picking one: call `get_weekly_departures`, then `search_bus_lines` for the day the user picks.
- If the user says a line shown on Gjirafa Travel is wrong, or a bus didn't come or was late, offer to report it with `report_route_problem`. Say what you'll send, and send only what they told you. A report doesn't change a booking or get a refund.

## 6. How Gjirafa Travel works

- Paying (cards, Apple Pay, Google Pay; not on the bus), tickets (no need to print; seats are given on the bus), what each Travel Flex allows and until how many hours before departure, refunds when the operator cancels, changes, open returns, the student discount, the service fee or how to reach support: call `get_travel_help` with the topics, and answer from its FAQ. Don't guess a rule it doesn't give.

## Rules

- Never say that a seat is booked, held or paid. Booking happens only on travel.gjirafa.com.
- Quote prices as the results give them, with their currency. Don't promise that they won't change.
- Don't invent departures, operators or prices that aren't in the results.
