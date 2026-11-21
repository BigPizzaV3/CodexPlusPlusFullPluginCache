---
name: meeting-action-items-to-tasks
description: Turn a recorded meeting into dated tasks on the user's Kai task list, and optionally block time for the big ones. Finds the meeting Kai captured, reads its recap and action items, skips anything already on the task list or calendar, creates a task per commitment the user owns (with due date, priority, and a link back to the meeting), and can add focus blocks to the calendar. Creates only; never sends or deletes. Use when the user asks to extract, pull out, or capture action items, follow-ups, to-dos, or commitments from a meeting, standup, call, or sync, or to turn meeting notes into tasks. Requires the Kai connector.
---

# Meeting action items to tasks

Read the meeting Kai sat through, date each of the user's commitments as a task, and block
time for the ones that need it. This skill creates tasks and calendar blocks. It never sends
email and never deletes anything.

## Tools this skill uses

`list_meeting_sessions`, `get_meeting_sessions`, `list_tasks`, `list_tags`, `create_task`,
`list_calendars`, `list_events`, `create_event`.

If the meeting tools aren't available in this conversation, say so and suggest a fresh
conversation that opens with the word "meeting".

## Steps

### 1. Find the meeting

- "My last meeting" means the most recent recorded session: call `list_meeting_sessions`
  with `after` set seven days back and take the newest by `startedAt` that has a `summary`
  (or `processingStatus: "complete"`). The list also contains upcoming and unprocessed
  sessions with no summary and empty `actionItems`; those aren't meetings yet. The same
  meeting can appear more than once; treat entries with the same title and start as one.
- If the user names a meeting, person, or day, match on `title`, `participants`, or date.
- If two sessions are equally plausible, list them and ask.

Kai only knows meetings its notetaker joined. If there's nothing in range, say so.

### 2. Read it

Call `get_meeting_sessions` with the session `id`, without `includeTranscript`. Use
`summary` and `actionItems`. Each action item has `content`, `assignee`, `dueDate`,
`priority`, `status`, and a `taskId` when it already became a task.

Set `includeTranscript: true` only if `actionItems` is empty and the user wants you to dig
for commitments in what was said. Transcripts are large (about 8,500 tokens per hour).

### 3. Decide what becomes a task

- Only the user's own commitments. Items assigned to someone else are reported, not
  created. Kai tasks belong to the user.
- Skip any item that already has a `taskId`.
- Call `list_tasks` (open tasks, the default) with `updatedAfter` set to the meeting date
  and skip anything with a matching title. Never create the same thing twice.
- Call `list_tags` once if the user uses tags, and reuse an existing tag ID where the topic
  clearly matches. Don't invent tags.

If the user asked you to "show" or "pull out" the items rather than create them, stop here
and present the list with proposed due dates. Create only when they say so.

### 4. Create the tasks

For each commitment call `create_task` with:

- `title`: the commitment as a verb phrase, in the user's words ("Send Ana the revised
  timeline"), not the meeting's sentence about it.
- `due`: `YYYY-MM-DD`. Use the date agreed in the meeting; if none was agreed, propose one
  from context and say it's proposed.
- `priority`: `high` for anything with a hard deadline or an external dependency, otherwise
  leave the default.
- `estimatedDurationMinutes`: a realistic estimate when the work is obvious.
- `description`: one line, "From <meeting title>, <date>."
- `source`: the meeting's `openLink` from the session result, so the task links back.
- `tags`: existing tag IDs only.

### 5. Block time for the big ones

When the user asks for time blocks, or a commitment is clearly over an hour of work:

- Call `list_calendars` and pick the user's writable `primary` calendar (ask if there's
  more than one).
- Call `list_events` for the target day (tomorrow unless the user said otherwise) and find a
  free slot inside working hours.
- Call `create_event` with `accountId`, `calendarId`, `title` (the task title), `start` as
  a local wall-clock date-time with no `Z` or offset, `duration` in ISO 8601 (`PT2H`),
  `isAllDay: false`, `timeZone` (the user's zone), `taskId` (links the block to the task),
  `addConferencingLink: false`, and `freeBusyStatus: "busy"`.
- No attendees. A focus block is the user's own time.

### 6. Report

List the tasks created with their due dates, the blocks created with their times, and what
was skipped and why (already existed, assigned to someone else). Say plainly that nothing
was sent and nothing was deleted.

## Guardrails

- Create, never send or delete. If the user wants a follow-up email, that's a separate
  request: draft it, show it, send only on their word.
- Don't assign tasks to other people. There's no such thing in Kai.
- Don't create a block that overlaps an existing event on a `primary` calendar.
- Dates are `YYYY-MM-DD` for tasks and wall-clock date-times for events. Never guess a
  time zone; use the user's configured one unless they name another.
