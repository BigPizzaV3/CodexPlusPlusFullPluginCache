## month-end-close

**Cadence:** Monthly, {{ASSESSMENT_DAY}} minus 3–4 days
**Surface:** Desktop
**Prerequisites:** `contract-profile.md` and `commercial-profile.md` (Pattern 14); `{{FOLDER}}/routine-state/month-end-close/last-run.md`
**Priority:** Standard

**Instructions:**
```
Period = the calendar month (or valuation period per the contract profile) ending on
{{ASSESSMENT_DAY}} — use that explicit date; if this run fires late, still close the same
period, do not roll forward to the next one.

Using the contract and commercial profiles in this folder, run in sequence for {{PROJECT}}:
$valuation for the period, $material-reconciliation for the same period,
$prelims-monitor to date, and $cost-to-complete. Rates come only from the
commercial profile — where a line has no rate, show it quantities-only and say so; never invent
a rate. Save the valuation HTML to {{FOLDER}} with the period-end date in the filename.
Lead the reply with the data-quality coverage line for the period before any priced figures —
a thin recording month silently corrupts every number downstream.
Read and update {{FOLDER}}/routine-state/month-end-close/last-run.md — note only what's new
versus last month's close (e.g. a line that flipped from quantities-only to priced).
```
