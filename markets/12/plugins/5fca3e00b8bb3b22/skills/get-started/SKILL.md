---
name: get-started
description: Exact wet-lab calculations and lab paperwork. Use when a scientist asks how much to weigh for a molarity, how much stock to dilute (C1V1), how to set up a serial dilution, a PCR or qPCR master mix, an LNP formulation or a 6- to 384-well plate layout; needs a lab document template (SOP, protocol, lab notebook entry, freezer or chemical inventory, deviation log, risk assessment, calibration log); wants reagent label text as a materials table; or asks how to write SOPs, keep lab notebooks, track inventory or meet data-integrity rules.
---

# Verbex Lab Tools

Exact answers for wet-lab bench work: the numbers to weigh and pipette, plate layouts, and lab documentation.

## Which tool answers which question

| The scientist asks | Call |
| --- | --- |
| How much do I weigh for X mM in Y mL? / How much stock for a dilution? | `solution_prep` |
| Plan a serial dilution (factor, tubes, volume) | `serial_dilution` |
| PCR or qPCR master mix for N reactions | `pcr_master_mix` |
| LNP formulation from RNA mass, N/P and lipid mol% | `lnp_formulation` |
| Lay out a 6- to 384-well plate | `plate_map` |
| Write a protocol / a lab notebook entry | `protocol_template` / `eln_template` |
| Turn reagent label text into a materials table | `parse_reagent_label` |
| A lab document template, or "how should I…" about SOPs, notebooks, inventory, data integrity | `search`, then `fetch` the best result |

Call the calculator directly for any number the scientist will act on; do not calculate it yourself and do not search first.

## How to answer

- Lead with the number to use (mass, volume, wells), exactly as returned, with units and the same significant figures.
- Show the self-check, warnings and safety notes. Call the result "checked", not "validated".
- Ask for a missing input (molecular weight, stock concentration, units) instead of guessing it.
- For a template, describe what it contains and give the link to the editable Word or Excel file from `fetch`.
- Cite the url of any guide or template you use.
- Results are calculation and documentation aids; the scientist checks them against their own lab's requirements.
