---
name: resource-analysis
description: Analyse plant equipment and materials — hire periods, idle time, consumption,
  planned-vs-actual allocation variance. Not labour (use labour); for a formal plant
  status document use plant-report.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Plant and Material Resource Analysis

Analyse plant equipment utilisation and material usage for a Gather project — hire periods, idle time, material consumption patterns, allocation variance, and efficiency recommendations. Plant hire is often the second-largest cost on construction projects after labour, making idle equipment identification an immediate cost-saving opportunity.

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
4. Calculate the **span in days** — this is used for utilisation calculations.

---

## Step 2: Retrieve Plant Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourcePlant`
- **Project:** the resolved project UUID
- **Date range:** the resolved `from` and `to` dates

If the report returns no data, follow **Pattern 3 (Empty Data Handling)**. Proceed to Step 3 (materials) regardless — one resource type may have data even if the other does not.

---

## Step 3: Retrieve Material Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardResourceMaterial`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

If the report returns no data, follow **Pattern 3 (Empty Data Handling)**. Proceed to Step 4 (allocation) regardless.

---

## Step 4: Retrieve Allocation Data

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardAllocation`
- **Project:** the resolved project UUID
- **Date range:** the same `from` and `to` dates

This provides planned vs actual allocation for plant and materials. If no data is returned, note that allocation comparison is not available and proceed with the analysis of actuals only.

---

## Step 5: Analyse Plant Equipment

**Schema check (Pattern 12).** Utilisation = Days Used ÷ Days on Site requires the plant report to distinguish the **two** — days the item was *on site* and days it was *used*. Before calculating, verify (via `getReportSchemas` or the first data response) that both are available. If the report records **usage only** (no days-on-site field), **degrade explicitly**: switch to **span-based utilisation**, where "days on site" is taken as the span from the item's first recorded date to its last recorded date (inclusive), and say so in the caveats — "Days on site inferred from first-to-last recorded date; utilisation may be overstated for items that left and returned." Never invent a days-on-site figure.

**Divide-by-zero guard (Pattern 12).** If Days on Site (or the inferred span) is 0 for an item, render Utilisation % as **"n/a"** with a data-quality flag — never 0, never an error.

Save the Step 2 response to a scratch file and run
`python3 ../../scripts/shift_analytics.py <plant.json> --format md > <scratch>/shift-analytics-summary.md`.
Read the summary for per-item hours-on-hire, idle days, longest consecutive-idle run, and
off-hire candidates instead of computing per-item totals by hand; cite it in the Plant Summary
and Detail tables below.

For each plant item in the data from Step 2, calculate:

| Field | Calculation |
|---|---|
| **Description** | Equipment name/description as recorded |
| **Type/Category** | Equipment type or category (e.g., excavator, crane, generator) |
| **Days on Site** | Number of days the item was recorded as on site during the period (or the first-to-last span if days-on-site is unavailable — see schema check) |
| **Days Used** | Number of days the item was actually used/operated |
| **Idle Days** | Days on Site minus Days Used |
| **Utilisation %** | (Days Used / Days on Site) × 100 — render "n/a" if Days on Site = 0 |
| **Status** | See classification below |

### Plant Status Classification

Classify each item based on utilisation:

Boundaries are contiguous and use **≥** consistently: Active **≥60%**, Underutilised **≥30% and <60%**, Idle **<30%**.

- **Active** — Utilisation **≥60%**. Equipment is being used regularly.
- **Underutilised** — Utilisation **≥30% and <60%**. Equipment is on site but not being used often enough to justify the hire cost. Flag with: "Below 60% utilisation — review whether this item is still needed on site."
- **Idle** — Utilisation **<30%**. Equipment is rarely used. Flag with: "Significantly underutilised — consider off-hiring or reallocating."
- **Long-idle** — On site for the entire period (or near-entire) but used fewer than 5 days total. Flag prominently: "On site for [N] days but used only [M] days — strong candidate for off-hire."

Sort the plant table by **Utilisation % ascending** (worst-utilised first) to draw attention to cost-saving opportunities.

### Plant Summary Statistics

| Metric | Value |
|---|---|
| **Total Plant Items** | [count of distinct items] |
| **Active (≥60%)** | [count] ([%]) |
| **Underutilised (≥30% and <60%)** | [count] ([%]) |
| **Idle (<30%)** | [count] ([%]) |
| **Long-Idle** | [count] |
| **Average Utilisation** | [mean utilisation % across all items] |
| **Total Days on Site** | [sum across all items — this represents total hire-days] |
| **Total Days Used** | [sum across all items] |
| **Overall Utilisation** | (Total Days Used / Total Days on Site) × 100% — render "n/a" if Total Days on Site = 0 |

---

## Step 6: Analyse Material Usage

For each material type in the data from Step 3, calculate:

| Field | Calculation |
|---|---|
| **Material** | Name/description of the material |
| **Unit** | Unit of measurement (e.g., tonnes, m3, litres, nr) |
| **Total Qty Used** | Sum of all usage in the period |
| **Working Days** | Number of days with recorded usage |
| **Avg Daily Consumption** | Total Qty divided by Working Days |
| **Max Daily Usage** | Highest single-day consumption |
| **Min Daily Usage** | Lowest single-day consumption (excluding zero days) |

### Usage Pattern Analysis

For each material, assess the consumption pattern over the period:

- **Increasing** — daily consumption is trending upward (later period averages higher than earlier)
- **Decreasing** — daily consumption is trending downward
- **Steady** — daily consumption is relatively consistent (variation within +/-25% of the mean)
- **Sporadic** — usage is irregular with no clear pattern (large gaps between usage days)

### Anomaly Detection

Flag any of the following:
- **Spike:** Any single day where consumption exceeds **2x the average daily consumption** — flag as "Anomalous spike: [qty] [unit] on [date] (avg is [avg])"
- **Drop:** Any period of **3+ consecutive working days** where consumption falls below **0.5x the average** — flag as "Significant drop in [material] usage from [start date] to [end date]"
- **Zero usage periods:** If a material was being consumed regularly and then has **5+ consecutive days of zero usage**, flag as "Usage stopped for [material] from [date] — check if work requiring this material has paused or if recording has lapsed"

### Material Summary Statistics

| Metric | Value |
|---|---|
| **Material Types Tracked** | [count of distinct materials] |
| **Total Usage Records** | [count of daily records across all materials] |
| **Materials with Anomalies** | [count] |
| **Materials Increasing** | [list] |
| **Materials Decreasing** | [list] |

---

## Step 7: Analyse Allocation Variance

If allocation data from Step 4 is available, compare planned vs actual for both plant and materials.

**Divide-by-zero guard (Pattern 12).** Variance % = (variance ÷ planned) × 100. Where **planned = 0** (actual recorded but nothing planned), render Variance % as **"n/a"** with a data-quality flag — never as a number or an error — and describe the item narratively as "actual with no plan".

### Plant Allocation Variance

For each plant item (or category) with an allocation:

| Item/Category | Planned Days | Actual Days | Variance | Variance % |
|---|---|---|---|---|
| [item] | [planned] | [actual] | [actual - planned] | [(variance/planned) x 100] |

Flag items where:
- **Over-allocated (actual > planned by >20%):** "Exceeding planned allocation — review whether additional plant was necessary or if the programme has slipped"
- **Under-allocated (actual < planned by >20%):** "Below planned allocation — check if work requiring this plant has been delayed or descoped"

### Material Allocation Variance

For each material type with an allocation:

| Material | Planned Qty | Actual Qty | Variance | Variance % |
|---|---|---|---|---|
| [material] | [planned] | [actual] | [actual - planned] | [(variance/planned) x 100] |

Flag materials where:
- **Overconsumption (actual > planned by >15%):** "Material usage exceeding plan — potential wastage, rework, or scope change"
- **Underconsumption (actual < planned by >25%):** "Material usage significantly below plan — check if associated work is behind programme"

If allocation data is not available, state: "Planned allocation data is not available for this project/period. Analysis is based on actual usage only. Consider setting up allocations in Gather for future variance tracking."

---

## Step 8: Present Results

Read `references/report-template.md` for the
exact output structure (Summary, Plant Equipment, Materials, Allocation Variance,
Recommendations, Caveats) and fill it with the data computed in Steps 5–7.

---

## Related Skills

After presenting the analysis, suggest these related skills:

- `$delivery-notes` — Review delivery records for materials arriving on site
- `$estimator` — Derive labour-hour unit rates (hrs/unit) from progress and labour data to complement the plant and material picture
- `$labour` — Analyse labour resource hours alongside plant and material usage for a complete resource picture
