---
name: diary
description: Search, list and summarise diary shift records — shifts, what happened
  on site, supervisor records. Not keyword/theme searches across narratives (use narrative-search)
  or a single known record ID (use record).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Site Diary — Shift Records

Search, list, and summarise shift records from the Gather site diary. This skill handles everything from broad "show me last month's shifts" queries to specific "what happened on Tuesday" drill-downs.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve the Project

Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.

Parse `the user’s request` to identify the project name portion. The arguments may contain a mix of project name, date range, and supervisor name — separate them before resolving:

- **Project name** — typically the first word(s) that match a known project
- **Date range** — phrases like "last week", "January", "2026-01-15 to 2026-02-15"
- **Supervisor name** — a person's name not matching a project, often preceded by "by" or "from" (e.g., "by Tom Williams")

If `the user’s request` is empty, follow Pattern 1's fallback: call `getMyProjects` and auto-select if only one project, or ask the user to choose.

---

## Step 2: Parse Date Range and Filters

Parse the date range from `the user’s request` using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.

- If an explicit date range is found (e.g., "last week", "January 2026", "2026-01-10 to 2026-01-20"), normalise it to `from` and `to` dates.
- If no date range is found in `the user’s request`, default to **last 4 weeks** (today minus 28 days to today).
- If a **supervisor name** is present in `the user’s request`, note it for filtering in Step 3. Look for patterns like:
  - "by Jane Smith"
  - "from Tom Williams"
  - A name appearing after the project name and date range
- If one or more **tags** are present in `the user’s request` (e.g., "tag:night-shift", "tagged civils", or a token matching a known tag), note them for filtering in Step 3.

Confirm the interpreted parameters with the user if any ambiguity exists (e.g., "Did you mean the project 'Alpha' or the supervisor 'Alpha Team'?"). If the input is clear and unambiguous, proceed without confirmation.

---

## Step 3: Fetch Shift Records

**For pure summary or count queries** (e.g. "how many shifts last month", "who recorded shifts") where the user has not asked to drill into specific records or apply filters that need record IDs, fetch `getCachedReport` with `dashboardShiftTable` **first** — this returns aggregated data in a single call with no pagination (Pattern 4's own advice). Only fall back to `getShiftRecords` below when individual record IDs or record-level filters are actually needed.

Call `getShiftRecords` with the following parameters:

- **Project UUID** — from Step 1
- **from** — start date from Step 2
- **to** — end date from Step 2
- **Supervisor filter** — if a supervisor name was identified in Step 2, apply it. The supervisor filter takes the supervisor **name** — pass it as the user gave it and let the API match; do not attempt to resolve it to an ID first.
- **Tags filter** — if one or more tags were identified in Step 2, apply them.

**Handle pagination and rate limits per Pattern 4 (Pagination and Rate Limits) from `../../shared/patterns/04-pagination-rate-limits.md`** — 25 records per page at 2 requests per second, and warn the user before fetching if the total exceeds 100 records, offering to narrow the date range or add a supervisor/tags filter. Wait for confirmation before fetching beyond that threshold.

**If no records are returned**, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md`:
- State clearly: "No shift records found for [project name] between [from] and [to]."
- If a supervisor filter was applied, suggest trying without the filter.
- Suggest possible causes: date range too narrow, no shifts recorded yet, wrong project.
- Offer to retry with different parameters.

---

## Step 4: Present Summary View

This is the default view for broad queries like "show me shifts", "what shifts were recorded last week", or "list diary entries".

Present all matching records as a **chronological table**:

| # | Date | Shift ID | Supervisor | Tags | Last Modified |
|---|---|---|---|---|---|
| 1 | 2026-01-15 | abc-123 | Jane Smith | day-shift, civils | 2026-01-15 18:30 |
| 2 | 2026-01-16 | def-456 | Tom Williams | night-shift | 2026-01-16 07:15 |
| 3 | 2026-01-17 | ghi-789 | Jane Smith | day-shift, rail | 2026-01-17 19:00 |

Below the table, include a summary line:

> **[N] shift records** found for **[project name]** between **[from date]** and **[to date]**. [M] distinct supervisors recorded shifts.

If results were paginated, note: "(Showing all [N] records across [P] pages.)"

If results were truncated due to the 100-record warning and the user chose not to fetch all, note: "(Showing first [N] of [total] records. Use a narrower date range to see all records.)"

---

## Step 5: Present Detail View

This view applies when the user asks for specifics: "what happened on 15 January", "show me the details for that shift", or "tell me about shift abc-123".

For each shift record being examined in detail, call `getShiftRecord` with the individual record's UUID to retrieve full field data.

**Cap on detail fetches:** if more than **5 records** would be fetched in detail, confirm with the user before starting (e.g. "This will fetch [N] full records individually, taking about [N/2] seconds. Proceed?") and pace the calls at 2 requests per second per **Pattern 4** in `../../shared/patterns/04-pagination-rate-limits.md`.

Parse **all answer types** from the response:

- **Simple fields** (text, numbers, booleans): supervisor name, weather conditions, temperature, wind speed, location, general notes. Display as key-value pairs.
- **Date/time fields** (ISO 8601 format): shift start and end times. Calculate and display the **shift duration** (e.g., "8h 30m").
- **List fields** (repeatable groups returned as arrays of row objects): worker lists with name, role/trade, hours worked. Present as a formatted table.
- **Image fields** (arrays of asset references with download URLs): photos attached to the record. List each with its description (if available) and download URL.

---

## Step 6: Format and Present Detailed Results

Present detailed shift record(s) chronologically with the following structure for each record:

### Shift: [date] — [supervisor name]

**Shift Details**

| Field | Value |
|---|---|
| **Date** | [date] |
| **Supervisor** | [name] |
| **Location** | [location, if available] |
| **Start Time** | [start time] |
| **End Time** | [end time] |
| **Duration** | [calculated duration] |
| **Tags** | [tags, or "None"] |

**Weather**

| Field | Value |
|---|---|
| **Conditions** | [weather description] |
| **Temperature** | [temperature] |
| **Wind** | [wind conditions] |

**Narrative**
> [Full supervisor notes/observations — present as a blockquote to distinguish from structured data]

**Workers ([count] on shift)**

| Name | Role/Trade | Hours |
|---|---|---|
| John Doe | Excavator Operator | 8.0 |
| Sarah Lee | General Labourer | 7.5 |

**Photos/Assets**
- [Description or filename] — [download URL]
- [Description or filename] — [download URL]

If any section has no data (e.g., no photos, no weather recorded), omit that section entirely rather than showing empty tables.

---

## Related Skills

After presenting results, suggest these related skills for further exploration:

- `$record` — View full details for a specific shift record by ID
- `$narrative-search` — Search across shift narratives for specific keywords or topics
- `$photos` — Browse a photo timeline extracted from shift records
