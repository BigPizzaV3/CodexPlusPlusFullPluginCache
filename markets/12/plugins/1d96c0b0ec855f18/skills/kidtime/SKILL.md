---
name: kidtime
description: Build and keep a shared custody calendar with Kidtime — pick a custody pattern (2-2-3, alternating weeks, every other weekend and more), set and move hand-offs, add holidays, birthdays and school breaks, and see who has the kids on any date. Use when a separated or co-parenting parent wants to plan, check or change custody time.
---

# Kidtime

Kidtime is a custody calendar for separated parents. Its tools run the same actions as the Kidtime
app, so what you make here is a real Kidtime calendar the person can open on the web or keep in the
app.

## No account needed

Every tool works without signing in. A calendar made in chat belongs to the person, and nobody else
sees it or is told about it until they share or claim it. Only a parent who already keeps their
family in the Kidtime app needs to sign in, to reach that family.

## Order of work

1. **Look first.** Call `groups_list` before making anything: the person may already have a
   calendar from an earlier chat. Make a new one with `groups_save` only when there is none, or when
   they ask for another.
2. **Let them choose the pattern.** If they have not named one, call `custody_patterns_list`: it
   shows a picker. Wait for their choice. If they describe their schedule instead ("every other
   weekend, Friday to Monday"), match it to a pattern and confirm it with them.
3. **Set the schedule** with `custody_schedules_save`, then check the first hand-offs with
   `events_list`. If they are wrong, call `custody_schedules_save` again (it replaces the schedule).
   Do not patch single hand-offs to fix a wrong schedule.
4. **Show it** with `events_list`: it draws the month, with each parent's colour.
5. **Changes** — moving a hand-off, extra time with the kids, or a one-off event — go through
   `events_save`; removing one through `events_delete`. Ask before deleting.
6. **Holidays and breaks**: `traditions_list` to see what is on, `traditions_save` to add or remove,
   `traditions_get` for who had the kids on a holiday in past years. A birthday is a person's: set
   it with `members_save`.

## More detail

Read the file that matches the request before acting on it:

- `references/patterns-and-schedules.md`: choosing and saving a pattern, start day, hand-off times
- `references/handoffs-and-events.md`: moving a hand-off, extra time with the kids, one-off events,
  deleting
- `references/holidays-and-traditions.md`: holidays, birthdays, school breaks, past years
- `references/reading-the-calendar.md`: who has the kids when, nights and splits, answering clearly
- `references/sharing-and-keeping.md`: the calendar's link, PDF, keeping it, deleting it

## Never

- Never mention prices, plans, trials or upgrades, and never send the person to a payment page.
- Never give legal advice or say who should have custody. Kidtime records and plans a schedule; for
  what a court would decide, suggest a family law attorney or mediator.
- Never invent a member id or a groupId. Take them from `groups_list`, `groups_save` and
  `members_list`.
