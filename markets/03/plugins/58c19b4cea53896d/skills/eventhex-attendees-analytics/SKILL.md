---
name: eventhex-attendees-analytics
description: Attendees, registrations, check-ins, revenue, exhibitor leads, exports and franchise-wide analytics.
---

# Attendees & analytics

## Per-event numbers

`get_event_stats(eventId, include:[…])` — registration totals, plus inline extras (no file download):

- `trend` — day-by-day registrations + cumulative
- `revenue` — collected / pending / refunded + net
- `tickets` — per-ticket registration & paid counts

`getCheckInStats(eventId)` for on-site check-in figures; `audienceInsights(eventId)` for audience breakdowns.

## Franchise-wide

`get_franchise_summary` — event count + total registrations. NOTE: counts ALL participant types (attendees + speakers + exhibitors + sponsors); for attendees-only use `get_event_stats`. `get_franchise_profile` / `list_invoices` for account/billing.

## Individual attendees

- `searchAttendees(eventId, query)` → matches; `getAttendeeDetails(eventId, …)` for one record.
- `update_attendee(eventId, …)` to fix a registration.
- `listOrders(eventId)` for payments; `listExhibitors` / `getExhibitorLeads` for exhibitor data.
- `exportAttendees(eventId)` — PII export; requires the `registrations:export` scope; only on explicit user request.

## Free-form questions

- `queryDatabase(eventId, …)` — analytics queries the dedicated tools don't cover (always event-scoped automatically).
- `semanticSearch(eventId, query)` — natural-language search across event content.

## Reply rules

- Say which event and which measure each number is ("paid attendees for WebCastle Meet", not "165").
- Don't paste bulk PII into chat — summarize, and use exports for full lists.
