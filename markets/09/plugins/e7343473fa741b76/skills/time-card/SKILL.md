---
name: time-card
description: Time card and hours worked calculator. Totals clock-in/clock-out punches (multiple in and out per day, overnight shifts, lunch breaks, 12-hour or military time) with the calculate_hours tool, splits regular, overtime, and double time per workweek, computes gross pay, and exports CSV and a printable PDF timesheet.
---

# ShiftSum Time Card

Use `calculate_hours` whenever the user wants hours worked added up from clock times: a time card calculator, hours calculator, timesheet, "how many hours is 8:45 to 5:30", biweekly totals, or overtime from punches.

1. Put every day of the period in one call as `entries`. Each day gets a `day` label (an ISO date such as `2026-09-28` when known, otherwise `Mon`, `Tue`...) and `punches` as `{start, end}` pairs. Use several pairs for split shifts or a clocked-out lunch; an end earlier than the start is an overnight shift.
2. Put a lunch or break that was not clocked out as `unpaid_break_minutes` (for example "30 min lunch" = 30). Do not invent breaks the user did not mention.
3. Keep times as the user wrote them (`8:45`, `17:30`, `5:30 pm`, `9` and `5`). Times without am/pm are resolved by the tool and listed in `assumptions`; do not guess am/pm yourself.
4. Overtime: default `us_federal` (over 40 h per workweek at 1.5x). Use `california` only if the user works in California or asks for daily overtime and double time. Use the override fields for other thresholds (for example `daily_overtime_after_hours: 8`). Pass `hourly_rate` only if the user gives a pay rate. Pass `rounding` only if the employer rounds punches.
5. Biweekly: include both weeks; dates (or `week: 1/2`) keep overtime per workweek.
6. If `assumptions` is not empty, state it first and ask the user to confirm. Then reply with the total in H:MM and decimal, the regular/overtime split, gross pay if a rate was given, every warning verbatim, and the CSV and PDF links. Say once that overtime rules vary by jurisdiction and the result is informational.

To change one day, call `calculate_hours` again with the full corrected list. Do not use this skill for take-home pay after taxes, legal questions about breaks or overtime, reminders to clock in or out, or plain unit conversions with no clock times.
