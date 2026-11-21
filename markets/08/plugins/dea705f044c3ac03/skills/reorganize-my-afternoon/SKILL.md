---
name: reorganize-my-afternoon
description: Reschedule part of the user's day through Kai when something comes up. Reads every connected calendar for the window, separates what can move (solo blocks, internal meetings the user owns) from what should stay (external attendees, all-day events, calendars they can't edit), proposes new times, and moves events only after the user approves the plan. Drafts a note to affected attendees, sent only on the user's word. Use when the user asks to clear, free up, reorganize, reshuffle, or reschedule an afternoon, morning, day, or a set of meetings, or to move things because something urgent came up. Requires the Kai connector.
---

# Reorganize my afternoon

Read the window, propose the moves, and change nothing until the user approves. Then move
the events and offer a note to the people affected.

## Tools this skill uses

`list_calendars`, `list_events`, `get_events`, `update_event`, `delete_event` (only on an
explicit request to cancel), `list_accounts`, `create_email_draft`, `send_email_draft`.

If the calendar tools aren't available in this conversation, say so and suggest a fresh
conversation that opens with the word "calendar".

## Steps

### 1. Read the window

- Pin down the window. "This afternoon" is from now (or 12:00 if it's still morning) to
  the end of the working day. Ask if the user's phrasing is ambiguous.
- Call `list_calendars`. Note each calendar's `role` (`primary` calendars block
  availability; `contextual` ones are information only) and whether the user can edit it.
- Call `list_events` for the window with `includeFields: ["attendees", "calendarName"]`.
  Attendees are dropped from large responses unless requested, and you need them to know
  who's affected.

### 2. Sort movable from fixed

Movable by default:

- Solo blocks (no attendees, or only the user), including task blocks (`isTaskLike: true`),
  which keep their link to the task when moved.
- Internal meetings the user organizes, where every attendee shares the user's email domain.
- One occurrence of a recurring meeting (moved with `seriesUpdateMode: "single"`).

Keep by default, and say why:

- Events with external attendees, unless the user names them as movable.
- All-day events, events with `userCanEdit: false`, and out-of-office placeholders
  (marked `free`).
- Anything the user said must stay.

If the user said "move everything", still list the external ones and ask before touching
them. Those moves send real calendar updates to people outside the company.

### 3. Find landing slots

Call `list_events` for the next two working days. Propose slots inside the user's working
hours that don't overlap existing events on `primary` calendars. Keep each event's duration.
Prefer the same time on the next day for recurring 1:1s. If nothing fits, say so rather than
stacking meetings.

### 4. Show the plan and wait

Present a short table: event, current time, proposed time, who's affected, and a separate
line for what stays and why. Ask for approval. Let the user turn down individual moves.

Nothing has changed yet, and say so.

### 5. Move on approval

For each approved event call `update_event` with `id`, `accountId`, `calendarId`, and a
full `timing` object: `start` as a local wall-clock date-time with no `Z` or offset,
`duration` in ISO 8601 (`PT30M`, `PT1H`), `isAllDay: false`, and `timeZone` (the user's
zone unless they named another). The three timing fields must be sent together. Use
`seriesUpdateMode: "single"` for a recurring occurrence.

Attendees on a moved event receive the provider's normal update automatically.

Only call `delete_event` if the user explicitly asks to cancel something. It sends
cancellations to every attendee.

### 6. Offer the note

For moves that affect other people, offer a short message. If they accept:

- Call `list_accounts` with `integrationGroup: "email"` for the sending account (ask if
  there's more than one).
- Call `create_email_draft` with `accountId`, `to` (the affected attendees), a plain
  `subject`, and a two-sentence `bodyText`: what came up, the new time. Match the user's
  usual tone.
- Show the draft. Call `send_email_draft` only after the user confirms in a later message.

### 7. Report

List exactly what moved and to when, what stayed, and whether a note went out. If nothing
was approved, say the calendar is exactly as it was.

## Guardrails

- Never move, cancel, or send without the user's approval of that specific action.
- Don't add attendees, change titles, or add conferencing links while moving.
- Times are wall-clock in `timeZone`. Never send `Z` or an offset in `start`.
- `list_events` omits declined invites by default. That's usually right for this job.
- `contextual` calendars don't block availability, so don't treat their events as conflicts.
