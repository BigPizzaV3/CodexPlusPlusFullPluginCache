---
name: final-account
description: Assemble the running, always-current final account — measured work, agreed
  vs unagreed CEs with evidence grades, records-supported vs claimed totals, and a
  negotiation appendix. Internal commercial-review draft, never for issue to the other
  party.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Final Account Builder (Ref FA-NNN)

A running, always-current final account position — a rebuild assembled fresh each run from what
the plugin already produces: the measured-work method (`$valuation`), the
compensation-event/variation register, dayworks, and the prelims position. It reflects the latest
agreed CEs, claimed CEs, and records each time — never "the" final account, only the position
**as of this run**.

**Scope note:** internal commercial-review draft only — not the final account statement for issue
to the other party, not a certified valuation (`$valuation`), not legal advice. Follow the
shared patterns in
`../../shared/patterns/01-project-resolution.md` for project resolution (Pattern 1), report
numbering (Pattern 8), cross-register reconciliation (Pattern 9), contract profile (Pattern 13),
commercial profile (Pattern 14), and the cost ledger (Pattern 16). Resolve contract-type
terminology (compensation event / Relevant Event / claim) via Pattern 5 before Step 3, and use it
consistently for the contract type in play.

**Local files this skill reads (never writes):**
- **Pattern 13 (Contract Profile)** — `contract-profile.md` for `main_option`. Option A (priced
  activity schedule): measured work = completed activities only. Option B (BoQ): standard measure.
  Options C–F: measured-work section is records-backed support for the Defined Cost application,
  not the PWDD assessment itself. State which applies, or state the assumption and point once to
  `$contract-profile` if absent.
- **Pattern 14 (Commercial Profile)** — `commercial-profile.md` for rates, retention, prelims
  allowance. Unpriced lines run quantities-only (Pattern 14 rule 2).
- **`ce-register.md`** (working-folder convention shared with the routines pack) — the
  Contractor's own record of CE dates and status; the read-only Gather API has no such field.
  **Absent** → every CE in Step 3 is either reused from a session ref or user-supplied this run,
  stated plainly; nothing is assumed agreed or unagreed by default.
- **Pattern 16 (Cost Ledger)** — `commercial/cost-ledger.md`, **context only** (e.g. sanity-check
  a claimed value against cost incurred). Never substitutes for the records-supported/claimed
  figures in Steps 2–5, which are records- and rate-based, not cost-based.

**Session refs reused, never re-derived where they exist:** a prior `AP-[NNN]` (valuation) for
measured work, `QT-[NNN]` (quotation) for a priced CE, `CE-[NNN]` (notification) for event
description and grounds, `CV-[NNN]` (CVR) for the internal value/cost cross-check. Cite the ref
each time one is reused rather than recomputing its figures from scratch.

---

## Step 1: Resolve Project and Read the Local Files

1. Resolve the project (Pattern 1).
2. Read `contract-profile.md` (or `<project>`-slugged variant). Note `main_option` and state which
   "measured work" meaning applies (see Profiles note above), or state the assumption if absent.
3. Read `commercial-profile.md` (or slugged variant) for rates, `retention_pct`, `prelims`. A
   profile whose `project` doesn't match is ignored — say so (Pattern 13/14 rule 4).
4. Read `ce-register.md` if present, for CE refs, grounds, dates, and status. A register whose
   `project` doesn't match is ignored — say so.
5. Read `commercial/cost-ledger.md` if present, for context only (see Profiles note above).
6. Scan this conversation for reusable `AP-`, `QT-`, `CE-`, `CV-` refs and list which were found —
   this run's measured work and CE tables are built from them wherever they exist, never
   re-fetched or re-priced from scratch.

---

## Step 2: Measured Work

Establish the cumulative measure, in order of preference, **stating the basis used**:

1. **A prior `AP-[NNN]` valuation in this conversation** — reuse its cumulative priced measure.
2. **Run the `$valuation` method now** (that skill's Steps 2–7): cumulative quantities from
   `dashboardProgress`, priced at `activity_rates` from the commercial profile.

Unpriced lines (no matching rate) go to a **quantities-only annex** — quantity and unit shown,
value column reading "rate not in commercial profile", **excluded from every total** in this
skill. Point once to `$commercial-profile`; never block on a missing rate (Pattern 14
rule 2).

---

## Step 3: Compensation Events / Variations

Two tables, kept strictly separate — the skill's central discipline.

### AGREED (implemented)

| Ref | Ground / Clause | Agreed Value | Source |
|---|---|---|---|
| CE-[NNN] | [e.g. 60.1(1)] | £[X] | [ce-register.md status / user-supplied this session] |

### UNAGREED

| Ref | Ground / Clause | Claimed Value | Records-Supported Value | Evidence Grade | Next Procedural Step |
|---|---|---|---|---|---|
| CE-[NNN] | [e.g. 60.1(2)] | £[X] (QT-[NNN] / user-supplied) | £[X] or "not yet quantified" | [A/B/C] | [e.g. "62.3 quotation due [date]"] |

Rules:
- **Ground / Clause**: from `ce-register.md`'s Ground column if present, else the Pattern 7
  event-to-clause mapping applied to the register's event description, else the user directly.
  Never invent one all three leave silent — state "ground not confirmed" instead.
- **Claimed value**: a `QT-[NNN]` quotation in this conversation, or a figure the user states now
  — cited either way. Neither → "not yet quantified", never guessed.
- **Records-supported value**: only what the records actually evidence — where a `QT-[NNN]`
  exists, recompute from the evidence it cites (not the claimed total); else "not yet quantified"
  rather than a lower guess.
- **CE status (agreed vs unagreed) and every date** are read from `ce-register.md` or supplied by
  the user this session — never assumed; the read-only Gather API carries no CE data. Where the
  correspondence register (Pattern 17) carries a **confirmed** notification or reply for a CE,
  cite it alongside the date ("notified 2026-01-12 per [COR-003]") — an evidence-cited date beats
  an asserted one in any negotiation.
- **Next procedural step**: `$nec-deadlines` logic against the register's dates (e.g. "62.3
  quotation due [date]", "61.4 reply overdue since [date] — notify the failure"); missing dates →
  "no dates in ce-register.md for this CE — cannot determine the next deadline."

### Evidence Grades

Mechanical, and they grade **the records, not the merits of the claim** — say so wherever a grade
is shown:

| Grade | Criteria |
|---|---|
| **A** | Every element of the claim cites specific records (record IDs / dates) that support it |
| **B** | Core records support the claim, with stated gaps in one or more elements |
| **C** | Assertion-led — little or no contemporaneous record support |

An A-grade claim can still fail on entitlement; a C-grade claim can still be contractually valid
but unevidenced. The grade says nothing about who is right.

---

## Step 4: Dayworks, Prelims and Other Heads

- **Dayworks** — reuse any `DW-[NNN]` sheet(s) from this conversation, or a user-supplied list of
  daywork values. No sheet and no figure → "no dayworks recorded this run."
- **Prelims position** — run the `$prelims-monitor` method: weekly headcount vs allowance,
  elapsed vs tender duration, projected overrun exposure. Cite a prior `PS-[NNN]` if one exists
  this conversation, otherwise derive it now. No `prelims` block in the commercial profile →
  quantities-only, per that skill's own degrade rule.
- **Other heads** — anything else (contra charges, LAD provisions, retention releases already
  agreed) is **user-supplied only**, each a distinctly labelled line, never derived from records or
  invented. No items offered → "none supplied."

---

## Step 5: The Statement

Build up **two** totals in parallel — never blend them:

| Line | Records-Supported | Claimed |
|---|---|---|
| Measured work (Step 2) | £[X] | £[X] (same figure — measured work is not in dispute) |
| Agreed CEs (Step 3) | £[X] | £[X] (same figure — agreed CEs are not in dispute) |
| Unagreed CEs (Step 3) | Σ records-supported column | Σ claimed column |
| Dayworks (Step 4) | £[X] | £[X] |
| Prelims position (Step 4) | £[X] | £[X] |
| Other heads (Step 4) | £[X] | £[X] |
| **Gross Position** | **£[X]** | **£[X]** |
| Retention (`retention_pct` per profile) | £[X] | £[X] |
| **Net Position** | **£[X]** | **£[X]** |

**Negotiation gap** = Claimed Net Position − Records-Supported Net Position. State it plainly as
the negotiation gap, not a discrepancy, not an error — never narrowed by inventing a number
in between (Hard Rule 1).

Cross-check (Pattern 9, ±0.5% tolerance, flag — never silently resolve): the records-supported
measured-work and agreed-CE lines against any `AP-[NNN]`/`CV-[NNN]` cumulative figures already in
this conversation.

---

## Step 6: Open Risks

Always present, even if every entry reads "none identified this run":

- **Time bars passed or approaching (61.3)** — each unagreed CE's aware/notified date run through
  `$nec-deadlines` logic; flag any within 2 weeks of the 8-week bar or already passed.
- **Deemed-acceptance opportunities available today** — any PM silence (61.4 reply, 62.3 reply)
  that a failure-notification would start the clock on right now.
- **Unvalued notified events** — a CE in the register with no claimed figure and no `QT-[NNN]`.
- **Records gaps that will be attacked** — every Grade B/C line from Step 3 and every
  quantities-only line from Step 2, named specifically — these are what the other party's QS
  targets first.

---

## Step 7: Negotiation Appendix (Internal Only)

Per open unagreed item (each Step 3 unagreed CE, plus any Step 6 risk worth a line): **strongest
evidence** (cited, e.g. "CE-014: narrative + labour data corroborate 6 standing shifts, record IDs
[...]"), **weakest point** (honest — a records gap, contractual vulnerability, time-bar risk),
and a **one-line drafted position**.

Hard Rule 3 applies here in full: no settlement predictions, no probability language, floor
is records-supported, ceiling is claimed, nothing invented between them.

---

## Step 8: Present the Final Account

Apply Pattern 8 for the `FA-[NNN]` ref (session-local; increment on a prior `FA` ref, else
`001`). Read `references/output-template.md` and use
its structure and standing caveat verbatim.

---

## Hard Rules

1. **Never blend the claimed and records-supported totals.** Section 5 always shows both; the gap
   is the negotiation gap — never reconciled away or averaged into one figure.
2. **Evidence grades (A/B/C) grade the records, not the claim's contractual merits** — state this
   every time a grade appears.
3. **No settlement predictions, no probability-of-success percentages, no "likely outcome"
   language** anywhere in this output, especially the negotiation appendix. The floor is
   records-supported; the ceiling is claimed; nothing is invented between them.
4. **CE statuses (agreed/unagreed) and every CE date are user- or `ce-register.md`-supplied, never
   assumed** — the read-only Gather API carries no compensation-event data.
5. Early warning is always **"notified"**, never "raised".
6. UK English.

---

## Related Skills

- `$valuation` — measured-work method Step 2 reuses (`AP-[NNN]`)
- `$ce-builder` — draft the clause 61.3 notification for a Step 6 unnotified event
- `$ce-quotation` — price an unagreed CE (`QT-[NNN]` feeds Step 3's claimed/records-supported figures)
- `$nec-deadlines` — the deadline behind every Step 3/6 "next procedural step"
- `$dayworks` — the signature-ready sheet behind any `DW-[NNN]` reused in Step 4
- `$cvr` — cross-check its `CV-[NNN]` value-to-date against Step 5's records-supported figures
- The red-team agent — adversarially tests the records-supported position and negotiation appendix before a live negotiation
