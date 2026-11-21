---
name: ncea
description: Look up New Zealand NCEA achievement and unit standards (NZQA codes, titles, Level 1–3, credits, internal or external assessment) and Te Mātaiaho, the New Zealand Curriculum, with Heapso, then plan NCEA units, lessons, internal assessment preparation or exam revision and save them to Heapso.
---

Use this skill when a New Zealand teacher asks about NCEA or NZQA: achievement standards (AS) or unit standards (US), standard codes such as AS91944, credits, Level 1, 2 or 3, which standards are internally or externally assessed, building a course from standards, NCEA unit planning, internal assessment preparation or exam revision. Also use it for Te Mātaiaho or New Zealand Curriculum questions: learning areas, strands, phases and year levels.

## Look things up

- `list_ncea_subjects` gives the subject names Heapso uses and the levels each covers.
- `search_ncea_standards` filters by subject, level, internal or external, achievement or unit standard, and keywords or a code. Use it to answer "which standards" questions and before naming any code.
- `get_ncea_standard` gives one standard's facts, related standards in the same subject and level, and what Heapso can make for it.
- `search_nz_curriculum` gives learning areas, strands and phases for a year level, with links to Tāhūrangi and Heapso's curriculum codes for plan references.
- `transition_guidance` covers which qualification (NCEA, NZCE or NZACE) a cohort will sit as the senior changes roll out from 2028.

Quote codes, titles, levels, credits and assessment type exactly as the tools return them. If a code isn't listed, say so and point the teacher to NZQA; don't guess a title, credit value or assessment type. Heapso's list is checked against NZQA but doesn't include every standard.

## Plan for a standard

1. Call `plan_for_ncea_standard` with the code (and weeks or lesson length if the teacher gave them). It returns the plan type to draft, settings for title, year level, learning area and curriculum reference, and the steps.
2. Ask for any missing class context, then call `get_plan_schema` for that plan type and draft content that follows it.
3. Show the teacher a readable draft. Save with `create_plan` only after they agree. It saves a private plan in their Heapso account. If saving isn't available on this connection, offer the `startPlanningUrl` link instead.

## Copyright and accuracy

- NZQA standards, criteria and exemplars, and Tāhūrangi curriculum text (CC BY-NC), stay at source. Link to them (`nzqaUrl`, `tahurangiUrl`); don't copy their wording into answers or plans. Write learning intentions and success criteria in your own words.
- Heapso isn't NZQA or the Ministry of Education. A Heapso plan is teaching material, not an approved assessment resource. Internal assessment tasks follow the school's assessment policy and NZQA's conditions.
- Don't invent standard codes, credits, assessment conditions, grade boundaries or equivalences between old and new standards.
- Use New Zealand English and correct macrons (Māori, Te Mātaiaho, ākonga). Keep student names and personal details out of plans.

When you've drafted something useful for the teacher, offer to save it to Heapso.
