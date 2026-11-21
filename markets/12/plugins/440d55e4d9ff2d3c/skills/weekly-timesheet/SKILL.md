---
name: weekly-timesheet
description: Build a weekly timesheet from TimeTackle - a person's hours per day and per project or tag for a week, with untagged time and days with little tracked time called out. Use when the user asks for their timesheet, what they worked on this or last week, or a weekly summary of their time.
---

# Weekly timesheet

Summarize one person's week from their calendars. Explicit instructions from the user (which week, which person,
grouping, format) take priority over these steps.

## Input

- The week. If none is given, use the current week (Monday to Sunday) and say so; "last week" is the previous one.
- The person: the connected user unless they name someone else.
- Optionally the property to group by (for example Project); otherwise the top-level tags.

## Steps

1. Call `get_account` for the user's email and `syncRange`. If the week reaches outside the sync range, say so.
2. Call `get_imported_calendars` and pick the person's calendars: those whose `user.email` is the person's email.
   - For someone else, they must appear in the list; if they don't, say you cannot see their calendars and stop.
   - Use the `timezone` of their calendar unless the user gave one, and say which one you used.
3. Daily totals: call `get_meeting_analytics` with `measures: ["hours"]`, `groupBy: "none"`, `granularity: "day"`,
   `meetingsOnly: false`, the week's `dateFrom` / `dateTo`, `timezone`, and `calendarIds` set to the person's calendars.
4. Time by project or tag: call `get_meeting_analytics` with `measures: ["hours"]`, the same dates, timezone and
   `calendarIds`, and either:
   - `groupBy: "primary_tag"` (no `tagKey`) for hours per tag, including an UNTAGGED row; or
   - the property the user named: find it with `get_properties` (`search`), then `groupBy` by its `state` and
     `tagKey` set to its key.
5. Optionally, for detail, call `get_events` with the person's `calendarIds`, the week's dates and `timezone` to list
   the week's events by day (page with `page` if there are more).

## Output

- A day-by-day table: date, hours.
- A table of hours per project or tag, with UNTAGGED as its own row when present.
- The week's total hours, the exact dates and the timezone.
- Call out days with no or very little tracked time, without assuming a standard working day unless the user gives
  one. If untagged time is large, suggest tagging it in TimeTackle.
- If a result has a `syncRangeWarning`, include it.

## Do not

- Do not invent events, projects or hours; report only what the tools return.
- Do not judge the person's productivity; describe the time.
- Do not create or change anything; to add missing time, the user can ask to log it.
