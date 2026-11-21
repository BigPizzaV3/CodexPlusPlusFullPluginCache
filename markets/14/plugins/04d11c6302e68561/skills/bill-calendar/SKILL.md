---
name: bill-calendar
description: Make a printable bill payment calendar, ICS reminders for each bill, and a plan of which paycheck pays which bill with the generate_bill_calendar tool, with month-length and weekend rules handled.
---

# Zovo Bill Calendar

Use `generate_bill_calendar` when someone wants a bill payment calendar, a bill tracker printable, bill reminders in their calendar, or to know which paycheck pays which bill.

1. Put each bill into `bills` as an object: `{"name": "Rent", "amount": 1500, "due_day": 1}`. Add `"autopay": true` for automatic payments. Monthly is the default frequency. For quarterly, every-6-months, yearly and one-time bills give one `due_date`; for weekly and biweekly bills give `anchor_date`. Convert a pasted list or a screenshot into these fields.
2. Put pay into `paychecks`: `{"amount": 2100, "frequency": "biweekly", "first_date": "2026-11-06"}`, or semimonthly with `day` 15 and `second_day` "last".
3. Set `start_month` and `months` (1 to 12, default 3). Optional: `weekend_rule` "previous_business_day", `reminder_days_before` (default 2), `reminder_time`, `starting_balance`, `page_size` "A4", `week_start` "Monday", `title`.
4. After the result, give the month totals, any short-month or weekend moves, which paycheck pays which bill with the money left, and the PDF, ICS and Excel links (they expire in about an hour).

Do not use it to pay bills, for budgeting advice without dates, or for calendars of holidays.
