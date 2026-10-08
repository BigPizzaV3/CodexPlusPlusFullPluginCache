---
name: find-mataro-events
description: Find upcoming public events and activities in Mataró by topic, category, date, venue, or location. Use for plans today, tomorrow, this weekend, or on a specified date.
---

# Find Mataró events

Use `search_events` for agenda questions. Interpret relative dates in the Europe/Madrid time zone and pass explicit `date_from` and `date_to` values for requests such as today, tomorrow, or this weekend. Use a short query or category filter only when the user provides one. For details about a result, call `get_event` with the exact returned URL.

Give the event's local start time, end time when available, and venue. Make its title the single link to its public Mataró.fm page; do not append original source names or links to every item, since that page already shows them. Show original sources when the user asks or when needed to clarify a claim. Say when a venue, end time, or other requested detail is absent. A source text saying an event is free does not guarantee that all attendance conditions are known; state only what the tool returns. If no events match, report the searched dates and filters rather than inventing alternatives.
