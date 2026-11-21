---
name: flyer-to-calendar-event
description: Extract one calendar event from a visible flyer, poster, screenshot, or photographed notice and create an editable Event Creator card. Use when the user asks to turn event artwork or an image-based announcement into an event. Require the image to be visible and readable; do not invent text, decode an unreadable QR destination, or create multiple events.
---

# Flyer To Calendar Event

Turn one visible event flyer into one accurate, editable event.

## Inputs

Use the attached or otherwise visible flyer, poster, screenshot, or photographed
notice together with any corrections the user provides.

## Workflow

1. Confirm that the image is available and readable enough to identify an
   event. If it is missing or unreadable, ask the user to attach a clearer image
   or paste the relevant text.
2. Identify the single event the user wants.
   - If the image advertises several sessions, dates, or performances and the
     user did not choose one, ask which one to create.
   - Distinguish event facts from decorative, sponsor, and promotional text.
3. Extract only supported event facts:
   - a concise title;
   - start and end information or an explicit duration;
   - an IANA time zone when the flyer or conversation establishes one;
   - an optional venue or address, description, and clearly readable HTTP(S)
     event URL.
4. Check visually ambiguous details before scheduling.
   - Ask one concise clarification when a numeric date, missing year, time,
     duration, timing mode, or time zone has more than one material
     interpretation.
   - Do not infer a URL from a QR code whose destination is not visibly decoded.
   - Do not invent obscured or cropped text.
5. Choose the timing mode.
   - Use timed timing when the flyer specifies or clearly intends a time of day.
   - Use all-day timing only for a genuinely date-based event, not merely
     because the time is unreadable. Treat its end date as inclusive.
   - For a timed event, include an explicit IANA time zone when known. Otherwise
     allow `display-event` to use its client time-zone hint; if the tool cannot
     resolve one, ask the user for it and retry.
6. Invoke `display-event` once with the normalized event and only supported
   optional details.
7. Present the resulting editable card. Briefly disclose any non-obvious
   interpretation that remained necessary.

## Output

Deliver one editable Event Creator card based on the readable event facts in
the image.

## Boundaries

- Do not claim to use an OCR, QR-decoding, browsing, or image-retrieval service
  that is not available in the conversation.
- Do not create multiple events from one invocation.
- Do not add attendees, recurrence, reminders, or calendar-account writes.
- Do not claim the event was added to a calendar. The user exports it from the
  widget.
