---
name: aviation-use-cases
description: Find and evidence AI use cases for an aviation organisation or role with the Airside Labs Aviation Tools, including the data each needs and the EASA AI-level screen, without overstating what the catalogue shows.
---

# Aviation AI use cases: landscape, search, fetch, screen

Use this workflow when someone asks what AI could do for an airline, airport, ANSP, MRO,
regulator or a role inside one, what data it would need, or how a use case sits against
EASA's AI framework.

## Steps

1. **Start with the landscape.** Call `use_case_landscape` first, grouped by `org_type`, then
   narrow with `org_type` and `group_by=role` or `sector`. This tells you what the catalogue
   covers and the exact spellings the filters accept. Counts describe the catalogue, not the
   industry; never present a count as market evidence.
2. **Search with operational nouns.** `search_use_cases` works best on the things people do and
   the systems they touch (turnaround, stand allocation, NOTAM triage, engine health), not on
   abstractions. Take the top handful, not the whole list.
3. **Fetch the few records the argument needs** with `get_use_case`. Each record carries the
   role, the organisation type, every data requirement with its update cadence, the EASA screen
   where assessed, and nearest neighbours. Three well-chosen records beat thirty summaries.
4. **Go sideways when asked for alternatives:** `similar_use_cases` for the neighbours of one
   record; `data_requirements` for a role's or organisation type's aggregate data profile;
   `trace_data_lineage` to say where a data requirement's knowledge comes from.
5. **Screen with the framework, page-cited.** `easa_ai_framework` returns the AI-level, hazard
   class and technique-ceiling tables from the public EASA document with page references. The
   level and hazard on a use case are a title-level screen with a confidence, not a certification
   finding; say so.
6. **File what you could not find.** If the user needed something the catalogue lacks, call
   `report_unmet_need` once with what was asked and what came back. If they have a correction or
   an addition, `submit_suggestion`. Both are read by a person; `feedback_status` says what
   happened later.

## Output requirements

- Name the organisation type and role the answer is scoped to.
- For each use case cited, give its ID, the data it needs with cadence, and the EASA screen if
  present, with the confidence stated.
- Separate what the catalogue records from what you infer.
- Carry the provenance note: the catalogue is Airside Labs' proprietary corpus for use inside
  the user's analysis, not for redistribution as a dataset; the EASA tables are public text that
  may be quoted with their page reference.

## Do not

- Quote landscape counts as adoption rates or market size.
- Describe a use case as certified, approved or compliant on the strength of the screen.
- Fetch dozens of full records when the question needs three.
