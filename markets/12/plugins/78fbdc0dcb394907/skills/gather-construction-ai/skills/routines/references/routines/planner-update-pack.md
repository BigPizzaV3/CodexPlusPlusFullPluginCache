## planner-update-pack

**Cadence:** Monthly, {{REVISION_DUE_DATE}} minus 2–3 days (before each programme revision)
**Surface:** Desktop
**Prerequisites:** `programme/programme-baseline.md` with a confirmed activity mapping; `{{FOLDER}}/routine-state/planner-update-pack/last-run.md`
**Priority:** Standard

**Instructions:**
```
Period = since the imported baseline's data date, or since the period end recorded in
{{FOLDER}}/routine-state/planner-update-pack/last-run.md — whichever is later.

Run the Programme Advisor update pack (Mode 3) for {{PROJECT}}: the task-level change table
— programme task ID and name | actual start | actual finish | % complete (with derivation) |
evidence reference — over the user-confirmed mapping only. List separately: Gather activities
with recorded work but no mapped task (candidates to add), and mapped tasks with no recorded
work in the period (for the planner to confirm dormant or re-sequence).

Save the table to {{FOLDER}}/planner-update-[period-end].md and reply with the headline
counts plus anything the planner must decide. Applying the changes and rescheduling happens
in Project/P6/Asta — this pack is the input, and says so.
Update routine-state/planner-update-pack/last-run.md with the period end covered.
```
