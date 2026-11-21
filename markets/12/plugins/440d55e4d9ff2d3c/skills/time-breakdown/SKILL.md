---
name: time-breakdown
description: Break down where time went in TimeTackle - hours by tag, project, client, department or any other property for a period, optionally per person or per calendar, including untagged time. Use when the user asks how time was split, what took the most time, or hours per tag or property.
---

# Time breakdown

Answer "where did the time go?" with hours per tag or property value for a clear date range. Explicit instructions
from the user (period, people, property, format) take priority over these steps.

## Input

- A period. If none is given, use the last full week and say so. Convert relative periods ("last month",
  "this quarter") to exact `YYYY-MM-DD` dates.
- What to break down by: a property the user names (Project, Client, Department, ...) or, if none, the top-level tags.
- Optionally per person or per calendar, or limited to specific calendars.

## Steps

1. Call `get_account` and read `syncRange`. If the period falls partly or fully outside it, tell the user that data
   only exists from `syncRange.start` to `syncRange.end` before showing numbers.
2. Find the property. Call `get_properties` with `search` set to the name the user gave (for example "Client").
   - Note its `key` and `state` (PRIMARY or SECONDARY).
   - If several properties match, ask which one. If none match, list a few property keys and ask; do not guess.
   - If the user named no property, skip this step and break down by the top-level tags (step 3, no `tagKey`).
3. Call `get_meeting_analytics`:
   - `measures: ["hours"]` (add `"count"` if the user asks how many meetings or entries).
   - `groupBy: "primary_tag"` for a PRIMARY property, `"secondary_tag"` for a SECONDARY one.
   - `tagKey`: the property's key, to get hours per value. Omit it to get hours per tag; that view includes an
     "UNTAGGED" row for time with no tag.
   - `splitBy: "user"` for per person, or `"calendar"` for per calendar.
   - `dateFrom`, `dateTo`, and `timezone` (the user's stated timezone, otherwise the `timezone` of their own calendar
     from `get_imported_calendars`; say which one you used).
   - `calendarIds` only if the user limited the calendars.
4. If `summary.nextOffset` is not null, call again with `offset` set to it until it is null, and combine the rows.
5. If the result has a `syncRangeWarning`, repeat it to the user.

## Output

- A table sorted by hours, largest first: value, hours (one decimal), share of the total (%). With `splitBy`, one row
  per person (or calendar) and value, or a person × value table if it stays readable.
- The total hours and the exact date range.
- With `tagKey`, say that time without a value for that property is not included. Without `tagKey`, show UNTAGGED
  as its own row.
- Follow the result's `visualization` hint if the user wants a chart.

## Do not

- Do not invent values, people or hours that are not in the tool results, or fill gaps with estimates.
- Do not describe a person's performance; report hours only.
- People and calendars are limited to what the user can access in TimeTackle; do not suggest others exist.
