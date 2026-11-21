---
name: meeting-load-review
description: Review meeting load in TimeTackle - meeting hours and counts over time, the mix of meeting lengths and sizes, recurring versus one-off meetings, and who organizes the most, with practical suggestions grounded in the numbers. Use when the user asks about meeting overload, how much time goes to meetings, or how to reduce meetings.
---

# Meeting load review

Give a short, data-backed picture of meeting load for a period, for the user or the calendars they choose. Explicit
instructions from the user take priority over these steps.

## Input

- A period. If none is given, use the last 4 full weeks and say so. Use exact `YYYY-MM-DD` dates.
- Whose meetings: the user's own calendars by default, specific calendars, or everything the user can access.

## Steps

1. Call `get_account` and read `syncRange`; if the period reaches outside it, say so.
2. Choose calendars: for "my meetings", call `get_imported_calendars` and use those whose `user.email` is the user's
   email; pass them as `calendarIds`. For a team or the workspace, omit `calendarIds`. Use the user's timezone, or
   their calendar's `timezone`, and say which one you used.
3. Call `get_meeting_analytics` (meetings only, the default) with the same `dateFrom`, `dateTo`, `timezone` and
   `calendarIds` each time:
   - Totals: `measures: ["hours", "count", "median_duration", "median_attendees"]`, `groupBy: "none"`.
   - Trend: `measures: ["hours"]`, `groupBy: "none"`, `granularity: "week"`.
   - Length mix: `measures: ["hours", "count"]`, `groupBy: "meeting_length"`.
   - Size mix: `measures: ["hours", "count"]`, `groupBy: "meeting_size"`.
   - Recurring vs one-off: `measures: ["hours", "count"]`, `groupBy: "recurring"`.
   - Top organizers: `measures: ["hours", "count"]`, `groupBy: "organizer"`, `limit: 10`.
4. If a result has a `syncRangeWarning`, keep it for the summary.

## Output

- Headline numbers: total meeting hours, number of meetings, average hours per week, median meeting length and
  attendees.
- The weekly trend (rising, falling or flat, with the numbers).
- Short tables for length mix, size mix, recurring vs one-off, and the top organizers.
- Two or three suggestions that follow from the numbers, for example reviewing a large block of recurring meetings or
  shortening default lengths if most meetings are 60 minutes. Tie each suggestion to a figure.
- The exact period, calendars covered and timezone.

## Do not

- Do not invent figures or benchmarks; compare only within the user's own data.
- Do not judge individuals; describe organizers by meeting time, and only show them if the user asked about the team.
- Calendars are limited to those the user can access in TimeTackle.
