---
name: cvr
description: Build the monthly CVR — records-backed value at commercial-profile rates
  vs imported actual cost, margin by head, movement since last CVR, user-supplied
  accruals and liabilities. Draft for commercial review, never the accounts. Cost
  side needs cost-import.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Cost Value Reconciliation (Ref CV-NNN)

The monthly management reconciliation: value earned against cost incurred, margin by head,
and movement since the last CVR — built from records-backed value (Pattern 14 rates, see
`../../shared/patterns/14-commercial-profile.md`) and the
imported cost ledger (Pattern 16, see
`../../shared/patterns/16-cost-ledger.md`), with every adjustment
user-supplied and labelled. Follow the shared patterns: project resolution (Pattern 1,
`../../shared/patterns/01-project-resolution.md`), date parsing
(Pattern 2, `../../shared/patterns/02-date-range-parsing.md`), report
numbering (Pattern 8, `../../shared/patterns/08-report-numbering.md`),
and the commercial QA gate (Pattern 9,
`../../shared/patterns/09-commercial-qa-gate.md`).

**Scope note:** this is an internal management document, drafted for commercial review. It is
not the management or statutory accounts, not a certified valuation (use `$valuation`
for the application itself), and not a forecast (use `$cost-to-complete` /
Commercial Forecast agent). The cost side is only as good as the imported ledger — this skill
never invents a cost.

**Local files this skill reads (never writes):**
- **Pattern 16 (Cost Ledger)** — `commercial/cost-ledger.md`, the cost side. Absent → the CVR
  degrades to a **value-side shell**: full value build-up with the cost and margin columns
  reading "no cost ledger imported — run $cost-import", still complete and useful.
- **Pattern 14 (Commercial Profile)** — `commercial-profile.md` for rates, retention,
  prelims allowances. Unpriced lines go quantities-only, per Pattern 14 rule 2.
- **Pattern 13 (Contract Profile)** — `contract-profile.md` for `main_option`. Under
  **Options C–F** say so prominently: cost is Defined-Cost-shaped and the external value is the
  PWDD assessment, so the internal CVR margin and the contract margin are different animals —
  this CVR is the internal management view.

---

## Step 1: Resolve Project, Period, and Previous CVR Position

1. Resolve the project (Pattern 1) and the CVR period (Pattern 2 — normally a calendar month).
2. Resolve the **previous CVR position**, in this order: (a) an earlier `CV-[NNN]` ref in this
   conversation — reuse its cumulative value/cost/margin; (b) user-supplied previous figures
   (third `the user’s request` token, or asked for); (c) neither → treat as the **first CVR**: no
   movement section, stated prominently.
3. Read the three local files above (or their `<project>`-slugged variants). A file whose
   `project` does not match is ignored (say so — Pattern 13/14/16 rule).

---

## Step 2: Value to Date

Establish cumulative value earned, in this order of preference, **stating the basis used**:

1. **An `AP-[NNN]` valuation earlier in this conversation** — reuse its gross cumulative
   (before retention; a CVR reconciles value earned, not cash certified).
2. **Derive it now** — run the `$valuation` method (Steps 2–6 of that skill: cumulative
   quantities from `dashboardProgress` priced at profile rates, plus the prelims line) for the
   period end. Unpriced lines go to a quantities-only annex and are **excluded from the value
   total** (say so — an unpriced line is a gap, not zero value).
3. **User-pasted internal valuation** — accepted verbatim, cited "user-supplied this session".

Then take **value adjustments — user-supplied only**, each a distinctly-labelled line: internal
over/under-measure vs the application, work in progress not yet measurable, materials on site,
and value for notified-but-unagreed CEs (cite `QT-[NNN]`/`CE-[NNN]` refs where they exist in
this conversation; a CE with no quotation ref and no user figure is listed **unvalued** — never
guessed). No adjustments offered → the section reads "none supplied".

---

## Step 3: Cost to Date

From `commercial/cost-ledger.md` (Pattern 16): the cumulative cost table by CVR head, cited
"per the imported cost ledger ([source system], period to [date])". Respect the confirmed
column semantics — never re-read a period column as cumulative or vice versa (Pattern 16
rule 2).

Then take **cost adjustments — user-supplied only**: accruals (cost incurred, not yet costed),
subcontract liabilities (including retention held on subcontractors), and provisions. Each is a
labelled line under its head; none are ever derived (Pattern 16 rule 3).

**Date alignment gate:** if the ledger period end differs from the CVR period end by more than
a few days, flag it prominently — value to [date A] against cost to [date B] is a mismatched
reconciliation, and the gap is stated on every affected total.

---

## Step 4: Reconcile

Where the ledger's CVR heads and the value build-up can be aligned (labour, plant, materials,
subcontract, prelims/staff — via the Pattern 16 head mapping), reconcile per head; the
remainder reconciles at the totals line only (say which).

| Head | Value to date | Cost to date | Margin | Margin % |
|---|---|---|---|---|

Totals: **cumulative value | cumulative cost | cumulative margin | margin %**. If the
commercial profile carries tender allowances (e.g. `prelims`), compare the relevant head
against its allowance and flag overruns (the `$prelims-monitor` method).

Cross-checks (Pattern 9, ±0.5% tolerance, flag — never silently resolve):
- Value total vs any `AP-[NNN]` cumulative in this conversation.
- Cost grand total vs the ledger's own total row (as recorded at import).

---

## Step 5: Movement Since Last CVR

Skip on a first CVR (say so). Otherwise, against the Step 1 previous position:

| | Previous CVR | This CVR | Movement |
|---|---|---|---|
| Value to date | | | |
| Cost to date | | | |
| Margin | | | |

**Drivers commentary** — only where records or session refs support it, cited: productivity
movement (`PG` refs / `dashboardProgress`), idle plant exposure (`OH` refs), prelims run-rate
(`PS` refs), CE value newly quoted (`QT` refs), weather (`WI` refs). Timing language is
"coincides with", never "caused by" — and a margin movement with no records-backed driver is
reported as **unexplained**, for the commercial manager to run down, not narrated away.

---

## Step 6: Gaps & Risks

Always present:
- Cost heads with cost but no reconcilable value (and vice versa)
- Unmapped cost codes from the import; unpriced value lines from Step 2
- Unvalued notified CEs
- Ledger/CVR date misalignment (Step 3 gate)
- Any reliance on user-supplied adjustments (list them — they are the least auditable lines)

---

## Step 7: Present the CVR

Apply Pattern 8 for the `CV-[NNN]` ref (session-local; increment on a prior `CV` ref, else 001).

```
COST VALUE RECONCILIATION — [Project Name]
Ref: CV-[NNN]
Period: to [CVR period end] | Cost ledger: [source], period to [date] | Currency: [GBP]
Contract Option: [A–F / "not confirmed"] | Previous CVR: [date / "none — first CVR"]

1. SUMMARY — value, cost, margin, margin %, and the headline movement, in two sentences
2. VALUE TO DATE — basis stated; adjustments table (each line labelled user-supplied)
3. COST TO DATE — by head, per the imported ledger; adjustments table
4. RECONCILIATION — the Step 4 table
5. MOVEMENT — the Step 5 table + drivers commentary (omit on a first CVR, say so)
6. GAPS & RISKS — Step 6, always present
7. STANDING CAVEAT
```

The standing caveat, always, unmodified:

> This is a draft cost value reconciliation for internal commercial review, built from
> user-supplied cost data and records-backed value — **it is not the management or statutory
> accounts, and not a certified valuation**. Accruals, liabilities, and provisions are as
> supplied by the user and should be reviewed against the accounting system before this CVR is
> relied on. This document is internal — do not issue the cost side to the other party.
> Ref: CV-[NNN] is a session-local sequence number for cross-referencing.

If Step 3 found no cost ledger, present the value-side shell (sections 1–2 with cost/margin
columns marked, section 6, the caveat) and point once to `$cost-import`.

---

## Hard Rules

1. **Never invent a cost, an accrual, or an adjustment.** Every non-records figure is either
   from the imported ledger (cited) or user-supplied (labelled). No "typical" anything
   (Pattern 14 rule 1, Pattern 16 rules 1 & 3).
2. **Column semantics as confirmed at import** — never reinterpret period vs cumulative
   (Pattern 16 rule 2).
3. **Margin movement is explained only by cited drivers** — otherwise it is "unexplained",
   stated plainly.
4. **The cost side never goes to the other party** (Pattern 16 rule 6) — outputs for external
   use come from `$valuation`, not from here.
5. UK English throughout.

---

## Related Skills

- `$cost-import` — imports the cost side this skill reconciles (Pattern 16 producer)
- `$valuation` — the records-backed external application; its gross cumulative feeds Step 2
- `$commercial-profile` — the rates the value side is priced at
- `$cost-to-complete` — the forward-looking counterpart (this skill is backward-looking)
- `$prelims-monitor` — prelims allowance tracking cited in Step 4/5 commentary
- `$ce-quotation` — prices the unagreed-CE value lines Step 2 lists
- `$cashflow` — the forward, dated counterpart: phases this reconciliation's value and cost through the payment cycle
- `$final-account` — the settlement view; cross-check its records-supported measured work against this CVR's value to date
