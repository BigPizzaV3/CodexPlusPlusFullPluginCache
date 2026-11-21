---
name: programme-create
description: Draft a construction programme from scope and your achieved norms — user-confirmed
  logic, engine-computed dates, NEC 31.2 checklist, exported as MS Project XML for
  the planner to own. A skeleton, never a finished plan.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Draft Programme Builder (Ref DP-NNN)

Builds a **draft programme skeleton**: activities from your scope, durations from evidence
(your achieved norms or your stated rates — never invented), logic you confirm, dates computed
by the deterministic CPM engine, shaped from birth to what NEC clause 31.2 requires a
programme to show, and written as MSPDI XML that MS Project opens natively (P6 and Asta
import it). Follow the shared patterns: project resolution
(Pattern 1, `../../shared/patterns/01-project-resolution.md`), report numbering (Pattern 8, `../../shared/patterns/08-report-numbering.md`), the contract profile (Pattern 13, `../../shared/patterns/13-contract-profile.md`), and the
programme conventions (Pattern 15, `../../shared/patterns/15-programme-baseline.md`).

**Scope note — the boundary that keeps planners as allies:** this skill drafts; the planner
plans. The output is a DRAFT-marked skeleton for a planner to own, re-sequence, resource-level
and buildability-check in their planning tool. It is never submitted as-is, never called the
Accepted Programme, and never resource-levelled here. Under NEC, a compliant **first**
programme is worth real money (25% of PWDD may be withheld without one — NEC3 50.3 / NEC4
50.5), which is exactly why the draft leaves nothing 31.2 requires silently absent: gaps are
listed for the planner, not papered over.

---

## Step 1: Scope and Contract Frame

1. Resolve the project (Pattern 1) and the draft's purpose from `the user’s request`: **tender**,
   **first programme** (clause 31), or **recovery** (re-drafting around a live position).
2. **Activity list**, in order of preference: user-supplied list (pasted scope/BoQ sections);
   the project's Gather activity names (`dashboardProgress`) as a starting set the user
   prunes; never invented beyond what the user confirms. Capture per activity, where offered:
   quantity + unit, work area/chainage, and any method notes.
3. **Contract frame** from `contract-profile.md` (Pattern 13): starting date, access dates,
   Completion Date, **Key Dates and Sectional Completions** (typed distinctly — their
   consequences differ), and the 31.2 information requirements as amended. Absent profile →
   user-supplied dates with the standard assumption statement.
4. **Possessions/access windows** — user-stated list (dates or recurring patterns). The user
   chooses how each is modelled: a calendar exception (work only inside possessions) or an
   SNET constraint on the affected activities. Never assumed.

## Step 2: Durations From Evidence

For each activity, in order of preference — the source is cited on every line:

1. **Rate library** (`estimating/rate-library.md`): duration_hours = quantity × norm (hrs/unit)
   ÷ gang size (user-stated). Cite "per the rate library ([sweep date])" and carry LOW BASIS
   flags through to the draft.
2. **User-stated** norm, gang size, or direct duration — cited "user-supplied this session".
3. **Neither** → the activity enters the draft with duration **"TBC by planner"** (a 1-day
   placeholder flagged loudly in the 31.2 checklist) — **never an invented duration**.

## Step 3: Logic — Proposed, Then Confirmed

Propose the network from the method the user describes ("piers before deck, two fronts,
waterproofing follows steel by area") plus defaults stated as defaults (sequential within a
work area, FS links, no lags unless stated). Present the full logic table (predecessor →
successor, type, lag) and **confirm it before anything becomes a link** — the same discipline
as the import mapping (Pattern 15 rule 5). Non-interactive runs: exact-statement-of-assumption,
and the draft is marked "logic unconfirmed — planner review required".

## Step 4: TRA and Float — the User's Risk, Never Ours

Time risk allowances are the Contractor's own assessment (and their absence on critical
activities is a recognised 31.3 rejection ground). Ask for the user's TRA view (per activity,
per work type, or a stated %). **Never fabricate a TRA.** Non-interactive or not offered →
the TRA column reads "REQUIRED — state before submission" and the 31.2 checklist flags it red.
TRA entered as user-stated is modelled as explicit TRA activities or duration uplift (user's
choice), shown separately per 31.2's requirement.

## Step 5: Compute the Draft's Dates

Build the sidecar-schema JSON (tasks, links, calendars from Step 1's possessions model,
constraints) and run the engine:

    python3 ../../scripts/cpm.py <draft.json>

The engine's forward/backward pass gives the draft its dates, float, and critical path —
labelled **"DRAFT — engine-computed"** (there is no Accepted Programme to misrepresent here;
the label distinguishes computed-draft from planner-owned). Check the computed Completion
against the contract frame: planned Completion beyond the Completion Date, or a Key
Date/Section missed, is the headline finding, not a footnote. python3 unavailable → the draft
is written with logic but undated, stated plainly.

## Step 6: The 31.2 Checklist

Show what the draft carries against what clause 31.2 requires the programme to show —
starting date, access dates, Key Dates, Completion, planned Completion, order and timing of
the works **and of the Client's and Others' work**, float, TRA, health and safety periods,
method statements per operation, resources per operation. Each row: PRESENT (with source) /
GAP — FOR THE PLANNER. The checklist ships inside the draft's md summary — an honest draft
knows what it is missing.

## Step 7: Write the Files

1. `programme/draft-programme-<purpose>-<date>.xml` via
   `python3 ../../scripts/write_mspdi.py <draft.json> --out <file>` — the
   title carries the DRAFT marker; never overwrite without confirming (`--force`).
2. A companion md summary: provenance (sources per duration, confirmed/unconfirmed logic,
   TRA status), the 31.2 checklist, the engine's critical path, and the handover note.
3. **Never** write to `programme/programme-baseline.*` — the draft is not the imported
   baseline (Pattern 15 rule 7).

## Step 8: Report

`Ref: DP-[NNN]` per Pattern 8. Sections: 1 SUMMARY (activities, computed span, planned
Completion vs Completion Date, critical path headline); 2 DURATION SOURCES (cited per line,
LOW BASIS and TBC flags); 3 LOGIC (confirmed/assumed); 4 TRA STATUS; 5 THE 31.2 CHECKLIST;
6 FILES WRITTEN; 7 STANDING CAVEAT:

> This is a DRAFT programme skeleton generated from stated scope, cited norms, and confirmed
> logic — **it is not a resource-levelled, buildability-checked construction programme, and
> it is not submitted to anyone by this plugin**. A planner must own, verify, and complete it
> in the planning tool before it goes near a tender or a clause 31 submission. Durations
> marked TBC and the 31.2 gaps listed above are the planner's punch-list.
> Ref: DP-[NNN] is a session-local sequence number for cross-referencing.

---

## Hard Rules

1. **No invented durations, norms, gang sizes, or TRAs** — every duration cites the rate
   library or the user; missing input → TBC flag, never a guess.
2. **Logic becomes links only on confirmation** (non-interactive: assumption-marked draft).
3. **The DRAFT marker travels everywhere** — file title, md summary, report header.
4. **Never writes the imported-baseline files**; the engine computes draft dates via the
   script only (Pattern 15 rule 3).
5. The planner owns the output — the skill says so, every run.
6. UK English throughout.

---

## Related Skills

- `$rate-library` — the achieved norms Step 2 prices durations from
- `$contract-profile` — the contract frame (dates, Key Dates, 31.2 as amended)
- `$programme-import` — import the planner's finished version back for analysis
- `$programme-impact` — indicative what-ifs on an imported programme
- The Programme Advisor agent — health-checks the finished submission against 31.3
