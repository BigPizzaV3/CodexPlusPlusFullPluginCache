---
name: travel-reservation-event
description: Turn one visible flight, train, bus, ferry, hotel, or other travel reservation into an editable Event Creator card. Use when the user provides itinerary or booking details for one segment or stay. Normalize cross-zone timing into the app's single event time zone; do not retrieve bookings, check live status, expose unnecessary sensitive data, or batch-create an itinerary.
---

# Travel Reservation Event

Turn one supplied travel reservation into one accurate, editable event.

## Inputs

Use reservation or itinerary details visible in the conversation and any
preferences the user provides. Handle one transportation segment or one lodging
stay at a time.

## Workflow

1. Select the single reservation to create.
   - If the source contains several segments or stays and the user did not
     choose one, ask which one to use.
   - Do not silently merge connections, return journeys, or separate bookings.
2. Extract the supported facts.
   - Build a concise title that identifies the journey or stay.
   - Capture the scheduled start, scheduled end or explicit duration, and the
     relevant IANA zones.
   - Use the departure, boarding, or check-in place as the event location unless
     the user prefers another location.
   - Put useful terminal, platform, destination, check-in, or checkout context
     in the description.
   - Include a valid HTTP(S) booking or information URL only when it is visible
     in the source.
3. Protect sensitive information.
   - Include a confirmation or booking reference only when the user asks for it
     or clearly expects it in the calendar entry.
   - Omit payment data, ticket barcodes, loyalty numbers, passport details, and
     other unnecessary credentials.
4. Normalize timing into one event time zone.
   - For transportation, normally use the departure location's IANA zone.
     Interpret the departure in that zone, interpret the arrival in its local
     destination zone, then convert the arrival instant into the chosen event
     zone for `endLocal`.
   - Preserve the original arrival local time and destination zone in the
     description when that context helps the traveler.
   - For lodging, use the property's IANA zone. Use timed timing when explicit
     check-in and checkout times are intended; otherwise use inclusive all-day
     dates.
   - Resolve date-line crossings, overnight arrivals, and DST before invoking
     the tool. Confirm that the end instant is after the start instant.
5. Ask one concise clarification when an ambiguous date, airport or station,
   local time, time zone, or missing arrival date could change the event.
   Do not ask about missing optional details.
6. Invoke `display-event` once with the normalized event.
7. Present the resulting editable card and briefly note any important zone
   conversion used.

## Output

Deliver one editable Event Creator card for one travel segment or lodging stay,
with timing represented accurately in one IANA zone.

## Boundaries

- Do not retrieve reservations from email, airline, hotel, or booking services.
- Do not look up live delays, gates, platforms, cancellations, or check-in
  status.
- Do not create several itinerary events in one invocation.
- Do not add attendees, recurrence, reminders, or calendar-account writes.
- Do not claim the reservation was changed or added to a calendar. The user
  exports the event from the widget.
