---
name: one-on-one-prep
description: Prepare for upcoming one-on-ones using the user's connected Calendar and recent one-on-one records in Meetings. Use for 1:1 prep with follow-ups, suggested agenda items, and sources.
---

# One-on-one prep

This workflow is read-only. If Calendar or Meetings is unavailable, explain which part of the prep cannot be determined and stop.

## Find upcoming one-on-ones

Use the user's requested day. Otherwise, in the Calendar timezone (or thread timezone if unavailable), use today before 6:00 PM on weekdays, the next weekday at or after 6:00 PM, or the next Monday on weekends. For today, search from now to day-end unless the user requests all of today; for a future day, search the full day.

Discover an event-list/search tool from the user's actually connected Calendar connector and follow its schema and pagination. Do not assume a provider or connector ID, or substitute Meetings' upcoming plan. If multiple calendars are plausible and context does not identify one, ask the user to choose. Limit Calendar reads to the selected day's events and their details; do not look back for history.

Candidates must contain the current user and exactly one other attendee. If attendees are missing from the list, fetch likely events' details before classifying them. Use recurrence metadata when available as context, not as evidence of prior one-on-one notes.

## Find relevant history

Use [$Meetings](app://connector_openai_chatgpt_meetings) `find_all` for the last month, with the other attendee's name or email in `attendee_names` / `attendee_emails` and dates in `start_time` / `end_time`, following the available schema. Titles, topics, and keywords are model-side selection criteria, never `find_all` parameters or attendee values. Follow returned `cursor` pagination within that month as needed to identify the newest relevant records, preserving the default page size and maximum limit.

Confirm prior one-on-ones using titles, participants, and likely candidates' notes when needed. Exclude group meetings and unrelated history; ask the user to choose if ambiguity remains. Fetch selected records with `note_id=<find_all.id>`, normally the latest 2 relevant meetings per person, reusing notes already fetched. A specific meeting identifier supplied by the user can bypass discovery.

## Prepare the brief

For each person with at least one fetched prior one-on-one record, give the upcoming time, up to 3 follow-ups, up to 3 suggested agenda items, and at most 2 source meetings, newest first. Use fetched notes/transcripts as factual grounding and distinguish suggestions from recorded commitments. If the sources support no specific follow-ups or agenda, say so. Keep transcript quotes to short excerpts needed to resolve ambiguity.

Link source titles using this format:

```markdown
[<meeting title>](codex://mcp-app/chatgpt-meetings@openai-curated-remote/meetings.open/meeting/<note-id>)
```

Use the exact durable private `id` returned by `find_all` or `fetch`, unchanged, rather than an HTTPS permalink or provider join URL. Preserve HTTPS permalinks for browser or external-system workflows.

Briefly list skipped people and upcoming times when no relevant prior one-on-one record could be fetched; do not generate prep for them. If nobody qualifies, say that no upcoming one-on-ones had relevant prior notes.
