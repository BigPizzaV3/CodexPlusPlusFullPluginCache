---
name: nowistay-daily-brief
description: Prepare a concise cross-property operations brief from Nowistay bookings, missions, and conversations. Use for daily briefs, today's arrivals or departures, upcoming guests, urgent work, operational handovers, and questions such as "what needs attention today?".
---

# Nowistay Daily Brief

Build the brief with the fewest complete MCP calls.

## Workflow

1. Resolve property names and IDs once with `list_properties`. For all properties, omit `search`; paginate only when the response says more properties exist.
2. Resolve relative dates in each property's timezone. Use `get_property` only when the timezone is needed and not already available.
3. Fetch bookings in one portfolio-wide request whenever possible. For multi-property or broad date ranges, use `list_bookings` with `response_format=table`, `limit=500`, and `include_details=false`. Follow `resultMetadata.nextOffset` until `hasMore=false`.
4. Fetch missions with `list_missions`. Use compact results for a small focused request; use `response_format=table` and `limit=500` for a portfolio-wide brief.
5. Fetch conversations only when the user explicitly asks about messages or unresolved guest communication. Do not read conversations merely to enrich a general brief.
6. Retrieve full booking, mission, report, or conversation details only for items that need explanation or action.

## Brief format

Present only useful operating information, ordered by urgency:

- urgent incidents or failed missions;
- arrivals and departures with property, guest, time, and readiness risks;
- unassigned, overdue, or blocked missions;
- guest conversations that need a host decision;
- a short next-actions list.

Use property names in the response. Identify a guest only when the user requested guest-level information or when the identity is necessary to act on a specific arrival, departure, or conversation; otherwise identify the stay by property and dates. Never include guest email, phone, postal address, private notes, or message content in a general brief. Keep internal IDs out of the prose unless the user asks for them or they are needed to disambiguate records. If a broad query is paginated, finish every page before claiming the brief is complete.

## Efficiency rules

- Do not call `list_bookings` once per property when omitting `property_ids` returns the whole eligible portfolio.
- Do not use full-detail list responses for broad requests.
- Do not call `get_booking` or `get_mission` for every row.
- Do not describe complete server results as truncated merely because the UI displays a shortened preview; trust `resultMetadata.hasMore` and pagination fields.
