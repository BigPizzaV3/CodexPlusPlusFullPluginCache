---
name: record
description: Look up a specific shift record by ID — displays workers, weather, narratives,
  photos. Use when the user supplies or has just been shown a shift record ID.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Shift Record Detail

Look up a single shift record by its UUID and display every field in a structured, readable format. This skill is the deepest level of detail available for a diary entry — it renders all answer types including text, dates, lists, and image attachments.

Follow the shared patterns: `../../shared/patterns/03-empty-data-handling.md` (empty data handling).

---

## Step 1: Extract the Shift Record ID

Extract the shift record ID from `the user’s request`.

**Acceptance rule:** accept any token that looks like a record identifier — do not enforce a strict UUID format. If `the user’s request` contains an ID-like token, use it directly as the record identifier for the API call in Step 2 and let the API reject it if it is invalid (handled in Step 2).

**If `the user’s request` contains extra text alongside the ID** (e.g., "show me the details for 1a2b3c4d-..."):
- Extract just the ID-like token and ignore surrounding text.

**If `the user’s request` is empty or contains no ID-like token:**
- Do **not** guess or assume a record ID.
- Ask the user to provide one:
  > "Please provide a shift record ID. If you don't have one, you can use `$diary` to search for shift records and find the ID you need."
- Stop here and wait for user input before proceeding.

---

## Step 2: Fetch the Shift Record

Call `getShiftRecord` with the extracted ID from Step 1.

**If the call succeeds**, proceed to Step 3 with the full response data.

**If the call fails or returns an error** (e.g., record not found, invalid UUID, permission denied):
- State clearly what went wrong: "Could not retrieve shift record [UUID]. [Error message from API]."
- Suggest possible causes:
  - The UUID may be incorrect — double-check it or use `$diary` to find the correct ID.
  - The record may belong to a project you do not have access to.
  - The record may have been deleted.
- Follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md` for guidance on presenting empty or error results.

---

## Step 3: Domain Field Semantics

The record carries these Gather-specific fields — extract each for presentation in Step 4:

- **Simple fields:** supervisor name, weather conditions, temperature (with unit), wind, location, general notes.
- **Shift start/end time and date recorded:** calculate shift duration as end minus start, in hours and minutes (e.g. "10h 30m") — handle a shift spanning midnight correctly (end time is the following day). Format times as "07:30" and dates as "15 January 2026".
- **Photos:** an asset reference (ID, download URL, description/caption, filename) per attached image. Preserve download URLs exactly as returned — do not modify or truncate them.
- **Worker/equipment/material lists:** worker rows carry name, role/trade, hours worked, and possibly start/end times; equipment rows carry type, hours used, operator; material rows carry description, quantity, unit.

---

## Step 4: Present the Structured Output

Combine all parsed data into a clear, sectioned format. Use the following structure:

---

### Shift Details

| Field | Value |
|---|---|
| **Record ID** | [the UUID used to fetch this record] |
| **Date** | [shift date, formatted as "15 January 2026"] |
| **Supervisor** | [supervisor name] |
| **Location** | [location/zone, or omit row if not recorded] |
| **Start Time** | [formatted start time, e.g., "07:30"] |
| **End Time** | [formatted end time, e.g., "18:00"] |
| **Duration** | [calculated duration, e.g., "10h 30m"] |

### Weather

| Field | Value |
|---|---|
| **Conditions** | [weather description] |
| **Temperature** | [value with unit] |
| **Wind** | [wind description] |

If no weather data was recorded for this shift, omit this section entirely.

### Narrative

> [Full supervisor notes and observations, presented as a blockquote]
>
> [If the narrative spans multiple paragraphs, preserve the paragraph breaks]

If no narrative was recorded, omit this section entirely.

### Workers

Present the worker list as a table. Include all sub-fields available in each row:

| Name | Role/Trade | Hours | Start | End |
|---|---|---|---|---|
| John Doe | Excavator Operator | 8.0 | 07:30 | 15:30 |
| Sarah Lee | General Labourer | 10.5 | 07:00 | 17:30 |
| Mike Chen | Steel Fixer | 8.0 | 07:30 | 15:30 |

Below the table, include a summary:
> **[N] workers** on this shift. **Total hours: [sum of all worker hours]**.

If start/end times are not available for workers, omit those columns. If no workers were recorded, omit this section entirely.

### Photos/Assets

List each attached image with its description and download URL:

- **[Description or filename]** — [download URL]
- **[Description or filename]** — [download URL]

If an image has no description, use the filename. If neither is available, label it as "Photo 1", "Photo 2", etc.

> **[N] photos** attached to this record.

If no photos were attached, omit this section entirely.

### Tags

Display any tags applied to this record as a comma-separated list:

> **Tags:** day-shift, civils, section-3

If no tags are present, omit this section entirely.

---

## Presentation Rules

1. **Omit empty sections** — if a section has no data (no weather, no photos, no narrative), leave it out entirely. Do not show empty tables or placeholder text like "N/A".
2. **Preserve data fidelity** — display all values exactly as returned by the API. Do not round numbers, truncate text, or modify URLs.
3. **Calculate derived values** — shift duration and total worker hours should be calculated and presented even though they are not explicit fields in the response.
4. **Format consistently** — use the same date format, time format, and table style throughout the output.

---

## Related Skills

After presenting the record, suggest these related skills for further exploration:

- `$diary` — Search for more shift records around the same date or from the same supervisor
- `$narrative-search` — Find other records mentioning the same issues, locations, or keywords from this narrative
