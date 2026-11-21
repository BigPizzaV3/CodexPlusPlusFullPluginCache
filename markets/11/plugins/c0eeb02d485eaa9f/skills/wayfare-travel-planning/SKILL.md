---
name: wayfare-travel-planning
description: Use when a user wants to access their connected Wayfare account, list or review trips, plan/import an itinerary, or add/edit activities in an existing Wayfare trip.
---

# Wayfare travel planning

Use the connected Wayfare MCP server as the source of truth for account identity, trip data, and persisted changes. Never claim that a trip, day, or activity exists until a Wayfare tool confirms it.

## Available server capabilities

The existing Wayfare MCP integration documents six semantic tools: `get_profile`, `list_trips`, `get_trip`, `import_itinerary`, `add_activity`, and `update_activity`. Confirm actual availability and schema from connected tool discovery rather than inventing unsupported arguments or functionality. Use the production server's discovered schema; the server may change independently from this package.

- For account checks, use `get_profile` without changing any data.
- For 'what's coming up' or previous-trip queries, retrieve trips using `list_trips`; call `get_trip` for itinerary detail. Honour pagination.
- For travel recommendations, discuss dates, travel time, geographical coherence, time zones and practical transfer times before proposing an itinerary. Distinguish advice from data that is actually in Wayfare.
- For writing an itinerary, show the proposed destinations, date range and key activities to the user and obtain their approval before invoking `import_itinerary`. Never create a trip on the basis of exploratory language alone.
- For `add_activity` or `update_activity`, match the correct trip and calendar date/record; confirm any meaningful changes before sending. The server must enforce ownership and permissions.

## Safeguards

- Each user must authorise their own Wayfare account with OAuth; never use someone else's account or place credentials in prompts, files or tool arguments.
- Never infer a trip ID, activity ID, coordinate, flight detail, booking status, or timezone when it can be read or looked up. Avoid inventing hotel or transport reservations.
- Imports support a maximum of 31 days, 100 activities, 20 transport legs, and 10 accommodation records. If a request exceeds those limits, explain the limitation rather than silently truncating.
- For writes, use a stable requestKey of 8–128 alphanumeric, underscore or hyphen characters. Retry with the **same key and identical normalized payload**; do not reuse a key for a different change.
- Respect existing dates, booked activities, timings and transport boundaries unless the user explicitly asks for a change and the tool permits it.
- Avoid deletion or wider sharing requests: the initial six-tool interface does not provide delete or sharing actions. Do not claim those actions succeeded.
- This package connects to Wayfare's production endpoint. Public availability depends on approval and publication; do not claim it has been publicly reviewed before approval. If the remote server is unavailable, disabled, or authentication fails, explain that accurately. Do not bypass OAuth or route around its permissions.
