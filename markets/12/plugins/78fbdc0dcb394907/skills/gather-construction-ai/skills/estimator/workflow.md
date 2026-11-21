---
name: estimator
description: Builds a labour-hour rate card — unit rates (hrs/m, hrs/m2, hrs/m3, hrs/nr)
  from output quantities vs labour hours, for productivity benchmarking and effort
  forecasting. Hours only; monetary pricing needs user-supplied cost rates.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Estimator — Derive Unit Rates from Actual Performance

Build a project-specific rate card by comparing recorded output quantities against the labour hours used to deliver them. The resulting rates are **labour-hour unit rates** (e.g. hrs/m, hrs/m³) that reflect real site productivity and are directly usable for effort forecasting and productivity benchmarking.

**Rate convention (used throughout):** rates are expressed as **hours per unit** (hrs/unit). Where cross-referencing `$measured-mile` or `$progress`, which express productivity as **units per hour** (units/hr), state the reciprocal explicitly — units/hr = 1 ÷ (hrs/unit).

**No financial data:** these are hours-per-unit rates, not prices. The Gather API holds no cost or rate money. Converting to a monetary rate (for a CE valuation or quotation) requires the user to supply labour cost rates (£/hr) — state this whenever pricing is mentioned.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project, Date Range, and Activity Filter

Parse `the user’s request` for three possible components:

1. **Project name** — resolve using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
2. **Date range** — parse using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`. If no date range is specified, default to the last 4 weeks.
3. **Activity type filter** — if the user specifies an activity type (e.g. "drainage", "fencing", "earthworks"), store it for filtering in Steps 2–4. This is optional.

Confirm the interpreted parameters with the user:
> "I'll build a rate card for **[project name]** from **[start date]** to **[end date]**[, filtered to **[activity type]** activities]. Does that look right?"

If the date range is unambiguous (exact dates provided), skip confirmation and proceed.

---

## Step 2: Retrieve Output Quantities (Progress Data)

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardProgress`
- **Project:** the resolved project UUID
- **Date range:** the parsed from/to dates

This returns progress records showing output quantities per activity — what was actually produced (metres of drainage, square metres of paving, cubic metres of excavation, etc.).

If no data is returned, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. Specifically suggest:
- Progress data may not be recorded for this period — check with the site team
- The date range may be too narrow — try expanding it
- The activity type filter may not match any recorded activities — try without the filter

Extract from the response:
- Activity name / description
- Output quantity per activity per record
- Output unit (m, m², m³, nr, tonnes, etc.)
- Date of each record

If an activity type filter was specified in Step 1, filter results to only include activities matching that filter (use fuzzy matching — e.g. "drainage" should match "Surface Water Drainage", "Foul Drainage Installation", etc.).

---

## Step 3: Retrieve Resource Allocation Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardAllocation`
- **Project:** the resolved project UUID
- **Date range:** the same from/to dates

This returns planned and actual resource allocation per activity — what was expected vs what was used.

Extract from the response:
- Activity name / description
- Planned resource hours per activity
- Planned unit rates (if available)
- Actual allocated hours per activity

---

## Step 4: Retrieve Actual Labour Hours

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the same from/to dates

This returns actual labour hours worked, broken down by person/role and potentially by activity.

Extract from the response:
- Total labour hours per activity (where activity-level breakdown is available)
- Labour hours by role/trade (to understand crew composition)

---

## Step 5: Calculate Derived Unit Rates

For each activity that has **both** output quantity data (from Step 2) **and** labour hours data (from Steps 3–4), calculate the derived unit rate:

1. **Total output quantity** — sum all progress records for the activity
2. **Total labour hours** — sum all labour hours attributed to the activity (see the hours-source precedence rule below)
3. **Derived unit rate** = total labour hours / total output quantity
   - Express as: hours/m, hours/m², hours/m³, hours/nr, etc. depending on the output unit
   - **Reciprocal:** where you cross-reference measured-mile or progress, also state units/hr = 1 ÷ (hrs/unit).

### Hours-source precedence (allocation vs labour report)

Two reports carry hours: `dashboardAllocation` (Step 3, actual **allocated** hours) and `dashboardResourceLabour` (Step 4, actual **recorded labour** hours). When both provide activity-level hours and they disagree:

1. **Prefer `dashboardResourceLabour`** (actual recorded time worked) as the numerator for derived rates.
2. Use `dashboardAllocation` actual hours only where the labour report has no activity-level breakdown for that activity.
3. If the two sources differ by more than ~10% for an activity, use the labour-report figure but **flag the discrepancy** under Data Quality (Section 4): "Allocated hours ([X]) and recorded labour hours ([Y]) differ by [Z]% for [activity] — rate uses recorded labour; verify attribution."

### No activity-level attribution (mirror `$progress`)

Labour is often recorded at shift level, not broken down by activity. In that case:

- **Do not** derive per-activity rates from unattributed labour — state: "Labour hours are not broken down by activity, so per-activity unit rates cannot be derived."
- Offer a **single blended rate** only if **one activity clearly dominates output** (e.g. one activity is ≥80% of total output and the units are consistent): "One blended rate is offered because [activity] accounts for [X]% of output; it is total labour hours ÷ total output = [rate] hrs/[unit], and it attributes all labour — including other minor activities — to the dominant one."
- If no single activity dominates, do not produce a blended rate — it would misattribute hours across incomparable units.

### Zero / near-zero output guard (Pattern 12)

If an activity has labour hours but **zero or near-zero recorded output**, the rate (hours ÷ 0) is undefined. **Exclude the activity from the rate card** and flag it under Data Quality: "[Activity] — [X] labour hours recorded against zero/negligible output; rate is n/a (Pattern 12). Likely a data-entry gap — output not recorded, or hours misattributed." Never render this as a number or an infinite rate.

### Confidence Assessment

Assign a confidence level to each derived rate using **both** record count **and** dispersion — record count alone is naive, because ten wildly scattered records are less reliable than they look.

**Step 1 — provisional tier by record count:**

| Data Points | Provisional Tier |
|---|---|
| 10 or more records | `HIGH` |
| 5–9 records | `MED` |
| Fewer than 5 records | `LOW` |

**Step 2 — dispersion check.** For each activity, compute the per-record rate (hrs/unit) for every record and take the **max/min rate ratio**. A `HIGH` tier requires **≥10 records AND a max/min ratio < 2**. If the ratio is ≥ 2, **downgrade one tier** (HIGH→MED, MED→LOW) and note: "Downgraded for dispersion — per-record rates range [min]–[max] hrs/[unit] (ratio [X])."

**Step 3 — record the min–max range.** For every rate, capture the minimum and maximum per-record rate; show this range in the rate card (Section 2) so the point rate carries its own spread evidence.

**Flag activities with fewer than 5 data points** with a warning:
> "Low confidence — only [N] data points. Rate may not be representative."

Activities with only 1 data point should still be shown but clearly marked:
> "Single record only — treat as indicative, not reliable."

---

## Step 6: Compare Against Planned Rates

For each activity where planned rates are available from the allocation data (Step 3):

1. **Planned rate** — from allocation data (planned hours / planned quantity)
2. **Actual rate** — the derived rate from Step 5
3. **Variance** = ((Actual rate - Planned rate) / Planned rate) x 100%
   - Positive variance means the activity took more hours than planned (slower)
   - Negative variance means the activity took fewer hours than planned (faster)

Flag significant variances:
- Variance > +20%: "Significantly slower than planned"
- Variance > +50%: "Major overrun — investigate causes"
- Variance < -20%: "Faster than planned — verify data accuracy"

**Rate-library comparison (if `estimating/rate-library.md` exists):** where an activity in this
run also appears in the library (exact name/unit match, or a mapping the library records as
confirmed), add a "library norm" column — this project's derived rate vs the library's achieved
range — cited "per the rate library ([sweep date])" and carrying any LOW BASIS flag the library
records. The library is written ONLY by `$rate-library`; this skill reads it, never
updates it, and a missing or non-matching library simply means the column is omitted (say so
once).

---

## Step 7: Present the Rate Card

Read `references/output-template.md` and use its exact
structure. Fill every placeholder `[…]` with data; do not add, remove, or reorder sections.
Apply **Pattern 8 (Report Numbering)** from
`../../shared/patterns/08-report-numbering.md`.

---

## Related Skills

After presenting the rate card, suggest these related skills for deeper analysis:

- `$progress` — Review the underlying progress data in detail for specific activities
- `$labour` — Analyse the labour hours breakdown by person, role, and period
- `$benchmark` — Compare these derived rates against other projects or industry benchmarks
- `$measured-mile` — Establish a representative baseline period to quantify disruption (measured-mile expresses productivity as units/hr — the reciprocal of the hrs/unit rates here)
- `$rate-library` — Sweep these norms across the portfolio into the versioned library this skill's Step 6 compares against
