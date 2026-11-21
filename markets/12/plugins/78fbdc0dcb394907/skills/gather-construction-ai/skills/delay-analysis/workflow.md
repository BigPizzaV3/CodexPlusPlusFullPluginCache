---
name: delay-analysis
description: Builds a delay register from site records — identifies, categorises and
  quantifies delays from narratives, access restrictions and weather data, for delay
  claims and lost-time analysis.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Delay Analysis — Build a Delay Register from Site Records

Systematically scan shift narratives, access records, and shift data to identify, categorise, and quantify delays. Produces a chronological delay register suitable for claims preparation, project reviews, and programme analysis.

Naming the method on every output is mandatory — an unlabelled bespoke technique is the first thing opposing counsel attacks.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project and Date Range

Parse `the user’s request` for:

1. **Project name** — resolve using **Pattern 1**.
2. **Date range** — parse using **Pattern 2**; default to the last 4 weeks if unspecified. Users
   frequently need longer periods for a delay register — suggest a broader range if the default
   seems too narrow (e.g. "would you prefer the last 3 months?").

Confirm the interpreted parameters with the user unless the date range is unambiguous (exact
dates provided): "I'll build a delay register for **[project]** from **[start]** to **[end]** —
scanning narratives, access records, and shift data. Does that look right?"

---

## Step 2: Retrieve Narrative Data

Call `getCachedReport` with **Report:** `dashboardNarrative`, the resolved project UUID, and the
parsed from/to dates. No data returned → follow **Pattern 3 (Empty Data Handling)**.

Scan every narrative entry for delay-related language, case-insensitive, with variations. Use
**Pattern 10 (Contractual Event Keywords)** — `../../shared/patterns/10-contractual-event-keywords.md`
— as the base categories (access/possession, instructions/changes, standing/delay, physical
conditions, third party, information, weather), plus these delay-analysis-specific additions:
**resource shortage** (short staffed, understaffed, no operatives, plant breakdown/failure, no
plant, awaiting plant, material shortage, awaiting delivery) and **rework/rejection** (rejected,
failed inspection, abortive, reworked). Apply Pattern 10's false-positive rule throughout.

For each match:
- Record the date, shift, supervisor
- Extract the matching text with 1–2 sentences of surrounding context
- Note which category the match falls into (a single narrative may match multiple categories)

---

## Step 3: Retrieve Access / Possession Data

Call `getCachedReport` with **Report:** `dashboardAccessPossession`, then `dashboardAccessNonPossession`, both for the same project UUID and date range.

Extract: dates where access/possession was restricted, denied, or reduced; duration of
restrictions; reason (if recorded); location/area affected.

Cross-reference with Step 2 narrative matches — a narrative mentioning an access issue on the
same date an access record confirms a restriction is corroborating evidence.

---

## Step 4: Retrieve Shift Data for Cross-Reference

Call `getCachedReport` with **Report:** `dashboardShiftTable` for the same project/range.

Use shift data to identify: **short shifts** (significantly shorter than the norm, e.g. <6 hours
when standard is 10+ — may indicate an early finish due to a delay event); **non-working days**
(expected working days with no shift recorded — may be delay-related or simply weekends/holidays);
**reduced crew sizes** (fewer resources than typical — may indicate restricted working).

Calculate the project's normal shift pattern (standard shift duration and crew size, both
median; expected working days per week) and flag shifts deviating significantly from these norms.

---

## Step 5: Retrieve Full Detail for Significant Events

For the most significant delay events (multiple corroborating sources, or lasting more than half
a day), call `getShiftRecord` for full shift detail: complete narrative text, attached photos
(may show delay conditions), full resource list, weather conditions recorded.

**Quote what you use:** never paste a fetched record's full JSON into the transcript — pull only
the fields the register needs (narrative excerpt, resource counts, weather value) and quote just
those, per Pattern 4's per-record fetch rule.

**Where the shift-record IDs come from:** `getShiftRecord` requires a specific record ID. First
check whether the Step 2/4 dashboard rows already carry one (**Pattern 12** — verify the field
exists before relying on it): if so, use those IDs directly. If not, call `getShiftRecords`
filtered to the significant events' date(s) to obtain IDs, then `getShiftRecord` per ID (25/page,
2 requests/second — pace both loops, **Pattern 4**).

**Pagination and rate limits (Pattern 4):** a detail loop of N records takes at least ~N/2
seconds — warn the user of the wait before a large loop. This skill applies a **deliberately
stricter 10-record threshold** than Pattern 4's general 100-record warning, because each
significant-event fetch is an individual call and delay analysis rarely needs more than the top
events: over 10 records, warn of the calls/wait and ask whether to proceed or focus on top events.

---

## Step 6: Categorise Each Delay Event

Assign every identified delay to one of the following categories:

| Category | Code | Description |
|---|---|---|
| Access / Possession | ACC | Site access restricted, possession not granted, area blocked |
| Weather | WEA | Adverse weather preventing or restricting work |
| Design / Information | DES | Awaiting design, RFI response, information, or instruction |
| Client / PM Instruction | CLI | Stop notice, suspension, variation instruction, directed change |
| Third Party / Utility | TPU | Utility diversions, statutory undertaker works, third party interference |
| Resource Shortage | RES | Insufficient labour, plant breakdown, material shortage |
| Rework / Rejection | REW | Work rejected on inspection, abortive work, rework required |
| Other | OTH | Any delay not fitting the above categories |

**Weather (WEA) caveat — mandatory wherever a WEA row appears:** a keyword-flagged weather narrative is a LEAD for investigation, not evidence of a clause 60.1(13) qualifying event. The contractual test is a measurement exceeding the stated once-in-ten-year value per the Contract Data measurements, applied by `$weather-impact` — not the presence of weather language in a narrative. Carry this qualification into every WEA row in the register (the Chronological Delay Register description and the Cause Breakdown).

For each delay event, record:
1. **Date** — when the delay occurred
2. **Category** — from the table above (code and description)
3. **Description** — concise summary of what happened, drawn from the narrative
4. **Duration** — **shift-hours of delay (the event's duration on the affected shift), not person-hours** — from shift data, narrative context, or access records. This is the DA register unit per **Pattern 11 (One Event, One Register)** from `../../shared/patterns/11-one-event-one-register.md`. Do not multiply by crew size here (crew size is captured separately in "Affected resources"). When converting hours to days, use the **median shift duration for the period as the divisor and state it** (Pattern 11 rule 3).
5. **Affected resources** — number of people/plant affected (from shift data)
6. **Evidence references** — shift record IDs, narrative excerpts, access data references
7. **Confidence** — HIGH (corroborated by multiple data sources), MED (single clear source), LOW (inferred from indirect evidence such as short shifts)

**Programme baseline (Pattern 15):** Before finalising the register, check for `programme/programme-baseline.md` per **Pattern 15** (`../../shared/patterns/15-programme-baseline.md`). If it exists and its project matches, add a **"Critical (per imported programme)"** flag/note to each delay event:

- For events whose affected activity has a user-confirmed mapping (Pattern 15 rule 3) to a baseline task, flag Yes/No using total float and criticality **exactly as stored in the export at its data date** (state the date) — never recompute CPM (Pattern 15 rule 2).
- Cite it: "per the imported programme ([revision], exported [date])."
- Events on unmapped activities are noted **"not mapped to the programme"** — never guessed.
- Absent file or project mismatch → state the standard limitation (no baseline/critical-path data) and continue with the category-based Risk Owner logic above; point to `$programme-import`.

---

## Step 7: Present the Delay Register

Read `references/da-output-template.md` for the
exact 5-section register format (Headline, Chronological Delay Register, Cause Breakdown,
Timeline, Key Observations), the `DA-[NNN]` header block, and Risk Owner assignment rules.
Cite **Pattern 11 (One Event, One Register)** for the register-format discipline (shift-hours
unit, never summed with AC/WI totals) rather than restating it here.

---

## Step 8: Caveats and Data Quality Notes

Always include — do not modify this text:

> **Important notes on this delay register:**
> - Delays are identified from recorded data — narratives, access records, and shift patterns. Events not recorded in shift diaries will not appear.
> - Duration estimates are approximate — they are derived from narrative context, shift start/end times, and access records. Precise durations require further investigation.
> - Categorisation is based on the language used in narratives and may require human review — some events could reasonably fall into multiple categories.
> - This register identifies delay **events**, not necessarily delay to the **programme**. A delay event may not have impacted the critical path. Programme impact assessment requires separate analysis.
> - LOW confidence events are inferred from indirect evidence and should be verified before inclusion in any formal submission.
> - Risk Owner classification (Employer/Contractor/Shared) is indicative based on category. Actual contractual entitlement depends on the specific contract terms — use Pattern 5 (Contract Type Resolution) for contract-specific assessment.
> - Where any WEA (weather) event appears in this register: a keyword-flagged weather narrative is a LEAD for investigation, not evidence of a clause 60.1(13) qualifying event — the contractual test is a measurement exceeding the stated once-in-ten-year value per the Contract Data measurements, applied by `$weather-impact`.
> - Ref: DA-[NNN] is a session-local sequence number for cross-referencing. It does not replace the project's own delay register numbering.

---

## Related Skills

After presenting the delay register, suggest these related skills for deeper analysis:

- `$weather-impact` — Quantify the specific impact of weather on productivity and working time
- `$access` — Detailed analysis of access and possession patterns
- `$measured-mile` — Establish baseline productivity to quantify the disruption effect of delay events
- `$narrative-search` — Search for specific terms or events in more detail across all narratives
- `$programme` — Assess programme impact of the identified delays
- `$programme-import` — Import an MS Project/P6 baseline to flag which delay events sit on the critical path, as stored (Pattern 15)
