# Patterns and schedules

A **schedule** is a custody pattern laid over the calendar: it makes the repeating **hand-offs**,
the moments the kids move from one parent to the other. The time between two hand-offs is a
**stay**.

## Choosing the pattern

- If the person has not named a pattern, call `custody_patterns_list`. It shows a picker. Wait for
  their choice; do not pick for them, and do not reuse a pattern from an earlier chat.
- If they describe their schedule instead, match it and confirm before saving:
  - "every other weekend" → `alternating-weekends` (80/20)
  - "the 1st and 3rd weekend of the month" → `first-third-weekends` (80/20)
  - weekdays with one parent and every weekend with the other → `every-weekend` (70/30)
  - "week on, week off" → `alternating-weeks` (50/50)
  - "2 days, 2 days, 3 days" → `2-2-3` (50/50)
- If nothing matches, say so. A schedule can still be built from repeating hand-offs with
  `events_save` (see `handoffs-and-events.md`).

## Saving it with `custody_schedules_save`

- **startDate** is the person's real first day, such as the coming Friday. Nothing before it changes.
- **patternShift** says how far into the pattern that day falls, 0 to 6. The pattern's day 0 is
  `startDate` minus `patternShift`. Every other weekend starting on a Friday is
  `alternating-weekends` with `patternShift` 4.
- **toMemberId** is the parent who has the kids on the pattern's day 0, its first nights. For
  `alternating-weekends` that is the parent with the weekdays.
- **Times.** `exchangeTime` when every hand-off is at the same time (17:00 if left out).
  `transitionTimes` when they differ: one HH:MM per hand-off, in the order they fall from day 0. The
  pattern list says how many hand-offs a pattern has (`transitionCount`). Example: a Friday 5 PM
  pick-up and a Monday 9 AM drop-off are `['17:00', '09:00']`.
- **timeZone** is the person's IANA zone. Ask if you do not know it.
- Saving **replaces** the hand-offs from `startDate` to `endDate` (a year unless given).

## Checking it

Call `events_list` for the first two weeks and read the first hand-offs back: day, time, and who
gets the kids. If any is wrong, call `custody_schedules_save` again with corrected values. That
replaces the schedule cleanly. Do not fix a wrong schedule by editing single hand-offs.
