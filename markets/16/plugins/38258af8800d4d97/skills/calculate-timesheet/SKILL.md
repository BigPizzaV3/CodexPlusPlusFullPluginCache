---
name: calculate-timesheet
description: Use when the user wants hours worked, a timesheet or time card total, overtime, or gross pay from their shift start and end times, or wants that timesheet exported as a CSV.
---

# Calculate a timesheet

Use the Timesheet Calculator tools for the arithmetic instead of adding up hours yourself.

1. Collect each shift's start and end time, plus any unpaid break in minutes. Accept everyday formats such as 9am, 9:00 AM, or 17:30. If a time is ambiguous, such as "5" with no am or pm, ask which one the user means.
2. Pass one entry per shift to `calculate_hours_worked`, even for a single one-off or overnight shift (such as 10pm to 6:30am), so the user sees the timesheet card. Include a day label when the user gives one. Treat the whole list as one pay period.
3. Add `hourlyRate` only when the user gives a rate. Add `weeklyOvertimeAfterHours` or `dailyOvertimeAfterHours` only when the user names a cutoff; otherwise the default is overtime after 40 hours in the period.
4. When the user asks for a file, a spreadsheet, or a CSV, including follow-ups like "export that" or "make a CSV" about a timesheet calculated earlier in the chat, call `export_timesheet_csv` with the same shifts and settings. Do not write the CSV yourself or use a built-in file or spreadsheet tool; the card has the Download CSV button.
5. The card already shows the table and totals. Reply with one short sentence of totals; do not repeat the table, paste CSV text, or add a download link.

Limits: the calculator does not store shifts, clock anyone in or out, file payroll, or compute taxes, withholding, or benefits. Say so plainly if the user asks for one of those, and do not present estimates for them as results from this plugin.
