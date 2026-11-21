---
name: asbuilt-programme
description: Reconstructs the as-built programme — actual start/finish/active/dormant
  per activity — for EOT/claims (as-planned vs as-built). Chat, Mermaid, HTML Gantt
  and time-chainage (linear works) outputs. Not forecasts (programme) or current-period
  output (progress).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# As-Built Programme

An as-built programme reconstructs, from recorded data, when each activity **actually** started, finished, was active, and stood dormant — not a forecast of when it will finish. As-planned vs as-built comparison is a core recognised delay-analysis method, and a reliable as-built record is often the first thing a claim or EOT submission needs.

**Scope note:** reconstructs *timing* only — actual start, finish, activity, dormancy — from `dashboardProgress` records. Not forecasting/schedule-risk (use `$programme`), not current-period output/variance/productivity (use `$progress`), and not delay causation or entitlement — it produces the timing evidence `$delay-analysis` and the Time & Claims Advisor build on.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

**Project resolution:**

1. Parse `the user’s request` for a project name and an optional date range.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Date range — documented exception to the Pattern 2 default:**

An as-built reconstruction needs an activity's full history to establish a true start and finish. Unlike other skills in this plugin, **default the date range to project start (earliest `dashboardProgress` date) through today**, not the last 4 weeks. If the user supplies an explicit range, use it and note that any activity starting before the range began shows as "already in progress at range start", not a true as-built start.

1. Parse any date range from `the user’s request` using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`, applying the full-history default above in place of Pattern 2's 4-week default.
2. Per Pattern 2's confirmation rule, confirm the interpreted range with the user only if the input required non-trivial interpretation (e.g. an ambiguous relative phrase, or the user asking for "the whole project" when the true earliest data date is uncertain). A clearly stated range or an unambiguous "since project start" proceeds without confirmation.

---

## Step 2: Verify Data Granularity Before Reconstructing Timing

Reconstruction is only possible if `dashboardProgress` carries a **date** per row, not just an aggregate total. Verify before any date-based work (**Pattern 12**):

1. Call `getReportSchemas` (or inspect the first response) to confirm rows are per-date, per-activity (date, activity, unit, plannedQuantity, actualQuantity).
2. **Date-granular confirmed** → proceed to Step 3 with the full reconstruction.
3. **Aggregate-only** (single cumulative total per activity, no per-date rows) → degrade explicitly:
   - State plainly: "Actual start/finish/dormancy timing cannot be reconstructed — `dashboardProgress` returns aggregate totals only, no per-date breakdown."
   - Fall back to **narrative-based reconstruction**: scan `dashboardNarrative` for the first and last dated mention of each activity (Pattern 10 keyword categories) as proxy start/finish dates.
   - Label every such date, duration, and dormancy figure **LOW confidence** throughout the output and in Caveats — never at the same confidence as progress-derived dates.

---

## Step 3: Retrieve Data

### 3a: Progress Data

Call `getCachedReport` with **Report:** `dashboardProgress`, the resolved project UUID, and the full date range from Step 1. Per **Pattern 4**, chunk ranges longer than about a month **month by month** and merge, rather than one call for the whole history.

**Extract per row:** date, activity, unit, planned quantity, actual quantity.

### 3b: Working Days

Call `getCachedReport` with **Report:** `dashboardShiftTable` for the same range. Extract working days and the working pattern (5/6/7-day week) — needed to convert calendar days to working days and to size the Step 4 dormancy threshold.

### 3c: Narrative and Access Context

Call `getCachedReport` with **Report:** `dashboardNarrative` and `dashboardAccessPossession` for the same range — not used for timing itself, they feed the Step 5 dormancy annotation.

Any report returning no data → **Pattern 3 (Empty Data Handling)**: state which was empty, likely causes, and which downstream section (dormancy annotation, working-day conversion) is affected.

---

## Step 4: Reconstruct Per-Activity As-Built Timing

For each activity found in the progress data (Step 3a), calculate:

| Field | Calculation |
|---|---|
| **As-Built Start** | First date with recorded actual output > 0. **Caveat:** accurate only to the recording interval — weekly-entered progress can hide a true start up to a week earlier. |
| **Cumulative Actual / Planned** | Sum actualQuantity and plannedQuantity across **every row for the activity in the full range** — no sampling/estimating; a mis-summed total silently flips the status below. Show both totals as output columns so the arithmetic is checkable. If the plan series only carries worked-day rows, note the planned total may understate the full plan. |
| **As-Built Finish / Status** | Cumulative actual ≥ planned → **Complete**, finish = last date with recorded output. Actual < planned (or no planned total to compare) → **Ongoing at data cut-off**, finish blank. |
| **Active Days** | Count of distinct dates with actual output > 0. |
| **Elapsed (Calendar) Days** | As-built start to finish (or data cut-off if ongoing). |
| **Elapsed (Working) Days** | Same span converted using the Step 3b working-day pattern. |
| **Dormant Days** | Sum of the length of all dormant windows (below). |

**Dormant windows:** any gap of **more than 5 working days** with zero recorded output, between as-built start and finish (or data cut-off if ongoing). State the 5-working-day threshold in the output as an overridable assumption. Record each window's start, end, and length in working days.

**Guards (Pattern 12):** no planned total → status defaults to "Ongoing" (never guess Complete), noted. Zero active days across the range → "no recorded output in period", not a computed start/finish from nothing.

---

## Step 5: Annotate Dormancy with Evidence, Not Causation

For every dormant window from Step 4, look for corroborating evidence — but **never assert the gap was caused by** anything found. Use **"coincides with"** throughout, never "caused by"/"due to":

1. Scan `dashboardNarrative` inside the window's span (**Pattern 10** keyword categories: access/possession, instructions/changes, standing/delay, physical conditions, third party, information, weather).
2. Scan `dashboardAccessPossession` for any access restriction or missed/cancelled possession overlapping the window.
3. State each candidate as "coincides with [category] — [brief evidence]" and rate confidence:
   - **HIGH** — direct, specific corroboration (e.g. a named restriction spanning the full window, repeated narrative entries naming the activity).
   - **MEDIUM** — partial overlap or indirect corroboration.
   - **LOW** — a weak/generic keyword hit (Pattern 10 false-positive rule: discard routine-operation matches, keep prevented/disrupted/changed work).
4. No overlapping evidence at all → **"no recorded explanation"** — a data-quality finding to surface, not to paper over with a guess.

---

## Step 6: As-Planned vs As-Built Comparison (Conditional)

**Gated on data availability (Pattern 12):** only possible if planned/baseline start and finish **dates** (not just quantities) exist in the retrieved data.

- **Planned dates present** → present planned vs as-built start/finish and variance in working days per activity, using Step 4's Complete/Ongoing status logic.
- **Planned dates absent** (the normal case) → **omit this section entirely**: "As-planned vs as-built comparison is not available — the data provides planned quantities but no planned start/finish dates. Reconstructing planned dates from planned quantities would be a fabrication and is not attempted." Never infer a planned date from a quantity or run rate.

**Programme baseline (Pattern 15):** before the omission above, check `programme/programme-baseline.md` (`../../shared/patterns/15-programme-baseline.md`). If it exists and its project matches:

- Produce the comparison from the baseline's planned start/finish, **only for activities with a user-confirmed mapping** (Pattern 15 rule 3) — never guess a mapping. Variance in working days, same status logic as Step 4.
- Flag each mapped activity's criticality **exactly as stored in the import at its data date** — never recompute CPM (Pattern 15 rule 2). Cite every baseline-sourced row: "per the imported programme ([revision], exported [date])."
- Unmapped activities stay reconstruction-only — the no-fabricated-planned-dates guardrail still applies.
- File absent or project mismatch → the omission above stands: state the limitation, point to `$programme-import`.

**Method labelling:** when this section runs, the Method line reads "As-Planned vs As-Built comparison (SCL Protocol family, simplified — single whole-period comparison, not windowed; criticality as stored in the imported programme)". The windowed variant needs a CPM engine this plugin does not run, and is labelled separately if offered.

---


## Step 7: Present the As-Built Programme (Chat + Mermaid)

Read `references/render-chat.md` for the exact report structure (Summary, Activity Table, Timeline cards, Dormancy Register, As-Planned vs As-Built comparison, Caveats block, and the closing Mermaid Gantt chart). Apply **Pattern 8 (Report Numbering)** for the `Ref: AB-[NNN]` line. Fill every placeholder with real data; do not add, remove, or reorder sections.

---

## Step 8: Shareable HTML Gantt (Generated by Default)

Generated automatically after Step 7 whenever the full per-date reconstruction ran (skip only for an explicit chat-only request, a user decline, or the Step 2 narrative-based fallback). Read `references/render-gantt.md` for the data schema, template markers, output filename, and fallback behaviour.

---

## Step 9: Time-Chainage Output (Offered for Linear Works)

Offer for linear/chainage-based work (rail, pipeline, tunnel, road, viaduct/bridge deck) or on request; skip unasked for non-linear projects. Read `references/render-time-chainage.md` for chainage-source resolution (never guessed — imported baseline per Pattern 15, user-confirmed task-name/WBS pattern, or user-pasted map), the planned/as-built banding rules, the data schema, and fallback behaviour.

---

## Related Skills

- `$delay-analysis` — feed the dormancy windows into the master delay register for causation/entitlement
- `$measured-mile` — use as-built timing to select un-impacted vs impacted baseline periods
- `$programme` — forward-looking counterpart: forecasts and schedule-risk ranking
- `$narrative-search` — dig into a specific dormant window
- `$data-quality` — check whether recording gaps undermine confidence in this reconstruction
- `$programme-import` — import an MS Project/P6 baseline for a genuine comparison (Pattern 15)
