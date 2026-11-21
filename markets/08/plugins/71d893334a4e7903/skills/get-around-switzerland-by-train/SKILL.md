---
name: get-around-switzerland-by-train
description: Answer Swiss train and public-transport questions with the Swiss Activities tools — timetables, connections to airports, resorts and summits, scenic trains and which rail pass or day ticket pays off for a trip. Use when someone asks for a train, bus or boat connection in Switzerland, a scenic train, the Swiss Travel Pass or another Swiss rail pass.
---

# Get around Switzerland by train

- **A connection:** `plan_journey` with origin, destination and the Swiss local time. «Arrive by» questions use `arrival`, lake cruises `boat`. Give departure, arrival, line, platform and transfers exactly as returned, and the ticket link.
- **Which ticket or pass pays off:** `recommend_rail_pass` with the dates, the stops in travel order with nights, every traveller's age and the country of residence. It prices the trains with live fares and ranks single tickets, Swiss Half Fare Card, day passes, Swiss Travel Pass and regional passes. Say which products it could not compare exactly (`not_compared`), and that mountain excursions come on top — `advisor_url` compares them too.
- **What a pass covers:** `find_rail_passes`; a price for a date and group: `check_availability` with the pass `id`.
- **Scenic trains** (Glacier Express, Bernina Express, GoldenPass) and mountain railways are bookable products: `search_activities`, then `check_availability`.
- Times and prices only from the tools; if a connection is not found, offer another time or a nearby station.
