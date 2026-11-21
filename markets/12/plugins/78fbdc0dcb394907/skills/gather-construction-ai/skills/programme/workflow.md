---
name: programme
description: Explicitly-invoked programme forecast — schedule-risk ranking, run-rate
  and earned-schedule (SPI(t)) forecast completion lenses. No critical path (no logic-link
  data from API). Not current-period output (use progress).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Programme

Analyse programme and milestone performance — planned vs actual progress, a **schedule-risk ranking** of activities most behind, and forecast completion dates based on current run rates.

**Scope note:** not a critical-path analysis. Per **Pattern 15** (`../../shared/patterns/15-programme-baseline.md`), the Gather API provides no baseline programme, logic links, or critical path — float and true critical-path status cannot be determined absent an imported baseline. Activities are ranked by *schedule risk* (variance and run-rate ratio), a proxy for — not a substitute for — critical-path impact. Invoked explicitly (`$programme`); for current-period output and productivity, use `$progress`.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

**Project resolution:** parse `the user’s request` for a project name; resolve via **Pattern 1** from `../../shared/patterns/01-project-resolution.md`; store the UUID and name for all subsequent calls.

**Date range:** parse via **Pattern 2** from `../../shared/patterns/02-date-range-parsing.md`. Default: last 4 weeks. Per Pattern 2, confirm only if interpretation was non-trivial (e.g. "I'll analyse programme performance for **[Project Name]** from **[start date]** to **[end date]**. Proceed?"); exact dates, named months, clearly stated periods proceed without confirmation.

---

## Step 2: Retrieve Progress Data

Call `getCachedReport` (report `dashboardProgress`, resolved project UUID, confirmed date range). Extract per activity/milestone: name/identifier, planned and actual output/progress to date (cumulative quantity or %), unit of measure, planned start/finish dates (if present), actual start date (first date with recorded output).

If no data, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. Progress data may not be configured for all projects — suggest the user check.

---

## Step 3: Retrieve Working Day Data

Call `getCachedReport` (report `dashboardShiftTable`, same project/dates). Extract: total shifts, number of working days (distinct dates with ≥1 shift), working pattern (5/6/7-day week), non-working days (no-shift dates, excluding weekends for a Mon-Fri project). Essential for run rates and completion forecasts.

---

## Step 4: Retrieve Access Impact Data

Call `getCachedReport` twice, same project/dates:
- **4a `dashboardAccessPossession`** — possessions granted, missed/cancelled, durations, timeliness.
- **4b `dashboardAccessOverview`** — access restrictions, no-access periods, reduced access, access windows.

**Purpose:** access data explains *why* progress may be behind programme — a project that lost 5 working days to access restrictions is not judged the same as one with full access that underperformed.

If either report returns no data: "No access/possession data available — analysis will proceed without access impact adjustment."

---

## Step 5: Analyse Each Activity / Milestone

For each activity or milestone identified in the progress data (Step 2), calculate:

### 5a: Variance Analysis

| Field | Calculation |
|---|---|
| **Planned Progress to Date** | Cumulative planned quantity/% from `dashboardProgress` |
| **Actual Progress to Date** | Cumulative actual quantity/% from `dashboardProgress` |
| **Variance (Quantity)** | Actual - Planned (positive = ahead, negative = behind) |
| **Variance (%)** | (Actual - Planned) / Planned * 100. If Planned = 0, render as "n/a" with a data-quality flag — never a number (Pattern 12 divide-by-zero convention) |
| **Status** | Ahead (variance > +5%), On Track (-5% to +5%), Behind (variance < -5%), Significantly Behind (variance < -20%) |

### 5b: Run Rate Analysis

| Field | Calculation |
|---|---|
| **Current Run Rate** | Actual output achieved in the period / working days in the period (from Step 3). If working days = 0, render as "n/a" with a data-quality flag (Pattern 12) |
| **Required Run Rate** | Remaining output to complete / remaining working days to planned finish date. **Only computable if a planned finish date is present** (the API provides no baseline programme) — otherwise render "—" and state it is unavailable per Pattern 12 |
| **Run Rate Ratio** | Current run rate / required run rate (>1.0 = on track to finish early, <1.0 = will overrun at current pace). If required run rate is 0 or unavailable, render as "n/a" with a data-quality flag — never a number (Pattern 12) |

### 5c: Forecast Completion

Forecasts anchor to the **data cut-off date** — the `to` date, the last date output is known — **not** today (anchoring to today would silently assume zero progress between cut-off and run date).

Produce **two scenarios** rather than a single point estimate:

| Field | Calculation |
|---|---|
| **Total Scope** | Total planned quantity (if available) |
| **Remaining Work** | Total scope - actual progress to date |
| **Current Run Rate** | From Step 5b (output over the period / working days) |
| **Best Sustained Rate** | The highest rate the project has demonstrably sustained — e.g. the best single week in the period if weekly data is available. If only an aggregate figure is available, state that the two scenarios collapse to one (best sustained rate = current rate) and say so. |
| **Working Days to Complete (Scenario A — current rate)** | Remaining work / current run rate |
| **Working Days to Complete (Scenario B — best sustained rate)** | Remaining work / best sustained rate |
| **Forecast Completion — Scenario A** | Data cut-off date + Scenario A working days (skipping non-working days per the observed working pattern from Step 3) |
| **Forecast Completion — Scenario B** | Data cut-off date + Scenario B working days (same skipping rule) |
| **Planned Completion Date** | From the planned schedule (if available) |
| **Forecast vs Plan** | Each scenario's forecast completion − planned completion (positive = late, negative = early) |

Present Scenario A as the central case and Scenario B as the best-achievable case — a forecast **range**, not false precision.

If total scope is unavailable, forecast completion cannot be calculated — present only run rate and variance analysis.

**Divide-by-zero guard (Pattern 12):** if current run rate is 0 (no output in the period), working days to complete is undefined — render "n/a" with a data-quality flag and state "no output recorded in the period, so a completion date cannot be forecast", never a number or an infinite date.

**Programme baseline (Pattern 15):** before relying solely on the API's planned finish dates, check for `programme/programme-baseline.md` per **Pattern 15** (`../../shared/patterns/15-programme-baseline.md`).

- **Exists and project matches:** for activities/milestones with a user-confirmed mapping (rule 3) to a baseline task, compare run-rate forecast dates (Scenarios A/B) against the **imported planned milestone dates**; report the variance in working days, citing "per the imported programme ([revision], exported [date])."
- Criticality for mapped items is now available — **exactly as stored in the export at its data date, never recomputed** (rule 2) — state the date. This supplements, not replaces, Step 6's schedule-risk ranking.
- Unmapped items keep the run-rate-only treatment.
- **Absent:** the "no critical path from the API" caveat stands — state the limitation and point to `$programme-import`.

### 5d: Earned-Schedule Extrapolation (Third Forecast Lens)

A third forecast lens, alongside Scenarios A/B — trend-based (SPI(t)), not critical-path, computable only for activities with a confirmed Pattern 15 baseline mapping. Read `references/earned-schedule.md` for the calculation (PD, Elapsed, ES(t), SPI(t), forecast duration/completion) and the never-average rule for presenting all three lenses side by side in Step 8.


## Step 6: Rank Activities by Schedule Risk

Rank all activities by variance (Step 5a), most behind to most ahead. This is a **schedule-risk ranking**, not a critical-path assessment (Pattern 15 — see Scope note). Flag:

1. **Significantly behind** (variance < -20%): highest schedule-risk drivers (potential, unconfirmed, critical-path impact).
2. **Behind** (variance < -5%): requires monitoring.
3. **On track** (-5% to +5%): performing as planned.
4. **Ahead** (variance > +5%): capacity to absorb future delays.

For each "Significantly behind"/"Behind" activity, note quantity behind programme, working days of delay (shortfall / current run rate), and current vs required run rate.

---

## Step 7: Cross-Reference with Access Restrictions

For activities behind programme (Step 6), cross-reference with access data (Step 4):

1. Identify access restrictions, missed possessions, or cancellations coinciding with the period.
2. Calculate **working days lost to access issues**. Access impact is recorded in possession *hours*; convert using the **median shift duration for the period** (Step 3) as divisor — e.g. 24 possession-hours ÷ 10-hour median shift ≈ 2.4 working days. **Always state the divisor used** (mirrors Pattern 11's hours→days rule).
3. Compare access impact against the delay — an association, not proven causal apportionment:
   - Lost ≥ behind → "The delay is **consistent with** access restrictions — recorded loss is at least as large as the shortfall, though this does not by itself prove access is the sole cause."
   - Lost < behind → "Access restrictions are **consistent with** [N] of [M] days of delay — the remaining [M-N] days are associated with other causes."
   - None → "No access restrictions recorded — the delay is associated with other causes."

Commercially significant: access-caused delay may carry different contractual implications than productivity shortfall. Causation (vs consistency) requires a formal delay analysis — `$delay-analysis`.

---


## Step 8: Present the Programme Health Summary

Read `references/output-template.md` for the exact report structure (Headline, Programme Status, Activity Breakdown, Activities at Risk, Access Impact, Run Rate Analysis, Forecast Summary — three lenses never averaged, Caveats). Fill every placeholder with data; do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** for the `Ref: PM-[NNN]` line.

---

## Related Skills

After presenting the programme analysis, suggest these related skills for deeper investigation:

- `$progress` — Detailed progress data review with daily/weekly output trends, including the full period-by-period S-curve and earned-schedule table
- `$programme-impact` — Logic-driven (CPM) impact assessment where the earned-schedule trend needs a critical-path answer
- `$access` — Deep-dive into access and possession data, including timeliness and restriction patterns
- `$delay-analysis` — Formal delay analysis identifying causes and responsibility for delays
- `$estimator` — Derive actual unit rates from the progress and labour data to validate run rates
- `$commercial-report` — Full commercial report incorporating programme status alongside labour, plant, and cost data
- `$programme-import` — Import an MS Project/P6 baseline to compare forecasts against imported planned milestones, with criticality as stored (Pattern 15)
