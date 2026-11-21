---
name: ce-quotation
description: Price an NEC clause 62 compensation event quotation — Changes to the
  Prices, Completion/Key Date delay, Defined Cost assessment. Pricing stage after
  ce-builder's clause 61.3 notification.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# CE Quotation Builder (Clause 62)

Builds the priced quotation a Contractor submits under **clause 62** once a CE has been notified and the PM has instructed (or is deemed to have instructed) quotations. Follows `$ce-builder`, which produces the clause 61.3 notification with evidence.

**Scope:** NEC only (NEC3/NEC4 ECC). JCT loss-and-expense or FIDIC claim valuations are out of scope — point to `$ce-builder` (adapts per contract type) or `jct-contracts`/`fidic-contracts`.

**Prerequisite:** either (1) a prior `$ce-builder` notification this conversation — reuse its `CE-[NNN]` ref, event description, and evidence, extending rather than re-fetching, or (2) fresh event details now (project, event description, date(s), NEC edition and Option). Neither available → ask first.

**NEC3 vs NEC4 clause numbering (stated once here):** this skill cites both editions' numbers
inline the first time a clause appears in a step, then uses the NEC4 number alone afterwards in
that step — dividing date/assessment 63.1/63.3 (NEC3) → 63.1/63.5 (NEC4); time risk allowances
63.6 (NEC3) → 63.8 (NEC4); "wait and see" bar 63.7 (NEC3) → 63.9 (NEC4); early-warning reduction
63.5 (NEC3) → 63.7 (NEC4). Confirm the edition in Step 1; read every later bare clause number
against it.

Follow the shared patterns under `../../shared/patterns`: 01 (project resolution), 02 (date parsing), 03 (empty data handling), 04 (pagination/rate limits).

### Contract Profile (Pattern 13)

Before fixing timescales, Fee percentage, or checking for X1, look for a contract profile per **Pattern 13**. If present, use its `contract_family`, `main_option`, any `z_clause_amendments` (e.g. an amended 62.3 period), and whether `X1` is under `secondary_options` — cite "per the contract profile (as amended)". Absent → proceed on the unamended standard form, stating prominently: "assuming the unamended NEC3/NEC4 ECC — run `$contract-profile` to capture project amendments." Never invent a Fee percentage or amendment the profile does not state.

---

## Step 1: Resolve Project, Event, Edition, Option, and Fix the Dividing Date

Resolve the project (Pattern 1). Resolve the CE: reuse `CE-[NNN]` from a prior `ce-builder` run this conversation, or take the event description and date(s) supplied fresh. Confirm the NEC edition (NEC3/NEC4) and main Option (A–F) — from the contract profile if one exists, otherwise ask.

**Fix the dividing date (clause 63.1) and state how it was fixed:**

- **NEC4 — PM/Supervisor communication** (instruction, notification, certificate, or a changed earlier decision — e.g. a 60.1(1) Scope change): dividing date is **the date of that communication**.
- **NEC4 — other compensation events** (e.g. 60.1(2) access, 60.1(3) something not provided, 60.1(13) weather): dividing date is **the date the CE is notified** under 61.3.
- **NEC3:** dividing date is **the date the PM instructed, or should have instructed, quotations**.

**PM-instruction CE (dividing date is a communication date):** state plainly this CE is assessed on **forecast Defined Cost only** — no compensable work precedes the instruction. Actual costs must never adjust the assessment either way, even if known before the quotation is agreed (63.9 NEC4 / 63.7 NEC3 — assumes competent, prompt reaction; neither party gains from "wait and see").

---

## Step 2: Gather Actual Impact Evidence Before the Dividing Date

Only relevant where the dividing date falls **after** the event start (e.g. access or weather CE with impact already running). Gather, in parallel, evidence strictly before the dividing date: **labour standing time** (`dashboardResourceLabour`), **plant** (`dashboardResourcePlant`), **diary narratives** (`dashboardNarrative`, and `getShiftRecords` where dashboard detail is insufficient — Pattern 4 pagination applies).

Cite the record ID for every figure used. **Pattern 12:** never invent a figure — "not quantifiable from available records" where data cannot support one. **Pattern 11:** if a DA/AC/WI register already exists for the same period, cite its figure and Ref rather than re-deriving — never sum across registers. **"Coincides with" discipline:** a record's timing alone never proves it was *caused by* the CE — the causal link rests on narrative, not dates alone.

---

## Step 3: Changes to the Prices

Build a build-up table split at the dividing date fixed in Step 1.

| SCC Heading | Actual Defined Cost (to dividing date) | Forecast Defined Cost (from dividing date) | Basis |
|---|---|---|---|
| People | [£X, cite record IDs / "n/a — PM-instruction CE"] | [£X, forecast basis stated] | [Short SCC / SCC] |
| Equipment | ... | ... | ... |
| Plant and Materials | ... | ... | ... |
| Charges | ... | ... | ... |
| **Time-related (prolongation) cost** | [£X, cite record IDs / "n/a — PM-instruction CE"] | [£X, or "not quantifiable — no prelims rate in commercial profile"] | per commercial profile (Pattern 14) |
| **Fee** (@ [profile %]) | ... | ... | applied to both columns |
| **Total — Changes to the Prices** | **£X** | **£X** | |

Rules for populating it:
- **Actual column:** only populated where the dividing date falls after some impact has already run (Step 2 evidence, cited by record ID). PM-instruction CE → "n/a — forecast Defined Cost only" per Step 1.
- **Time-related (prolongation) cost:** delay days from the Step 4 delay assessment × the commercial profile's prelims establishment rate — `prelims.establishment_weekly ÷ working days per week` (state the divisor) — cited "per commercial profile" (Pattern 14). No commercial profile or no `prelims` block → "not quantifiable — no prelims rate in commercial profile": never invent a rate, never silently omit the row. Usually the largest single money line in an EOT-driven CE.
- **Forecast column:** must include **time risk allowances** for matters with a significant chance of occurring — the Contractor's entitlement under **63.8 (NEC4) / 63.6 (NEC3)** — stated as such, not folded silently into one number.
- **Fee:** at the profile's Fee percentage (or the stated standard-form fallback).
- **SCC basis:** Short SCC for Options A/B; SCC or Short SCC by agreement for Options C, D, E.
- **Quotation-preparation cost:** excluded under A/B; included from Options C onwards.
- **X1 deflation:** if the contract profile lists `X1`, add a line noting Defined Cost at the dividing date is deflated to base-date levels via the Price Adjustment Factor (X1.5), People/Equipment using base-date levels from Contract Data.

---

## Step 4: Delay Assessment — the Two-Programme Method (63.3 NEC3 / 63.5 NEC4)

Entitlement is the movement of **planned Completion**, assessed by the two-programme method (the January 2019 amendment to 63.5, folding NEC's Practice Note 1 into the contract):

- **Programme 1 — updated to the dividing date:** take the Accepted Programme current at the dividing date, update with actual progress, other compensation events already in the system, and non-CE delays up to the dividing date, and reschedule — fixing where planned Completion stood immediately before the new event.
- **Programme 2 — with the CE impacted:** add the new CE to Programme 1, logic-linked into the network, and reschedule. The further movement of planned Completion is the entitlement.

State explicitly: **this mark-up is not a clause 32.2 programme revision** and is not itself submitted for acceptance — an assessment device only. If the Accepted Programme is stale, unsubmitted, or recently rejected for reasons unrelated to this CE, first attempt to agree a programme to assess against (Practice Note 1); only failing agreement does the PM assess unilaterally under clause 64, based on the previous Accepted Programme.

**Terminal float is preserved:** the Completion Date moves by exactly the same amount as planned Completion — no more, no less. Same rule for any Key Date.

**Programme baseline (Pattern 15):** before building Programme 1 from narrative/progress records alone, check for `programme/programme-baseline.json` (sidecar) and its companion `.md` per **Pattern 15** (`../../shared/patterns/15-programme-baseline.md`).

Read `references/two-programme-worked-example.md` for the engine-execution procedure (sidecar + python3 + confirmed baseline → run `scripts/cpm.py` for Programme 1 status-dated to the dividing date, then with `--impact` for Programme 2; EOT movement = difference between the two `project_finish` values, INDICATIVE-bannered per Pattern 15), the explicit-degrade rules, and the exact rendering (compact text Gantts + Mermaid chart).

---

## Step 5: Assumptions Under Clause 61.6

Where an effect is too uncertain to forecast reasonably, do not guess — list it as an assumption the PM should state under **61.6** (e.g. "assumed no further access restriction beyond [date]"). If later shown wrong, the PM's correction is itself a compensation event under **60.1(17)**. None → "No 61.6 assumptions required — all effects were forecastable from the evidence gathered."

---

## Step 6: Evidence Schedule

Reuse the shared table format at `../ce-builder/references/evidence-schedule.md`, covering only records dated up to the dividing date (Step 2).

---

## Step 7: Summary and Quotation Header

Read `references/output-template.md` for the header
block (with the `QT-[NNN]` ref, Pattern 8) and the closing summary table / submission timetable
(Changes to the Prices, Completion/Key Date delay, and the 62.3/62.6 deadlines).

---

## Step 8: Shareable HTML Version (On by Default for Full Runs)

For any full run (project, event, and edition/Option all resolved), generate a presentable HTML version by default, without asking, right after the chat report.

1. Build the output as one JSON object covering the header fields, Step 3 build-up table, Step 4 programmes and Mermaid chart, Step 5 assumptions, Step 6 evidence schedule, and Step 7 summary table.
2. Read the shared template `../../shared/templates/ce-submission-template.html`.
3. Splice the JSON between `/*__CE_SUBMISSION_DATA__*/` and `/*__END_CE_SUBMISSION_DATA__*/` (keep both markers), document type `"quotation"`.
4. Write to `ce-quotation-[project-slug]-[QT-NNN].html` in the working directory and state the path.

**Skip** only for a chat-only request or a decline when told a file is about to be written. Template unreadable → say so, present chat-only, never hand-build a substitute HTML file.

---

## Rules

- **Never sum register totals (Pattern 11):** cite the master register's figure by Ref — never re-total across registers.
- **"Coincides with" discipline:** never assert timing alone proves causation — narrative content carries the causal link.
- **One-stop shop:** state plainly: once accepted (expressly or by deemed acceptance under 62.6), the CE is implemented and the assessment is final (65.2/66.2) — a head of cost or time not included now cannot be added later.
- **UK English**. Early warnings are **"notified"**, never "raised".
- Supports the commercial manager's submission; **not legal advice**. Contract-specific amendments override anything stated here (see Contract Profile above).

---

## Related Skills

- `$ce-builder` — the prior clause 61.3 notification stage this skill follows
- `$nec-deadlines` — track the 62.3 and 62.6 timescales above
- `$delay-analysis`, `$access`, `$weather-impact` — registers for Step 2 evidence (Pattern 11)
- `$programme` — forward-looking schedule-risk view behind Step 4's Accepted Programme
- `$contract-profile` — captures Fee %, amended periods, secondary options
- `$programme-import` — imports/confirms the Step 4 Accepted Programme baseline (Pattern 15)
