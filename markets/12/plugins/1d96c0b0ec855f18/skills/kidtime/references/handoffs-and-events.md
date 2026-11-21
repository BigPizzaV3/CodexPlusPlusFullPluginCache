# Hand-offs and events

A **hand-off** is an event that moves the kids from one parent to the other: an event with
`custodyTransitions`, one entry per child who moves, from one parent to the other. Its attendees are
both parents and the kids who move. Every other event (a game, a school play) has no
`custodyTransitions`. Member ids come from `members_list`; never make one up.

## Three different requests

1. **Moving a hand-off.** "This Friday's 5 PM pick-up is Saturday at 10 AM instead." Find that
   hand-off's `eventId` with `events_list` and call `events_save` with the `eventId` and only the new
   times. For a repeating hand-off, `scope` `single` (the default) moves this one; `future` moves
   this one and every later one.
2. **Extra time with the kids.** "I'll take them next weekend, even though it's Alex's week." That is
   a new stay, so add two hand-offs with `events_save`: one to the person when it starts (Friday) and
   one back to the other parent when it ends (Sunday). The regular schedule stays as it is around it.
3. **A one-off event.** No `custodyTransitions`: a timed event with `startDateTime`, `endDateTime` and
   `startTimeZone`, or an all-day one with `startDate` and `endDate`. `rrule` makes it repeat, such as
   `FREQ=WEEKLY;BYDAY=TU` for every Tuesday.

A regular arrangement with no matching pattern (a Tuesday evening visit and a Friday overnight every
week) is built the same way: repeating hand-offs with `rrule`, each with its own time.

## Rules

- `endDateTime` must be after `startDateTime`.
- Times are ISO instants in UTC. Convert from the person's local time and set `startTimeZone`.
- With an `eventId`, send only what changes.
- **Deleting** goes through `events_delete`. Ask before deleting more than one event. For a repeating
  event, `single` deletes this one, `future` this one and every later one, `all` the whole series
  except the days both parents have confirmed.
- After a change, call `events_list` and tell the person what the calendar now shows.
