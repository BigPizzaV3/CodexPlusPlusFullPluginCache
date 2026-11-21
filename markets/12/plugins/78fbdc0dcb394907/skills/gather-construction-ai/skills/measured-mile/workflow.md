---
name: measured-mile
description: Calculates productivity disruption using the measured mile method — compares
  baseline vs impacted period output rates to quantify loss, for disruption and productivity
  claims.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Measured Mile — Productivity Disruption Analysis

Compare productivity between a baseline (unimpacted) period and a disrupted period to quantify the loss factor attributable to disruption. The measured mile is a recognised methodology in construction claims for demonstrating productivity loss with project-specific data.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Confirm Parameters

Extract from `the user’s request`:
- **Project name** — resolve using Pattern 1
- **Baseline period** — the unimpacted period (dates when work proceeded without significant disruption)
- **Impacted period** — the disrupted period (dates when disruption affected productivity)

If the user has not provided two distinct date ranges, explain what a measured mile analysis requires:

> "A measured mile analysis compares productivity between two periods on the same project:
> - **Baseline period**: A period of unimpacted work on similar activities — this establishes the 'normal' productivity rate
> - **Impacted period**: A period where disruption affected productivity — this shows the reduced rate
>
> Please provide both date ranges. For example: 'baseline January 2026, impacted March 2026'"

If the user provides only one date range, ask which period it represents and request the other.

Optionally accept an **activity filter** to focus on specific work activities.

---

## Step 2: Retrieve Baseline Period Data

Call `getCachedReport` with `dashboardResourceLabour` for the **baseline period** to get:
- Total labour hours consumed
- Hours by person/trade

Call `getCachedReport` with `dashboardShiftTable` for the **baseline period** to get:
- **Working days** (distinct dates with at least one shift) — use this as the working-day count for the period, **not** a figure inferred from the labour report
- Median shift duration (used for any hours→days conversion, per Pattern 11)

Call `getCachedReport` with `dashboardProgress` for the **baseline period** to get:
- Output quantities achieved per activity
- Units of measurement (m, m², m³, nr, etc.)

### Baseline validation (confirm the baseline is genuinely unimpacted)

A measured mile is only valid if the baseline period was itself undisrupted. Validate it — the data is one call each away:

- Call `getCachedReport` with both `dashboardNarrative` and `dashboardAccessPossession` for the **baseline period** in a single disruption-keyword pass: scan narrative entries for disruption keywords (access, standing time, delay, rework, weather — see Pattern 10) and check the access report for missed/cancelled possessions or restrictions.

Record the result: if the baseline shows recorded disruption, the baseline rate is suppressed and the loss factor will be **understated** — carry this into the Confidence Assessment (Step 7 / Section 5). If the baseline is clean, note "baseline validated — no material disruption recorded."

If progress data is not available or only contains high-level percentages, note this limitation. The analysis can still compare labour hours between periods but cannot calculate a true output-based loss factor.

Follow Pattern 3 if any report returns no data.

---

## Step 3: Retrieve Impacted Period Data

Call `getCachedReport` with `dashboardResourceLabour` for the **impacted period** to get:
- Total labour hours consumed
- Hours by person/trade

Call `getCachedReport` with `dashboardShiftTable` for the **impacted period** to get:
- **Working days** (distinct dates with at least one shift) — the working-day count for the impacted period, from shift records, not the labour report
- Median shift duration

Call `getCachedReport` with `dashboardProgress` for the **impacted period** to get:
- Output quantities achieved per activity
- Units of measurement

---

## Step 4: Calculate Baseline Metrics

For each activity with data in both periods (or for the project as a whole if activity-level data is not available):

- **Total output quantity** achieved in the baseline period
- **Total labour hours** consumed in the baseline period
- **Baseline productivity rate**: output per labour hour (e.g., 2.5 m²/hour)
- **Average daily output**: total output ÷ working days
- **Average daily labour hours**: total hours ÷ working days
- **Headcount**: average number of workers per day

---

## Step 5: Calculate Impacted Period Metrics

For the same activities:

- **Total output quantity** achieved in the impacted period
- **Total labour hours** consumed in the impacted period
- **Impacted productivity rate**: output per labour hour
- **Average daily output**: total output ÷ working days
- **Average daily labour hours**: total hours ÷ working days
- **Headcount**: average number of workers per day

---

## Step 6: Calculate Disruption Impact

**Rate convention:** productivity here is **output per labour hour** (units/hr), e.g. 2.5 m²/hr. This is the reciprocal of the estimator's hrs/unit convention (units/hr = 1 ÷ hrs/unit) — state the reciprocal when cross-referencing `$estimator`.

### Loss Factor
```
Loss Factor = (Baseline Rate - Impacted Rate) / Baseline Rate
```

Express as a percentage. For example, if baseline rate is 2.5 m²/hour and impacted rate is 1.8 m²/hour:
- Loss Factor = (2.5 - 1.8) / 2.5 = 0.28 = **28% productivity loss**

**Divide-by-zero guard (Pattern 12):** if the **baseline rate is 0** (no baseline output, or zero baseline hours), the loss factor is undefined — render as "n/a" with a data-quality flag and stop: a measured mile cannot be computed without a valid baseline rate. Likewise, any productivity rate whose denominator (labour hours) or output basis is 0 renders "n/a", never a number.

### Lost Output
Calculate what the impacted period SHOULD have produced at baseline rates:
```
Expected Output = Impacted Period Labour Hours × Baseline Rate
Lost Output = Expected Output - Actual Impacted Output
```

### Additional Hours
Calculate extra labour hours consumed due to lower productivity:
```
Hours at Baseline Rate = Actual Impacted Output / Baseline Rate
Additional Hours = Actual Impacted Hours - Hours at Baseline Rate
```

**Pattern 11 (one event, one register):** the Additional Hours and Lost Output figures quantify disruption-related lost time. Do **not** sum them with lost-time totals from `delay-analysis` (DA), `access` (AC), or `weather-impact` (WI) — the same event legitimately appears in several registers and they use different units. Where those registers exist in the conversation, cross-reference them by Ref number and state: "Do not sum measured-mile additional hours with DA/AC/WI register totals — they overlap by design." Any hours→days conversion uses the median shift duration (from Step 2/3) as its divisor — state it.

### Per-Activity Breakdown
If activity-level data is available, calculate the loss factor per activity. Some activities may be more affected by disruption than others.

**Per-activity divide-by-zero guard (Pattern 12):** exclude any activity whose baseline rate or output is 0 from the per-activity loss table and flag it under the Confidence Assessment rather than rendering a number.

---

## Step 7: Assess Comparability

Before presenting results, assess whether the two periods are genuinely comparable:

- **Similar activities?** — the same or similar work types should be compared
- **Similar conditions?** — were weather, access, and resource levels broadly similar (excluding the disruption being measured)?
- **Sufficient data?** — each period should have at least 10 working days of data for statistical reliability
- **Similar resource levels?** — baseline and impacted periods should have comparable headcounts (a significant change in manning can affect productivity independently of disruption)
- **Baseline genuinely unimpacted?** — from the baseline validation in Step 2 (`dashboardNarrative` + `dashboardAccessPossession`): if the baseline period itself shows recorded disruption, the baseline rate is suppressed and the loss factor is **understated** — state this explicitly.
- **Learning-curve position?** — where in the project does the baseline sit? This is one of the two classic measured-mile attacks:
  - An **early-project baseline** (crews still climbing the learning curve) *understates* achievable productivity, so it *understates* the loss.
  - A **late, post-learning baseline** (peak efficiency) *overstates* the achievable rate, so it *overstates* the loss versus a still-ramping impacted period.
  - Prefer a baseline drawn from a **representative, steady-state** stretch of the work — not the single best week, which tribunals reject as cherry-picking.

Rate the overall confidence:
- **High confidence**: same activities, comparable conditions, 20+ working days per period, stable headcount
- **Medium confidence**: similar activities, broadly comparable conditions, 10-19 working days
- **Low confidence**: different activities, different conditions, or fewer than 10 working days in either period

---

## Step 8: Present Results

Read `references/output-template.md` for the exact report structure (Headline, Side-by-Side Comparison, Disruption Impact, Per-Activity Breakdown, Confidence Assessment, Caveats). Fill every placeholder with data; do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** for the `Ref: MM-[NNN]` line.

---


## Related Skills

- `$delay-analysis` — identify what caused the disruption in the impacted period
- `$estimator` — derive detailed unit rates for both baseline and impacted periods
- `$labour` — detailed labour hours analysis for both periods
- `$weather-impact` — if weather is the suspected disruption cause
- `$programme` — assess programme impact of the productivity loss
