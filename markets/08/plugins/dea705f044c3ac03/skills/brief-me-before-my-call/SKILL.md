---
name: brief-me-before-my-call
description: Prepare the user for an upcoming meeting or call from their Kai data. Finds the next event on their calendar (or the one they name), recalls the last recorded meeting with the same people (recap and action items), checks the latest email thread with them, and reports who it is, what was agreed, and what the user still owes. Read-only, changes nothing. Use when the user asks to be briefed, prepped, or caught up before a call, meeting, or 1:1, or asks what they agreed or promised with a specific person. Requires the Kai connector.
---

# Brief me before my call

Bring back the three things the user would have looked up by hand: who they're about to
speak to, what was agreed the last time, and what's been said in writing since. Then stop.
This skill only reads. It never drafts, sends, moves, or deletes anything.

## Tools this skill uses

`list_events`, `get_events`, `list_meeting_sessions`, `get_meeting_sessions`, `search_emails`,
`list_thread_emails`, `list_tasks`. All read-only.

If these tools aren't available in the current conversation, say so and suggest a fresh
conversation that opens with the word "calendar" or "meeting", since ChatGPT loads a subset of
Kai's tools per conversation based on topic.

## Steps

### 1. Find the meeting

- If the user names a meeting, person, or time, use that.
- Otherwise call `list_events` from now to the end of the day, with
  `includeFields: ["attendees", "description"]`. Attendees are dropped from large responses
  unless you ask for them, and they're the whole point here.
- If nothing with other people is left today, extend the range to the next working day and
  say you did.
- The meeting is the next event that has at least one attendee who isn't the user. Skip
  all-day events, task blocks (`isTaskLike: true`), and events marked `free`, such as
  out-of-office placeholders. If two candidates are equally plausible, ask which.

Note the counterpart names and email addresses from `attendees`. Read the event
`description` for the agenda or the invite text.

### 2. Recall the last meeting with them

- Call `list_meeting_sessions` with `after` set about 90 days back.
- The list includes upcoming and unprocessed sessions as well as recorded ones. Only
  sessions with a `summary` (or `processingStatus: "complete"`) and a `startedAt` in the
  past count as recorded. The same meeting can appear more than once; treat entries with the
  same title and start as one.
- Match sessions on `participants` (email or name) or on a title that matches the event.
  Take the most recent one or two.
- Call `get_meeting_sessions` with those `ids`, without `includeTranscript`. The `summary`
  and `actionItems` are what you need. Each action item carries `content`, `assignee`,
  `dueDate`, `status`, and a `taskId` when it already became a task.
- Only set `includeTranscript: true` if the user asked a specific question the summary
  doesn't answer, and then for one session at a time. Transcripts run to roughly 8,500
  tokens per hour of meeting.

If there's no recorded meeting with these people, say so plainly. Kai only knows the
meetings its notetaker joined.

### 3. Check the thread

- Call `search_emails` with `participants` set to the counterpart addresses and `after`
  set about 60 days back. Leave `query` empty unless the user gave a topic.
- Take the most recent thread and call `list_thread_emails` with its `threadId`. Messages
  come back oldest first.
- Work out who spoke last. If the last message is inbound and unanswered, the user owes a
  reply. If it asks a question, quote it.

### 4. Optional: open commitments

If the last meeting produced action items assigned to the user, call `list_tasks` (open
tasks, the default) and see whether they were done or are still open. Action items with a
`taskId` already exist as tasks; report their state rather than suggesting they be created.

## What to report

Five to eight sentences, in this order, each with its date:

1. Who and when: the meeting title, time, and the people in it.
2. Last time: the decisions and the action items, split into "you said you'd" and "they
   said they'd".
3. Since then: the state of the email thread, and whether the user owes a reply.
4. Anything the event description adds (agenda, links, a request).

Say what you couldn't find. "No recorded meeting with Ana in the last 90 days" is a useful
sentence. Never invent history to fill a gap.

## Guardrails

- Read only. If the user follows up with "reply to her" or "move the call", that's a
  different job: draft or propose, show it, and act only when they confirm.
- Don't paraphrase a commitment into something stronger than what the recap says.
- Times are in the user's configured time zone. If the user asks for another zone, pass it
  as `timeZone` on `list_events` and `ianaTimeZone` on the other calls.
- Results may be truncated (`truncated: true`) or have fields elided (`elidedFields`).
  Narrow the date range rather than guessing from a partial list.
