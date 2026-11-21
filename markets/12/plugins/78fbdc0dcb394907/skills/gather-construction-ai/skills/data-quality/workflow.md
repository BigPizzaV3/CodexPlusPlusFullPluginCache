---
name: data-quality
description: Assess Gather diary data quality — missing narratives, incomplete records,
  coverage gaps, double-booked people and duplicate shifts. Add "duplicates" for the
  targeted double-booking sweep; add "review" for a record-level punch-list of defective
  records.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Data Quality Assessment

Assess the completeness and quality of data recorded in Gather for a project — gaps in recording, missing fields, inconsistencies, coverage issues. Good data quality is the foundation of every analysis this plugin produces; poor data undermines delay registers, commercial reports, and claim narratives.

Follow the shared patterns under `../../shared/patterns`: 01 (project resolution), 02 (date parsing), 03 (empty data handling), 04 (pagination/rate limits).

---

## Step 1: Resolve Project and Date Range

1. Parse `the user’s request` for a project name and optional date range.
2. Resolve the project using **Pattern 1**; store the UUID and name for all subsequent calls.
3. Parse any date range using **Pattern 2**; default to the **last 4 weeks** if unspecified;
   confirm with the user if ambiguous.

---

## Step 2: Retrieve Data (parallel calls)

Make the following `getCachedReport` calls **in parallel** for the resolved project and date range: `dashboardShiftTable` (shift coverage/supervisor activity), `dashboardResourceLabour` (labour recording completeness), `dashboardResourcePlant` (plant recording), `dashboardResourceMaterial` (material recording), `dashboardProgress` (progress recording), `dashboardNarrative` (narrative completeness), `dashboardAccessPossession` (access recording).

Retrieve only the reports needed for diary completeness, coverage and duplicate checks, within the scope set by the runtime conventions.

Also call `getShiftRecords` for the first page (up to 25 records) to inspect individual record completeness — a **sample** of actual record structure (see the Step 11 sampling caveat: field-level statistics from this page are a sample, not the full population).

---

## Step 3: Assess Shift Coverage

From `dashboardShiftTable`, analyse:

### Calendar Coverage

Save the `dashboardShiftTable` result to the scratchpad and run
`python3 ../../scripts/shift_analytics.py <shifttable-file> --format md` — read
its coverage-gap output instead of computing expected/actual working days and gap dates in
context. Cite it: "Coverage computed by scripts/shift_analytics.py over [N] dashboardShiftTable
rows." Script unavailable → fall back to counting weekday dates with no shift record manually and
say so.

### Shift Patterns
Supervisors active (how many submitted records); records per supervisor (evenly distributed or
concentrated); weekend/night shifts (records outside normal working days indicating extended
operations).

See the flag lookup table at the end of Step 7 for the exact sentence wording (rows 1–2).

---

## Step 4: Assess Narrative Quality

From `dashboardNarrative` and the sample shift records:

**Completeness:** records with narratives vs total records (% with narrative text); empty
narratives (blank or <10 words).

**Quality indicators:** average narrative word count; very short narratives (<20 words, may lack
useful detail); boilerplate detection (identical/near-identical narratives across multiple days —
copy-paste recording).

See the flag lookup table at the end of Step 7 for the exact sentence wording (rows 3–5).

---

## Step 5: Assess Resource Recording

**Labour** (`dashboardResourceLabour`): days with labour data vs working days (coverage %);
average workers per day (consistent or spiking/dropping?); days with zero labour (list — may be
genuine non-working days or recording gaps).

**Plant** (`dashboardResourcePlant`): plant items recorded (count); days with plant data vs
working days. Zero plant data → "No plant data recorded. If plant is on site, utilisation
tracking is not being captured."

**Materials** (`dashboardResourceMaterial`): material types recorded (count); days with material
data vs working days. Zero material data → "No material usage recorded. Material tracking may
not be configured."

---

## Step 6: Assess Progress Recording

From `dashboardProgress`: activities tracked (count); activities with planned targets (both
planned and actual, enabling variance analysis); activities with zero actual (tracked but no
recorded output); frequency (daily, weekly, or sporadic updates).

See the flag lookup table at the end of Step 7 for the exact sentence wording (rows 6–7).

---

## Step 7: Assess Access Recording

From `dashboardAccessPossession`: possessions recorded (count); if the project operates under
possessions/access windows, check completeness; zero access data → see the flag lookup table
below (row 8).

### Flag Sentence Lookup Table (Steps 3–7)

Read `references/dq-flag-lookup.md` — one shared
pattern for every flag sentence in Sections 2–5 and 9 of the report, replacing the eight
near-duplicate sentence templates that used to live inline in Steps 3–7.

---

## Step 8: Per-Supervisor Quality Breakdown

**Purpose:** recording quality is a habit problem, not a data problem — this breakdown shows
**who to coach**, not who to blame, routing Step 12's recommendations (and the Data Assurance
agent's remediation plan) to specific people rather than generic team instructions.

From `dashboardShiftTable` (records per supervisor) and `dashboardNarrative` (narrative
presence/length per record), build one row per supervisor active in the period:

- **Records** — count of shift records attributed to that supervisor.
- **% with Narrative** = (their records with a narrative present ÷ their total records) × 100.
- **Avg Narrative Words** — average word count over **only** records with a narrative present (a
  supervisor with zero narratives has no defined average — render "n/a" per the Pattern 12
  divide-by-zero convention, not `0`).
- **Assessment**, in order: Records < 5 → `"—, sample too small"`; else % with Narrative ≥ 90 and
  Avg Words ≥ 30 → `"consistently detailed"`; else % with Narrative < 60 → `"narratives often
  missing — coaching opportunity"`; else Avg Words < 20 → `"narratives present but thin —
  coaching opportunity on detail"`; else → `"inconsistent — narratives present but patchy"`.

Diagnostic only — like Access and Consistency, does **not** feed the Step 11 weighted score; it
re-slices Step 4's Narrative Completeness data by supervisor.

**Caveat:** narrative length is a proxy for engagement, not usefulness — a short narrative can be
sufficient and a long one can still be boilerplate (Step 4). Use this table to start a coaching
conversation, not to rank performance.

---

## Step 9: Quality Trend

**Purpose:** show whether recording quality is improving, stable, or declining across the period — a single-point-in-time score cannot show direction.

1. Chunk the date range into **weeks**; if it exceeds 12 weeks, chunk into **months** instead.
2. For each chunk, compute two cheap sub-scores straight from the Step 2 dashboard aggregates, no
   per-record fetch: **Coverage %** = (days with ≥1 shift record ÷ expected working days) × 100
   (same formula as Step 3/Section 1); **Narrative %** = (records with a narrative present ÷
   total records) × 100 (the presence component of Step 4/Section 1, without word-count/boilerplate).
3. **Small-sample guard:** skip any chunk with fewer than 3 expected working days. Fewer than
   **3 usable chunks** remain → do not compute a trend — state "The selected range is too short
   for a reliable trend (fewer than 3 usable chunks after excluding short chunks)" and omit the
   rest of this section (Pattern 12 — no fabricated trends).
4. Otherwise present the chunk table, then one sentence: average `(Coverage % + Narrative %) / 2`
   across the first half of usable chunks vs the second half (round down on an odd count; the
   middle chunk sits in neither half). Second-half average >5pp **above** first → **improving**;
   >5pp **below** → **declining**; otherwise → **stable**.

---

## Step 10: Cross-Check Consistency

Look for inconsistencies across data sources: labour vs shifts (days with shift records but no
labour data, or vice versa); progress vs labour (progress recorded but no labour — may indicate
backdated entry); narrative vs events (narratives mentioning events — delays, weather,
instructions — absent from other sources).

**Double-booking signal (cheap proxy — no extra fetches).** Run
`python3 ../../scripts/shift_analytics.py <labour-file> --format md` over the
`dashboardResourceLabour` result already retrieved — it flags any person-date candidate (default:
recorded hours >14 that day). List candidates found and recommend the targeted sweep below for
confirmation. The proxy misses double-bookings whose combined hours stay under the threshold —
say so when any flag is raised.

### Targeted duplicate sweep — `the user’s request` contains "duplicates"

When the user asks for it (e.g. `$data-quality [project] [period] duplicates`), read
`references/dq-duplicate-sweep.md` for the full
record-level sweep procedure, the language-discipline rule, and the Step 3–9 skip.

---

## Step 11: Present the Data Quality Report

Read `references/dq-output-template.md` for the exact
10-section report structure, sub-score formulas, scoring thresholds, and caveats text (do not
modify the caveats). Fill every placeholder with data computed in Steps 1–10; for Section 1's
summary and Sections 2–5's flag sentences, use the Step 7 lookup table.

**Coverage-gap and duplicates-sweep arithmetic are not computed in-context** — see the
shift_analytics.py wiring above (Steps 3, 10).

---

## Step 12: Review Mode — Record Review Punch-List

**Trigger:** only when `the user’s request` contains "review" (case-insensitive) — e.g. "review", "review
records", "record review", "which records need fixing", "punch list". Skip on a normal run — it
costs up to 10 extra record fetches a default quality check doesn't need.

Run **after** the Step 11 report is presented in full. Read
`references/dq-review-mode.md` for the full
candidate-selection, fetch, checklist, punch-list table, and read-only-reminder procedure.

---

## Related Skills

- `$diary` — review individual shift records to investigate specific gaps
- `$record` — view a single record in full detail to assess field completeness
- `$narrative-search` — search narratives (quality of results depends on narrative completeness)
- `$commercial-report` — relies on data quality; run this check first
