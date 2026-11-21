---
name: keep-track-of-people
description: Keep the workspace's record of a person at an event up to date: save or dismiss them, replace the note, record a meeting on the event calendar, mark outcomes (contacted, replied, meeting booked or held, opportunity). Use when the user says they want to meet, met, contacted or heard back from someone, or wants a note kept.
---

Two tools write, both scoped to one saved event, and nothing here contacts anyone.

1. **Identify the person.** Take the `link_id` from `list_event_people`, `get_person` or `search_prospects` (the `events` entries carry it). Pass it as `event_person_id` to `update_person`, or in `link_ids` to `set_people_status`. If the user names someone you have not listed yet, find them first; never guess an id.
2. **Status.** `set_people_status` with `pursue` (going after them), `watch` (later), `dismiss` or `new` (undo) takes several people at once. `update_person` takes `status` too, for one person along with other changes.
3. **Notes.** `update_person` with `note` replaces the whole note, so read the current note from `get_person` (`profile.note`) and carry forward what the user wants kept. Write the note in the user's words; do not add claims they did not make. An empty string clears it.
4. **Meetings.** `update_person` with `meeting_at` (an ISO 8601 time with offset), `meeting_where` and `meeting_about` records the meeting on the event's own calendar in Prompt Prospect. Resolve day names against the event's dates from `event_overview` and ask when the time is ambiguous. This sends no invitation and confirms nothing with the other person: say "recorded", never "booked" or "scheduled with". `meeting_at: null` clears it.
5. **Outcomes.** `update_person` with `outcomes` marks what happened (`contacted`, `replied`, `meeting_booked`, `meeting_held`, `opportunity`); `clear_outcomes` undoes one. Mark only what the user reports.

Boundaries: only the fields the user asked about change (the tool leaves the rest alone); confirm the person's name back in the answer; never record a meeting or an outcome the user did not state.
