---
name: event-briefing
description: Prepare a Swoogo event overview, readiness audit, or registration trend briefing from live event data. Use for event status, agenda gaps, registration counts, or planning summaries; not for applying changes or attendee-level exports.
---

# Prepare an event briefing

Read [the shared workflow rules](../../references/workflow-rules.md).

1. Resolve the event and any requested reporting dates. If no event is specified, use available conversation context or list accessible events so the user can select one.
2. Call `swoogo_get_event_bundle` with `event_id` for the initial event, sessions, speakers, sponsors, registration types, packages, and questions. The bundle fetches initial pages and may omit records or return component errors. It is a starting snapshot, not proof of completeness. Use the corresponding list tools and their pagination for a complete audit.
3. For registration totals or trends, call `swoogo_registrations_get` using `event_id` and, when useful, `group_by: day`, `week`, `month`, or `reg_type`. Use `date_from` and `date_to` in `YYYY-MM-DD` format. Do not pass an email for an aggregate briefing. The schema does not support grouping by source.
4. Map registration type IDs to names from the bundle or `swoogo_registration-types_get`. The aggregate total comes from pagination metadata, but grouped counts cover at most 5000 records. Surface `_warning`; narrow date windows if complete grouped counts are needed. Weekly buckets begin Sunday.
5. Check only requested readiness areas: event dates/timezone, incomplete session details, speaker assignments, capacity versus registration counts, and form requirements. Use `swoogo_get_sessions` with `expand: registrantCount` for session registrations; those counts differ from attendance. Fetch detail before calling a field absent. Capacity zero means unlimited for sessions.
6. For form audits, inspect `swoogo_get_registration_form`; report observed required fields, choices, and validation constraints. Do not infer conversion rates or claim a form change would produce a measured lift without supporting data.

Deliver a concise briefing with event identity and dates, key counts and reporting scope, agenda/readiness findings, and prioritized suggested next actions. Identify missing, failed, and partial data separately from zero. Keep this workflow read-only; hand requested edits to the appropriate registration or agenda workflow.
