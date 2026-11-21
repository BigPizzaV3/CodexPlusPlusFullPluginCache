---
name: cost-import
description: Import actual cost from your accounting system (COINS, Eque2, Sage —
  CSV export) with user-confirmed column and cost-head mapping; writes the local cost
  ledger the CVR reads. Costs as stated, never invented. Cost side only — value comes
  from valuation/cvr.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Cost Ledger Import (Ref CL-NNN)

The Gather API carries no cost data — the cost side of a CVR lives in the accounting system.
This skill parses a cost-ledger export (CSV from COINS, Eque2, Sage, or a cost spreadsheet) and
writes `commercial/cost-ledger.md`, the normalised local cache `$cvr` reads. This skill
is the **producer** of **Pattern 16 (Cost Ledger)** in
`../../shared/patterns/16-cost-ledger.md`; read it before starting —
it governs the file schema and the consuming rules. Also follow **Pattern 1** (project
resolution) and **Pattern 8** (report numbering).

**Scope note:** this skill imports and normalises cost **as stated in the export** — it never
estimates, scales, or apportions a cost, and never derives an accrual. If a figure isn't in the
export or supplied by the user, it is "not in the imported ledger", not a guess. The
reconciliation itself is `$cvr`'s job.

---

## Step 1: Locate the File

Resolve the project (Pattern 1). Then find the ledger file:

- A file the user names in `the user’s request`, or
- A working-folder scan for `.csv` files with ledger-ish names (containing "cost", "ledger",
  "CVR", "COINS", the project name) — **confirm before using it**, the same discipline as
  `programme-import` Step 1.

**Format handling:**
- `.csv` → parse directly (Step 2).
- `.xlsx`/`.xls` → do not guess at binary contents. If a Python environment with `openpyxl` is
  available, offer to convert the named sheet to CSV first (show the sheet names and confirm
  which); otherwise instruct: "Save the ledger sheet as CSV (File → Save As → CSV) and re-run
  with the `.csv` file." Stop rather than parse a spreadsheet blind.
- A pasted table in the conversation is accepted as equivalent to a CSV.

---

## Step 2: Column Mapping (the Critical Discipline)

Show the header row and the first three data rows back to the user, then propose a column
mapping:

| Target field | Notes |
|---|---|
| Cost code | The ledger's own code (required) |
| Description | Line description (required) |
| Period cost | Cost this period only |
| Cumulative cost | Cost to date |
| Committed cost | Orders placed, not yet costed (optional) |
| Accrual | Only if the export itself carries one (optional) |

**Period vs cumulative is the classic double-count.** Never guess which a value column is —
propose from the header wording, then have the user confirm (non-interactive runs: state the
proposed reading as an explicit assumption). If only one value column exists, confirm whether
it is period or cumulative; record the answer in the provenance block. A total/summary row in
the export is used as a cross-check (Pattern 9, ±0.5% tolerance), never double-counted into
the body.

Confirm the **currency** and the **ledger period end / data date** (from the export header or
the user — never today's date).

---

## Step 3: CVR-Head Mapping

Map each cost code to a CVR head: **labour, plant, materials, subcontract, prelims/staff,
other**. Propose from the descriptions (exact/contains matching, the same discipline as
`programme-import` Step 4), show the full proposed table, and have the user confirm or correct
it. Anything unresolvable stays in an **unmapped list** — never force-matched. Where the user's
CVR uses different heads, adopt theirs (the heads are a convention, not a rule).

---

## Step 4: Validate and Confirm

Summarise back before writing:

- Source system and filename; ledger period end / data date; currency
- Row count; value columns found and their confirmed semantics (period/cumulative/committed)
- Total per CVR head, and the grand total vs any total row in the export (Pattern 9 check)
- Unmapped cost codes (count + list)

---

## Step 5: Write the Ledger File

Write `commercial/cost-ledger.md` following the **Pattern 16** schema exactly: provenance block
(source system, filename, period end/data date, currency, column semantics as confirmed,
commitments/accruals included or not), the normalised cost table by CVR head (with period and
cumulative columns where carried), and the confirmed cost-code ↔ CVR-head mapping plus the
unmapped list.

If `commercial/cost-ledger.md` already exists, **do not overwrite without confirming**: show
its existing provenance block (source, period end) and ask whether to replace it, or keep both
periods by appending this period's table (the CVR reads the latest period and uses the prior
one for movement). Non-interactive runs: state the existing provenance, state the assumption to
replace, and continue.

---

## Step 6: Report

```
COST LEDGER IMPORT
Ref: CL-[NNN]
Source: [filename] | System: [COINS/Eque2/Sage/spreadsheet/stated] | Period to: [date] | Currency: [GBP]

1. IMPORT SUMMARY
   Rows: [n] | Value columns: [period/cumulative/committed as confirmed]
   Grand total: [X] (cross-check vs export total row: [match/±diff])

2. COST BY CVR HEAD
   | Head | Period | Cumulative | Committed |

3. UNMAPPED COST CODES
   [list, or "none"]

4. WHAT THIS UNLOCKS
   - $cvr — cost vs value reconciliation for this period

5. CAVEAT
   Costs are as stated in the imported ledger — nothing estimated, scaled, or accrued by this
   skill. Accruals, liabilities, and provisions are supplied to $cvr directly.
```

Remind the user once (Pattern 16 rule 6): this file carries commercially sensitive cost data —
keep it out of shared repositories (`.gitignore`), and never circulate it to the other party.

---

## Hard Rules

1. **Costs as stated — never invented, scaled, apportioned, or interpolated** (Pattern 16
   rule 1).
2. **Period vs cumulative is user-confirmed, never guessed** (Pattern 16 rule 2).
3. **No derived accruals.** Accruals/liabilities/provisions enter at `$cvr` as
   user-supplied adjustments, never here (Pattern 16 rule 3).
4. Only this skill writes `commercial/cost-ledger.md` (Pattern 16 rule 5).
5. Binary spreadsheets are never parsed blind — convert to CSV first.
6. UK English throughout.

---

## Related Skills

- `$cvr` — reconciles this ledger against records-backed value
- `$commercial-profile` — the value-side rates file (Pattern 14)
- `$valuation` — the records-backed value the CVR compares against
