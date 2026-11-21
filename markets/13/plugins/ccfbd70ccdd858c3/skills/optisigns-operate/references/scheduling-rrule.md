# Scheduling

A schedule plays different content at different times. Build it, then put the schedule on screens.

1. `optisigns_schedule_create(name)`
2. `optisigns_schedule_item_add(scheduleId, contentId, contentType asset|playlist, startDate, endDate,
   timezone?, rrule?)`, one call per time slot
3. `optisigns_screen_assign_content(deviceIds, contentId: <scheduleId>, contentType: "schedule")` (confirm)

Check the result with `optisigns_schedule_item_list(scheduleId, startDate?, endDate?)`; its range filters
are ISO UTC.

## Time and timezone

- `startDate` / `endDate` are the **screen's local wall-clock time**: `YYYY-MM-DDTHH:mm` (seconds
  optional). Write "9 am" as `T09:00`, no `Z`.
- A value with `Z` or an offset is treated as an instant and converted to `timezone` if you pass one.
  Prefer plain local times.
- **Read the screen's timezone** from `optisigns_screen_diagnose(screenId)` → `deviceTimezone` (an IANA
  name such as `America/Chicago`). Pass it as `timezone`. If screens in the schedule sit in different
  zones, say so; one schedule's times apply as local time on each screen.
- Unknown zone names and impossible dates (Feb 30) are refused.
- Defaults: `startDate` = now; `endDate` = start + 1 hour (one-off) or + 24 hours (recurring). `endDate`
  must be after `startDate`.
- For a recurring item, `startDate`/`endDate` are the **first occurrence**; the time of day repeats.

## RRULE cookbook

| Need | rrule |
|---|---|
| Every day | `RRULE:FREQ=DAILY` |
| Weekdays (Mon–Fri) | `RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR` |
| Weekends | `RRULE:FREQ=WEEKLY;BYDAY=SA,SU` |
| Specific days (Tue and Thu) | `RRULE:FREQ=WEEKLY;BYDAY=TU,TH` |
| Every other Monday | `RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=MO` |
| Monthly on the 1st | `RRULE:FREQ=MONTHLY;BYMONTHDAY=1` |
| First Monday of each month | `RRULE:FREQ=MONTHLY;BYDAY=1MO` |
| Yearly (a date each year) | `RRULE:FREQ=YEARLY` (from `startDate`'s month and day) |
| Weekdays until Dec 31 | `RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;UNTIL=20261231T235959` |
| 10 times then stop | `RRULE:FREQ=DAILY;COUNT=10` |
| One-off | omit `rrule`, or `RRULE:FREQ=DAILY;COUNT=1` |

- `UNTIL` is screen-local wall clock too (`YYYYMMDDTHHMMSS`, no `Z`).
- An rrule without `FREQ=DAILY|WEEKLY|MONTHLY|YEARLY`, or with `COUNT=1`, is saved as a one-off
  (`RRULE:FREQ=DAILY;COUNT=1`). Say so if the user expected it to repeat.
- `optisigns_schedule_repeat_presets(startDate ISO UTC)` returns the portal's presets (Daily, Weekly on
  <day>, Does not repeat) for a start date, if you want the portal's exact rules.

## Overlaps are rejected

Items whose times overlap on the same schedule are refused; there is no priority. To show a special
promo over normal content, split the normal item around it, e.g. normal 08:00–12:00 and 13:00–20:00, promo
12:00–13:00. Use back-to-back times (one ends 12:00, the next starts 12:00).

## Daypart worked example

"Breakfast menu 6–11, lunch 11–14, dinner 14–21, every day, at the Main St store."

1. `optisigns_screen_search("Main St")` → screen id; `optisigns_screen_diagnose` → `deviceTimezone:
   America/Chicago`.
2. `optisigns_schedule_create("Main St – Menus")` → `scheduleId`.
3. Three `optisigns_schedule_item_add` calls, `timezone: "America/Chicago"`, `rrule: "RRULE:FREQ=DAILY"`:
   - breakfast `2026-11-02T06:00` → `2026-11-02T11:00`
   - lunch `2026-11-02T11:00` → `2026-11-02T14:00`
   - dinner `2026-11-02T14:00` → `2026-11-02T21:00`
4. Ask the user, then `optisigns_screen_assign_content(contentType: "schedule")` and confirm.
5. Tell them: "From 6 am tomorrow, Main St shows breakfast until 11, lunch until 2, dinner until 9 pm
   (Central time)."

**Outside the dayparts** (21:00–06:00 here): the schedule's default content is not settable with these
tools. Either add an item for those hours (e.g. a closed slide 21:00 → 06:00 next day) or ask the user to
set the default content on the schedule in the OptiSigns portal. Say which you chose.

## Future go-live

`optisigns_screen_assign_content` is always immediate. To launch content later:

1. Create a schedule with an item that starts at the go-live time (and, if needed, an item for what plays
   until then).
2. Assign the schedule to the screen now. The screen switches by itself at the start time.

`optisigns_screen_cancel_scheduled(screenId)` cancels a scheduled go-live or temporary content set
elsewhere (for example in the portal); it is confirm-gated.

## Editing items: SINGLE vs ALL

`optisigns_schedule_item_update(scheduleId, itemId, scope, …)` is confirm-gated and changes screens
immediately; the old content and timing are not kept.

- `scope: "ALL"` (default): the whole series. `startDate`/`endDate` are the series' first occurrence as
  `optisigns_schedule_item_list` returns it. Changing `rrule` needs ALL.
- `scope: "SINGLE"`: one occurrence; on a recurring item pass `occurrenceStart` (that occurrence's current
  start, local time). The rest of the series stays.
- Omitted times are kept; you can change only `contentId` + `contentType`.
- Removing: `optisigns_schedule_item_remove` (confirm), `SINGLE` needs `startDate` of the occurrence.

Example, "skip the promo this Friday only": `optisigns_schedule_item_remove(scope: "SINGLE",
startDate: "2026-11-06T12:00")`.
