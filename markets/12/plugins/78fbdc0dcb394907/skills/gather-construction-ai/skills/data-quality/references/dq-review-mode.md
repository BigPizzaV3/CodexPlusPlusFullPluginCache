# Step 12: Review Mode — Record Review Punch-List (Detail)

Run this **after** the Step 11 report has been presented in full.

1. **Identify worst candidate dates.** From the dashboards already fetched in Step 2, list dates that have a shift recorded (`dashboardShiftTable`) but are missing a narrative (`dashboardNarrative`), missing labour (`dashboardResourceLabour`), or missing progress (`dashboardProgress`). These are the candidate dates for record-level inspection.
2. **Fetch the records.** Call `getShiftRecords` filtered to those candidate dates, following **Pattern 4** (25/page, 2 requests/second) from `../../../shared/patterns/04-pagination-rate-limits.md`. If more than 10 candidate records result, warn the user and confirm before proceeding — by default, fetch only the **10 most recent** candidates.
3. **Inspect each record.** Call `getShiftRecord` for up to 10 records (pace per Pattern 4). Apply this completeness checklist — the same criteria as the record-completeness hook, so findings are consistent with anything already flagged elsewhere in the session:
   - Narrative present and >10 words
   - Workers listed
   - Weather recorded
   - Shift start/end times present
   - Shift duration plausible (2–14h)
   - Photos attached where the record type expects them
4. **Build the punch-list.** For each inspected record with at least one defect:

   | # | Date | Supervisor | Record ID | Missing / Defective | Priority |
   |---|---|---|---|---|---|
   | 1 | [date] | [name] | [record ID] | [list of failed checklist items] | [High/Medium/Low] |

   Priority: **High** if the narrative is missing or ≤10 words (narratives are the claims-critical field); **Medium** if workers or shift times are missing; **Low** if only weather or photos are missing. Where a record fails more than one check, list every defect but assign the single highest applicable priority.

   If the Step 10 proxy (or a prior targeted sweep this session) flagged double-bookings or
   duplicate entries, include those records in the punch-list too: `DOUBLE-BOOKING CANDIDATE`
   rows are **High** (they corrupt labour and timesheet data until resolved);
   `DUPLICATE-ENTRY CANDIDATE` rows are **Medium**. Both keep the candidate language — the
   punch-list action is "confirm which record is right in Gather", not "delete record X".
5. **Follow-up line per High item.** For each High-priority row, add one action sentence directly below the table, e.g.: "Ask [supervisor] to add the narrative for [date] — records are editable in Gather, not through this plugin."
6. **Close with the read-only reminder** (always include, do not modify):

   > This plugin is read-only — it cannot edit or fix records. Fixes happen in Gather. After remediation, re-run `$data-quality` for the same project and period and compare the new DQ ref against this one to confirm the gaps have closed.
