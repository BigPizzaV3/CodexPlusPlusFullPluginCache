---
name: labour
description: Analyse labour hours by person, trade, period — who worked when, overtime,
  utilisation. For roster/headcount (who's on site, mobilisation), use people.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Labour Resource Analysis

Analyse labour resource hours for a Gather project — breakdown by person, trade/role, and time period with overtime detection, trend analysis, and utilisation statistics.

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
3. If the input is ambiguous (e.g., "January" without a year), confirm with the user before proceeding.
4. Calculate the **span in days** between `from` and `to` — this determines the aggregation period used in Step 4.

---

## Step 2: Retrieve Labour Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the resolved `from` and `to` dates

If the report returns no data, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. State clearly that no labour data was found for the specified project and period, suggest possible causes, and offer to retry with different parameters.

**Schema check (Pattern 12).** Before computing per-person or per-day metrics, verify the labour report exposes per-person **daily** granularity (a row per person per date). Inspect the first response (or call `getReportSchemas`). If the report only provides period-level or per-person totals without daily rows, **degrade gracefully**: compute period-level breakdowns only, skip the By Person "Days Worked"/"Avg Hours/Day" and the per-day overtime flags in Step 6, and state explicitly in the output which metrics were downgraded and why. Never invent daily values.

---

## Step 3: Retrieve Shift Context

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardShiftTable`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

Extract from this data:
- **Total working days** in the period (days where at least one shift was recorded)
- **Shift durations** — typical shift start/end times, standard shift length
- **Non-working days** — days with no recorded shifts (weekends, stand-downs, etc.)

This context is essential for calculating averages and detecting overtime accurately. If this report returns no data, note the limitation but continue with labour data alone — use calendar days as a fallback denominator for averages.

If a `dashboardShiftTable` fetch for this project/period already exists in the conversation (e.g. from a prior skill in the same agent run), reuse it per **Pattern 21 (Fetch-Once Cache)** from `../../shared/patterns/21-fetch-once-cache.md` instead of calling again.

---

## Step 4: Compute Aggregates (`shift_analytics.py`)

Save the raw `getCachedReport` results from Steps 2 and 3 to scratch files, then run:

```
python3 ../../scripts/shift_analytics.py <labour.json> <shifttable.json> \
    --format md > <scratch>/shift-analytics-summary.md
```

Read the summary instead of summing rows yourself. It gives: hours by person (total, days
worked, avg hours/day), hours by trade/role (headcount, % of total, avg/person), hours by ISO
week (Mon–Sun) and headcount by day. If daily granularity
is unavailable, the summary marks the affected metrics "unavailable" — state this rather than
inventing values (Pattern 12). For date ranges **over 60 days**, re-bucket the script's weekly
figures into months yourself (the script does not aggregate to month); for **≤60 days** use its
output as-is (daily if ≤14 days is wanted, ask the script's per-week table to be read alongside
the raw daily rows).

Cite the script in the output: "Labour hours computed by `shift_analytics.py` over [N]
`dashboardResourceLabour` rows."

---

## Step 5: Key Statistics and Peak/Trough

From the Step 4 summary, take **Total Labour Hours**, **Total Individuals**, **Working Days**
(from the shift-table file, or calendar weekdays as fallback), **Avg Hours per Working Day**
(Total Hours ÷ Working Days), and **Avg Hours per Person per Day** (the script's person-day
basis: total hours ÷ Σ person-days actually worked). Read **Peak Day** and **Trough Day** (highest/lowest non-zero total) off the script's
headcount-by-day table.

---

## Step 6: Classify Overtime and Flags

Use project-configured commercial overtime thresholds when supplied. Otherwise use clearly labelled comparison defaults of >10 recorded hours per person per day and >50 recorded hours per person per ISO week. These compare recorded effort for resource and cost review; they do not establish contractual overtime entitlement or assess health, fitness, safety or legal compliance. Do not classify rest periods or consecutive turns.

Apply comparisons to the Step 4 summary's per-person and per-day figures where available (do not invent missing daily values):

### Individual Hours Comparisons
- **Above daily comparison:** recorded hours exceed the configured daily threshold.
- **Above weekly comparison:** recorded hours exceed the configured weekly threshold.

### Workforce Flags
- **Zero-hour days:** any working weekday with zero total hours in the headcount-by-day table.
- **Significant variance:** any day's total hours >2x or <0.5x the daily average.

Present all flags in a dedicated **Flags and Alerts** section, grouped into hours comparisons and workforce anomalies.

---

## Step 7: Identify Trends

Compare the period-over-period data (from Step 4c) to identify the overall trend:

- **Increasing** — if each period's total hours are generally higher than the previous (use a simple linear direction check across at least 3 data points)
- **Decreasing** — if each period's total hours are generally lower
- **Stable** — if variation between periods is within ±15%
- **Drifting** — if variation between periods is **>15% and ≤30%** (some movement, but no large swings)
- **Volatile** — if there are large swings (**>30% variation**) between consecutive periods

These bands are contiguous: ≤15% Stable, >15–30% Drifting, >30% Volatile — no gap.

State the trend clearly: "Labour hours are **[increasing/decreasing/stable/drifting/volatile]** over this period."

If there are at least 4 weeks of data, calculate the **week-on-week change** as a percentage for the most recent two complete weeks and state it explicitly.

---

## Step 8: Present Results

At Step 8, read `references/output-template.md` for the exact report structure (Summary, Trend, Period Breakdown, By Person, By Trade/Role, Flags and Alerts, Caveats). Fill every placeholder with data; do not add, remove, or reorder sections.

---

## Related Skills

After presenting the analysis, suggest these related skills:

- `$estimator` — Derive unit rates by combining labour hours with progress output
- `$people` — View individual profiles and assignment details for specific team members
