## submission-pack-32-2

**Cadence:** Monthly, {{REVISION_DUE_DATE}} minus 3–4 days (the clause 32.2 interval per the contract profile)
**Surface:** Desktop
**Prerequisites:** `programme/programme-baseline.json` current; `contract-profile.md` (the as-amended 32.2 interval and required programme contents); `{{FOLDER}}/routine-state/submission-pack-32-2/last-run.md`
**Priority:** Standard

**Instructions:**
```
Run the Programme Advisor's 32.2 Submission Pack (Mode 5) for {{PROJECT}} covering the period
since the date in routine-state/submission-pack-32-2/last-run.md: progress narrative per
mapped activity from the records, dormancy evidence, the CE schedule with planned-Completion
effects (cross-referenced to any ce-quotation movement run this period), the TRA statement
from STORED values, and possession commentary where tagged.

Alongside the narrative, emit the machine-readable actuals table and — where the round-trip
writer is available — the actuals update file (write_mspdi.py --actuals-only) so the planner
imports the month's progress instead of re-keying it. State, as always, that the reschedule
itself happens in the planning tool.

Save the pack to {{FOLDER}}/32-2-pack-[period-end].md and update
routine-state/submission-pack-32-2/last-run.md with the period end. Everything in the pack
cites its record or its STORED source; nothing is recomputed.
```
