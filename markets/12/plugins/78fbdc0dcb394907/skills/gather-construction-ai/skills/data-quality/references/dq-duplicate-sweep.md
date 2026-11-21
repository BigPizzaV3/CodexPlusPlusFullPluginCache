# Targeted Duplicate Sweep — Full Procedure (Step 10)

Triggered when `the user’s request` contains "duplicates" (e.g.
`$data-quality [project] [period] duplicates`) — the check for "people are being allocated
to duplicate shifts and it's hard to find".

1. Fetch the period's shift records via `getShiftRecords` (**Pattern 4**: 25/page, 2
   requests/second; warn and confirm if the period needs more than 2 pages), and save
   `dashboardResourceLabour` for the same period to the scratchpad.
2. Run `python3 ../../../scripts/shift_analytics.py <labour-file> --format md` —
   flags every same-person/same-date candidate; do not group or sum hours in context. Its
   candidates carry no start/end time, so confirm each via `getShiftRecord` (**quote only the
   fields you use** — times, location, supervisor — never the whole record): times overlap →
   `DOUBLE-BOOKING CANDIDATE`; times don't overlap (e.g. day/night shift) → "split shifts — looks
   legitimate, confirm intended", never a defect.
3. **Duplicate shift records** — two records same date, same supervisor/location, materially
   identical crew and narrative → `DUPLICATE-ENTRY CANDIDATE` (the whole record doubled, not just
   one person). Show both IDs and `lastModified` stamps (the later entry is usually the
   accidental copy — say "usually", not "certainly").
4. Present as a table sorted worst-first (double-bookings, duplicate entries, split shifts to
   confirm), each row carrying both record IDs for the fixer to go straight to in Gather.

**Language discipline:** every finding is a **candidate** — which record is wrong is for the site
team to confirm in Gather. Never assert a specific record is the error, and never frame findings
as anyone's fault — double-allocations are usually a planning-tool slip; the point of the sweep is
that they're currently hard to *see*. These duplicates silently corrupt everything downstream —
labour hours, timesheet verification, daywork sheets — which is why they matter
more than they look.

In a targeted "duplicates" run, Steps 3–9 and the composite score are skipped: present the sweep
table, the affected downstream skills line, and the read-only reminder, under the normal
`Ref: DQ-[NNN]` header.
