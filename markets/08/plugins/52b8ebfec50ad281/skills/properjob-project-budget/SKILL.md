---
name: properjob-project-budget
description: Reconcile construction, supplied fees, fittings, tax and contingency into a transparent overall project budget. Use when someone asks for the all-in cost, total money needed or costs beyond the building estimate.
---

# Build a whole-project budget

## Country and language

Reply in the requested or conversation language. Keep the actual project country,
currency, units and tax basis independent of language; do not infer them from a
translation or a shared currency symbol. Use local currency and the supplied tax basis; distinguish upfront costs from each recurring period. Do not assume UK fee percentages, VAT, grant eligibility or transaction charges abroad.

For international documents, number formats or jurisdiction questions, read the
[country and language rules](../properjob-building-work/references/international-workflows.md),
also available at `skill://proper-job/properjob-building-work/references/international-workflows.md`.

## Workflow


Start from the existing construction result or supplied quote and identify its
currency, tax treatment and included scope. Reuse that price. Read
`properjob-building-work` before requesting a new supported construction price;
this skill does not add fee, tax, finance or land valuation engines.

Prepare a ledger with amount/range, source, cost basis and one inclusion status
per item: additional, already included, alternative, unknown or not applicable.
Consider only relevant design/survey costs, authority/inspection charges,
separate fittings/appliances, external works, service connections, temporary
accommodation, contingency and user-supplied land/lease costs. Possible costs
are not automatically required costs.

- Use calculator-returned construction prices unchanged. Additional amounts or
  percentages must be explicitly supplied by the user or a cited applicable
  quote/source; label their origin. If the user chooses a contingency percentage,
  show the base it applies to and do not add it again if already included.
- Ordinary host arithmetic may sum known compatible amounts and calculate a
  supplied percentage. This is budget bookkeeping, not a new engine estimate.
  Identify construction estimates and actual supplied prices separately.
- Keep currencies separate. Do not infer tax rates, exemptions or eligibility;
  preserve the returned basis. Unknown/mixed tax prevents a claimed tax-inclusive
  total. When current jurisdictional guidance is requested, verify official
  sources and keep unconfirmed applicability explicit.
- Prevent double counting bundled fees, fittings, contractor margin, contingency
  and tax. If scope overlap cannot be resolved, show separate amounts without
  a combined total. Alternative offers are not additive costs.
- Keep recurring rent, finance payments and operating costs separate from upfront
  capital costs. Do not capitalise rent, guess loan terms, deduct an unconfirmed
  grant or count a deposit as an extra on top of a price that includes it.

Show a known subtotal with its basis and list every unresolved requested item
beside it. If any material amount, inclusion or tax basis is missing, explicitly
call the result a partial budget; never treat unknown as zero or call it all-in.
When combining compatible ranges, summed endpoints are a planning envelope, not
a statistically calibrated interval. Ask the question that resolves the largest
remaining gap and leave the ledger useful if the answer is unknown.
