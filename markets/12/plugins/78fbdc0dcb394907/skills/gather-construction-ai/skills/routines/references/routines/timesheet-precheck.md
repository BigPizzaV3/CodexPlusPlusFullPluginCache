## timesheet-precheck

**Cadence:** Weekly, aligned to the payroll cycle — e.g. Tuesdays, 08:00 (before the pay run)
**Surface:** Desktop
**Prerequisites:** `{{FOLDER}}/timesheets/` drop folder; `{{FOLDER}}/routine-state/timesheet-precheck/last-run.md`; `commercial-profile.md` optional (prices the variance)
**Priority:** Standard

**Instructions:**
```
Check {{FOLDER}}/timesheets/ for timesheet files (CSV/XLSX/markdown) added or modified since
the date recorded in {{FOLDER}}/routine-state/timesheet-precheck/last-run.md.

If there are none: reply in two lines ("No new timesheets since [date] — nothing to verify")
and stop.

For each new file, run $timesheet-check for {{PROJECT}} against it, covering the date
span the timesheet itself contains (explicit dates from the file, not the run date). Keep the
full four-verdict discipline and the reverse sweep. Lead the reply with the exceptions ranked
by hours (or value where the commercial profile prices them), then the draft query text.
A recording gap (NO RECORDS) is reported as a gap, never as absence.

Update routine-state/timesheet-precheck/last-run.md with today's date and the files verified.
This output names individuals — internal commercial review only.
```
