---
name: estimate-setup-cost
description: Estimate what a UAE company setup costs with Dubai Setup Index — itemised IFZA formation and five-year costs, official Dubai mainland licence estimates, and published free-zone package prices — keeping every unknown cost explicit. Use when the user asks how much a Dubai or UAE company, licence or visa setup costs.
---

# Estimate a UAE setup cost

Explicit user instructions take priority over this workflow.

1. **IFZA:** `estimate_ifza_setup` with the visas (title, and whether the person
   is already in the UAE) and licence term; `estimate_ifza_five_year` for the
   longer view.
2. **Dubai mainland:** `get_mainland`, then `estimate_mainland_licence` with
   the exact DET activity code, one or two owners and the annual rent. Six
   activities were sampled in the official simulator. Other listed DET codes
   use its fee rule; preserve `derived-from-simulator-rule`, `availabilityNote`
   and `rentNote` whenever returned. Do not call a derived estimate a directly
   observed official quote.
3. **Any other free zone:** `get_free_zone` and its published packages. No
   estimator covers it; say so.

Rules:

- Report `pricedSubtotalAed` with its unresolved lines and exclusions beside
  it. `selectedTotalAed` is null when anything is unknown, and full totals are
  always null — never add one up yourself.
- The mainland figure is licence fees only. The rent assessment is not the
  rent; rent, visas, approvals and renewal are separate.
- If an estimator refuses a scenario, report the refusal. Do not extrapolate.
- These are dated reference figures, not quotes. Give the date and cite the page.

Use `list_free_zones` with an explicit `term_months` and `visa_count` for sorted
package references. `include_unpriced` explains published but excluded offers.
Use `compare_setup_scenarios` after selecting an exact activity to keep founder
assumptions consistent. `completeSetupTotalAed: null` is unknown, not zero.
An overdue review is not an expired offer; known expired offers cannot win the
comparison. A current headline does not replace a dated calculator result.
