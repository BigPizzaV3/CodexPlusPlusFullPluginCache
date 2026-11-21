---
name: shift-scheduler
description: Employee schedule maker. Builds a weekly staff shift schedule from staff, roles, availability, hour limits and the shifts to cover with generate_shift_schedule (a solver that checks each hard rule and explains open shifts), checks an existing schedule with check_schedule, and exports a printable PDF, Excel and per-employee calendar files.
---

# Rotawise Shift Scheduler

Use `generate_shift_schedule` when the user wants a work schedule made: "employee schedule maker", "make a weekly schedule for 6 employees", "restaurant staff schedule", "need 2 people on each shift", "rotating schedule so weekends are fair", "who should close on Friday".

1. Put each person in `staff`: `name`, `roles` only if shifts need roles, `max_hours`/`min_hours` only if given, `unavailable` for days or times they cannot work ("Mon", "Sat before 14:00"), `available` only for people who can work ONLY certain times, `preferred` for soft wishes. If the user attached an availability CSV/XLSX, pass it as `staff_file` (typed `staff` entries override the same names).
2. Put each shift in `shifts` once, using day ranges: `{"day":"Mon-Fri","start":"07:00","end":"15:00","role":"cook","headcount":2}`. An end before the start is an overnight shift. Keep times as the user wrote them; bare times like "7-3" are resolved and listed in `assumptions`.
3. Rules: `min_rest_hours` (default 10), `max_consecutive_days` (6), `overtime_after_hours` (40), `allow_overtime` (false), `max_shifts_per_day` (1). Pass `week_start` (a date) and `time_zone` when known.
4. Reply with coverage, each open shift with its reason and options verbatim, hours per person with overtime flags, the day-by-day schedule, and the PDF, Excel and calendar links (they expire in about an hour). Do not invent assignments the tool did not return or move people yourself.

Use `check_schedule` when the user already has a schedule: pass each shift with its people as `assignments` (or the attached file as `schedule_file`) and any staff rules. Report each problem. To fix it, call `generate_shift_schedule` with the same shifts and staff plus the new constraint (for example Sam `unavailable: ["Mon"]`).

To change anything, call the tool again with the full corrected input. Do not use these tools for job searches, time clocks, payroll or legal questions about scheduling laws.
