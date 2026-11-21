# Pattern 4: Pagination and Rate Limits

`getShiftRecords` returns a maximum of 25 records per page and is rate-limited to **2 requests per second** — pace multi-page fetches and per-record `getShiftRecord` loops accordingly, and warn the user of the approximate wait before starting a large loop (a 50-record detail fetch takes roughly 25 seconds). `getPeople` is also paginated at **100 per page** — workspaces with more than 100 people require additional pages. Handle pagination as follows:

1. Make the first call — check if the response indicates more pages
2. If more pages exist, continue fetching until all records are retrieved
3. If the total exceeds 100 records, warn the user:
   "Found [N] shift records for this period. Fetching all of them will require [N/25] API calls. Do you want to proceed, or narrow the date range?"
4. For skills that only need summary data (not individual records), prefer `getCachedReport` with `dashboardShiftTable` instead — it returns aggregated data without pagination limits

**Skills affected by pagination:** `diary`, `photos`, `delay-analysis` (when pulling individual records), `narrative-search` (when following up matches with full records), `weather-impact` (when pulling individual records for weather detail).

**Skills NOT affected:** Any skill that exclusively uses `getCachedReport` (labour, progress, access, resource-analysis, estimator, commercial-report, benchmark, programme). Dashboard reports are returned as a single response — but a wide date range returns one large payload, so keep ranges to about one month per call. Note: `people` **is** affected via `getPeople` (100 per page), and `delivery-notes` mines shift records so Pattern 4 applies to it.

**Re-runs within a session or day:** call `getShiftRecords` with `limit` at its default working value (≤25) and pass `modifiedSince` (ISO 8601 timestamp of the last fetch) so a re-run only returns records that changed since — never re-pull an unchanged period from scratch. `getMyProjects` similarly takes `limit`/`page`; page it rather than assuming a single page covers every project.

**Quote what you use, not the whole record:** once a `getShiftRecord` result is fetched, quote into the transcript only the specific fields the downstream step actually needs (e.g. the narrative excerpt, the tag, the timestamp) — never paste the full JSON object. This applies wherever Pattern 4 applies.
