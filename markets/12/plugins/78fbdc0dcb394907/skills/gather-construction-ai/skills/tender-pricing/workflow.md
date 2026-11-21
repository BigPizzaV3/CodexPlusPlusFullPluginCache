---
name: tender-pricing
description: build the tender pricing from the imported BoQ — labour from your achieved
  norms, plant/materials/subcontract from your quotes, OH&P as your stated decision;
  every line labelled with its source, gaps flagged UNPRICED, never a market rate.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Tender Pricing Build-Up

This skill **is** Pattern 18 operationalised: the bill is priced from exactly four admissible
sources — your achieved labour norms, your quotes, the client's own billed rate where you elect
to adopt it, or nothing at all (**UNPRICED — flagged**). Read
`../../shared/patterns/18-tender-bill-boq.md` — **Pattern 18** (the
tender bill, quotes, and pricing build-up; this skill is its producer) and **Pattern 14**
(commercial profile — see note below for what it is *not* used for here) — plus **Pattern 8**
(report numbering).

**Scope note:** `the user’s request` names the tender for the report header only — this skill works
entirely from local tender files (`tender/boq.json`, `tender/quote-register.md`,
`estimating/rate-library.md`), not the Gather API, and resolves no Gather project (Pattern 1
does not apply). It prices; it does not recommend a bid decision, predict a win, or speculate
about competitors (Pattern 18 rule 6) — that is the business's call, and the Bid Advisor's
settle mode is where the priced build-up gets that review.

**Local files this skill reads (never writes unless stated):**
- **`tender/boq.json` + `tender/boq.md`** (Pattern 18) — the bill being priced. Written only by
  `$boq-import`. Absent → stop (Step 1).
- **`estimating/rate-library.md`** (the `rate-library` skill's output) — achieved labour-hour
  norms, with LOW BASIS provenance. Absent → no library source; the user may state a norm
  directly, or the line goes UNPRICED.
- **`tender/quote-register.md`** (Pattern 18) — subcontract/supply quotes, with scope basis and
  exclusions as stated. Maintained by the user / `$quote-levelling`. Absent → SUBCONTRACT
  is unavailable for every line; state this once.

**What this skill does NOT read:** `commercial-profile.md` (Pattern 14). That file prices a
*live, won* project against rates you already control — a tender has no contract yet, and
blending a different project's daywork or plant rates into a bid is exactly the unlabelled,
unsourced figure Pattern 18 exists to prevent. Labour £/hr, gang sizes, and plant/material rates
here come **only** from user input this session or `tender/quote-register.md` (Pattern 18 rule
3) — never a commercial profile, never a market or "typical" rate book.

---

## Step 1: The Bill Is the Anchor — Nothing to Price Without It

1. Look for `tender/boq.json` in the working directory. **Absent → stop here.** Say plainly:
   "No imported bill of quantities found — there is nothing to price. Run `$boq-import`
   first." Do not proceed on an assumed or hand-typed bill.
2. Present → read `tender/boq.md` alongside it for provenance (source file, column semantics as
   confirmed at import, section summary, whether the bill carries the client's own rate/amount
   columns).
3. Read `estimating/rate-library.md` if present — note its sweep date(s), the covered
   projects/window, and every LOW BASIS flag on a norm this bill's items might use.
4. Read `tender/quote-register.md` if present — note each row's package, subcontractor, total,
   scope basis, and exclusions as stated.
5. Ask for (or take from `the user’s request`/conversation) the session-stated inputs Step 2 needs:
   labour **£/hr** and **gang size(s)** per trade, and plant/material rates not covered by a
   quote-register row. State plainly wherever a figure is missing: "not stated this session —
   the affected lines go UNPRICED."
6. Label the tender in the report header from `the user’s request` (or ask) — a display label, not a
   project match (see Scope note).

---

## Step 2: Per-Item Build-Up — Four Sources, Labelled

For **every** bill item, build up its price from whichever of these four elements applies —
labelling the source on every line is not optional, it is the entire discipline:

**(a) LABOUR** — `hours = qty (as billed) × library norm (hrs/unit)`, norm cited to
`estimating/rate-library.md` with its sweep date and **LOW BASIS flag carried through** wherever
the norm carried one. No norm for this activity → ask for a user-stated norm this session
("user-supplied this session, not library-derived" — label it as such) or mark the hours line
**UNPRICED — flagged**. `£ = hours × user-stated £/hr`. No £/hr stated → show the hours (real
information) with the £ column **UNPRICED**, never a zero, never an assumed rate.

**(b) PLANT/MATERIALS** — user-stated rates this session, or a cited `tender/quote-register.md`
row (supplier quotes count too, not just subcontract packages). Never a market, "typical", or
catalogue rate under any name.

**(c) SUBCONTRACT** — a `tender/quote-register.md` row cited by package and subcontractor, with
its **package coverage stated** (in scope or not) and **exclusions carried verbatim** from the
register. An excluded scope (e.g. "excludes rock excavation") is not re-priced from thin air —
the excluded portion is its own **UNPRICED — flagged** line, named for what it is.

**(d) CLIENT'S BILLED RATE** — only where the bill carries the client's rate/amount column (per
`boq.md`'s confirmed column semantics) **and** the user elects, this session, to adopt it.
Label exactly: "client's billed rate, adopted as the tender basis (user election)" — never
presented as if the business derived it.

**Anything else** — no norm, no stated rate, no quote, no adopted client rate — is **UNPRICED —
flagged**, carried to Step 4's totals as a named exclusion with its billed quantity. Never zero,
never a "typical"/benchmark figure standing in.

Present the build-up per item:

| Item Ref | Description | Unit | Qty (as billed) | Element | Source Label | Hours (labour only) | £ |
|---|---|---|---:|---|---|---:|---:|

Roll up to a **per-section** summary (matching `boq.md`'s section structure) for the Step 5
report — item-level detail lives in `tender/pricing.json`.

---

## Step 3: Prelims, OH&P, and Risk — Yours to State, Never Ours to Compute

**Prelims** — from the user's tender prelims model: staff numbers, establishment weekly rate,
duration, all **user-stated**. A duration may cite a `$programme-create` tender draft's
computed span (a `DP-[NNN]` ref, if one exists) — cite as "per DP-[NNN] ([draft purpose])",
never invent one.

**OH&P and risk allowance** — **USER-STATED ONLY** (Pattern 18 rule 4). Ask for both if not
already given. Present each as its own labelled line: "OH&P: [X]% — user-stated commercial
decision" and "Risk allowance: [£X / X%] — user-stated commercial decision". **The percentage or
figure itself is never computed, never suggested, not even as a range or a "typical markup".**
Applying straightforward arithmetic against the priced total to show the £ value (Step 4) is
not "computing OH&P" — only the rate/figure must never originate from the skill. Not supplied →
"OH&P — REQUIRED, not stated this session" (or the risk equivalent) — never a default
percentage, never zero standing in, never folded into the total as if nil.

---

## Step 4: Totals — Honest Gap

Present, in this order:

1. **Priced total (before OH&P/risk)** — sum of every priced line from Step 2 (labour £ +
   plant/materials + subcontract + adopted client rates) plus Step 3's prelims line where stated.
2. **OH&P and risk applied** — where Step 3's figure(s) were stated, show the £ value as
   straightforward arithmetic against the priced total, labelled with the user-stated rate it
   came from; **not stated** → "REQUIRED, not stated this session", never folded in as zero.
3. **Tender total** — priced total plus OH&P/risk applied, only where the latter was stated;
   otherwise state plainly it is incomplete pending that decision.
4. **UNPRICED items** — every line flagged in Step 2, with **billed quantity**, unit, and why
   (no norm / no rate / no quote / excluded scope with no separate cover) — the honest gap the
   settlement meeting needs to see, not a rounding error to hide.
5. **LOW BASIS exposure subtotal** — the £ value of every priced labour line whose hours rest on
   a norm flagged LOW BASIS in Step 2(a), as both an amount and a % of the priced total — "how
   much of the price rests on thin norms", a single figure the settlement meeting can weigh.
6. **ASSUMPTIONS REGISTER** — one row per user-stated figure, norm interpretation, or adopted
   client rate used anywhere in this build-up:

   | # | Item / Line | Figure | Stated As | Source |
   |---|---|---|---|---|

   Every £/hr, gang size, plant/material rate, adopted client rate, prelims figure, OH&P %, and
   risk allowance appears here once — the audit trail for every non-quote, non-library figure.

---

## Step 5: Write the Files and Report

1. Write **`tender/pricing.json`** — row-level, matching `tender/boq.json`'s items: item ref,
   qty as billed, each element (a)–(d) present with its £/hours and source label, or
   `"UNPRICED"` where flagged — never a null standing in silently for a real number.
2. Write **`tender/pricing.md`** — provenance (bill/`boq.md` revision priced, rate-library sweep
   date(s), quote-register rows cited, generation date), the section build-up summary, the Step
   4 totals, and the assumptions register. **Only this skill writes these two files** (Pattern
   18).
3. **Overwrite-confirm:** if the files already exist, show their existing provenance and ask
   whether to replace or keep both (a dated second build). **Non-interactive:** state the
   assumption to replace and continue: "Non-interactive run — replaced the prior pricing build;
   prior provenance shown above."
4. **Sensitivity reminder (state every write):** this build-up is competitively sensitive from
   its first line — keep it local, out of shared repositories (`.gitignore`), never circulate it
   to the client or a subcontractor, before or after award (Pattern 18 intro / Pattern 14 rule
   5).

At Step 5, after writing the files above, read
`references/output-template.md` for the exact
report structure (Summary, Section Build-Up Table, Unpriced Items, Low Basis Exposure, Prelims/
OH&P/Risk, Assumptions Register, Files Written, Next Steps, Standing Caveat). Apply Pattern 8
for the `Ref: TP-[NNN]` line.

---

## Hard Rules

1. **Exactly four admissible pricing sources, labelled on every line** — achieved norms (LOW
   BASIS carried through), user-stated rates or quote-register citations, the client's own
   billed rate (labelled theirs, adopted by user election), or UNPRICED. No market or "typical"
   figure, ever (Pattern 18 rule 3).
2. **OH&P, risk allowances, and margins are commercial decisions — user-stated only**, own
   labelled lines, never computed or suggested, not even as a range (Pattern 18 rule 4).
3. **UNPRICED never becomes zero or an invented number** — carried to totals as a named
   exclusion with its billed quantity, every time.
4. **Quantities are as billed — never adjusted silently.** A suspected billing error is a
   flagged query for the estimator, not a corrected number (Pattern 18 rule 1).
5. **No commercial-profile.md rates enter this build-up** — see the Scope note above.
6. Only this skill writes `tender/pricing.json` and `tender/pricing.md`.
7. UK English throughout.

---

## Related Skills

- `$boq-import` — writes the bill this skill prices; absent bill stops Step 1
- `$quote-levelling` — level multiple quotes per package before adopting one into Step
  2(c)'s SUBCONTRACT element
- `$rate-library` — the achieved norms Step 2(a) prices labour hours from, with LOW BASIS
  provenance
- `$estimator` — single-project norms where the portfolio library hasn't swept the
  relevant activity yet
- `$programme-create` — the tender draft whose computed duration Step 3's prelims may cite
- The Bid Advisor agent — settle mode reviews this build-up against the bill and quote
  coverage before submission
