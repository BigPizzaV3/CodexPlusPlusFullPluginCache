---
name: cost-to-complete
description: Forecast remaining labour hours and estimate at completion (EAC) from
  actual Gather productivity. Budget/variance needs a user-supplied planned baseline
  — Gather holds no cost or budget data.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Cost to Complete — Labour Hours Forecast

Forecast the remaining labour effort and estimate at completion (EAC) based on actual productivity data from Gather. This skill uses labour hours as the unit of measurement — financial cost data is not available through the Gather MCP.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

Apply **Pattern 9 (Commercial QA Gate)** from `../../shared/patterns/09-commercial-qa-gate.md` **for the unit-consistency and rounding/reconciliation checks only** (Pattern 9 checks 1 and 5) before finalising totals — the currency, tax-basis, and variation-status checks (2–4) do not apply, because Gather exposes no currency, VAT, or variation data.

**Important limitation:** This is a labour-hours-based forecast, not a financial forecast. The Gather MCP does not expose contract sums, rates, or cost data. The output quantifies effort (hours, gang-shifts) not cost (£). To produce a financial EAC, the user must apply their own rates to the hours forecast. Any budget/variance comparison depends entirely on a **planned-hours baseline the user supplies** — Gather holds no baseline.

---

## Step 1: Resolve Parameters

Extract from `the user’s request`:
- **Project name** — resolve using Pattern 1
- **Date range** — resolve using Pattern 2. This is the "actuals to date" period. Default to project start to today if no range specified.

Per **Pattern 2**, confirm the interpreted range only if the input required non-trivial interpretation (e.g. "I'll forecast the cost to complete for **[Project Name]** based on actuals from **[start]** to **[end]**. Proceed?"). Exact dates and clearly stated periods proceed without confirmation.

---

## Step 2: Retrieve Actual Data

Call the following `getCachedReport` reports **in parallel** for the resolved project and date range: `dashboardResourceLabour` (labour), `dashboardProgress` (progress), `dashboardNarrative` (for risk assessment in Step 7), and `dashboardAccessPossession` (for risk assessment in Step 7).

### 2a: Labour Data (`dashboardResourceLabour`)

Extract:
- **Total labour hours to date** — the cumulative hours consumed
- **Hours by trade/role** — breakdown showing which trades have consumed the most hours
- **Working days in the period** — count of distinct dates with labour recorded
- **Average daily hours** — total hours / working days
- **Average daily headcount** — **use the headcount reported directly by `dashboardResourceLabour` if that field is present** (verify per **Pattern 12**). Only if no headcount field exists, derive it as daily hours ÷ assumed shift length, and in that case **state the assumed shift length in the output** (e.g. "headcount derived assuming a [X]-hour shift"). Never present a derived headcount without stating the assumption.
- **Trend** — are daily hours increasing, decreasing, or stable? (compare first half of period to second half)

Follow Pattern 3 if no data is returned.

---

## Step 3: Analyse Progress Data

From the `dashboardProgress` data retrieved in Step 2, extract:
- **Activities and their planned vs actual output** — what has been achieved against plan
- **Percentage complete** per activity (if available)
- **Overall percentage complete** (weighted if multiple activities)
- **Units of measurement** for each activity

If progress data is only available as high-level percentages (not per-activity quantities), note this limitation. The forecast will be less precise.

If no progress data is available, the forecast can only use labour hour trends (see Step 5 alternative).

---

## Step 4: Calculate Productivity Rates

For each activity with both labour hours and progress data:

```
Productivity Rate = Output Achieved / Labour Hours Consumed
```

Example: If 500m of cable has been installed using 2,000 labour hours, the productivity rate is 0.25m per labour hour.

Also calculate:
```
Hours per Unit = Labour Hours Consumed / Output Achieved
```

Example: 2,000 hours / 500m = 4 hours per metre.

Present the rates per activity:

| Activity | Output Achieved | Unit | Hours Consumed | Hours per Unit | Output per Hour |
|---|---|---|---|---|---|
| [activity] | [qty] | [unit] | [hours] | [X] | [Y] |

---

## Step 5: Forecast Remaining Hours

### Method A: Activity-Based Forecast (preferred — requires progress data)

For each activity:
```
Remaining Output = Planned Total Output - Actual Output
Forecast Remaining Hours = Remaining Output × Hours per Unit (from Step 4)
```

Sum across all activities for the total forecast remaining hours.

### Method B: Percentage-Based Forecast (if per-activity data not available)

```
Overall % Complete = from progress data
Forecast Total Hours = Actual Hours to Date / (% Complete / 100)
Forecast Remaining Hours = Forecast Total Hours - Actual Hours to Date
```

**Assumption to state:** Method B assumes the reported **% complete reflects earned quantities** (physical work done), **not elapsed time or elapsed programme**. If the percentage is a time-based or subjective estimate rather than measured output, the forecast is unreliable — say so in the output. **Divide-by-zero guard (Pattern 12):** if % Complete is 0, the forecast is not calculable — render as "n/a" with a data-quality flag rather than dividing.

### Method C: Trend-Based Forecast (if no progress data available)

```
Average Daily Hours = Total Hours / Working Days
Estimated Remaining Working Days = [user must provide or estimate]
Forecast Remaining Hours = Average Daily Hours × Remaining Working Days
```

Note: Method C is the least reliable. If using this method, state clearly that the forecast is based solely on labour hour trends and does not account for scope or progress.

Always state which method was used.

---

## Step 6: Calculate Estimate at Completion (EAC)

```
EAC (Hours) = Actual Hours to Date + Forecast Remaining Hours
```

**Variance requires a user-supplied baseline — Gather does not hold one.** Do not imply a planned-hours figure surfaces from the data. Explicitly ask the user:

> "Gather does not hold a planned-hours baseline. If you have a planned/tendered total labour-hours figure for this project, provide it and I'll calculate variance against it. Otherwise I'll present the EAC as an absolute forecast with no variance."

Calculate variance **only if the user supplies Planned Total Hours**:
```
Planned Total Hours = [user-supplied baseline — flag as user input]
Variance = EAC - Planned Total Hours
Variance % = (EAC - Planned Total Hours) / Planned Total Hours × 100
```

**Divide-by-zero guard (Pattern 12):** if the supplied baseline is 0, render Variance % as "n/a".

If the user does not supply planned total hours, note: "No baseline planned hours available for comparison. The EAC is presented as an absolute figure."

---

## Step 7: Risk Assessment

Scan for factors that could affect the forecast:

### From Narrative Data
From the `dashboardNarrative` data retrieved in Step 2, scan for risk indicators using the canonical keyword list in **Pattern 10 (Contractual Event Keywords)** from `../../shared/patterns/10-contractual-event-keywords.md` — do not maintain a separate list here — and apply Pattern 10's false-positive rule (a hit qualifies only if the sentence describes work being prevented, disrupted, or changed). Additionally note forward-looking phrases that signal risk to the remaining works: "behind programme", "slipping", "undermanned", "unable to resource", "design incomplete", "awaiting information".

### From Access Data
From the `dashboardAccessPossession` data retrieved in Step 2, check for access restrictions that could affect future productivity.

### Productivity Trend
Compare productivity rates from the first half of the period vs the second half. Is productivity improving, declining, or stable?

If Method C was used (no progress data), hours-per-unit rates are not available — base the trend on daily labour hours only and state: "Trend based on daily labour hours only — output rates not available under Method C."

---

## Step 8: Present the Forecast

Read `references/output-template.md` and use its
structure verbatim — do not reorder or rename sections. Section 3 (Activity Breakdown) is
conditional: include only if Method A (activity-based) was used; if Method B or C was used, omit
it and note under Section 2 "Activity breakdown not available — [Method B/C] used". This
conditional omission is the **only** permitted deviation from the structure. Apply **Pattern 8
(Report Numbering)** from `../../shared/patterns/08-report-numbering.md`
for the `CC-[NNN]` ref.

---

## Related Skills

- `$estimator` — Derive detailed unit rates from actual project performance
- `$labour` — Granular labour analysis by person, trade, and shift pattern
- `$progress` — Detailed planned vs actual output analysis
- `$programme` — Programme status and forecast completion dates
- `$commercial-report` — Include the EAC forecast in a period commercial report
- `$measured-mile` — Compare productivity across periods to validate forecast assumptions
