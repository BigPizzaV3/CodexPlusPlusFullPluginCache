---
name: countdown-calendar
description: Make a printable countdown calendar to one event (month grid, paper-chain strips or tear-off cards) with days-to-go numbers, weekday-only counting and skip dates, plus an ICS file with milestone reminders, using the generate_countdown_calendar tool.
---

# Zovo Countdown Chain

Use `generate_countdown_calendar` when the user wants a printable countdown, a paper chain countdown, tear-off countdown cards, "days until" a trip, wedding, birthday or holiday to cross off, or school days or work days left.

1. Pass `event_date` (YYYY-MM-DD) and `event_name`. If the user gives a date without a year, pass it as written; the tool uses the next one and says so.
2. Pass `start_date` only when the user names one; otherwise the countdown starts today. Pass `timezone` when you know the user's time zone.
3. Pick `style`: `chain` for a paper chain or strips, `tear_off` for cards, otherwise `grid`.
4. For school days or work days, set `weekdays_only: true` and put holidays in `skip_dates`. Do not invent holidays; ask once if the user says "skip holidays" without dates.
5. Put short daily notes in `messages` only when the user gives them.
6. After the tool returns, say the days to go and the counting rule, list the milestone dates, quote any "Check:" and "Assumed:" lines, and give the PDF and ICS links.

If the tool says the event is before the start date or more than 400 days away, tell the user and offer the fix it suggests. Do not use this skill for a live timer with minutes and seconds, a full-year wall calendar, or plain date arithmetic with no printable.
