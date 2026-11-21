---
name: commercial-report
description: Generates a weekly or monthly commercial period report — labour, plant,
  materials, progress, access and key issues aggregated, for commercial reviews and
  management summaries. No cost or value data; monetary figures are user-supplied.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Commercial Report

Generate a comprehensive **operational commercial period report** for a project — aggregating labour, plant, materials, progress, access performance, and key issues into a single structured document suitable for management review.

**Scope of data:** Gather holds **no cost or value data** — no contract sums, rates, valuations, VAT, or variation values. This report quantifies operational effort and performance (hours, headcount, output, access), not money. Any monetary figures in the output are **user-supplied** and must be flagged as such. Do not invent or imply financial figures.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

Apply **Pattern 9 (Commercial QA Gate)** from `../../shared/patterns/09-commercial-qa-gate.md` **for unit-consistency checks only** (Pattern 9 check 1) before finalising totals — the currency, tax-basis, and variation-status checks do not apply, because no currency, VAT, or variation data exists in Gather.

---

## Step 1: Resolve Project and Reporting Period

**Project resolution:**

1. Parse `the user’s request` for a project name and a reporting period.
   - The project name typically comes first; the period follows (e.g., `"Alpha January 2026"`, `"Beta week ending 2026-01-17"`).
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Period resolution:**

1. Parse the remaining arguments for a date range using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no period is specified, default to **last 4 weeks**.
3. Per **Pattern 2**, confirm the interpreted period only if the input required non-trivial interpretation (e.g. "I'll generate the commercial report for **[Project Name]** covering **[start date] to [end date]**. Proceed?"). Exact dates, named months, and clearly stated periods proceed without confirmation.
4. Also calculate the **previous period** of equal length immediately preceding the reporting period (e.g., if the report covers January 2026, the comparison period is December 2025). This will be used for period-on-period comparison in Step 4.

> **API call volume:** Step 2 makes ~7 `getCachedReport` calls for the reporting period. Running the Step 4 comparison repeats these for the previous period — about **14 `getCachedReport` calls in total**. Before running the comparison, confirm with the user: "The period-on-period comparison roughly doubles the number of API calls (~14 in total). Include the comparison, or report the current period only?"

---

## Step 2: Pull Data for the Reporting Period

Make the following `getCachedReport` calls for the resolved project and reporting period. Each call targets a different dashboard report:

### 2a: Shift Activity
- **Report:** `dashboardShiftTable`
- **Extract:** total shift count, number of working days (distinct dates with shifts), list of active supervisors, shifts per supervisor.

### 2b: Labour
- **Report:** `dashboardResourceLabour`
- **Extract:** total labour hours, daily headcount figures, headcount by trade/role, hours by trade/role, average daily headcount, peak headcount (and the date it occurred).

### 2c: Plant & Equipment
- **Report:** `dashboardResourcePlant`
- **Extract:** list of plant items on site, utilisation data (hours used vs hours available if present), plant count by type.

### 2d: Materials
- **Report:** `dashboardResourceMaterial`
- **Extract:** materials recorded, quantities, delivery dates, material types.

### 2e: Progress
- **Report:** `dashboardProgress`
- **Extract:** output achieved per activity, planned output (if available), planned vs actual variance, productivity rates (output per working day).

### 2f: Access & Possession
- **Report:** `dashboardAccessPossession`
- **Extract:** possessions requested, possessions granted, possession timeliness, duration data.

- **Report:** `dashboardAccessOverview`
- **Extract:** overall access performance, restrictions encountered, access windows used vs available.

### 2g: Narratives (for key-issue scanning in Step 5)
- **Report:** `dashboardNarrative`
- **Extract:** all narrative/free-text entries with their date and recording supervisor. Step 5 scans these entries — without this call there is no text to scan.

**Empty data handling:** If any individual report returns no data, note it but continue with the remaining reports. Follow **Pattern 3 (Empty Data Handling)** — do not silently omit a section. Instead, include the section header with a note: "No [data type] data recorded for this period."

---

## Step 3: Calculate Period KPIs

From the data collected in Step 2, calculate and store the following key performance indicators:

| KPI | Calculation |
|---|---|
| **Total Shifts** | Count of shifts from `dashboardShiftTable` |
| **Working Days** | Distinct dates with at least one shift |
| **Average Daily Headcount** | Sum of daily headcounts / working days |
| **Peak Headcount** | Maximum single-day headcount and the date |
| **Total Labour Hours** | Sum from `dashboardResourceLabour` |
| **Labour Hours per Working Day** | Total labour hours / working days |
| **Hours by Trade** | Breakdown of labour hours per trade/role |
| **Plant on Site** | Count of distinct plant items from `dashboardResourcePlant` |
| **Plant Utilisation** | Hours used / hours available (if data supports it) |
| **Progress vs Plan** | Actual output / planned output as % (per activity and overall, if planned data is available) |
| **Output per Working Day** | Total output / working days (per activity) |
| **Access Timeliness** | Possessions on time / total possessions as % |
| **Access Restrictions** | Count and description of restrictions encountered |

---

## Step 4: Compare Against Previous Period

Repeat the same `getCachedReport` calls from Step 2 but using the **previous period** dates calculated in Step 1.

Calculate the same KPIs for the previous period and then compute deltas:

| KPI | Current Period | Previous Period | Change | Direction |
|---|---|---|---|---|
| Total Shifts | [value] | [value] | [+/- value] | [up/down arrow or text] |
| Avg Daily Headcount | [value] | [value] | [+/- value] | ... |
| Total Labour Hours | [value] | [value] | [+/- value] | ... |
| Progress % | [value] | [value] | [+/- pp] | ... |
| Access Timeliness | [value] | [value] | [+/- pp] | ... |

If no data exists for the previous period, note: "No prior period data available for comparison — this may be the first reporting period for this project."

---

## Step 5: Scan Narratives for Key Issues

Scan the `dashboardNarrative` entries retrieved in Step 2g. Use the canonical keyword list in **Pattern 10 (Contractual Event Keywords)** from `../../shared/patterns/10-contractual-event-keywords.md` — do not maintain a separate keyword list here. Pattern 10 covers Access/possession, Instructions/changes, Standing/delay, Physical conditions, Third party, Information, and Weather categories.

Apply the Pattern 10 **false-positive rule**: a keyword hit qualifies only if the sentence describes work being prevented, disrupted, or changed. Discard routine-operation matches (e.g. "waiting for concrete to cure", "toolbox talk instruction", "delivery delayed 10 minutes").

For safety items (not in Pattern 10), additionally note any mention of "incident", "near miss", "accident", "injury" — flag these for awareness only, not as commercial events.

Compile a list of notable events with their dates, the supervisor who recorded them, and a brief summary of the issue.

---

## Step 6: Present the Commercial Report

Read `references/output-template.md` and use its
exact structure. Fill every placeholder `[…]` with data; do not add, remove, or reorder
sections. Apply **Pattern 8 (Report Numbering)** from
`../../shared/patterns/08-report-numbering.md` for the `CR-[NNN]`
reference.

---

## Formatting Rules

- All numbers rounded to sensible precision: hours to 1 decimal place, percentages to whole numbers, quantities to the unit recorded.
- Where data is unavailable for a section, retain the section header and state: "No [data type] data recorded for this period."
- Direction arrows: ↑ = increase, ↓ = decrease, → = stable (within ±5%).
- The report must be self-contained — a reader should not need to query further to understand the period's commercial position.

---

## Related Skills

After presenting the report, suggest these related skills for deeper analysis:

- `$benchmark` — Compare this project's performance against other projects in the portfolio
- `$delay-analysis` — Deep-dive into delays and disruption events identified in this report
- `$programme` — Detailed programme and milestone analysis with forecast completion dates
- `$labour` — Granular labour analysis by person, trade, and shift pattern
- `$estimator` — Derive unit rates from the labour and progress data in this report
