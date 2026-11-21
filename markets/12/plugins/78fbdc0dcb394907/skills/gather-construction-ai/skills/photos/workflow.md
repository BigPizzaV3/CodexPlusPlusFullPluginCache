---
name: photos
description: Build a chronological photo/evidence timeline from shift records — dates,
  locations, supervisor attribution, for progress review or claims. Invoke explicitly
  (`$photos`); not model-invoked — expensive per-record fan-out.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Photos

Build a chronological photo and evidence timeline from shift records — listing all attached images with their dates, locations, supervisor attribution, and associated narrative context. This skill is used for building photographic evidence records, reviewing site progress documentation, and assembling photo evidence for claims.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

**Project resolution:**

1. Parse `the user’s request` for a project name, a date range, and an optional search term.
   - Example inputs: `"Alpha January 2026"`, `"Beta last week drainage"`, `"Gamma 2026-01-01 to 2026-01-31 concrete pour"`
   - A search term (if present) is typically the last word or phrase after the date range.
2. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
3. Once resolved, store the project UUID and name for all subsequent calls.

**Date range:**

1. Parse the date range using **Pattern 2 (Date Range Parsing)** from `../../shared/patterns/02-date-range-parsing.md`.
2. If no date range is specified, default to **last 4 weeks**.
3. Confirm the interpreted parameters: "I'll retrieve photos for **[Project Name]** from **[start date]** to **[end date]**[, filtering for '[search term]' if specified]. Proceed?"

---

## Step 2: Retrieve Narrative Data with Image Links

Call `getCachedReport` with **Report name:** `dashboardNarrative` for the resolved project and
date range — this carries narrative comments **and image links (asset UUIDs)** per shift
without a per-record fetch. Also call `getCachedReport` for `dashboardShiftTable` (same
project/period) for supervisor and location context per shift.

Collect every asset UUID found in the narrative data, keyed by shift date, and set aside the
narrative excerpt each image is attached to.

---

## Step 3: Resolve Asset URLs (`bulkGetAssets`) and Fill Gaps

Call `mcp__gather__bulkGetAssets` with the collected UUIDs, batched at **up to 100 per call**,
to get signed URLs (valid 1 hour) — this replaces a per-record `getShiftRecord` fetch for every
photo.

**Only if** a shift's asset UUIDs are not resolvable from the narrative data (no image links
present in Step 2 for that shift, or the field name / caption a photo was attached to is needed
and isn't in the narrative), fall back to `getShiftRecord` for **that shift only**. Pace any
such fallback loop at 2 requests per second per **Pattern 4 (Pagination and Rate Limits)** from
`../../shared/patterns/04-pagination-rate-limits.md`, and if more than
**~25** records would need it, state the cost and ask first: "This needs [N] individual record
fetches (~[N/2]s). Proceed?" Quote **only the asset and narrative-excerpt fields** from each
`getShiftRecord` result into the transcript — never the full record JSON.

**Extract per photo:** shift date/time, supervisor, location (from Step 2's shift-table data),
asset reference, signed URL (from `bulkGetAssets`), field name and caption (from narrative data
or the Step 3 fallback), and the associated narrative excerpt.

---

## Step 4: Build the Photo Timeline

From all extracted data, build a master list of every photo/image found across all shift records.

For each photo entry, record:
1. **Date** — the shift date
2. **Time** — shift time if available, otherwise just the date
3. **Location** — from the shift record's location field
4. **Supervisor** — who recorded the shift containing this photo
5. **Field name** — which form field the photo was attached to (provides context on what the photo documents)
6. **Caption/description** — any text directly associated with the image
7. **Narrative context** — the relevant portion of the shift narrative that relates to this image
8. **Asset reference** — the asset ID or reference code
9. **Download URL** — the URL where the image can be accessed

Sort the complete list chronologically (earliest first).

---

## Step 5: Apply Search Filter (if specified)

If the user specified a search term in `the user’s request`:

1. Filter the photo list to only include entries where:
   - The **narrative context** contains the search term (case-insensitive), OR
   - The **caption/description** contains the search term, OR
   - The **field name** contains the search term, OR
   - The **location** contains the search term
2. Report how many photos matched: "Found [N] photos matching '[search term]' out of [total] total photos."
3. If no photos match the search term, show the filter result as empty and suggest: "No photos matched '[search term]'. Try a broader term, or remove the filter to see all [total] photos."

---

## Step 6: Present the Photo Evidence Log

### Summary

| Metric | Value |
|---|---|
| **Project** | [project name] |
| **Period** | [start date] to [end date] |
| **Total Shift Records Reviewed** | [count] |
| **Total Photos Found** | [count] |
| **Photos Matching Filter** | [count] (only if a search filter was applied) |
| **Date Range of Photos** | [earliest photo date] to [latest photo date] |
| **Supervisors Contributing** | [list of distinct supervisors] |

### Chronological Evidence Log

Group photos by date. Present each date as a **numbered list**, not a table — long asset URLs corrupt table layouts, so give each photo its own entry with the URL on its own line:

**[Date — e.g., Monday 13 January 2026]**

1. **[time]** — [location] — [supervisor] — field: [field name]
   - Description: [caption or narrative excerpt]
   - Asset ref: [ref]
   - URL: [url]
2. **[time]** — [location] — [supervisor] — field: [field name]
   - Description: [caption or narrative excerpt]
   - Asset ref: [ref]
   - URL: [url]

**[Date — e.g., Tuesday 14 January 2026]**

3. **[time]** — [location] — [supervisor] — field: [field name]
   - Description: [caption or narrative excerpt]
   - Asset ref: [ref]
   - URL: [url]

Continue for each date that has photos, keeping the numbering continuous across dates.

### By Location (Alternative Grouping)

If the data contains meaningful location information, also provide a location-grouped summary:

| Location | Photo Count | Date Range | Supervisors |
|---|---|---|---|
| [location] | [count] | [first] to [last] | [names] |

### By Supervisor

| Supervisor | Photo Count | Date Range |
|---|---|---|
| [name] | [count] | [first] to [last] |

---

## Constraints and Important Notes

- **Bulk asset resolution first:** `bulkGetAssets` (up to 100 UUIDs/call) resolves signed URLs without a per-record fetch. Only the fallback path in Step 3 is rate-limited per **Pattern 4** (25/page at 2 req/s) and carries its own confirmation gate — do not restate those limits elsewhere.
- **Asset references, not images:** Signed URLs are valid for 1 hour. Use the host’s supported image preview when available; otherwise provide source links. Make this clear to the user: "The URLs below link to the original images in Gather (valid ~1 hour). Open them in a browser to view."
- **Narrative context:** Always include the associated narrative text with each photo. The narrative provides the "what and why" context that makes the photo useful as evidence.
- **Large result sets:** If more than 200 photos are found, present the first 50 in the chronological log and provide the summary tables (by location, by supervisor) for the full set. Offer to show additional pages of photos on request.

---

## Related Skills

After presenting the photo evidence log, suggest these related skills for further investigation:

- `$diary` — Read the full shift diary entries that contain these photos for complete narrative context
- `$narrative-search` — Search shift narratives for specific keywords across all records
- `$record` — View the complete details of a specific shift record referenced in the photo log
- `$progress` — Review progress data alongside the photographic record to correlate visual evidence with reported output
