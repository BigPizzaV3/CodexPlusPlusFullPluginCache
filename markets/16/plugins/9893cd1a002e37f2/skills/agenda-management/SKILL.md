---
name: agenda-management
description: Review or update a Swoogo event agenda, create or edit sessions, and add or update speakers. Use for schedule changes, room or speaker conflict checks, and agenda maintenance; not for attendee session enrollment or creating an event website.
---

# Manage sessions and speakers

Read [the shared workflow rules](../../references/workflow-rules.md).

1. Resolve the event, then read `swoogo_get_events` for event dates and timezone. Read affected sessions with `swoogo_get_sessions`; use `expand: speakers` when assignments matter. Complete the relevant date's pagination before declaring no schedule conflicts.
2. Resolve existing speakers through `swoogo_get_speakers` and, where needed, `swoogo_get_contacts`. Inspect current details before editing. A speaker profile is backed by an account contact, so changing profile fields can affect that contact elsewhere.
3. Turn the request into specific field changes. Session dates use `YYYY-MM-DD`; times require `HH:MM:SS`, in the event's timezone. Resolve ambiguous dates/timezones and material conflicts before writing. Use actual returned room/speaker identities; a guessed match is insufficient.
4. Check overlap for the same room or speaker using intervals where start is before the other end and end is after the other start; adjacent sessions are not an overlap. Missing dates, times, or assignments make the check incomplete. Do not claim the server enforces all conflicts or assume parallel sessions in different rooms conflict.
5. Use `swoogo_create_session` with `event_id` and `name` for a requested new session. Use `swoogo_update_session` with `session_id` for edits, sending only changed fields. Check for an existing matching session before creating or retrying a create. Use `swoogo_fields_get` with `object: session` for custom field choices.
6. For a requested new speaker, use `swoogo_speakers_create` with `event_id` and either a resolved `contact_id` or supplied email/name. Include `session_ids` only for requested assignments. Supplying profile fields can overwrite an existing contact; omit unrelated fields. A `session_error` may mean the speaker was created but an assignment failed: report that partial success and do not repeat the create.
7. Use `swoogo_update_speaker` for requested profile changes to an existing speaker. Follow live schemas for any assignment change; do not invent an assignment endpoint or duplicate a speaker to work around a missing operation.
8. Read back affected sessions/speakers. Show saved dates, times with timezone, room, and assignments; report failed operations separately. Do not send emails unless requested.

For review-only requests, return an agenda and specific findings without writes. For edits, summarize the actual before/after values and unresolved conflicts. Do not claim that a room is available outside the data inspected.
