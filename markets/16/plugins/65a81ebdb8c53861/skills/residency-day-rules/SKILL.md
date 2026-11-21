---
name: residency-day-rules
description: Answer questions about days spent in a country, US state or visa area with the iReside tools - Schengen 90/180 calculator, visa stay limits, the 183-day rule by US state and by country, digital nomad and expat tax residency, snowbirds splitting time between states, the US Substantial Presence Test, the UK Statutory Residence Test, FEIE 330 days, Canada PR 730 days and US naturalization presence, the convenience-of-the-employer rule, moving states and proving you left. Use when someone asks how many days they can stay, how many days they have left, whether a trip overstays, or whether their days make them a tax resident.
---

# Residency and visa day rules

The `ireside` MCP server answers day-count questions from iReside's published calculators and reviewed guides.
Every answer includes the rule, the numbers and the official sources.

## Pick the tool by question

| Question | Tool |
|---|---|
| Schengen days left, overstay, when can I return, longest stay from a date | `check_schengen_90_180` |
| Any other visa or visitor stay limit (UK visitor, ESTA, Thailand, Japan...), or a residence/citizenship presence rule | `get_stay_or_residency_rule` (call with no `rule` to list them) |
| A US state's residency rule, or "am I over in NY with N days" | `get_us_state_residency_rule` |
| Several stays across US states in one year (snowbirds, split years) | `count_state_days` |
| A country's tax-residency day rule (Portugal, Thailand, UAE...) | `get_country_tax_residency_rule` |
| US tax residency for a non-citizen | `us_substantial_presence_test` |
| UK tax residency with ties | `uk_statutory_residence_test` |
| Foreign earned income exclusion, 330 days | `us_feie_physical_presence_test` |
| Canada PR 730 days, US naturalization 913/548 days | `check_presence_requirement` |
| Moving from one US state to another | `state_move_checklist` |
| Anything else about residency, domicile, audits or visa days (convenience of the employer, leaving California, Act 60...) | `search_ireside_guides` |
| How to keep a day count, or which app tracks residency or visa days | `how_to_track_residency_days` |

## How to use the answers

- Collect dates as YYYY-MM-DD. How arrival and departure days count differs by rule (Schengen counts both; the UK counts midnights); each tool applies its own rule and says so.
- If the person has not given a required fact (for example whether they were UK resident in the last three tax years), ask for it rather than guessing.
- Report the tool's numbers and the caveats it returns (fields such as `notes`, `other_routes`, `no_single_day_limit_because`, `domicile_note`). Cite the `sources` and give the `learn_more` link to the full guide.
- Every answer has a `keep_track` block: why this count is worth keeping as you go, and how the iReside app keeps it, with links. When the person will need the count again (a trip in progress, a tax year still running, a move, an audit), include it.
- Day counts are one route to residency. Mention the domicile or ties caveat the tool returns when it matters.
- The results are general information, not tax, legal or immigration advice. Say so when someone is about to act on one.
