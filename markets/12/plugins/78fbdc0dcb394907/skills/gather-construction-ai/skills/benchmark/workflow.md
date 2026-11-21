---
name: benchmark
description: Compares performance across projects — labour productivity, resource
  utilisation, progress rates — to identify best/worst performers, for portfolio trends
  and senior management reporting.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Benchmark

Compare performance metrics across multiple projects — labour productivity, resource utilisation, progress rates, and allocation accuracy — to identify best and worst performers in a portfolio. Produces a side-by-side comparison suitable for senior management reporting.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Identify Projects to Compare

**If `the user’s request` contains project names:**

1. Parse `the user’s request` for two or more project names. Project names may be separated by commas, "and", "vs", or spaces followed by a date range.
   - Example inputs: `"Alpha, Beta, Gamma Q4 2025"`, `"Alpha vs Beta last month"`, `"Alpha Beta January 2026"`
2. For each project name, resolve it using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`:
   - Call `getMyProjects` and fuzzy-match each name.
   - If a name does not match the user's projects, call `getProjects` (all workspace projects) and try again.
   - If any name remains ambiguous, list the candidates and ask the user to clarify before proceeding.
3. Store each resolved project's UUID and name.

**If `the user’s request` is empty or contains fewer than two project names:**

1. Call `getMyProjects` to retrieve the user's assigned projects.
2. If the user has two or more projects, list them and ask: "Which projects would you like to compare? Select two or more by name or number, or type **all** to benchmark all of them."
3. If the user has only one project, inform them: "Benchmarking requires at least two projects. You currently have one project assigned. You can also specify projects by name from the workspace — would you like me to list all workspace projects?"
4. If the user selects "all", use every project returned by `getMyProjects`.

---

## Step 2: Confirm Comparison Period

1. Parse the remaining `the user’s request` (after extracting project names) for a date range using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no period is specified, default to **last 4 weeks**.
3. Per **Pattern 2**, confirm the interpreted date range only if the input required non-trivial interpretation (e.g. "I'll benchmark **[Project A]**, **[Project B]**[, ...] for the period **[start date] to [end date]**. Proceed?"). Exact dates and clearly stated periods proceed without confirmation.
4. The same date range will be applied to all projects for a fair comparison.
5. **Confirm the projects are genuinely comparable** before ranking: projects with different shift patterns, scopes, or activity types are not directly comparable. Ask, e.g.: "These projects should share a broadly similar shift pattern and work type for the ranking to be meaningful — for example a 24/7 rail-possession project and a Mon–Fri civils project are not directly comparable. Are these projects comparable, or would you prefer an unranked side-by-side?"

> **API call volume:** Step 3 makes **4 `getCachedReport` calls per project**, so benchmarking N projects is **4 × N calls** (e.g. 6 projects = 24 calls). Before a large fan-out (roughly 5+ projects / 20+ calls), warn the user and confirm: "Benchmarking [N] projects requires about [4×N] API calls. Proceed, or reduce the number of projects?"

---

## Step 3: Collect Data for Each Project

For **each** resolved project, make the following `getCachedReport` calls using the confirmed date range:

### 3a: Labour Data
- **Report:** `dashboardResourceLabour`
- **Extract per project:** total labour hours, daily headcount figures, average daily headcount, peak headcount, hours by trade/role.

### 3b: Progress Data
- **Report:** `dashboardProgress`
- **Extract per project:** output achieved per activity, planned output (if available), planned vs actual variance.

### 3c: Allocation Data
- **Report:** `dashboardAllocation`
- **Extract per project:** planned resource allocation vs actual allocation, variance.

### 3d: Shift Data
- **Report:** `dashboardShiftTable`
- **Extract per project:** total shifts, working days (distinct dates with shifts), active supervisors.

**Empty data handling:** If a report returns no data for a particular project, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`. Include the project in the comparison table but mark the affected metrics as "No data" rather than excluding the project entirely. Note at the bottom which projects had data gaps.

---

## Step 4: Calculate Comparable Metrics

For each project, calculate the following standardised metrics so projects of different sizes and durations can be compared fairly:

| Metric | Calculation | Unit |
|---|---|---|
| **Labour Hours per Working Day** | Total labour hours / working days | hrs/day |
| **Average Daily Headcount** | Sum of daily headcounts / working days | persons |
| **Peak Headcount** | Maximum single-day headcount | persons |
| **Output per Labour Hour** | Total output quantity / total labour hours (per activity where output data exists) | units/hr |
| **Output per Working Day** | Total output quantity / working days | units/day |
| **Planned vs Actual Variance (Labour)** | (Actual hours − Planned hours) / Planned hours as %. **Planned hours source: `dashboardAllocation` (3c)** — the planned resource allocation. Actual hours from `dashboardResourceLabour` (3a). If `dashboardAllocation` does not expose planned labour hours for the project (verify per **Pattern 12**), mark this metric "N/A — no planned-allocation data" and exclude it from ranking; do not fabricate a planned figure. | % |
| **Planned vs Actual Variance (Progress)** | (Actual output − Planned output) / Planned output as %. Source: `dashboardProgress` (3b). | % |
| **Allocation Accuracy** | Actual allocation / planned allocation as %. Source: `dashboardAllocation` (3c). | % |
| **Shifts per Working Day** | Total shifts / working days | shifts/day |
| **Trend Direction** | Compare first half of period to second half — is the metric improving, stable, or declining? | up/stable/down |

If planned data is not available for a project, mark planned-dependent metrics as "N/A" and note this in the output. **Divide-by-zero guard (Pattern 12):** any variance or ratio whose denominator is zero (planned = 0, output = 0, labour hours = 0) renders as "n/a" with a data-quality flag, never as a number.

---

## Step 5: Rank Projects

Rank only metrics that have a valid better/worse direction **and** are comparable across projects. Some metrics are **context-only** and must not be ranked or given a "Best".

**Directional (rankable) metrics:**
- **Allocation accuracy:** Closer to 100% = better (both over- and under-allocation are inefficiencies).
- **Planned vs Actual variance (labour and progress):** Closer to plan = better.
- **Output per Labour Hour / Output per Working Day:** Higher = better — **but only within a single activity measured in the same unit** (see the output-metric rule below).

**Context-only (NOT ranked, no "Best"):**
- **Labour Hours per Working Day**, **Average Daily Headcount**, **Peak Headcount**, **Working Days**, **Total Labour Hours**, **Shifts per Working Day** — these are **scale/size** metrics with no better/worse direction (a bigger crew is not "better" than a smaller one). Report them side by side for context only; leave the "Best" column as "—".
- **Trend Direction** — reported per project (↑/→/↓) for context and used in the narrative, but not given an ordinal rank or a "Best".

**Output-metric rule (critical — Fix for cross-unit ranking):** raw output metrics (**Output per Working Day**, **Output per Labour Hour**) are only comparable **between projects doing the same activity in the same unit**. You **cannot** rank m³ of excavation against metres of cable or m² of formwork, and you must not crown a "Best" across mismatched units.
- Group output metrics by **activity + unit**. Rank a project against others **only** where they share the same activity and unit.
- Where units do not match across the projects being compared, report the output figures **per project, UNRANKED**, and state: "Output metrics are reported per project only — activities/units differ between projects, so a cross-project output ranking is not valid."

Assign each project an ordinal rank (1st, 2nd, 3rd...) **per rankable metric only**.

**Overall rank — minimum-data qualification (Fix):** an average of per-metric ranks is only meaningful if projects are ranked on the **same set of metrics**. Averaging over different metric sets (because some projects are missing data) is invalid. There are **5 rankable metrics** (Output/Working Day, Output/Labour Hour, Plan vs Actual Labour, Plan vs Actual Progress, Allocation Accuracy). Require each project to have a valid rank on **at least 4 of the 5 rankable metrics** to receive an overall rank. Projects below that threshold are listed as **"insufficient data to rank"** and excluded from the overall ranking (but still shown in the comparison table). State the qualifying metric count for each project.

---

## Step 6: Present the Benchmark Comparison

Read `references/output-template.md` and use its exact
structure. Fill every placeholder `[…]` with data; do not add, remove, or reorder sections.
Apply **Pattern 8 (Report Numbering)** from
`../../shared/patterns/08-report-numbering.md`.

---

## Formatting Rules

- Round hours to 1 decimal place, percentages to whole numbers, output quantities to appropriate precision.
- Direction arrows: ↑ = improving, ↓ = declining, → = stable.

---

## Related Skills

After presenting the benchmark, suggest these related skills for deeper analysis:

- `$commercial-report` — Generate a full commercial period report for any individual project in the comparison
- `$estimator` — Derive detailed unit rates for a specific project to understand productivity differences
- `$programme` — Analyse programme and milestone performance for projects flagged as behind
- `$labour` — Detailed labour breakdown for a specific project to understand headcount and trade composition
