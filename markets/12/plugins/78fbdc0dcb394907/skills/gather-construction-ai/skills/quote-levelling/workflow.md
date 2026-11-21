---
name: quote-levelling
description: compare subcontractor quotes like-for-like against the imported BoQ package
  scope — INCLUDED/EXCLUDED/QUALIFIED/SILENT verdict per scope item, exclusions surfaced,
  adjusted comparison only with your plug rates; SILENT is a finding, never assumed
  included.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Quote Levelling (Ref QL-NNN)

Compare subcontractor quotes for one package like-for-like against the imported bill scope —
a per-item, per-quote coverage verdict, exclusions surfaced in the quote's own words, and an
adjusted comparison built only from plug rates the user actually supplies. This is the
**pre-award mirror** of `$subcontractor-check`: that skill verifies claimed hours/output
against records after an order is placed; this skill verifies claimed *scope* against the bill
before one is. Follow the shared patterns in
`../../shared/patterns/18-tender-bill-boq.md`, in particular **Pattern 18** (the tender
bill, quote register, and pricing build-up conventions this skill operationalises — especially
rule 5: scope verdicts are INCLUDED/EXCLUDED/QUALIFIED/SILENT, and SILENT is never assumed
inclusion) and **Pattern 8** (report numbering).

---

## Step 1: Resolve Tender, Package, Bill Scope, and Quotes

1. Require `tender/boq.json` (or the `<tender-slug>`-qualified variant per Pattern 18). **Absent
   → stop**: "No imported bill found for this tender — run `$boq-import` first," and do
   not proceed with any levelling from memory or assumption.
2. Identify the package from `the user’s request` (or ask). Filter the bill to the package's items by
   section path; if the package boundary is not obvious from the bill's section structure,
   confirm the item list with the user before building the matrix — a wrong scope boundary
   invalidates every verdict downstream.
3. Read `tender/quote-register.md` (Pattern 18) for quotes already recorded against this
   package.
4. **Quotes pasted or dictated this session** are levelled alongside register quotes but are
   **not** written to the register by this skill — each becomes a clearly-marked **suggested
   register row** (subbie, date, total, scope basis, exclusions as stated) presented at Step 5
   for the user to add. The register is **append-only** and user-maintained (Pattern 18): this
   skill proposes rows, it never edits or overwrites existing ones.
5. Where a quote's wording is genuinely ambiguous against a bill item, flag the ambiguity rather
   than picking a verdict — an unclear quote is a query back to the subcontractor, not a guess.

---

## Step 2: Scope Matrix

Build one row per package bill item/section, one column per quote:

| Bill Item | Unit/Qty | [Quote A] | [Quote B] | ... |
|---|---|---|---|---|
| [item ref — description] | [qty, unit] | [verdict] | [verdict] | |

Each cell is **exactly one** of:

| Verdict | Meaning | Evidence requirement |
|---|---|---|
| **INCLUDED** | The quote's wording explicitly covers this item | Quote the covering wording verbatim |
| **EXCLUDED** | The quote states an exclusion for this item | Quote the exclusion verbatim |
| **QUALIFIED** | Covered, but subject to a stated condition | Quote the condition verbatim |
| **SILENT** | The quote says nothing about this item, either way | State plainly that it is a finding — see below |

**Hard rule (Pattern 18 rule 5):** SILENT is a **finding**, never an assumption of inclusion.
Never infer coverage from price plausibility — a higher total does **not** imply broader scope,
and a lower total does not imply an exclusion the quote never states. A blanket phrase covering
one bill section (e.g. "all works per Section 3") covers **only** the items whose section path
matches — it does not extend to an item filed under a different section (a provisional item, a
different trade heading) merely because that item is logically related. Where a blanket phrase's
reach against a specific item is genuinely unclear, mark **SILENT** and say why, rather than
stretching the wording to cover it.

---

## Step 3: Levelling — Adjusted Comparison

**Only where the user supplies a plug rate or allowance** for a specific EXCLUDED or SILENT cell
(e.g. "price the rock-excavation exclusion at your £6,000 allowance", or "plug rock excavation
wherever it isn't included") does that cell get adjusted:

1. Apply the user's plug to every cell it names, **per quote, independently** — a plug applied
   "wherever not included" adds to each quote whose matrix cell for that item is EXCLUDED **or**
   SILENT, not only the quote that stated an explicit exclusion. Each adjusted cell is labelled
   **"user-stated plug"** with the figure and the instruction that triggered it.
2. Present **raw totals** (the quote as submitted) and **levelled totals** (raw + applicable
   plugs) side by side — never only the levelled figure.
3. **No plugs offered for a gap → that gap stays unlevelled.** State the raw totals only and
   list the un-plugged coverage gaps plainly ("Item 1 (general excavation): SILENT for both
   quotes, no plug supplied — not reflected in either total"). An unlevelled comparison is
   presented as exactly that — never quietly false-ranked as if it were like-for-like.
4. Never invent a plug, a market rate, or a "typical" allowance to close a gap the user did not
   price. An unpriced gap is a stated limitation, not a number.

---

## Step 4: Findings

1. **Cheapest-raw vs cheapest-levelled** — state both explicitly, even when they name the same
   quote. They often differ; say so plainly when they do (a quote that looks cheapest raw can
   lose that position once its exclusions are priced in) — and say so plainly when they do
   **not**, since an unchanged ranking still needs stating rather than left implicit.
2. **Per-quote risk notes** — breadth of SILENT items is a risk in its own right, independent of
   price: a quote silent on more of the package scope carries more unpriced/unconfirmed risk
   than one that states its exclusions clearly, even if its raw total is lower.
3. **Payment terms / programme conditions** — note differences the quotes themselves state
   (e.g. payment period, programme duration, sequencing conditions). A quote that states nothing
   here is SILENT on terms, not assumed to match another quote's stated terms.
4. **Suggested register rows** for any quote pasted this session (Step 1.4).

---

## Step 5: Present the Comparison

Apply **Pattern 8** for the `QL-[NNN]` ref (session-local; increment on a prior `QL` ref in this
conversation, else `001`).

```
QUOTE LEVELLING — [Tender Name] — [Package]
Ref: QL-[NNN]
Bill source: tender/boq.json ([package] scope, [N] items)
Quotes compared: [list, register + pasted-this-session marked]
Generated: [today's date]
```

1. **Scope Matrix** — the Step 2 table.
2. **Totals** — raw totals per quote; levelled totals per quote where any plug was supplied
   (each plugged cell/line cited "user-stated plug"); unlevelled gaps listed where no plug was
   given.
3. **Findings** — the Step 4 items.
4. **Suggested Register Rows** — for quotes pasted this session, ready for the user to add to
   `tender/quote-register.md` (append-only, Pattern 18).
5. **Standing caveat**, always, unmodified in substance:

> This is commercial comparison support — it evidences what each quote does and does not cover
> against the billed scope, and prices only the adjustments you supplied. **Subcontractor
> selection is the buyer's decision.** This skill never recommends a subcontractor, ranks them
> by suitability, or predicts which will be selected — it compares scope and price as stated.
> Ref: QL-[NNN] is a session-local sequence number for cross-referencing.

---

## Hard Rules

1. **Verdicts come from quote wording only, and are quoted verbatim** — never inferred from
   price, from what "usually" is included in a trade package, or from another quote's wording.
2. **SILENT never becomes INCLUDED** — under any circumstance, including a higher price, a
   broad-sounding blanket phrase that doesn't name the item, or the item's apparent minor value.
3. **Plugs are user-stated only** — no invented, market, or "typical" rates close a coverage
   gap. No plug supplied means the gap stays unlevelled and stated as such.
4. **No selection recommendation** — the plugin evidences the comparison; it never says which
   subcontractor to choose, scores them for "best value," or predicts an award outcome.
5. **The register is append-only** — this skill only proposes suggested rows for pasted quotes;
   it never edits or overwrites existing `tender/quote-register.md` rows.
6. UK English throughout.

---

## Related Skills

- `$boq-import` — imports the bill this skill compares quotes against (required first)
- `$tender-pricing` — the estimator's own build-up, for comparing quotes against your
  internal price as well as the bill scope
- `$subcontractor-check` — the post-award mirror: verifies claimed hours/output against
  records once an order is placed, using the same never-assume-from-silence discipline
- Bid Advisor agent — portfolio-level bid decision support drawing on this comparison
