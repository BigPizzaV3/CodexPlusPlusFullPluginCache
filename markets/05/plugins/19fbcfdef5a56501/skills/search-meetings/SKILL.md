---
name: search-meetings
description: Find recent meetings by date, participant, title, or topic and answer questions about their discussions, decisions, and action items from meeting notes and transcripts.
---

# Search meetings

## Find the relevant records

Use [$Meetings](app://connector_openai_chatgpt_meetings) for `find_all` and `fetch`. Start with `find_all` unless the user supplied an unambiguous meeting or note identifier.

- Use the requested date range and participants; `recent` defaults to the last 7 days. Pass dates as `start_time` / `end_time` and participants as `attendee_names` / `attendee_emails`, following the available tool schema. Titles, topics, and keywords are model-side selection criteria, never `find_all` parameters or attendee values.
- Follow returned `cursor` pagination within that scope as needed before concluding there is no match. Preserve the tool's default page size and maximum limit; do not silently widen the date range.
- Select candidates using titles, times, and attendees. Topic matches need not repeat the user's wording. If metadata is insufficient, fetch only likely candidates' notes to verify relevance before reading transcripts deeply. If ambiguity remains, show up to 5 candidates with title, time, and match reason, and ask the user to choose.
- Fetch selected records using `note_id=<id>` from the results, reusing any content already fetched. Prefer notes for summaries, decisions, and action items; use transcripts for speaker-specific questions, quotes, and detailed chronology.

## Answer with sources

Answer the user's question directly from fetched content, distinguishing inference from recorded facts. State any missing content or conflicts between notes and transcript; prefer the transcript for exact wording. Keep quotes short and relevant, and keep separate meetings' timelines clear.

Use calendar-scheduled meeting times when available, falling back to recording or transcript times. Link every source meeting title using this format:

```markdown
[<meeting title>](codex://mcp-app/chatgpt-meetings@openai-curated-remote/meetings.open/meeting/<note-id>)
```

Use the exact durable private `id` returned by `find_all` or `fetch`, unchanged. Do not substitute an HTTPS `permalink` or derive an ID from a provider join URL. Preserve HTTPS permalinks unchanged for workflows that need browser or external-system links.
