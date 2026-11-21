# Tools and their inputs

Every tool of the Paragrafiq set with the inputs it accepts. `as_of` is a date `YYYY-MM-DD`; where it is optional it
defaults to today, which is not the date of the facts for a past event: pass the date of the facts. Optional
inputs may be omitted or `null`. How to continue a result that has more parts is in `SKILL.md` ("Long results").

## Acts and provisions
- `find_czech_law_act`: required `query`; optional `as_of`
- `read_czech_law_provision`: required `act`, `provision`; optional `as_of`, `offset`
- `get_czech_law_provision_context`: required `act`, `paragraph`; optional `as_of`
- `search_czech_law_in_act`: required `act`; optional `words`, `preset`, `as_of`, `par_from`, `par_to`
- `get_czech_law_referring_provisions`: required `act`, `provision`; optional `as_of`, `scope`, `offset`
- `get_czech_law_provision_history`: required `act`, `provision`; optional `from`, `to`, `offset`
- `get_czech_law_transitional_provisions`: optional `amending_act`, `target_act`, `act`, `as_of`, `mentions`, `offset`
- `get_czech_law_general_rules`: optional `topic`, `as_of`
- `find_czech_law_definition`: required `term`; optional `act`, `as_of`, `offset`
- `find_czech_law_provisions`: required `terms`; optional `as_of`, `acts`, `max_acts`, `per_act`

## Decisions
- `find_czech_case_law_decision`: required `ref`
- `find_czech_case_law_by_question`: required `query`; optional `terms`, `courts`, `since`, `act`, `provision`, `limit`
- `search_czech_case_law`: required `query`; optional `courts`, `since`, `act`, `provision`, `limit`
- `read_czech_case_law_passages`: required `case_id`, `words`; optional `radius`, `max_hits`
- `get_czech_case_law_treatment`: required `case_id`; optional `since`, `limit`

## Reasons of bills and authority guidance
- `find_czech_explanatory_report`: optional `query`, `act`, `provision`, `as_of`, `limit`, `offset`
- `read_czech_explanatory_report`: required `dz_doc_id`; optional `provision`, `offset`, `outline_offset`
- `find_czech_guidance`: optional `act`, `provision`, `query`, `issuer_id`, `as_of`, `limit`
- `read_czech_guidance`: required `doc_id`; optional `offset`

## Calculation
- `calculate_czech_statutory_interest_and_deadlines`: required `calculation`; optional `principal`, `dueDate`, `paidDate`, `asOfDate`, `startDate`, `months`, `days`, `taxYear`

## Notes on inputs
- `act` accepts the `act_iri` returned by `find_czech_law_act`, the number ("121/2000 Sb.") or a name or abbreviation.
- `provision` is written as cited: "§ 30 odst. 1 písm. b)", "čl. II bod 4", or a node path ("par_30/odst_1").
- For `find_czech_case_law_by_question` and `search_czech_case_law`, `provision` requires `act`.
- For `find_czech_explanatory_report` and `find_czech_guidance`, `provision` requires `act`.
- For `get_czech_law_transitional_provisions` the three modes (`amending_act` with `target_act`; `target_act` alone; `act` alone)
  are described in step 6 of `SKILL.md`; `mentions` is a provision of the target act.
- `read_czech_case_law_passages` and `get_czech_case_law_treatment` take the `case_id` returned by `find_czech_case_law_decision`, `find_czech_case_law_by_question` or
  `search_czech_case_law`.
