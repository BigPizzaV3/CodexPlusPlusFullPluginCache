---
name: date-calculator
description: Count days between dates, count business days (working days) excluding weekends and public holidays for a country or state, find the date N calendar or business days before or after a date, and list public holidays, with the count_days_between, calculate_date_offset and list_holidays tools.
---

# Zovo Date Calculator

Use these tools for exact date arithmetic instead of mental math.

- `count_days_between`: "how many days between X and Y", "business days between two dates", "days between dates excluding weekends". The start date is counted; set `include_end_date: true` when the user says "through", "inclusive", or wants Excel NETWORKDAYS behaviour.
- `calculate_date_offset`: "what date is 90 days from today", "30 business days from Nov 3 in Germany", shipping and contract deadlines. Use `unit: "business"` for business/working days (negative `days` goes back). For calendar-day deadlines that must end on a working day, pass `roll: "next_business_day"`.
- `list_holidays`: "public holidays in Poland 2026", "Texas state holidays".

Tips:
1. Pass dates as YYYY-MM-DD. Call the tool right away when the dates are clear. If the user leaves out the year ("Dec 15 to Jan 10"), use the next upcoming occurrence and say which years you assumed; pass "today" for today. Ask only when a date is ambiguous, like 03/04/2026 (March 4 or April 3).
2. For business days, pass `country` (ISO code) and, when a state or region is named, `subdivision` (e.g. US + TX, DE + BY, GB + SCT, AU + NSW). Without a country only weekends are skipped.
3. Use `weekend_days` for non-standard weekends (e.g. friday + saturday) and `extra_holidays` for company closure days.
4. Observed holidays are handled: when a holiday falls on a weekend, the weekday it is observed on (for example US Independence Day 2027 on a Sunday, observed Monday July 5) is skipped as a holiday.
5. Report the result with its weekday and name the holidays that were skipped. For legal or court deadlines, mention that special rules (court holidays, service days) may apply and the result is informational.

Do not use for times of day or time-zone conversion, stock-market trading hours, carrier delivery estimates, or writing SQL/spreadsheet formulas.
