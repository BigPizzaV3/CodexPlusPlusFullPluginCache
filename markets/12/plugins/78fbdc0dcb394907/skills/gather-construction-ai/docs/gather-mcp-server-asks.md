# Gather MCP server — asks from the AI Quantity Surveyor plugin team

Written for the Gather MCP server team. These are the server-side changes that would cut
client-side (agent) token spend the most, ranked by expected impact. They come out of a
token-efficiency review of the ChatGPT Work plugin that sits on top of this MCP server —
see `docs/token-efficiency-action-plan.md` in the plugin repo for the full review.

None of these are blocking — the plugin works against the current API. They are ranked by
how much client-token cost each would remove, because that cost is paid on every skill run,
by every user, for as long as the gap exists.

---

## 1. `fields=` projection on `getShiftRecord`

**Problem.** `getShiftRecord` has no field projection — every call returns the full form
answer set (all simple fields, all date/time fields, all list-field rows, all asset
references), regardless of what the caller actually needs.

**Evidence.** 17 of the plugin's skills call `getShiftRecord` at least once per record in a
fan-out loop (one call per shift, because `getShiftRecords` only returns UUID + summary
metadata — see ask #7). The `photos` skill needs only the asset array; `narrative-search`
needs only the narrative field; `delay-analysis`'s record follow-up needs narrative +
weather + a couple of timestamps. Each of these callers currently receives — and must pay
transcript tokens to hold — the entire record: all worker rows, all resource line items,
every simple field, whether or not the skill's procedure touches them.

**Proposed shape.** `getShiftRecord(uuid, fields=["narrative","assets"])` (or a
`view=narrative-only|workers-only|assets-only` shorthand for the handful of shapes that
cover almost every real caller) returning only the requested top-level keys.

**Expected client token saving.** 60–80% off every per-record fetch across those 17 skills
— this is the single highest-impact ask on this list, because it multiplies by "one call
per shift record" rather than "one call per skill run".

---

## 2. Compact JSON responses

**Problem.** Every tool response is pretty-printed with two-space indentation. That
formatting is pure overhead once the response reaches an agent's context — the agent
parses it once and never needs the whitespace again, but pays for every space and newline
in the transcript.

**Evidence.** Applies to every tool, every call, with zero exceptions — `getCachedReport`
report bodies and `getShiftRecords` listings are the largest offenders by raw byte count.

**Proposed shape.** Serve compact JSON (`json.dumps(..., separators=(",", ":"))` or
equivalent) by default. If any existing integration depends on pretty-printed output,
gate it behind an explicit `pretty=true` query param or header rather than making it the
default.

**Expected client token saving.** Roughly 25% off every payload, for zero API surface
change — this is the cheapest ask on the list to ship and the only one with no new
parameters to design.

---

## 3. `fields=` / `summary=true` on `getCachedReport`

**Problem.** Dashboard reports often carry 10–25 columns per row (see `getReportSchemas`),
but a given skill question frequently needs two or three of them — e.g. "labour hours by
week" needs `Hours Worked` and `Shift Start Date` out of `dashboardResourceLabour`'s full
column set.

**Evidence.** Every skill that calls `getCachedReport` for an aggregate answer (labour
reporting, productivity tracking, access-overview summaries) currently receives full rows
and discards most columns client-side after reading them into context once.

**Proposed shape.** `getCachedReport(uuid, reportName, from, to, fields=["Hours Worked",
"Shift Start Date"])`, validated against `getReportSchemas`'s field list for that report;
or a `summary=true` flag that returns a small number of common aggregate shapes (sum/count
per day or per person) without a full row dump.

**Expected client token saving.** Similar order of magnitude to ask #1 (60–80% off the
report payload) for any question that only needs a subset of columns — which is most
questions.

---

## 4. Server-side narrative search

**Problem.** There is no way to search shift narratives server-side. Every skill that needs
to find "the shift where X happened" (a delay, a near-miss, a specific keyword) must pull
every shift record's narrative for a project and period via `getShiftRecords` +
`getShiftRecord` fan-out, then scan client-side.

**Evidence.** `narrative-search`, `events`, `ce-radar`, and `delay-analysis` all implement
this pull-then-scan pattern today. Each is bounded by the same per-record fan-out cost that
ask #1 addresses, compounded by having to pull records that turn out irrelevant just to
rule them out.

**Proposed shape.** A search endpoint — keyword or regex over shift narratives for a given
project and date range — returning record id, shift date, and a short excerpt (e.g. 200
characters around the match) rather than the full narrative or record.

**Expected client token saving.** Replaces an O(records-in-range) fan-out with a single
call whose response is bounded by match count, not record count — typically a 90%+
reduction for a targeted search over a multi-week range.

---

## 5. Aggregate endpoints for common cross-record computations

**Problem.** Several common questions are aggregates over many shift records — labour
hours by trade and week, plant idle days, weather-lost hours, duplicate-allocation detection —
and today the only way to answer them is to pull every underlying record or report row and
aggregate client-side.

**Evidence.** This is the pattern the plugin's own P1.17 client-side workaround exists to
manage (batching and caching the raw pulls so the aggregation only has to happen once per
skill run) — a workaround that would be unnecessary if the server did the aggregation.

**Proposed shape.** A small set of named aggregate endpoints (`aggregateLabourHours`,
`aggregatePlantIdleDays`, `aggregateWeatherLostHours`, `aggregateConsecutiveTurns`) scoped
by project and date range, returning the aggregate directly rather than the rows behind it.

**Expected client token saving.** Removes the raw per-record or per-row payload entirely
for these questions — savings scale with how many records the aggregate spans, typically
70%+ for a month-long window.

---

## 6. `modifiedSince` on `getCachedReport`, and official documentation of it on `getShiftRecords`

**Problem.** `getShiftRecords` already supports `modifiedSince` for incremental sync, but it
is not called out in the API's own documentation — the plugin only knows about it from
direct schema inspection, not from any published reference. `getCachedReport` has no
equivalent at all, so re-running a report after a known change window means re-pulling the
full date range instead of only what changed.

**Evidence.** Any skill re-checking a period it already pulled (a re-run after new site data
lands, or a scheduled daily refresh) currently has no way to ask "what changed since I last
looked" for report data, and has to guess at `getShiftRecords`'s support for the same from
the tool schema alone.

**Proposed shape.** Add `modifiedSince` to `getCachedReport` with the same semantics as
`getShiftRecords` (filter by last-modified, not by the report's own date field). Document
both in the public API reference, not only in the MCP tool description text.

**Expected client token saving.** Turns a full-range re-pull into an incremental one for
any re-run scenario — savings scale with how much of the range is unchanged, often 90%+ for
a daily re-check of a mostly-settled period.

---

## 7. Batch `getShiftRecord` (`uuids[]`, max 25)

**Problem.** `getShiftRecords` returns only UUID + summary metadata per record — there is no
field projection and no way to fetch more than one full record per call. Every skill that
needs full record detail across a set of shifts (not just one) pays one round trip, and one
PostToolUse hook firing, per record.

**Evidence.** This compounds directly with ask #1: even with field projection, a skill
needing narrative text from 20 shift records in a month still makes 20 separate calls
today, each carrying its own MCP round-trip overhead and triggering the plugin's per-call
hooks (evidence-discipline checks, etc.) 20 times over.

**Proposed shape.** `getShiftRecord(uuids=[...], fields=[...])` accepting up to 25 UUIDs per
call (matching the existing `getShiftRecords` page size), returning an array of records
keyed by UUID.

**Expected client token saving.** Does not reduce the payload itself (that's ask #1) but
removes N−1 round trips and N−1 hook firings for an N-record fetch — meaningful for
per-call overhead and for wall-clock latency on multi-record skills, and it composes with
ask #1 for the full saving on the fan-out pattern.

---

## 8. Expose contract sums and certified values where available

**Problem.** Today every monetary output the plugin produces (contract sum, certified
value to date, variation value) is user-supplied during the skill's interview step — the
MCP server exposes no read path to any of this even where Gather itself holds it.

**Evidence.** Every commercial-report-shaped skill (`commercial-report`, valuation,
variation-tracking) spends interview turns asking the user to type in figures that, for
many projects, already live in Gather's commercial data model. Those interview turns are
pure token cost with no data-quality upside over reading the number directly.

**Proposed shape.** A read endpoint (or fields on an existing one, e.g.
`getProjects`/`getProjectAssignments`) exposing contract sum, certified value to date, and
variation value where the workspace has them configured — read-only, matching the rest of
this API's access model.

**Expected client token saving.** Removes an interview round trip per commercial-report run
for any project where these values are configured in Gather — the saving is per-skill-run
rather than per-record, but it is paid on every commercial run for every affected project.
