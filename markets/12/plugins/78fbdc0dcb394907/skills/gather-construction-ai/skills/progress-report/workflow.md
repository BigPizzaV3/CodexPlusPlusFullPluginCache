---
name: progress-report
description: Generates a formal progress report for a period — progress metrics, narrative
  evidence, workforce summary, look-ahead — for client or management submission. Explicit
  invocation only ($progress-report); ad-hoc questions use progress.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Progress Report

Generate a structured progress report for a project period — the kind submitted to a client, included in a monthly report, or presented at a progress meeting. This combines progress metrics with supporting narrative evidence, workforce context, and a forward look.

This skill differs from `$progress` (which analyses planned vs actual in detail) and `$commercial-report` (which focuses on commercial KPIs). The progress report is a narrative-led document that tells the story of what happened, what was achieved, and what comes next.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

Apply **only checks 1 (unit consistency) and 5 (rounding and reconciliation) of Pattern 9 (Commercial QA Gate)** from `../../shared/patterns/09-commercial-qa-gate.md` before finalising quantities and rates. This report carries no money — the currency/VAT (check 2), baseline-budget (check 3), and variation-status (check 4) checks do not apply and must not be invoked here.

---

## Step 1: Resolve Project and Reporting Period

**Project resolution:**

1. Parse `the user’s request` for a project name and a reporting period.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Period resolution:**

1. Parse the remaining arguments for a date range using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no period is specified, default to **last 4 weeks**.
3. Per **Pattern 2**, confirm the interpreted period only if the input required non-trivial interpretation (e.g. "I'll generate the progress report for **[Project Name]** covering **[start date] to [end date]**. Proceed?"). Exact dates, named months, and clearly stated periods proceed without confirmation.

---

## Step 2: Retrieve Data (parallel calls)

Make the following `getCachedReport` calls **in parallel** for the resolved project and reporting period:

### 2a: Progress (`dashboardProgress`)
Extract: output achieved per activity, planned output (if available), planned vs actual variance, percentage complete.

### 2b: Shift Activity (`dashboardShiftTable`)
Extract: total shift count, working days, supervisors active, shift dates.

### 2c: Labour (`dashboardResourceLabour`)
Extract: total labour hours, headcount by trade/role, average daily headcount, peak headcount.

### 2d: Narratives (`dashboardNarrative`)
Extract: all narrative text from the period — this provides the contemporaneous record of what happened each day.

### 2e: Access (`dashboardAccessPossession`)
Extract: possessions requested, granted, timeliness, any restrictions.

Follow **Pattern 3 (Empty Data Handling)** for any report returning no data. Continue with available data.

---

## Step 3: Build the Period Narrative

From the narrative data (2d), construct a chronological summary of the period:

1. **Group narratives by week** (or by day for weekly reports)
2. For each week/day, summarise:
   - Key activities undertaken
   - Milestones achieved or missed
   - Issues encountered (delays, access problems, weather, design issues)
   - Instructions received or changes notified
3. Use the actual words from the diary records — this is contemporaneous evidence. Quote significant entries directly.

---

## Step 4: Summarise Progress Against Plan

From the progress data (2a):

1. For each activity with planned and actual data, calculate variance and status (Ahead / On Track / Behind / Critical — using the same thresholds as `$progress`)
2. Calculate overall progress percentage (weighted by planned quantities if available)
3. Identify the **top 3 achievements** (activities furthest ahead or with the most output) and **top 3 concerns** (activities furthest behind)

If planned data is not available, report actual output achieved and note: "Planned targets are not available — progress is reported as actual output only."

---

## Step 5: Summarise Workforce

From the labour data (2c):

1. Average daily headcount and trend (stable / ramping up / ramping down)
2. Peak headcount and the date
3. Trade mix — which trades were active and their proportion of total hours
4. Any days with zero or unusually low headcount (potential stand-downs or non-working days)

---

## Step 6: Identify Key Events and Issues

From the narratives (Step 3) and access data (2e), compile a list of significant events:

- Access delays or cancellations
- Weather impacts
- Instructions or changes received
- Safety events
- Plant breakdowns or resource issues
- Any event that affected progress

For each event, note the date and a brief description.

---

## Step 7: Look-Ahead

Based on the data and trends observed:

1. **Next period priorities** — what activities should be the focus based on current progress status?
2. **Resources needed** — based on headcount trends and activities behind schedule, is the current workforce sufficient?
3. **Risks** — flag any issues from the period that are likely to continue (recurring access delays, weather season, design issues)
4. **Recovery actions** — for any activity significantly behind, what run rate would be needed to recover?

Note: the look-ahead is based on trends from the reporting period. It is not a programme forecast — for that, suggest `$programme`.

---

## Step 8: Present the Progress Report

At Step 8, read `references/output-template.md` for the exact report structure (Executive Summary, Period Narrative, Progress, Workforce, Access & Possession, Key Events, Look-Ahead, Caveats). Fill every placeholder with data; do not add, remove, or reorder sections. Apply **Pattern 8 (Report Numbering)** for the `Ref: PR-[NNN]` line.

---

## Related Skills

- `$progress` — Detailed planned vs actual analysis with productivity rates
- `$programme` — Programme health, milestone analysis, and forecast completion
- `$commercial-report` — Operational commercial report aggregating resources, progress, and access (no cost/value data)
- `$labour` — Granular labour analysis by person and trade
- `$photos` — Photo evidence timeline to support the progress narrative
