---
name: plant-report
description: Produce a formal plant status report — register, movements, utilisation,
  off-hire recommendations — or an Off-Hire Mode ranking idle hired plant by weekly
  cost exposure. Explicitly invoked only (`$plant-report` or `$plant-offhire`).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Plant & Equipment Report

Generate a structured plant and equipment report for a project — a register of what is on site, utilisation performance, movements (mobilisations and demobilisations), and actionable recommendations for hire cost management.

This skill differs from `$resource-analysis` which provides an analytical deep-dive including materials and allocation variance. This report is a focused, management-ready plant status document suitable for plant managers, commercial reviews, or cost control meetings.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Reporting Period

**Project resolution:**

1. Parse `the user’s request` for a project name and optional date range.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Date range resolution:**

1. Parse any date range from `the user’s request` using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no date range is specified, default to the **last 4 weeks**.
3. If the input is ambiguous, confirm with the user before proceeding.

---

## Step 2: Retrieve Data (parallel calls)

Make the following `getCachedReport` calls **in parallel** for the resolved project and reporting period:

### 2a: Plant Data (`dashboardResourcePlant`)
Primary data source — all plant and equipment recorded on site during the period.

### 2b: Allocation Data (`dashboardAllocation`)
Planned vs actual plant allocation, if configured.

### 2c: Narrative Data (`dashboardNarrative`)
Search narratives for plant-related entries — breakdowns, mobilisations, demobilisations, idle equipment mentions.

Follow **Pattern 3 (Empty Data Handling)** if plant data returns empty. Note: if no plant data exists, this report cannot be generated — suggest the user check whether plant tracking is configured in Gather.

Save the raw `dashboardResourcePlant` result to a scratch file and run:

```
python3 ../../scripts/shift_analytics.py <plant.json> --format md > <scratch>/shift-analytics-summary.md
```

Read the summary for hours-on-hire per item, idle days, longest consecutive-idle run, and
off-hire candidates (default 3-day threshold) instead of summing rows yourself; cite it in
Section 2/6 as "computed by `shift_analytics.py` over [N] `dashboardResourcePlant` rows". Any
metric the script marks "unavailable" (e.g. no days-on-site column) still goes through the
Step 3 schema-degrade rule below — never invent it.

---

## Step 3: Build the Plant Register

**Schema check (Pattern 12).** Utilisation = Days Used ÷ Days on Site requires the report to distinguish **days on site** from **days used**. Before building the register, verify (via `getReportSchemas` or the first data response) that both fields exist. If the report records **usage only** (no days-on-site field), **degrade explicitly**: use **span-based utilisation**, taking "days on site" as the span from the item's first-to-last recorded date (inclusive), and note this in the caveats — utilisation may be overstated for items that left and returned. Never invent a days-on-site figure.

**Divide-by-zero guard (Pattern 12).** If Days on Site (or the inferred span) is 0, render Utilisation % as **"n/a"** with a data-quality flag — never 0, never an error.

From the plant data (2a), build a complete register of all equipment recorded during the period:

For each plant item:

| Field | Source |
|---|---|
| **Item ID / Reference** | As recorded in Gather |
| **Description** | Equipment name/description |
| **Type / Category** | Equipment type (excavator, crane, generator, etc.) |
| **First Recorded** | Earliest date this item appears in the period |
| **Last Recorded** | Latest date this item appears |
| **Days on Site** | Count of days the item was recorded (or the first-to-last span if days-on-site is unavailable — see schema check) |
| **Days Used** | Count of days the item was actively used/operated |
| **Idle Days** | Days on Site minus Days Used |
| **Utilisation %** | (Days Used / Days on Site) × 100 — render "n/a" if Days on Site = 0 |

---

## Step 4: Classify Equipment Status

Classify each item on **two independent axes** — a utilisation status and a movement status.

**Utilisation status** (contiguous, ≥ throughout): Active **≥60%**, Underutilised **≥30% and <60%**, Idle **<30% — rarely used, strong off-hire candidate**.

**Movement status.** Movement is inferred from first/last recorded dates relative to the period boundaries. A first appearance *at* the period start does **not** mean the item was newly mobilised — it was very likely already on site and may predate the range. Only a first appearance clearly *later* than the period start is a genuine mobilisation (mirrors how `$people` handles first-appearance). Classify:

- **Present at period start** — first recorded date is within ~3 days of the period start. Label as "present at period start (may predate this range)". Do **not** call this a mobilisation.
- **Mobilised** — first recorded date is more than ~3 days *after* the period start — genuinely brought to site during the period.
- **Demobilised** — last recorded date is more than 7 days before the period end (item stopped appearing well before the window closed — likely left site).
- **Continuous** — recorded from ~period start through to the final week, with no clear mobilisation or demobilisation.

An item carries one utilisation status and one movement status (e.g., "Active, Mobilised").

---

## Step 5: Identify Movements

Apply the **same movement definitions as Step 4** (do not use a second, looser rule here — the two steps must agree):

### Mobilisations
Items whose first recorded date is more than ~3 days **after** the period start — genuinely brought to site during the period. Items first recorded *at* the period start are **present at period start (may predate the range)**, not mobilisations — exclude them here.

### Demobilisations
Items whose last recorded date is more than 7 days before the period end — recorded earlier in the period but absent from the final week, so they likely left site. (This is the single demobilisation definition used throughout — it is the same condition as the "Demobilised" movement status in Step 4.)

### Continuous
Items present from ~period start through to the final week.

If narrative data (2c) mentions specific plant mobilisations or demobilisations, cross-reference to validate. Recording lag means an actual mobilisation may predate the first recorded date — state this where it matters.

---

## Step 6: Analyse Utilisation

### By Category
Group plant items by type/category and calculate aggregate utilisation:

| Category | Items | Avg Utilisation | Active | Underutilised | Idle |
|---|---|---|---|---|---|
| [type] | [count] | [%] | [count] | [count] | [count] |

### Utilisation Trend
If the period spans multiple weeks, calculate weekly utilisation to identify trends:
- Is overall utilisation improving, declining, or stable?
- Are specific categories trending worse?

### Cost Impact Assessment
For each idle or underutilised item, the waste is simply its **idle days** — each idle day is a hire-day with no productive output. Financial cost per day is not available through Gather; present the figure in hire-days so the user can apply their own rates.

---

## Step 7: Check for Plant-Related Issues in Narratives

Search the narrative data (2c) for plant-related keywords:
- "breakdown", "broken", "fault", "repair", "out of service", "not working"
- "wrong plant", "unsuitable", "too small", "too large"
- "waiting for plant", "plant not available", "no crane"
- "off-hired", "mobilised", "demobilised", "delivered", "collected"

For each match, record the date and narrative excerpt. These provide context for utilisation figures (e.g., an item may be idle because it broke down, not because it wasn't needed).

---

## Step 8: Present the Plant Report

Read `references/report-template.md` for the exact
output structure (Summary, Plant Register, Movements, Utilisation by Category, Plant Issues,
Recommendations, Allocation Variance, Caveats) and fill it with the data computed in Steps
3–7.

---

## Off-Hire Mode

Triggered by `$plant-offhire [project] [window]`, or a request for an off-hire review,
idle-plant ranking, or "hire costing money" analysis instead of a full status report. Reuses
Step 1 (project/period, default **last 4 weeks**) and Step 2's data retrieval — do not re-fetch
— then replaces Steps 3–8 with the commercial-profile rate lookup, recording-coverage gate,
OFF-HIRE CANDIDATE / MONITOR / IN USE classification, weekly cost exposure, and the ranked
off-hire report template. At this trigger, read
`references/offhire-mode.md` for the full procedure.

## Related Skills

- `$resource-analysis` — Analytical deep-dive including materials, allocation variance, and anomaly detection
- `$delivery-notes` — Track material deliveries alongside plant movements
- `$commercial-report` — Include plant summary in a period commercial report
- `$cost-to-complete` — Factor plant utilisation trends into completion forecasts
