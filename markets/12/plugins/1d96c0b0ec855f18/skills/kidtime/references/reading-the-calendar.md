# Reading the calendar

`events_list` returns what is on a calendar between two instants. Give `timezone` and an exact range
with `startDate` and `endDate`, such as this Sunday's midnight to two weeks later, or a whole month.

- **Who has the kids at a moment** is the parent the last hand-off before it went to: read the
  hand-off events (`custodyTransitions`, from which parent to which, for which child). The calendar
  drawing has the full bars; you get the hand-offs.
- **`analytics`** gives each parent's overnights and share of nights per month. Use it for "how many
  nights do I have" and "what is our split".
- **Custody percentage and "how many days a year"** (for example "how many days is every other
  weekend in a year"): call `events_list` for the whole period, such as twelve months from the
  schedule's start, then add up each parent's overnights across the months and give the percentage.
  Say it counts nights, and that the result is for this calendar's schedule, not a general rule.
- **`events`** are the hand-offs and other events. A hand-off's `custodyTransitions` say which child
  moves from which parent to which.
- **`traditionsByDate`** gives the holidays and birthdays on each day. A break is an event with its
  tradition.

## Answering

- Times come back in UTC. Say them in the event's own time zone (`startTimeZone`).
- Where the client can draw it, `events_list` shows the month as a calendar with each parent's
  colour. Then sum it up in a sentence or two ("Alex has Robin Monday and Tuesday, then you have him
  until Friday at 5 PM") instead of listing every day.
- "Who has the kids on Saturday?" is the block that covers Saturday night.
- For the saved pattern itself (its name, start and times) use `custody_schedules_list`.
