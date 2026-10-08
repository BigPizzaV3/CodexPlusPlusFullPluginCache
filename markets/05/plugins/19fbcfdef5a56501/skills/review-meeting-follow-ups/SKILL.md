---
name: review-meeting-follow-ups
description: Review a selected day of Meetings records for source-backed commitments, owners, deadlines, decisions requiring follow-up, and unresolved questions. Use when a user asks for an end-of-day meeting review, daily action-item digest, commitments from today's meetings, outstanding follow-ups, or a scheduled weekday meeting recap.
---

# Review meeting follow-ups

Produce a read-only daily follow-up digest from fetched Meetings records. Do not create tasks, send messages, change meeting settings, or write back to any system.

## Workflow

1. Resolve the review day.
   Use the date the user names. Otherwise use the current calendar day in the user's timezone when available, falling back to the thread timezone. Convert the day's start and end to timezone-aware ISO timestamps before searching.

2. Find that day's meeting records.
   Use [$Meetings](app://connector_openai_chatgpt_meetings) `find_all` with the day bounds. Follow pagination when needed. Do not substitute Calendar events for meeting records.

3. Fetch the source material.
   Fetch each result whose `fetch_status` is `fetchable` with `note_id=<id>`, newest first, up to 25 meetings. If more results exist, state how many were not reviewed. Record non-fetchable results and fetch failures under `Processing gaps`; do not invent content for them.

4. Extract only supported follow-up signals.
   Use fetched notes and transcript entries to identify:

   - explicit commitments or assigned action items;
   - an explicit owner and deadline, when stated;
   - decisions that require a concrete next step;
   - unresolved questions or blockers someone agreed to revisit.

   Treat a suggestion, topic, or aspiration as a commitment only when the source clearly assigns or accepts follow-up. Use transcript evidence when speaker attribution or exact wording matters. If a transcript is preliminary, label any transcript-only item as preliminary.

5. Attribute and deduplicate conservatively.
   Resolve the current user only from authenticated session context or an explicit user statement, never from attendance or speaker order. Put an item under `Your follow-ups` only when its owner unambiguously matches that identity. If current-user identity is unavailable, omit `Your follow-ups` and keep the stated owner under `Other owners / waiting on`, or use `Owner unclear`; never guess from an ambiguous pronoun. Merge repeated statements of the same item across meetings, but preserve every supporting source. Treat a later status as superseding an earlier one only when the later source explicitly updates it.

6. Return the digest.
   Keep every item traceable to a fetched meeting title and date or time. Preserve stated deadlines exactly. Write `No deadline stated` when none appears. Mark synthesis beyond an explicit source statement as `Inference`.
   Render each available source meeting title with the following Markdown template, using its exact durable private note ID from the `id` returned by Meetings unchanged.

   ```markdown
   [<meeting title>](codex://mcp-app/chatgpt-meetings@openai-curated-remote/meetings.open/meeting/<note-id>)
   ```

## Output

```text
# Meeting follow-up review for <date>

## Your follow-ups
- <commitment> — <deadline or No deadline stated>
  Source: <meeting title>, <time>

## Other owners / waiting on
- <owner or Owner unclear>: <commitment> — <deadline or No deadline stated>
  Source: <meeting title>, <time>

## Decisions needing follow-up
- <decision and concrete next step>
  Source: <meeting title>, <time>

## Unresolved questions
- <question or blocker and stated owner, if any>
  Source: <meeting title>, <time>

## Processing gaps
- <meeting title>: <not fetchable, pending, incomplete, or failed reason>

## Meetings reviewed
- <time>: <meeting title>
```

Omit empty action sections. Omit `Processing gaps` when there are none. If no meeting records exist, say so and stop. If records exist but contain no supported follow-ups, say that no explicit commitments or unresolved follow-ups were found and list the meetings reviewed.

## Rules

- Always use `find_all` before `fetch` unless the user supplies an exact note or Meeting identifier.
- Stay within the selected calendar day; do not pull older meetings merely to fill an empty digest.
- Prefer calendar meeting time in returned meeting metadata, then recording time as a fallback.
- Do not claim an owner, deadline, completion state, or decision that the fetched source does not support.
- Do not quote more transcript than needed to disambiguate an item.
- Do not execute follow-ups or create another automation. This skill only reports what the source meetings support.
- Use Meetings app deep links for meeting titles in Codex; leave HTTPS permalinks unchanged for any workflow that explicitly requires a browser or external-system URL.
