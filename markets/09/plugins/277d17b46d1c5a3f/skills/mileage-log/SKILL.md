---
name: mileage-log
description: Build an IRS-style mileage log (PDF and Excel) from trips, recurring trips or a CSV/XLSX file with generate_mileage_log, and compute a mileage reimbursement or deduction at the IRS rate for the trip date or an employer rate with calculate_mileage_reimbursement.
---

# Odometry Mileage Log

Use these tools when the user wants a mileage log, a mileage reimbursement or deduction amount, or the IRS mileage rate applied to their miles.

## generate_mileage_log
1. Turn each drive into a trip: `date` (YYYY-MM-DD; turn "Mon" into a real date from the conversation), `from`, `to`, `purpose`, optional `client`, and `miles` or `odometer_start` + `odometer_end`.
2. Round trips: "12.4 mi round trip" means 12.4 total, so pass `miles: 12.4` with `round_trip` false. Use `round_trip: true` only for one-way distances ("6.2 mi each way").
3. Repeating drives ("every weekday in October, 18 mi") go in `recurring`; holidays or days off go in `skip_dates`.
4. If the user attached a trip spreadsheet (CSV, TSV, XLSX), pass it as `file`. Typed trips and a file can be combined.
5. Pass `custom_rate_per_mile` only when the user names an employer or contract rate. Otherwise the IRS rate for each trip date is used.
6. Mark home-to-regular-office drives as `category: "commute"`; personal drives as `personal`. Medical, military moving and charity trips use their own categories.
7. After the call, report the total miles and amount, any flags to check, and give the PDF and Excel links (they expire in 24 hours).

## calculate_mileage_reimbursement
- Use for a total number of miles without a trip list. Give `date` (or `segments` when miles fall before and after July 1, 2026), `custom_rate_per_mile` for an employer rate, or `odometer_start`/`odometer_end` with `personal_miles`.

Do not use these tools to look up driving distances, track GPS, or answer gas price or car-buying questions. Do not invent miles: ask the user for any missing distance.
