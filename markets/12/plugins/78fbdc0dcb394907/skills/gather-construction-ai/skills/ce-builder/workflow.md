---
name: ce-builder
description: Build a CE notification (NEC clause 61.3), JCT loss and expense application,
  or FIDIC claim notice from diary evidence. Notification stage — for the priced clause
  62 response use ce-quotation.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Claim / CE Narrative Builder

Build a structured contractual submission from Gather site diary evidence. The output format adapts to the contract type:
- **NEC:** Compensation Event Notification (clause 61.3) with supporting particulars
- **JCT:** Loss and Expense application per clauses 4.20–4.21 (SBC 2016; DB 2016: 4.19–4.21)
- **FIDIC:** Claim notice per clause 20.2

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination); `../../shared/patterns/05-contract-type-resolution.md` (contract type resolution); `../../shared/patterns/06-notification-compliance.md` (notification compliance); `../../shared/patterns/07-event-to-clause-mapping.md` (event-to-clause mapping); `../../shared/patterns/13-contract-profile.md` (Pattern 13 — names the contract family Step 6 loads a format for).

Apply the appropriate contract knowledge skill (`nec-contracts`, `jct-contracts`, or `fidic-contracts`) before proceeding.

---

## Step 1: Understand the Event

Extract from `the user’s request` or ask the user for:
- **Project name** — resolve using Pattern 1
- **Event description** — what happened? (e.g., "late possession handover on Section 3", "design change to drainage", "unforeseen ground conditions in Trench B")
- **Event date(s)** — when did it happen? Resolve using Pattern 2
- **Contract type and edition** — resolve using Pattern 5
- **What is being claimed?** — time extension, additional cost, or both

If the user provides a date range but no event description, search narratives first (as per `$events`) to identify what happened, then confirm with the user before proceeding.

---

## Step 2: Gather Evidence from Site Records

Make calls 2a, 2b, and any applicable conditional calls (2c, 2d) **in parallel** for the event period:

### 2a: Narratives (`dashboardNarrative`)
Search for:
- Direct references to the event
- Impact descriptions (standing time, delay, disruption)
- Communications or instructions mentioned
- Contemporaneous observations by site staff

### 2b: Labour and Resources (`dashboardResourceLabour`)
Extract:
- Total labour hours during the event
- Standing time (if identifiable from resource data)
- Additional resources deployed
- Compare against a baseline period: make a second `dashboardResourceLabour` call covering the 7 days before the event start date

### 2c: Access Data — if access-related event (`dashboardAccessPossession`)
Extract:
- Possession requests vs grants
- Timeliness data
- Cancellations or restrictions

### 2d: Weather Data — if weather-related event
Pull weather information from shift records via `getShiftRecords` for the event period. Extract:
- Weather conditions recorded
- Days affected
- Impact on work activities

### 2e: Shift Records for Detail (only if needed)
Only fetch individual shift records via `getShiftRecords` if the dashboard reports above do not provide sufficient detail for the evidence schedule. For short events (1–5 days), fetch individual records. For longer events, rely on dashboard data and only fetch records for the most significant dates. Follow Pattern 4 for pagination. Extract:
- Specific diary entries describing the event and its impact
- Resource deployment on affected days
- Activities performed vs planned

---

## Step 3: Check Notification Compliance

Apply **Pattern 6 (Notification Compliance Check)** from `../../shared/patterns/06-notification-compliance.md`. Calculate the notification window based on the contract type, state whether the event is within or outside the window, and flag any deadlines approaching or passed. Include the specific dates and days remaining/elapsed in the output.

---

## Step 4: Identify the Contractual Basis

Map the event to the applicable contract clause using **Pattern 7 (Common Event-to-Clause Mapping)** from `../../shared/patterns/07-event-to-clause-mapping.md`. If the event matches a common category (access, instructions, weather, physical conditions, etc.), use the clause references from the pattern table.

If the event does not fit a common category, consult the full contract knowledge skill (`nec-contracts`, `jct-contracts`, or `fidic-contracts`) and present the options to the user for confirmation.

For each contract type, also note:
- **NEC:** Which clause 60.1 ground applies? Confirm NEC3 vs NEC4 edition (the 60.1(1)–(19) grounds are numbered identically in both; NEC4 adds 60.1(20) and 60.1(21), including additional compensation events stated in the Contract Data)
- **JCT:** Identify both the Relevant Event (time — clause 2.29 in SBC 2016; DB 2016 numbers its time clauses differently) and whether a Relevant Matter (cost, clause 4.22 SBC 2016 / 4.21 DB 2016) also applies. Not all Relevant Events are Relevant Matters (e.g., weather gives time but not money)
- **FIDIC:** Specify whether the entitlement is Cost only, Cost Plus Profit, EOT only, or a combination

---

## Step 5: Assess Impact

### Time Impact
From the shift records and narratives:
- How many days/shifts were affected?
- Was work stopped entirely or partially disrupted?
- What activities were impacted?
- Was the impacted work on the critical path (if programme data available from `$programme`)?

### Resource Impact
From the labour data:
- Standing time: how many gang-hours/shifts were unproductive?
- Additional resources: were extra resources deployed to mitigate?
- Productivity loss: compare output rates during vs before the event (reference `$measured-mile` if a full analysis is needed)

### Evidence Sufficiency Gate

Before assembling the submission, verify that every claimed impact cites at least one dated record retrieved in the earlier steps. If the retrieved records do NOT corroborate the event as the user described it (no matching narratives, dates, or resource impacts), say so explicitly, present what the records do show, and stop — do not produce a submission-formatted document on uncorroborated facts. When the gate trips, still return a short structured note under `Ref: CE-[NNN]` (the session-local sequence number per Pattern 8, e.g. `Ref: CE-001` — never "to be assigned"; the contract's own CE number is a separate field): what the records confirm, what they do not, and what a compliant submission would need — for NEC4 that includes the clause 63.1 dividing date and the Accepted Programme current at that date (clause 63.5); for NEC3, clause 63.3. If the event came from `$events` output, carry its HIGH/MEDIUM/LOW confidence rating into the submission's caveats.

---

## Step 6: Structure the Submission

Adapt the output format to the contract type. Never state a quantum that cannot be traced to retrieved records or an explicit user-supplied figure; where a value is an estimate, label it as an estimate and state the basis. Where a template field cannot be supported by the data, write "not quantifiable from available records" rather than inventing a figure.

**Load exactly one format, named by the contract profile (Pattern 13):**
- `contract_family` starting `NEC` → read `references/nec-format.md`
- `contract_family` starting `JCT` → read `references/jct-format.md`
- `contract_family` starting `FIDIC` → read `references/fidic-format.md`
- No contract profile present → resolve the family in Pattern 5 order: the user's request (e.g. "NEC4" in `the user’s request`), then the project's contract type from `getProjects`/`getMyProjects`; only if neither names a family ask the user. Never load more than one format file; state the unamended-standard-form assumption in the submission.

Each reference file's Evidence Schedule section cites the shared table format at
`references/evidence-schedule.md`.

---

## Step 7: Caveats

Always include:

> **Important notes:**
> - This submission is prepared from Gather site diary data. It provides the evidence foundation but requires commercial review before formal notification.
> - Financial quantification (contract rates, cost data, overhead calculations) is not available through Gather and must be prepared separately.
> - Clause references are based on the standard form contract. Check your specific contract for amendments or special provisions.
> - This is not legal advice. For disputes or adjudication, seek specialist legal or commercial advice.

---

## Step 8: Shareable HTML Submission (Generated by Default)

After presenting the chat submission from Step 6 and the caveats from Step 7, generate a self-contained, shareable HTML submission file built from the shared template — this is now produced **by default** for a full run, not an optional extra offered on request.

**When to generate it:**

- Generate it automatically, without asking, immediately after presenting the chat submission and caveats above.
- Skip it only if: the user's original request explicitly asked for chat-only output (e.g. "just show me here", "no files"); or the user declines when told a file is about to be written.

**Procedure:**

1. Read the template at `../../shared/templates/ce-submission-template.html`.
2. Build the run's data as a single JSON object matching the schema documented at the top of that template, setting `"type": "notification"` — this skill always produces a notice or application, never a priced quotation. (The same template also serves `$ce-quotation`, which sets `"type": "quotation"` and populates the nullable `headline` block with `pricesChange` / `completionDateChange` / `keyDateChanges`.) Map:
   - `ref`, `projectName`, `contractLine`, `date` from Step 6's header block
   - `parties.from` / `parties.to` from the contracting parties identified in Step 1
   - `sections` — one entry per numbered block in the Step 6 output (Event Description; Contractual Basis / Relevant Event / Notice; Programme Impact; Resource Impact / Loss and Expense / Initial Particulars; Assessment Basis / Next Steps; etc.), each as `{heading, paragraphs, table?, list?}`
   - `evidence` from the Evidence Schedule / Contemporary Records table
   - `assumptions` — any pricing or quantum assumptions stated in Step 6; omit the field entirely if none were made
   - `notes` from the Step 7 caveats bullets
   - `signature.preparedBy` / `signature.reviewedBy` — leave both `""` (renders a blank ruled line) unless the user supplied names
3. Splice this JSON between the two marker comments in the template with a plain string split on the marker tokens (split on the literal marker strings, not a regex) — locate the opening marker, locate the closing marker, and replace everything between them with `JSON.stringify` of the object from step 2. Keep both markers in place, immediately surrounding the data.
4. Write the result to `<ref>-ce-notification.html` in the working directory using the Write tool — one self-contained file, zero external requests.
5. State the file path to the user and note that it opens in any browser, prints to A4 portrait, and is safe to circulate standalone, detached from this conversation.

**Fallback:** if `../../shared/templates/ce-submission-template.html` cannot be read, say so plainly and present the chat submission from Step 6 only — do not hand-build a substitute HTML file.

---

## Related Skills

- `$events` — Identify potential contractual events across a broader period
- `$delay-analysis` — Build a comprehensive delay register
- `$measured-mile` — Quantify productivity disruption
- `$weather-impact` — Quantify weather impact for weather-related claims
- `$narrative-search` — Deep search for additional evidence
- `$programme` — Assess programme impact
- `$labour` — Detailed labour analysis for cost substantiation
