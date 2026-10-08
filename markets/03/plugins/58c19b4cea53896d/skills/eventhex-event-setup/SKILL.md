---
name: eventhex-event-setup
description: Create and fully set up an event — event, tickets, speakers, sessions, website — in the right order.
---

# Event setup

End-to-end flow for "create my event" requests. You act on ONE franchise.

## Order of operations

1. `create_event(title, startDate, endDate, …)` — returns the new `eventId` and `websiteUrl`. Share that link.
2. Tickets — one `create_ticket` per tier (see the `ticketing` guide for pricing/early-bird fields).
3. Agenda — `create_speakers` then `create_sessions` (see the `agenda` guide for breaks, sub-sessions, roles).
4. Website — `generate_website` → `apply_website` → `publish_website` (see the `website` guide; `improve_website` is for editing an existing live site).
5. `generate_seo(eventId)` for metadata; `getSetupChecklist(eventId)` to verify nothing is missing.

## Other event operations

- `updateEventDetails(eventId, …)` — change title, dates, venue, description.
- `clone_event(eventId, …)` — duplicate an existing event as the starting point for a new edition.
- `delete_event(eventId)` — destructive; only on explicit user request, restate what will be deleted.
- `getEventInfo(eventId)` — full event record; `get_event_domains(eventId)` — real website URL, slug, domains.

## Notes

- Dates: pass ISO strings; the event's timezone governs how they display.
- If the user asks for "an event like last time", `list_events` → `clone_event` beats rebuilding from scratch.
