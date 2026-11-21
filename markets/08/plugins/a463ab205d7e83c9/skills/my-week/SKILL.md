---
name: my-week
description: Summarize the user's schedule and workload from Minz.ai, including meetings, overdue and upcoming tasks, and recent sales activities, for today, this week or another short period. Use when the user asks what is on their plate, what is coming up, what is overdue, or to plan their day or week.
---

# My week

Turn the user's calendar, tasks and recent activities into a short plan.

## Data and its limits

- `general_calendar_search` takes either `from` and `to` (ISO date-times with a timezone offset, `to` after `from`, at most 90 days) or a `range` shortcut: `today`, `this_week` (Monday to Sunday) or `next_7_days`. With `range`, pass the user's IANA `timezone` when you know it; otherwise it resolves in UTC, so say which timezone you assumed. It returns events that overlap the range, with title, start, end and all-day flag, up to `limit` rows (at most 50). Cancelled events are excluded. Description, location, meeting link and attendees are never returned, and private events come back redacted. Do not guess who a meeting is with.
- `general_tasks_search` returns title, status, priority, due date and any linked deal or contact, up to 50 rows. `status` is an exact value such as `Todo`, `In_Progress` or `Done`. Use `overdue: true` for tasks due before today that are not done, `dueFrom`/`dueTo` for a due-date window, `dealId`/`contactId` for one record, and `sort` (`asc` or `desc`) to order by due date.
- `general_activities_search` returns activities (type, title, date), up to 20 rows, and never their notes. `query` matches titles only. Use `from`/`to` to bound the date and `sort: "asc"` to list upcoming ones oldest first.

## What to report

1. **Meetings** in the period, in time order, with day and time.
2. **Overdue tasks:** due date in the past and not done, highest priority first.
3. **Due in the period:** tasks due within the requested dates.
4. **Recently done:** a few recent activities, only if they help the user pick up where they left off.

End with one or two suggestions for what to tackle first. If a list hit its row limit, say it may be incomplete. Reply in the user's language.
