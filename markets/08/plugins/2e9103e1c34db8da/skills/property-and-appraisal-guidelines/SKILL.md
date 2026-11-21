---
name: property-and-appraisal-guidelines
description: Look up what Fannie Mae, Freddie Mac, FHA, VA or USDA require for a property type or an appraisal, and return the regulator's exact text with its citation and effective date. Use when a user asks about property or appraisal eligibility, for example manufactured homes, condos and condo project review, co-ops, mixed-use property, leasehold estates, 2-4 unit and investment property, flood insurance, minimum property requirements, appraisal timeliness, liquidation appraisals, appraisal age and updates, or how to complete the new URAR appraisal form (UAD 3.6, URAR Appendix F-1 reference guide).
---

# Property and appraisal guidelines

Answers collateral and appraisal questions with the agency's own words.

## Inputs
- The property type or appraisal topic.
- The agency or loan program, if named (Fannie Mae, Freddie Mac, FHA, VA, USDA).

## Map: where each agency puts the rule (checked 2026-10-12)
Freddie Mac citations are Freddie Mac Guide sections (write "Freddie Mac Guide 5703.1").

| Topic | Fannie Mae | Freddie Mac | FHA 4000.1 | VA M26-7 | USDA |
|---|---|---|---|---|---|
| Manufactured homes | B5-2-02 | 5703.1 "manufactured home" | II.A.1.b "Manufactured" | Ch. 12 Topic 40 "manufactured" | 7 CFR 3555.208 |
| Condominiums | B4-2.1-01 "condo" | 5701.1 "Condominium" | II.C.2.c "Condominium" | Ch. 16 "condominium" | HB-1-3555 12.11 |
| PUDs | B4-2.1-01 "PUD" | 5702.1 "PUD" | | | HB-1-3555 12.11 |
| Mixed-use property | B2-3-04 | 5601.5 "mixed-use" | II.D.12.a "Mixed Use" | | |
| Leasehold estates | B2-3-03 | 5704.1 "leasehold" | | Ch. 10 Topic 9 (k) "leasehold" | |
| Flood insurance | B7-3-06 | 8202.2 "flood" | II.A.1.b.iv "Flood" | Ch. 9 Topic 11 (b) "flood" | 7 CFR 3555.252(b) |
| Appraisal report forms | B4-1.2-01 | 5605.1 "appraisal report" | | Ch. 11 Topic 1 "appraisal" | HB-1-3555 12.5 |
| New URAR form (UAD 3.6) | URAR Appendix F-1 "URAR" | | | | |
| Age or validity of the appraisal | B4-1.2-04 | 5604.3 "days" | II.A.1.a "validity" | Ch. 13 Topic 7 "validity" (Notice of Value) | HB-1-3555 12.5 "days" |
| Minimum property requirements | | | II.D.3.b "Minimum Property" | Ch. 12 Topic 1 "minimum property" | HB-1-3555 12.1 |
| Repairs, completion | B4-1.2-05 "completion" | 5605.8 "completion" | II.D.3.n "Repair" | Ch. 10 Topic 23 "repair" | HB-1-3555 12.28 |

## How to use the map
1. Find the user's topic in the map. For each agency that applies, call `lookup_citation` with the citation in the map, then `find_in_section` with the terms shown in quotes. These are the agency's own words, and they may differ from the user's ("individual deposits" is FHA's term for large deposits).
2. The subsection shown (for example II.A.4.c.v) is where the answer usually sits; cite the subsection the passage actually comes from.
3. A blank cell, a topic not in the map, a `not_found` or an `ambiguous` result: fall back to `search_regs` (step 1 of Steps below). Never treat a blank cell as "the agency has no rule".

## Steps (topic not in the map)
1. Call `search_regs` with the topic in the regulator's vocabulary ("manufactured home", "leasehold estate", "liquidation appraisal"). Set `family` when the agency is known.
2. For the new URAR form and UAD 3.6, search "URAR" or the section name (for example "Sales Comparison Approach", "Condition and Quality Rating"). These documents are long: use `find_in_section` with the user's terms rather than paging the whole document.
3. Read the answering passages with `find_in_section`, or page the whole section with `get_obligation` until `next_offset` is null.
4. For FHA, check `version`: a section HUD's Update 18 revises has two texts. Quote the one that applies; if you don't know whether the user has adopted Update 18, quote the in-force text and state what the revision changes.

## Output
- Quote each relevant passage verbatim, with its `canonical_citation` and a link to `page_url`.
- State any `currency` warning and its dates. The UAD 3.6 / new URAR documents carry a mandatory date and a temporary exception; state both when they matter to the question.
- Summary after the quotes, labeled "Summary". Mention the research-only `notice` once per conversation.

## Do not
- Do not estimate a property's value or decide eligibility for a specific property. Quote the requirements.
- Do not answer from memory; if the corpus doesn't address it, say so.
- Explicit user instructions take priority over this skill.
