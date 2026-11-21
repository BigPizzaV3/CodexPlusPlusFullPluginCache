## monthly-cvr

**Cadence:** Monthly, {{LEDGER_DAY}} — the day after the accounting-system period export normally lands
**Surface:** Desktop
**Prerequisites:** `commercial-profile.md` (Pattern 14); `{{FOLDER}}/ledgers/` drop folder for the cost-ledger CSV; `{{FOLDER}}/routine-state/monthly-cvr/last-run.md`
**Priority:** Standard

**Instructions:**
```
Check {{FOLDER}}/ledgers/ for a cost-ledger CSV added or modified since the date recorded in
{{FOLDER}}/routine-state/monthly-cvr/last-run.md.

If there is none: reply in two lines ("No new cost ledger since [date] — no CVR built; drop
the [month] export into {{FOLDER}}/ledgers/ and rerun") and stop. Never build a CVR from a
stale ledger without saying so.

Otherwise run $cost-import for {{PROJECT}} against the newest file — where the column
semantics and head mapping match what commercial/cost-ledger.md recorded from earlier imports,
restate them as assumptions rather than re-asking — then $cvr for {{PROJECT}} for the
period the ledger itself covers (its period-to date, never the run date). The previous CVR
position is the one recorded in routine-state from last month's run — cite it.

Lead the reply with margin and margin movement, then any UNEXPLAINED movement (that is the
line a commercial manager acts on), then gaps. For accruals, liabilities, and provisions:
list last month's user-supplied adjustments and ask whether they still stand — never roll
them forward silently, and never invent one.

Update routine-state/monthly-cvr/last-run.md with the file imported, the period end, and the
closing value/cost/margin position (next month's movement line reads from it).
This output is internal — the cost side is never issued to the other party.
```
