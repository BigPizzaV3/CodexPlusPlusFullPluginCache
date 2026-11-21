---
name: programme-compare
description: Rev-to-Rev comparison of imported programme revisions — date and duration
  movement, logic changes, float and TRA erosion per task, all read as stored from
  each revision (a diff of two already-computed schedules, no recompute).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Programme Revision Comparison (Ref RV-NNN)

Compares two already-imported programme revisions task-by-task — what moved, what changed
logically, and where stored float eroded — read entirely from each revision's own sidecar.
Follow the shared patterns: project
resolution (Pattern 1, `../../shared/patterns/01-project-resolution.md`), report numbering (Pattern 8, `../../shared/patterns/08-report-numbering.md`), and — read before starting —
**Pattern 15** (Programme Baseline, `../../shared/patterns/15-programme-baseline.md`), whose v2 revision-history convention
(`programme-baseline-<rev>.json`, versions indexed in `programme-baseline.md`) is exactly what
this skill diffs.

**Scope note:** this skill never runs the engine. Every figure in every table below is read
**STORED** from one revision's sidecar or the other — dates, total float, criticality, links,
constraints, all as the planning tool computed them at that revision's own data date. There is
no CPM recomputation anywhere in this skill, no what-if float, and no blending of two revisions'
numbers into a single recalculated figure. Say this once, in the summary, and let every table
that follows rely on it rather than repeating the caveat per row.

---

## Step 1: Resolve Project and Revisions

Resolve the project (Pattern 1). Then list the available revisions from the working folder's
`programme/` directory: every `programme-baseline-<rev>.json` sidecar plus the current
`programme-baseline.json` (the latest), cross-checked against the revision history indexed in
`programme-baseline.md` (Pattern 15 v2). Show the list — revision label, export/data date,
source format — before picking two.

- If the user named two revisions in `the user’s request`, use them.
- If not, default to **previous vs latest**. In a non-interactive run, state this as the
  assumption and continue rather than asking.
- **Both revisions must be the same project.** A sidecar whose provenance names a different
  project is excluded from the list (say so) — never diffed against.
- Fewer than two revisions on file → stop: there is nothing to compare yet, point at
  `$programme-import` to bring in the next revision.

---

## Step 2: Match Tasks Between Revisions

Build the matched-task set before diffing anything:

1. **Stable ID first** — match on the sidecar's own `id` (the export's task UID/task_code).
2. **Fall back to exact name match** where IDs don't carry across — the Asta caution from the
   import format notes applies directly here: Asta Powerproject renumbers task UIDs on every
   export, so two Asta-sourced revisions must be matched by exact task name, not ID. State which
   basis (ID or name) was used per matched pair, or once for the whole set if uniform.
3. **Never fuzzy-match.** No contains-matching, no similarity scoring — that's the
   `programme-import` activity-mapping method for a different problem (Gather↔programme), not
   this one (programme↔programme). An item that matches by neither ID nor exact name is
   unmatched.
4. List, separately and without editorialising:
   - **Added** — present in Rev B, unmatched in Rev A (a genuinely new task, or a renumbered
     one that also changed name — both look the same from here).
   - **Removed** — present in Rev A, unmatched in Rev B.

   Added/removed tasks are **findings, not errors** — a revision legitimately adds or drops
   scope. Do not describe an unmatched task as a data problem unless the user says otherwise.

---

## Step 3: The Diff — All Values as Stored

Restate once here: **every value below is read from its own revision's sidecar — this skill
never runs `scripts/cpm.py` and never recomputes anything.** Cite each side as "Rev [A/B label],
exported [date]" per Pattern 15's STORED citation form.

For each matched task, build:

| Task (ID / name) | Rev A start→finish | Rev B start→finish | Date movement | Duration Δ | Total float movement | Criticality |
|---|---|---|---|---|---|---|

- **Date movement**: Rev B's stored start/finish minus Rev A's. State the unit used. If both
  revisions' tasks share a calendar, state the movement in working days per that calendar. **If
  the calendars differ between the two revisions** (different `calendar_id`, or the same ID with
  a changed weekly pattern/exceptions in the two sidecars), a true working-day delta isn't
  comparable — fall back to a **calendar-day** approximation and say so on that row, not just
  once in the preamble.
- **Duration Δ**: `duration_hours` difference, converted to days with the divisor stated (as
  `programme-import` does — default 8 h/day unless a revision's calendar states otherwise).
- **Total float movement** (the float-erosion column, carried into Step 4): `stored.total_float_hours`
  difference between revisions, converted to days with the stated divisor.
- **Criticality**: Rev A's `stored.critical` vs Rev B's — flag flips (critical→non-critical or
  the reverse) explicitly; a flip on a task that also lost float is a Step 4 headline candidate.

**Logic changes** — diff each revision's `links` list (pred/succ/type/lag_hours) over the Step 2
matched-task set:

| Link (pred → succ) | Change | Rev A | Rev B |
|---|---|---|---|
| ... | added / removed / retyped (FS↔SS↔FF↔SF) / lag changed | ... | ... |

A link touching an unmatched (added/removed) task is reported under that task's own
added/removed line, not as a logic change in this table — it isn't a change to shared logic.

**Constraint changes**: compare each matched task's `constraint` object (`type`, `date`)
revision-to-revision — a constraint added, removed, retyped, or moved to a different date is its
own row; don't fold it into the date-movement row above (a constraint move can explain a date
move, but the two are reported separately so the reader sees the mechanism, not just the effect).

**Milestones and Key Dates** — highlight separately from ordinary tasks: any matched task with
`type: milestone`, plus anything the Pattern 15 md file's confirmed Key Date / Sectional
Completion typing carries for either revision. A milestone's date movement is a headline in its
own right regardless of float (milestones typically carry zero float by construction).

---

## Step 4: Float / TRA Erosion Headline

From Step 3's total-float-movement column, rank matched tasks by float **lost** (Rev B minus
Rev A, negative = erosion), worst first. This is the skill's headline output — the one table a
reader should see first if they see nothing else.

For each eroded task, where `programme/ce-register.md` exists and names a CE with a stated
date/window, check whether the task's float-loss window overlaps that CE's window and say so —
**"coincides with", never "caused by"**. No `ce-register.md`, or no overlapping CE — say plainly
that no cross-reference is available; do not force one.

Tasks with **no total float data in one or both revisions** (a field the export didn't carry, or
a manually-scheduled task per Pattern 15/`programme-import`'s own caution) are listed separately
as a gap, not scored as zero movement.

---

## Step 5: Present the Comparison

Apply Pattern 8 for the `RV-[NNN]` ref (session-local; increment on a prior `RV` ref, else 001).

```
PROGRAMME REVISION COMPARISON — [Project Name]
Ref: RV-[NNN]
Rev A: [revision label], exported [date] | Rev B: [revision label], exported [date]
Matching basis: [ID / exact name / mixed, stated per Step 2]

1. SUMMARY — what moved (headline count of date/duration/logic changes), worst float erosion
   (task + days lost), logic-change count, added/removed count. One paragraph.

2. TASK DIFF — the Step 3 table (date movement, duration Δ, float movement, criticality flips)

3. LOGIC CHANGES — the Step 3 links table (added/removed/retyped/lag-changed)

4. CONSTRAINT CHANGES — the Step 3 constraint table

5. MILESTONES & KEY DATES — highlighted separately per Step 3

6. FLOAT / TRA EROSION — the Step 4 ranked table, worst first, with any CE cross-reference
   ("coincides with CE-[NNN]'s window") or "no ce-register.md — no cross-reference available"

7. ADDED / REMOVED TASKS — the Step 2 lists (or "none" — a genuine finding, state it plainly)

8. FOR THE 31.3 ACCEPTANCE REVIEW — one line pointing at the Programme Advisor: float erosion
   and logic changes found here are exactly the kind of evidence the 31.3 realism grounds (TRA
   plausibility, Scope/Works Information compliance) turn on — hand this comparison to the
   Programme Advisor rather than assessing acceptance here.

9. GAPS — unmatched tasks from Step 2, revisions lacking float data from Step 4, any calendar
   mismatch that forced calendar-day approximation in Step 3.

Ref: RV-[NNN] is a session-local sequence number for cross-referencing (Pattern 8).
```

---

## Hard Rules

1. **Stored values only, both sides, cited per revision.** Every figure is "Rev [A/B], exported
   [date]" — never a blended or recalculated number (Pattern 15's STORED/INDICATIVE split; this
   skill only ever touches STORED).
2. **No engine runs, no recompute.** This skill never shells out to `scripts/cpm.py` and never
   derives a date, float value, or criticality flag that isn't already sitting in one of the two
   sidecars.
3. **ID-then-exact-name matching, never fuzzy-guessed.** An unmatched task stays unmatched and is
   reported as added/removed — it is never paired on a "looks similar" basis.
4. **Erosion language is movement of stored float, never causation.** A float-loss window that
   overlaps a CE's window "coincides with" it — this skill never asserts the CE caused the loss.
5. UK English throughout.

---

## Related Skills

- `$programme-import` — writes the revisions this skill diffs (Pattern 15 producer);
  run it first for a revision not yet on file
- `$programme-impact` — the indicative side: where this skill stops at "what changed
  between two stored revisions", `programme-impact` runs the engine for a what-if/63.5-style
  forward projection
- **Programme Advisor** agent — hands the Step 5 output to the 31.3 acceptance review and the
  broader programme health check (trigger: "is our programme compliant" / "baseline vs actual")
