---
name: boq-import
description: Import a bill of quantities (CSV or pasted) with user-confirmed column
  mapping and section hierarchy into the local tender store the pricing build-up reads.
  Quantities as billed, never adjusted; totals cross-checked.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# BoQ Import (Ref BQ-NNN)

The Gather API carries no tender data — the bill being priced lives in a spreadsheet the
estimator holds locally. This skill parses a bill-of-quantities export (CSV, or a pasted table)
and writes `tender/boq.json` (the row-level sidecar) plus `tender/boq.md` (provenance), the
normalised local store `$tender-pricing` and `$quote-levelling` read. This skill
is the **producer** of **Pattern 18 (Tender Bill, Quotes, and the Pricing Build-Up)** in
`../../shared/patterns/18-tender-bill-boq.md`; read it before starting —
it governs the file split, the four admissible pricing sources, and the consuming skills'
rules. Also follow **Pattern 8** (report numbering, `../../shared/patterns/08-report-numbering.md`).

**Scope note:** this skill imports and normalises the bill **as billed** — it never adjusts a
quantity, never invents a rate, and never corrects a suspected billing error. A blank quantity,
a zero quantity, or a duplicated item reference is a **flagged query for the estimator**, not
something this skill fixes. Pricing the bill is `$tender-pricing`'s job; this skill only
gets the quantities into the store cleanly and honestly.

**Sensitivity:** everything under `tender/` is competitively sensitive from the first line —
gitignored in this repo (`tender/`), never circulated to the client, the subcontract market, or
anyone outside the bid team, before or after award. Say this once, at Step 4.

---

## Step 1: Locate the File

Find the bill:

- A file the user names in `the user’s request`, or
- A working-folder scan of `tender/` (and the working directory) for `.csv` files with
  bill-ish names (containing "boq", "bill", "bq", "tender", the project/tender name) —
  **confirm before using it**, the same discipline as `cost-import` Step 1.
- A pasted table in the conversation is accepted as equivalent to a CSV.

**Format handling:**
- `.csv` → parse directly (Step 2).
- `.xlsx`/`.xls` → do not guess at binary contents. If a Python environment with `openpyxl` is
  available, offer to convert the named sheet to CSV first (show the sheet names and confirm
  which); otherwise instruct: "Save the bill sheet as CSV (File → Save As → CSV) and re-run with
  the `.csv` file." Stop rather than parse a spreadsheet blind — the same rule as `cost-import`
  Step 1.

---

## Step 2: Column Mapping (the Critical Discipline)

Show the header row (and any title/provenance row above it) and the first several data rows
back to the user, then propose a column mapping:

| Target field | Notes |
|---|---|
| Item ref | The bill's own reference (e.g. `1.1`, `2.3`) — required |
| Description | Item description — required |
| Unit | m, m2, m3, t, nr, item, etc. — required |
| Quantity | The billed quantity — required |
| Client rate | Only where the bill carries one (optional) |
| Client amount | Only where the bill carries one (optional) |

**State plainly which shape this bill is.** A bill with no rate/amount columns is normal for a
design-and-build tender priced entirely by the contractor — say so ("rate-less bill — no client
rates or amounts to cross-check against"). A bill that does carry rate/amount columns is a
priced or partially-priced bill (e.g. a re-measurement contract, or a client cost plan) — map
those columns too, they are cross-checked at Step 3.

**Section/element hierarchy** — propose the source and confirm it, never guess:
1. A dedicated section column, if present (as in the sample bill), or
2. The item-ref structure itself (e.g. `3.2.1` → section 3, sub-section 3.2), or
3. Heading/section rows interspersed in the data (rows with a ref/description but no
   quantity, acting as a section title).

Show the proposed mapping and section-hierarchy source, and confirm both before proceeding
(non-interactive runs: state the proposed reading as an explicit assumption — column mapping,
bill shape, and hierarchy source all named — and continue).

---

## Step 3: Validate

Summarise back before writing:

1. **Row/item counts** — total rows parsed, and per-section counts.
2. **Section summary** — one line per section (name, item count, unit mix).
3. **Quantity sanity** — every row with a **blank or zero quantity** is listed as a query
   (never dropped from the store, never given an invented figure). Every **duplicated item
   reference** is also listed as a query (never silently renumbered or merged) — a repeated ref
   almost always means a mis-keyed bill, but the fix is the estimator's call, not this skill's.
4. **Totals cross-check** — only where the bill carries client rates/amounts: sum the computed
   or stated amounts and compare against any stated total row (Pattern 9, ±0.5% tolerance). A
   mismatch outside tolerance is **flagged, never resolved** — do not adjust a quantity or rate
   to make the total agree. For a rate-less bill, state plainly that there is no amount total to
   cross-check.

---

## Step 4: Write the Bill Files

Write two files:

- **`tender/boq.json`** — row-level sidecar, one entry per bill row: `ref`, `description`,
  `unit`, `qty`, `section_path`, and `client_rate`/`client_amount` where the bill carries them
  (omitted entirely for a rate-less bill). This is the store `$tender-pricing` and
  `$quote-levelling` read — bills run to thousands of items, so the JSON is the source of
  truth and the md file below is for humans.
- **`tender/boq.md`** — provenance: source filename, column semantics as confirmed (including the
  bill shape — rate-less / priced), section/hierarchy source, row and section counts, section
  totals (quantity-only for a rate-less bill; value totals plus the Step 3 cross-check where the
  bill carries amounts), and the full **queries list** (blank quantities, duplicate refs, and any
  total-row mismatch).

If `tender/boq.json` already exists, **do not overwrite without confirming**: show its existing
provenance (source filename, item count) and ask whether to replace it. Non-interactive runs:
state the existing provenance, state the assumption to replace, and continue.

Remind the user (once, per Pattern 18's preamble): `tender/` is competitively sensitive —
already gitignored in this repo, and this bill must never be shared with the client, the
subcontract market, or anyone outside the bid team, before or after award.

---

## Step 5: Report

```
BOQ IMPORT
Ref: BQ-[NNN]
Source: [filename] | Bill shape: [rate-less / priced] | Hierarchy source: [section column / item-ref structure / heading rows]

1. IMPORT SUMMARY
   Rows: [n] | Sections: [n] | Column mapping: [ref/description/unit/qty (+ rate/amount if present) as confirmed]

2. SECTION SUMMARY
   | Section | Items | Units present | [Section total, if the bill carries amounts] |

3. QUERIES — FLAGGED FOR THE ESTIMATOR
   | Ref | Issue | Detail |
   [blank/zero quantities, duplicate refs, any total-row mismatch — or "none found"]

4. WHAT THIS UNLOCKS
   - $tender-pricing — build the priced rate build-up against this bill
   - $quote-levelling — level subcontractor quotes against these bill sections

5. CAVEAT
   Quantities above are as billed — nothing adjusted, corrected, or invented by this skill. The
   queries in section 3 are for the estimator to resolve; this import records them, it does not
   fix them. tender/ is competitively sensitive — keep it out of shared repositories and never
   circulate it to the client or subcontract market, before or after award.

Ref: BQ-[NNN] is a session-local sequence number for cross-referencing (Pattern 8).
```

---

## Hard Rules

1. **Quantities as billed — never adjusted, corrected, or invented**, including blank/zero
   quantities and duplicate item references (Pattern 18 rule 1).
2. **Column semantics are user-confirmed at import, never guessed** — bill shape (rate-less vs
   priced), and the section/hierarchy source (Pattern 18 rule 2).
3. Only `$boq-import` writes `tender/boq.json` and `tender/boq.md` — consuming skills
   read them.
4. **Suspected billing errors (blank quantities, duplicate refs, total mismatches) are flagged
   queries for the estimator — never silently corrected, merged, or renumbered.**
5. `tender/` is competitively sensitive — gitignored in this repo, never circulated before or
   after award.
6. Binary spreadsheets are never parsed blind — convert to CSV first.
7. UK English throughout.

---

## Related Skills

- `$tender-pricing` — the priced rate build-up against this bill (Pattern 18)
- `$quote-levelling` — levels subcontractor quotes against this bill's sections
- `$rate-library` — achieved labour norms, one of the four admissible pricing sources
- Bid Advisor agent — portfolio-level view across the bill, quotes, and pricing build-up
