---
name: focus-timer
description: Run live pomodoro, countdown, and interval timers in the chat and plan study or work sessions into whole pomodoros with clock times and a calendar (.ics) file, using show_focus_timer and plan_focus_session.
---

# Zovo Focus Timer

Use `show_focus_timer` when the user wants a timer now:

- "pomodoro timer", "25/5", "50/10", "pomodoro timer for studying" -> `mode: "pomodoro"` with `work_minutes` and `short_break_minutes` from the ratio (defaults 25/5, long break 15 after every 4 rounds, 4 rounds).
- "10-minute timer", "countdown timer" -> `mode: "countdown"`, `work_minutes: 10` (decimals for seconds: 0.5 = 30 s).
- "45 seconds on, 15 off, 8 rounds" -> `mode: "interval"`, `work_minutes: 0.75`, `short_break_minutes: 0.25`, `rounds: 8`.
- Put what the user is working on in `label`. If they mention a start clock time, pass `start_time` plus `time_zone` when they name one (an IANA name, a city such as "Warsaw", or an abbreviation such as "EST").

Use `plan_focus_session` when the user describes a window to fill: "I have 3 hours to study until 5pm" -> `end_time: "17:00", available_minutes: 180`; "pomodoros from 9:00 to 12:30 with lunch at 12" -> `start_time`, `end_time`, and `breaks: [{"start":"12:00","end":"12:45","label":"Lunch"}]`. Pass `time_zone` and `date` when known. Leave `long_break_minutes` unset unless the user asks for a specific long break: the planner then shortens or drops the long break when that fits an extra focus block, and says so. Ask one short question if a lunch or meeting time is mentioned without a clock time.

After either tool returns, summarise in two or three lines (blocks, total focus minutes, end time, and any note about a shortened long break or a daylight-saving change), mention the live timer in the widget, and share the calendar link when present. Do not repeat every phase unless asked.

Do not use these tools for reminders about future appointments, questions about how long something takes (cooking, boiling an egg), unit conversions, the history of the Pomodoro Technique, or multi-day study schedules.
