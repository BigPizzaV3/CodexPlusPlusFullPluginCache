---
name: timesheet-check
description: Validate paid timesheets (person, date, hours) against Gather's signing-in
  attendance and labour hours, verdict per line, both directions. Not a subbie's quantity/daywork
  claim (use subcontractor-check).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Timesheet Check — Paid Hours vs the Signing-In Record

Validate the timesheets being paid against what Gather's records show actually happened on
site. Gather's people/labour data is the contemporaneous signing-in record; the timesheet is
the external document (agency, payroll, or subcontractor labour-only invoice). The output is a
records-based verification for commercial review — it is neutral, it checks **both
directions**, and it is not an accusation of fraud.

Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Locate and Parse the Timesheet

Resolve the project (Pattern 1) and period (Pattern 2). Then find the timesheet:

- A file the user names (CSV, XLSX, or a markdown/text table), or
- A file in the working directory whose name contains "timesheet" (**confirm before using
  it**), or
- Lines pasted into the conversation.

Parse into a normalised table: **Person | Date | Hours claimed | Trade (if present) |
Rate/Value (if present)**. Then **confirm the parse back to the user before verifying**: show
the first few rows, the row count, the date span, and total claimed hours. Do not proceed on
an unconfirmed parse — a mis-read column silently corrupts every verdict.

---

## Step 2: Match People to the Roster

Call `getPeople` for the project and match each timesheet name to the roster:

1. Exact match first.
2. Then obvious variants: case differences, surname-first ordering, initials ("J. Smith" /
   "John Smith"), common short forms (Dave/David).
3. Anything still unmatched goes to an **UNMATCHED NAMES** list — never guess a match. An
   unmatched name is reported as such, and its lines are excluded from hour comparisons (they
   appear in the exceptions section instead).

---

## Step 3: Pull the Signing-In Legs from Gather

Make both calls **in parallel** for the confirmed period:

- `getCachedReport` — **Report:** `dashboardResourceLabour` — recorded hours per person per
  date, with trade.
- `getCachedReport` — **Report:** `dashboardShiftTable` — shift-level attendance.

**Schema gate (Pattern 12):** if this workspace's labour data does not provide per-person,
per-date hours, degrade explicitly to **attendance-only checking** (present / not present per
date, no hours comparison) and say so in the output header. Never approximate hours from
aggregate figures.

**Coverage context:** note any dates in the period with no records at all (they drive the NO
RECORDS verdict below and must be reported as recording gaps, not absences). If coverage for
the period is thin, say so prominently and recommend `$data-quality` — a verification
against thin records proves little in either direction.

---

## Step 4: Verify Line by Line

For each matched timesheet line, compare claimed hours with recorded hours for that person on
that date. Tolerance: **±0.5 hours per line** by default (state it; adjust if the user asks).

| Verdict | Meaning |
|---|---|
| **MATCH** | Recorded hours within tolerance of claimed hours |
| **PARTIAL** | Person recorded on site that date, but hours differ beyond tolerance — show both figures and the variance |
| **NOT SUPPORTED BY RECORDS** | Records exist for that date and this person does not appear in them |
| **NO RECORDS** | Nothing recorded for that date at all — a **recording gap**, never evidence of absence |

**Language discipline:** "the records do not support 10.0 hours on 14 March" — never "he
didn't work", "she wasn't there", or any assertion that work did not happen. The records are
the claim, not the person's character.

### The reverse sweep (always run it)

Scan the recorded hours for the same people and period for days **worked but not claimed** —
recorded attendance with no matching timesheet line. Report these as UNDERCLAIMED / QUERY
lines. The check cuts both ways; finding underpayment as readily as overpayment is what makes
the output usable with the other party.

---

## Step 5: Report

```
TIMESHEET VERIFICATION
Ref: TS-[NNN]
Project: [name] | Period: [dates] | Timesheet: [source] | Tolerance: ±0.5h/line
[Coverage note if any dates lack records / attendance-only mode note if degraded]

1. SUMMARY
   Claimed: [X] lines, [Y] hours [, £Z where the timesheet carries rates]
   Recorded (matched people, period): [Y'] hours
   Variance: [Y - Y'] hours [, value at timesheet rates / commercial-profile rates — source
   cited per Pattern 14; omit value if no rates supplied]
   Verdicts: [n] MATCH / [n] PARTIAL / [n] NOT SUPPORTED / [n] NO RECORDS / [n] unmatched names

2. EXCEPTIONS (ranked by hours/value at variance)
   | Person | Date | Claimed | Recorded | Variance | Verdict | Evidence |
   (Evidence column cites the record IDs; MATCH lines are summarised, not listed.)

3. REVERSE SWEEP — recorded but not claimed
   | Person | Date | Recorded | On timesheet? | Note |

4. UNMATCHED NAMES
   [names + "confirm identity or supply the roster name" — no verdicts issued]

5. DRAFT QUERY (for the agency / payroll / subcontractor)
   [Factual, line-by-line, quoting the records: "Our site records for 14 March show 8.0
   hours for J Smith against 10.0 claimed (record c4d5…). Please review and confirm."]
   Caution: withholding payment may carry contractual notice requirements (pay-less notice
   under the Construction Act / Y(UK)2 where NEC applies) — check the contract profile and
   the contract knowledge skills before acting commercially on this verification.

NOTES
- Records-based verification for internal commercial review — a recording gap is not proof of
  absence, and this output is not an accusation.
- This output names individuals. Handle as personal data: internal use, minimum circulation.
- Ref: TS-[NNN] is a session-local sequence number for cross-referencing.
```

---

## Hard Rules

1. Never invent hours, rates, or name matches. Every figure is from the timesheet, the
   records, or the commercial profile (source cited).
2. NO RECORDS is a distinct verdict and always carries the coverage context.
3. The reverse sweep is not optional — a one-directional check is a collections tool, not a
   verification.
4. Value columns only where rates exist (timesheet's own rates or Pattern 14 commercial
   profile); otherwise hours-only, never blocked.
5. Confirm the parse (Step 1) and any fuzzy name match the user hasn't confirmed before
   issuing verdicts against them.

---

## Related Skills

- `$subcontractor-check` — quantity/daywork application verification (measured work,
  not paid-hours timesheets)
- `$people` — the roster and attendance view this skill verifies against
- `$labour` — hours analysis without an external document to verify
- `$data-quality` — run first when coverage looks thin
- `$commercial-profile` — supply rates to price the variance
