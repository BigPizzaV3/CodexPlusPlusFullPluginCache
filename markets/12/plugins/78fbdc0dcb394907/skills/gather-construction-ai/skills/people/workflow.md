---
name: people
description: Show workforce roster, headcount trends, mobilisation/demobilisation
  — who's on site, when they started/stopped, staffing levels. Not hours/effort/overtime
  (use labour).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# People

Show workforce roster, headcount trends, and mobilisation/demobilisation patterns for a project. Answers questions like "who is on site?", "when did they start?", "how has headcount changed?", and "what trades are represented?".

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

**Project resolution:**

1. Parse `the user’s request` for a project name and an optional date range.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Date range:**

1. Parse the remaining arguments for a date range using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no date range is specified, default to **last 4 weeks**.
3. Per **Pattern 2**, confirm the interpreted date range only if the input required non-trivial interpretation (e.g. "I'll show workforce data for **[Project Name]** from **[start date]** to **[end date]**. Proceed?"). Exact dates, named months, and clearly stated periods proceed without confirmation.

---

## Step 2: Retrieve the Workspace People List (optional enrichment)

`getPeople` returns the workspace master roster — all people who could potentially appear in shift records. It is used only to **enrich** trade/role and identifying details; the actual on-site presence comes from the labour and shift data in Steps 3–4. **Skip it by default** — proceed straight to Step 3 and note that trade/role comes from the labour data. **Only fetch it** if, after Step 3, trade/role turns out missing or sparse in the labour data and the user's request depends on it (e.g. explicitly asks for company/team affiliation `getPeople` alone carries).

**Pagination (Pattern 4).** `getPeople` is paginated at **100 per page**. A workspace with more than 100 people is silently truncated if you read only the first page. Loop: make the first call, check whether the response indicates more pages, and keep fetching until all people are retrieved before building the master list. If the total is large (several hundred), that is itself a reason to prefer the optional-skip path above.

Key fields to extract per person:
- Name
- Trade / role / job title
- Any other identifying fields (company, team, etc.)

Store the full list for cross-referencing in later steps.

If `getPeople` returns no data, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md` and inform the user: "No people records found in this workspace. People may not have been configured in Gather." (Presence analysis can still proceed from the labour and shift data.)

---

## Step 3: Retrieve Labour Records

Call `getCachedReport` with the following parameters:
- **Report:** `dashboardResourceLabour`
- **Project:** the resolved project UUID
- **Date range:** the confirmed start and end dates

This returns actual labour records showing which people worked on which days, their hours, and their trade/role.

**Extract per person per day:**
- Person name/identifier
- Date
- Hours worked
- Trade/role (as recorded in the labour data)

If this report returns no data, follow **Pattern 3 (Empty Data Handling)** — state that no labour records were found and suggest possible causes.

---

## Step 4: Retrieve Shift Attendance

Call `getCachedReport` with the following parameters:
- **Report:** `dashboardShiftTable`
- **Project:** the resolved project UUID
- **Date range:** the confirmed start and end dates

This provides shift-level attendance data that complements the labour data from Step 3.

**Extract:**
- Shift dates with attendees
- Supervisor per shift
- Any additional attendance metadata

Cross-reference with the labour data from Step 3 to build a complete picture of each person's on-site presence.

---

## Step 5: Build the Workforce Roster

For each person who appears in the labour records (Step 3) or shift attendance (Step 4):

1. **First appearance (mobilisation date):** The earliest date this person appears in any record within the date range. If their first appearance is the start of the date range, note "(or earlier — may predate the selected range)".
2. **Last appearance:** The latest date this person appears. Compare it to the **query range end** (the `to` date), **not** today — this keeps the status correct for historical ranges. If the last appearance is within 3 days of the range end, mark as **"Still active"** (i.e. still present at the end of the analysed window). Otherwise, show the date and note it as a potential demobilisation date. When the range end is in the past, phrase the status as "active at end of period" rather than implying present-day presence.
3. **Total days on site:** Count of distinct dates this person appears in records.
4. **Total hours:** Sum of hours from `dashboardResourceLabour` for this person.
5. **Trade/role:** From the labour data or the `getPeople` master list. If both sources provide a role, prefer the labour data (it reflects what they actually did on site).
6. **Average hours per day:** Total hours / total days on site.

Sort the roster by first appearance date (earliest first) to show mobilisation order.

---

## Step 6: Calculate Headcount Trends

Using the daily data from Steps 3 and 4, calculate:

### Daily Headcount
- For each date in the range, count the number of distinct people who worked.
- Identify the **peak headcount** (highest single-day count and the date).
- Identify the **lowest headcount** (excluding non-working days such as weekends if apparent from the data).
- Calculate the **average daily headcount** across all working days.

### Weekly Headcount
- Group daily headcount by week (Monday to Sunday).
- Show headcount per week to visualise the trend.

### Headcount by Trade
- For each trade/role, count the number of distinct people and their combined hours.
- Calculate the percentage of total headcount per trade.

### Mobilisation/Demobilisation Events
Identify significant changes in headcount between consecutive working days or weeks. Scale the threshold to the size of the workforce so it is meaningful on both small and large projects:
- Let **threshold = max(3, round(0.15 × average daily headcount))** — at least 3 people, or 15% of the average daily headcount if that is larger.
- A **mobilisation event** is a day where headcount increased by **threshold or more** compared to the previous working day (equivalently, a week where headcount rose by threshold or more over the prior week).
- A **demobilisation event** is the inverse — a decrease of threshold or more.
- For each event, note the date, the change magnitude, and (if identifiable) the people who joined or left.

---

## Step 7: Present the Results

### Workforce Roster

| # | Name | Trade/Role | First Day | Last Day | Status | Days on Site | Total Hours | Avg Hrs/Day |
|---|---|---|---|---|---|---|---|---|
| 1 | [name] | [trade] | [date] | [date] | Active / Left | [count] | [hours] | [avg] |
| 2 | ... | | | | | | | |

Sort by first appearance date. Bold any person still active.

### Headcount Summary

| Metric | Value |
|---|---|
| **Total Individuals** | [count of distinct people] |
| **Average Daily Headcount** | [value] |
| **Peak Headcount** | [value] on [date] |
| **Lowest Headcount** | [value] on [date] |
| **Current Headcount** | [most recent day's count] |

### Headcount by Trade

| Trade/Role | Headcount | % of Total | Total Hours | % of Hours |
|---|---|---|---|---|
| [trade] | [count] | [%] | [hours] | [%] |
| **Total** | [total] | 100% | [total hours] | 100% |

### Weekly Headcount Trend

| Week Commencing | Headcount | Change | Trend |
|---|---|---|---|
| [date] | [count] | — | — |
| [date] | [count] | [+/- N] | [up/down/stable] |
| ... | | | |

### Mobilisation / Demobilisation Events

| Date | Event | Change | Details |
|---|---|---|---|
| [date] | Mobilisation | +[N] people | [names or trades if identifiable] |
| [date] | Demobilisation | -[N] people | [names or trades if identifiable] |

If no significant mobilisation/demobilisation events are detected, state: "No significant mobilisation or demobilisation events detected in this period — headcount was relatively stable."

---

## Formatting Notes

- Use Markdown tables throughout for consistency.
- Round hours to 1 decimal place, percentages to whole numbers.
- If the roster exceeds 50 people, present the top 30 by days on site and offer to show the full list on request.
- Where a person appears in `getPeople` but has zero labour records in the selected period, do **not** include them in the roster — only show people who were actually active in the period.

---

## Related Skills

After presenting the results, suggest these related skills for deeper analysis:

- `$labour` — Detailed labour hours analysis including overtime and shift patterns
- `$resource-analysis` — Broader resource analysis including plant and material alongside workforce
- `$commercial-report` — Full period report that includes workforce data alongside progress and other resource summaries
