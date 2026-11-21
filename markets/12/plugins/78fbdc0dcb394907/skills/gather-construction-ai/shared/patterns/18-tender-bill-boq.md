# Pattern 18: Tender Bill (BoQ), Quotes, and the Pricing Build-Up

Tendering runs on three artefacts the Gather API knows nothing about: the bill of quantities
being priced, the subcontractor quotes received, and the pricing build-up itself. All three
live as local files under `tender/` — competitively sensitive from the first line (gitignored
in this repo; never circulated, before or after award).

**File conventions:**
- **`tender/boq.json`** (row-level: item ref, description, unit, quantity, section path, and
  the client's rate/amount columns where the bill carries them) plus **`tender/boq.md`**
  (provenance: source file, column semantics as user-confirmed, totals cross-check, section
  summary). Written ONLY by `$boq-import`. Bills run to thousands of items — the JSON
  sidecar is the store; the md is for humans.
- **`tender/quote-register.md`** — one row per subcontractor quote received: package, subbie,
  date, total, scope basis, exclusions as stated. Maintained by the user;
  `$quote-levelling` reads it and may APPEND clearly-marked suggested rows, never edit.
- **`tender/pricing.json` + `tender/pricing.md`** — the build-up, written ONLY by
  `$tender-pricing`: per bill item, the labour/plant/material/subcontract elements,
  each with its source label.

**Rules for consuming skills:**
1. **Quantities are as billed — never adjusted silently.** A suspected billing error is a
   flagged query for the estimator, not a corrected number.
2. **Column semantics are user-confirmed at import** (the Pattern 16 discipline — rate vs
   amount vs rate-less bills, never guessed).
3. **Exactly four admissible pricing sources, labelled on every line:** achieved norms
   (`estimating/rate-library.md`, LOW BASIS flags carried through), user-supplied rates or
   quotes (cited to the quote-register row), the client's own billed rates (labelled as
   theirs), or **UNPRICED — flagged**. No market rates, no "typical" anything, ever.
4. **OH&P, risk allowances, and margins are commercial decisions** — user-stated, presented
   as their own labelled lines, never computed or suggested by a skill.
5. Quote comparisons state each quote's scope verdict per bill section (INCLUDED / EXCLUDED /
   QUALIFIED / SILENT) — SILENT is a finding, not an assumption of inclusion.
6. No win/lose predictions, no competitor speculation — the plugin prices and evidences; the
   bid decision is the business's.
