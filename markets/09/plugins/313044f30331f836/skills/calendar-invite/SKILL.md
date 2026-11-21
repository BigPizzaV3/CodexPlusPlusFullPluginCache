---
name: calendar-invite
description: Make .ics calendar files and add-to-calendar links (Google Calendar, Outlook.com, Office 365, Yahoo) for one event or a repeating event with generate_calendar_event, or one .ics with many different sessions (a course or event schedule) with generate_event_series.
---

# InviteKit Calendar Files

Use `generate_calendar_event` when the user wants a calendar invite, an .ics file, or an add-to-calendar link for one event or one repeating event. Use `generate_event_series` when the user lists several different dates (a course, training plan, fixtures, conference sessions) that should import as one file.

1. Pass `start`/`end` as local times `YYYY-MM-DDTHH:MM` with the event's `time_zone` (a city like "Chicago" or an IANA zone like "America/Chicago"). Never convert to UTC yourself and never add an offset to `start`. Resolve relative dates ("next Tuesday") to real dates first.
2. All-day events: pass dates only (`2026-11-05`); `end` is the last day, inclusive.
3. `end` can be just a time ("21:00") on the start day. If no end is given the event lasts 1 hour.
4. Repeats: `recurrence.frequency` daily/weekly/monthly/yearly; weekly uses `weekdays` (["TU","TH"]); "second Tuesday" or "last Friday" uses `monthly_on: "nth_weekday"` with `nth` (2 or -1); "last working day of the month" uses `weekdays` ["MO","TU","WE","TH","FR"] with `nth` -1; end with `count` or `until` (not both); skipped dates go in `exceptions`.
5. If the time zone of a timed event is unknown, ask once. Ask for nothing else that is optional.
6. After the tool returns, give the date and time line, the repeat summary, any notes (skipped or repeated clock times, daylight saving changes, moved start dates) and the .ics download link plus the calendar links. For a series, mention that the Outlook.com, Office 365 and Yahoo links add only the first date.

Do not use these tools to email invitations, add attendees, read or change a calendar, track RSVPs, or find a meeting time across time zones.
