---
name: meeting-notes-to-focus-block
description: Turn one action item from visible meeting notes into a scheduled, editable Event Creator focus block. Use when the user asks to reserve time for a follow-up, deliverable, or preparation task identified in notes. Require one concrete action and an exact schedulable slot; do not create tasks, reminders, attendees, recurrence, or multiple blocks.
---

# Meeting Notes To Focus Block

Turn one meeting follow-up into one focused calendar block.

## Inputs

Use meeting notes visible in the conversation plus the user's chosen action,
duration, scheduling window, and time-zone context.

## Workflow

1. Identify the single follow-up to schedule.
   - Prefer the action the user names or an action clearly assigned to the user.
   - If several plausible actions remain, ask which one to schedule.
   - Do not schedule actions owned by someone else without the user's explicit
     request.
2. Define a concrete outcome for the block.
   - Write a short action-oriented title.
   - Distill two to five useful steps, acceptance criteria, or preparation notes
     into the description.
   - Include a relevant HTTP(S) source or meeting URL only when it is present in
     the notes or supplied by the user.
3. Resolve an exact timed schedule.
   - Use the start and end the user provides, or calculate the end from an
     explicit duration.
   - If only a broad window such as "Tuesday afternoon" is given, ask for an
     exact start time rather than choosing one silently.
   - Include an explicit IANA time zone when known. Otherwise allow
     `display-event` to use its client time-zone hint; if the tool cannot resolve
     one, ask the user for it and retry.
   - Confirm that the end is after the start and that the chosen time is not a
     nonexistent DST wall time.
4. Invoke `display-event` once with timed timing and the focused title,
   description, and any supported URL or location.
5. Present the resulting editable card. Keep the response centered on the
   scheduled block rather than re-summarizing the entire meeting.

## Output

Deliver one editable Event Creator card for a concrete follow-up focus block,
with a concise outcome and actionable description.

## Boundaries

- Do not create a task-system entry or mark an action item complete.
- Do not create multiple focus blocks from one invocation.
- Do not add attendees, recurrence, reminders, or calendar-account writes.
- Do not claim the block was added to a calendar. The user exports it from the
  widget.
