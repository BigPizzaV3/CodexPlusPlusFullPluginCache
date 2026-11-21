---
name: lufthaven-flights
description: Answer questions about the traveler's own flights from Lufthaven, and save flights they book. Use when they ask whether they are travelling, where they are, when they land, whether a flight is on time, which gate or terminal, how long security is, or when they mention booking a flight or ask to track one.
---

# Lufthaven flights

Lufthaven is the traveler's flight tracker. Its tools answer from the flights they saved, with live status.

## Which tool

- `travel_status`: the one flight that matters right now (in the air, boarding, next departure, just landed). Use it for "am I travelling", "where am I", "when do I land", "is my flight on time". Use it before planning anything time-sensitive, such as a meeting, a call or a pickup.
- `my_flights`: every saved flight still to come or underway, soonest first, with gates, terminals, delay, the incoming plane and the security wait at departure. Use it for trip overviews and for questions about a flight that is not the next one.
- `add_flight`: saves a flight so the traveler's phone tracks it. Use it when they say they booked a flight or ask to track one. Pass the flight as printed on the booking (`BA117`) and the local departure date (`YYYY-MM-DD`). If the answer lists several flights, call again with `from` set to the departure airport's three-letter code.

## How to answer

- Lead with the answer: "On time, gate B32, boards 14:05." Then one supporting fact if it helps.
- Times are local to each airport. Say which airport when a time could be read either way.
- Say only what the tools returned. If a gate, terminal or wait is missing, say it is not posted yet; never guess one.
- Save a flight only when the traveler booked it or asked. Do not save flights they are only comparing.
- Flights cannot be removed from here. If asked, say to remove it in the Lufthaven app.
- If a tool says the account cannot track flights yet, pass that on once and stop.
