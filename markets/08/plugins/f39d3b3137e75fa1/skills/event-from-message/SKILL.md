---
name: event-from-message
description: Extract one calendar event from pasted or visible message text and create an editable Event Creator card. Use when the user asks to turn an email, chat, invitation, announcement, or copied notice into one event. Require the source text to be available in the conversation; do not retrieve mail or create multiple events.
---

# Event From Message

Turn one message into one accurate, editable event.

## Inputs

Use message text that is visible in the conversation and any corrections or
preferences the user provides. Accept copied email, chat, invitation,
announcement, or notice text.

## Workflow

1. Identify the single event the user wants.
   - If the message contains several distinct events and the user did not choose
     one, ask which event to create.
   - Ignore signatures, quoted reply history, tracking text, and unrelated
     promotional copy.
2. Extract only supported event facts:
   - a concise title;
   - the start and end, or a start plus an explicit duration;
   - an IANA time zone when the source or conversation establishes one;
   - an optional description, location, and HTTP(S) event URL.
3. Separate source facts from assumptions.
   - Resolve relative dates against the conversation date.
   - Ask one concise clarification when ambiguity could change the scheduled
     date, time, duration, timing mode, or time zone.
   - Do not ask about missing optional details.
   - Do not invent a location, URL, end time, or time zone.
4. Choose the timing mode.
   - Use timed timing when a time of day is intended.
   - Use all-day timing only when the message describes a date-based event with
     no intended time of day. Treat its end date as inclusive.
   - For a timed event, include an explicit IANA time zone when known. Otherwise
     allow `display-event` to use its client time-zone hint; if the tool cannot
     resolve one, ask the user for it and retry.
5. Invoke `display-event` once with the normalized event. Include optional
   fields only when supported by the source or the user's instructions.
6. Present the resulting editable card. Briefly disclose any non-obvious
   interpretation that remained necessary.

## Output

Deliver one editable Event Creator card whose title, timing, time zone, and
optional details match the source.

## Boundaries

- Do not retrieve email, messages, or attachments from another service.
- Do not create multiple events from one invocation.
- Do not add attendees, recurrence, reminders, or calendar-account writes.
- Do not claim the event was added to a calendar. The user exports it from the
  widget.
