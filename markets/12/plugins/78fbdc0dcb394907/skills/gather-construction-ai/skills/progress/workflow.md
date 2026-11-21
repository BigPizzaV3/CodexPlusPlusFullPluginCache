---
name: progress
description: Tracks current-period progress — planned vs actual output, cumulative
  S-curves, earned-schedule SPI(t), productivity trends, run rate. Not forecasting
  (use programme) or as-built reconstruction (use asbuilt-programme).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Progress Tracking and Productivity Analysis

Track project progress against planned targets — planned vs actual output, run rates, productivity per labour hour, and identification of activities falling behind. This skill helps answer "are we on track?" and "where are we losing ground?"

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

**Project resolution:**

1. Parse `the user’s request` for a project name and optional date range.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Date range resolution:**

1. Parse any date range from `the user’s request` using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no date range is specified, default to the **last 4 weeks** (today minus 28 days to today).
3. If the input is ambiguous, confirm with the user before proceeding.
4. Calculate the **span in days** in the range. The number of **working days** is confirmed from shift records in Step 4 — do not guess it from the calendar here.

---

## Step 2: Retrieve Progress Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardProgress`
- **Project:** the resolved project UUID
- **Date range:** the resolved `from` and `to` dates

If the report returns no data, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. State clearly that no progress data was found, suggest possible causes (progress not being recorded, wrong date range, report not configured in Gather), and offer to retry.

**Feasibility note:** The depth of analysis depends on what `dashboardProgress` contains. If the report provides per-activity quantities and planned targets, the full analysis below is possible. If it only provides high-level percentages or summary figures, report those clearly and note the limitation: "Progress data for this project is reported at summary level only. Per-activity breakdown is not available from the current dashboard configuration."

---

## Step 3: Retrieve Labour Data for Productivity Calculations

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

This provides the labour hours needed to calculate productivity rates (output per labour hour). If this report returns no data, note that productivity rates cannot be calculated and proceed with progress data alone.

Optionally, also call `getCachedReport` with `dashboardAllocation` for the same range — if it carries planned hours per activity, those feed the labour-hour weighting in Step 6. Skip silently if the report is unavailable.

---

## Step 4: Retrieve Working Day Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardShiftTable`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

**Extract:**
- Total shifts recorded in the period
- Number of **working days** (distinct dates with at least one shift)
- Working days per week (to understand the working pattern — 5-day, 6-day, 7-day)

Use the **actual working days** from this report as the denominator for all run-rate (output per working day) calculations. Do **not** infer working days from a calendar guess. If this report returns no data, fall back to counting calendar days in the range and state explicitly: "Working days could not be confirmed from shift records — run rates are calculated against calendar days and may be understated."

---

## Step 5: Analyse Per-Activity Progress

For each activity or work item in the progress data:

| Field | Calculation |
|---|---|
| **Activity** | Name/description of the activity |
| **Unit** | Unit of measurement (e.g., metres, m2, tonnes, nr) |
| **Planned Qty** | Target output for this period |
| **Actual Qty** | Recorded output for this period |
| **Variance** | Actual minus Planned (positive = ahead, negative = behind) |
| **Variance %** | (Variance / Planned) x 100. If Planned = 0, render as "n/a" with a data-quality flag — never as a number (Pattern 12 divide-by-zero convention) |
| **Status** | Ahead (>5%), On Track (-5% to +5%), Behind (<-5%), or Critical (<-20%) |
| **Run Rate** | Actual Qty divided by **working days from Step 4** = output per working day |
| **Required Rate** | See gating note below — compute only if a planned finish date is present |

Sort the activity table by **Status** — Critical first, then Behind, then On Track, then Ahead.

**Required Rate gating (Pattern 12):** The required daily rate to recover to plan depends on the *remaining programme duration*, which requires a **planned finish date**. The Gather API does not provide baseline programme/Gantt data. Therefore:
- If the progress data for the activity includes a planned finish date → compute Required Rate = remaining quantity / remaining working days to that date.
- If no planned finish date is present → show "—" for Required Rate and state once in the output: "Required Rate is unavailable — the API does not provide planned finish dates, so remaining programme duration cannot be determined (Pattern 12)."

If activity-level data is not available, work with whatever level of detail the progress report provides and state the limitation.

---

## Step 6: Calculate Overall Metrics

Compute summary statistics across all activities:

| Metric | Value |
|---|---|
| **Total Activities** | [count of activities tracked] |
| **On Track or Ahead** | [count] ([percentage]%) |
| **Behind Schedule** | [count] ([percentage]%) |
| **Critical (>20% behind)** | [count] ([percentage]%) |
| **Weighted Progress %** | [see calculation below] |
| **Date Range** | [from] to [to] |

**Weighted progress %:** Choose the weighting basis in this order of preference — do **not** sum quantities across different units (metres + tonnes + nr is dimensionally meaningless):

1. **Labour-hour weighting (default):** If labour hours per activity are available (from the Step 3 labour data, or `dashboardAllocation` planned hours where present), weight each activity by its share of total labour hours:
   - weight = (labour hours for this activity / total labour hours across all activities)
   - Weighted progress = sum of (actual completion % x weight) for all activities.
2. **Single-unit quantity weighting:** Only if **all** activities share one common unit, weight by planned quantity share (planned qty for this activity / total planned qty) — summing quantities is valid only when the units are identical.
3. **Unweighted average (fallback):** If neither labour hours nor a single common unit is available, use a simple average of completion percentages and state: "This is an unweighted average — activities could not be weighted because labour allocation is not available and activities use mixed units."

State which basis was used in the output.

---

## Step 7: S-Curve — Cumulative Progress and Earned Schedule

At Step 7, read `references/earned-schedule.md` for the
full 7a/7b/7c method: the cumulative PLANNED curve (Pattern 15 baseline mapping, STORED dates
only, linear phasing assumption, degrade-if-absent rule), the cumulative ACTUAL curve (same
weighting basis as Step 6, single blended curve for mixed units), and the Earned Schedule read
(ES(t)/Elapsed/SPI(t) — no engine, no critical-path logic — standing "trend indicator, not
critical-path" caveat pointing to `$programme-impact`).

---

## Step 8: Calculate Productivity Rates

If labour data from Step 3 is available, calculate productivity for each activity:

| Activity | Output | Labour Hours | Productivity | Unit |
|---|---|---|---|---|
| [activity name] | [actual qty] | [hours allocated to this activity, if available] | [qty / hours] | [unit]/hr |

**Important:** Labour data may not be broken down by activity. In this case:
- Calculate **overall productivity** = total output (if a single primary activity) / total labour hours
- State: "Labour hours are not broken down by activity. Overall productivity rate is calculated against total labour hours — this is a blended rate across all activities."
- If there are multiple activities with different units, do not calculate an overall rate — it would be meaningless. Instead, note: "Productivity per activity cannot be calculated because labour is not allocated to individual activities in the data."

---

## Step 9: Identify Concerns

Flag the following automatically:

### Critical Concerns
- **Zero progress activities:** Any activity with zero actual output for the entire period — flag as "No recorded progress on [activity] for [N] days"
- **Critical deficit:** Any activity more than 20% behind planned — flag with the variance and what recovery rate would be needed

### Warnings

The run-rate-trend warnings below cannot fire from the single aggregate `dashboardProgress` call in Step 2 — one aggregate figure has no trend. To assess them, **split the analysed range at its midpoint and make two additional `getCachedReport` (`dashboardProgress`) calls** — one for the first half, one for the second — then compare per-activity run rates between the two halves. Only do this when each half contains at least ~5 working days; otherwise skip these two warnings and state: "Run-rate trend not assessed — the period is too short to split into two comparable halves."

- **Declining run rates:** Flag any activity whose run rate in the second half is materially lower than the first half (e.g. a drop of more than 20%).
- **Stalled activities:** Flag any activity with recorded progress in the first half but zero output in the second half.
- **Unrealistic recovery:** Only where a Required Rate could be computed (planned finish date present — see Step 5), flag any behind-schedule activity whose required recovery rate exceeds 2x the current run rate as "Recovery may require additional resources or programme revision".

If no concerns are identified, state: "No progress concerns detected — all tracked activities are on or ahead of plan."

---

## Step 10: Present Results

Read `references/output-template.md` for the exact report structure (Summary, Overall Assessment, Activity Breakdown, Cumulative Progress S-Curve and Earned Schedule — keep the midpoint trend-split gating from Step 9, Productivity, Concerns, Caveats). Fill every placeholder with data; do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** for the `Ref: PG-[NNN]` line.

---

---

## Related Skills

After presenting the analysis, suggest these related skills:

- `$estimator` — Derive detailed labour-hour unit rates (hrs/unit) from actual progress and labour data
- `$programme` — Forecast milestone completion dates based on current run rates, including the earned-schedule extrapolation
- `$labour` — Detailed labour hours breakdown to understand resourcing behind the progress figures
- `$programme-impact` — Logic-driven (CPM) impact assessment where the earned-schedule trend needs a critical-path answer
