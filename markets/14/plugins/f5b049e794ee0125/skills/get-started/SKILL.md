---
name: get-started
description: Use when the user first connects CrewSync or asks what it can do. Explains the read-only roster questions CrewSync answers and confirms the connection by fetching the next flight.
---

# Getting started with CrewSync

CrewSync gives read-only access to the roster of the airline crew member who connected the account.

1. Call `get_next_flight` and show the result. Use `now_local` from the result, not your own clock, to decide what today and tomorrow are.
2. Offer a few things to try:
   - a day or period of the roster, with days off and layovers (`get_schedule`);
   - the legs already flown as a logbook table (`get_logbook`);
   - the totals of a month (`get_month_summary`) or of the whole history saved in CrewSync (`get_career_stats`);
   - the hours as first published by the airline (`get_published_hours`);
   - METAR and TAF for an airport, by default the next destination (`get_airport_weather`);
   - for Brazilian airlines, duty and rest against RBAC 117 (`get_duty_limits`).
3. CrewSync is read-only. It cannot change, swap or request flights; say so if asked.
4. Duty and rest figures are estimates from the roster. The airline's records prevail.
5. Personal events are only available if the crew member turned them on in the CrewSync app. If `get_personal_events` says they are off, do not guess.
