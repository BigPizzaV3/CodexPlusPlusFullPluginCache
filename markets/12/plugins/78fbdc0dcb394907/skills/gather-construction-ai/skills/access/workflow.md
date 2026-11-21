---
name: access
description: 'Analyses possession and access records — planned vs actual windows,
  restrictions, timeliness. Triggers: access, possession, site entry, access delays.'
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Access and Possession Analysis

Analyse possession and access records for a Gather project — planned vs actual windows, late handovers, early handbacks, net lost time, and trend analysis. Access delays are among the most common compensation events on rail and infrastructure projects, and this skill quantifies their impact for contractual purposes.

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

---

## Step 2: Retrieve Access Data

Call `getCachedReport` for the resolved project UUID and the resolved `from`/`to` dates for each
report below (all take the same project/date-range parameters):

| Report | Provides | If empty |
|---|---|---|
| `dashboardAccessOverview` | High-level summary — total possessions, overall compliance %, total planned/actual hours | Follow **Pattern 3 (Empty Data Handling)** (`../../shared/patterns/03-empty-data-handling.md`); note that access/possession tracking may not be configured, or none were recorded in the period |
| `dashboardAccessPossession` | Individual possession records with planned and actual times | — (feeds Step 3) |
| `dashboardAccessNonPossession` | Non-possession access: site entry windows, red zone access, other restricted access that is not a formal possession | Note this and proceed with possession data only |

---

## Step 3: Analyse Each Possession

**Schema check first (Pattern 12** — `../../shared/patterns/12-schema-verification.md`): the per-possession calculations below need individual timestamps, so verify `dashboardAccessPossession` returns them for this workspace before relying on any row; if it returns aggregate-only figures, degrade per Pattern 12 — skip the per-possession table and late-start/early-handback/overrun breakdown, compute only the supported aggregates, and state "Per-possession timestamps are not available for this workspace — only aggregate access metrics are reported; late-start/overrun analysis was downgraded."

For each possession record from Step 2 (where per-possession timestamps are available), calculate the following:

| Field | Calculation |
|---|---|
| **Date** | Date of the possession |
| **Location** | Location/section identifier if available |
| **Planned Start** | The scheduled start time of the possession |
| **Actual Start** | The actual start time (when access was granted) |
| **Late Handover** | Actual Start minus Planned Start (positive = late start; zero or negative = on time or early). Lost time — never negative for this metric; clamp early starts to 0. |
| **Planned End** | The scheduled end time of the possession |
| **Actual End** | The actual end time (when access was handed back) |
| **Early Handback** | Planned End minus Actual End, **only when positive** (handed back early = lost time). If negative, it is an **overrun** — record it separately as Overrun Hours, not as negative lost time. |
| **Overrun Hours** | Actual End minus Planned End when positive (possession handed back **late** / ran beyond the planned window). Reported separately — an overrun is not a saving and must not offset a late start. |
| **Planned Duration** | Planned End minus Planned Start (in hours and minutes) |
| **Actual Duration** | Actual End minus Actual Start (in hours and minutes) |
| **Lost Time (late start + early handback)** | Late Handover + Early Handback, **each clamped at ≥ 0** — the time lost from the planned window at the start and end. **Report late start and early handback separately in the table; do not net an overrun against a late start.** On sequenced rail work a recovered end-time rarely compensates a lost start-time (different crews/activities), so an overrun must not be subtracted from Lost Time. Flag any possession that both started late **and** overran. |
| **Status** | Full (no lost time), Partial (some lost time), Missed (zero or near-zero actual duration), or Overrun (ran beyond the planned window) |

Present the possession table sorted by **date**, with Lost Time highlighted for any possession where time was lost and Overrun Hours shown in a separate column.

---

## Step 4: Quantify Labour Impact

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

Cross-reference labour data with possession delays to quantify the standing time impact:

1. For each possession with a late handover or early handback, identify the labour hours recorded on that date.
2. Estimate standing time: If a possession started 30 minutes late and there were 15 workers on site that day, the standing time impact is approximately 15 x 0.5 = 7.5 person-hours.
3. Calculate total estimated standing time across all affected possessions.

**Important caveats:**
- **Crew attribution:** the daily headcount from `dashboardResourceLabour` is the whole day's labour — it may span **multiple shifts and multiple possessions**. Do **not** assume the entire daily headcount was standing for one possession. Attribute crew to a possession's standing time **only where shift-level data confirms which operatives were on that possession** (verify per **Pattern 12** whether shift/possession-level headcount is available). Where it is not, state the crew figure is the day total and the estimate is an **upper bound**, or apportion explicitly and say how.
- This is an estimate. Actual standing time depends on whether workers could be redeployed to other tasks during the delay.
- State clearly: "Estimated standing time assumes workers could not be productively redeployed during access delays, and — where shift-level attribution is unavailable — that the day's headcount relates to the affected possession. Actual impact may be lower if alternative work was available or if labour was split across other shifts/possessions."
- If labour data is not available or cannot be matched to specific dates, skip this calculation and note: "Labour impact could not be quantified — labour data is not available for cross-referencing."

---

## Step 5: Aggregate Statistics

Compute summary statistics across all possessions in the period:

| Metric | Value |
|---|---|
| **Total Possessions** | [count of possession records] |
| **Possessions with Full Access** | [count with no lost time] ([%]) |
| **Possessions Affected** | [count with any lost time] ([%]) |
| **Possessions Missed** | [count with zero/near-zero actual duration] ([%]) |
| **Total Planned Hours** | [sum of all planned durations] |
| **Total Actual Hours** | [sum of all actual durations] |
| **Total Lost Hours** | [sum of Lost Time (late start + early handback), each clamped ≥ 0] |
| **Total Overrun Hours** | [sum of Overrun Hours — possessions handed back late] |
| **Access Efficiency** | [Total Actual / Total Planned] x 100% — render "n/a" with a data-quality flag if Total Planned = 0 (Pattern 12); see note |
| **Average Late Handover** | [mean late handover time across affected possessions] |
| **Worst Late Handover** | [maximum late handover] on [date] |
| **Average Early Handback** | [mean early handback across affected possessions] |
| **Worst Early Handback** | [maximum early handback] on [date] |
| **Est. Standing Time** | [from Step 4, if available] person-hours |
| **Date Range** | [from] to [to] |

**Access Efficiency > 100% is not "good".** Because actual duration can exceed planned duration when possessions overrun, this ratio can exceed 100% — that indicates an **overrun regime** (possessions consuming more than the planned window), **not** high performance. Do not let it mask lost start-time. When efficiency > 100%, report it explicitly as ">100% — overrun regime" and lead on Total Lost Hours and Total Overrun Hours instead. A regime that both loses start-time and overruns is a **disruption signal**, not efficiency. Standing time and Lost Hours — not the efficiency ratio — are the primary performance indicators.

---

## Step 6: Identify Patterns

Analyse the possession data for recurring patterns:

### By Day of Week
- Are delays concentrated on specific days? (e.g., Monday possessions consistently start late due to weekend overruns)
- Calculate average lost time per day of week and flag any day with significantly higher lost time than others.

### By Time of Day
- Are morning possessions more affected than evening? Do night possessions perform differently?
- Group by shift type if identifiable (day/night).

### By Location
- If location data is available, identify whether specific locations or sections have consistently worse access performance.

### Trend Over Time
- Compare week-on-week or period-on-period:
  - Is the situation **improving** (lost time decreasing)?
  - Is it **worsening** (lost time increasing)?
  - Is it **stable** (consistent level of delay)?
- State the trend clearly with supporting data.

### Repeat Offenders
- A single possession is **one event**, so it cannot itself be a "repeat offender". Group possessions by a recurring dimension — **location/section, route, or possession type** — and flag any group where delays have occurred on **3 or more occasions** in the period. Report the offender as the location/route/possession-type, not an individual possession.

---

## Step 7: Present Results

Read `references/access-output-template.md` for the exact
7-section report structure (Headline, Summary, Possession Detail, Non-Possession Access,
Labour Impact, Patterns and Trends, Contractual Relevance) and the caveats text (do not modify
the caveats). Fill every placeholder with data computed in Steps 1–6. Apply **Pattern 8
(Report Numbering)** from `../../shared/patterns/08-report-numbering.md`
for the `AC-[NNN]` ref.

---

## Related Skills

After presenting the analysis, suggest these related skills:

- `$delay-analysis` — Build a comprehensive delay register including access-related delays alongside other causes
- `$programme` — Assess how access delays are affecting overall programme milestones
- `$commercial-report` — Include access delay quantification in a formal commercial period report
