---
name: servicing-and-default-reporting
description: Look up mortgage servicing, default and loss-mitigation requirements from the Fannie Mae Servicing Guide, FHA Handbook 4000.1 Part III, VA, USDA and Ginnie Mae, and return the regulator's exact text with its citation and effective date. Use when a user asks about servicing obligations, for example HUD SFDMS default reporting and status codes, FHA default and foreclosure reporting deadlines, loss mitigation, partial claims, loan modifications, forbearance, delinquency and collection, escrow, investor reporting and remittance, bailee letters and document custody, or servicing transfers.
---

# Servicing and default reporting

Answers servicing and default questions with the regulator's own words.

## Inputs
- The servicing task or requirement the user asked about.
- The investor or insurer, if named (Fannie Mae, Freddie Mac, FHA, VA, USDA, Ginnie Mae).

## Map: where each agency puts the rule (checked 2026-10-12)
Freddie Mac citations are Freddie Mac Guide sections (write "Freddie Mac Guide 9203.3"). VA servicing is the M26-4 Servicer Handbook and 38 U.S.C. / 38 CFR.

| Topic | Fannie Mae | Freddie Mac | FHA 4000.1 | VA | USDA HB-1-3555 |
|---|---|---|---|---|---|
| Default and delinquency reporting (SFDMS) | F-1-21 "delinquent" | | III.A.4.a "SFDMS" | | |
| Loss mitigation | D2-3.1-01 "workout" | 9201.2 "evaluation hierarchy" | III.A.2.i "Loss Mitigation" | M26-4 Ch. 5 "loss mitigation" | 18.5 "loss mitigation" |
| Partial claim | | | III.A.2.i "Partial Claim"; claim filing IV.A.2.k | 38 U.S.C. 3737 "partial claim" | |
| Forbearance | D2-3.2-01 | 9203.3 "forbearance" | III.A.2.i "Forbearance" | | 18.5 "forbearance" |
| Foreclosure time frames | E-3.2-15 | 9301.11 "timeline" | III.A.2.o "foreclosure" | | 18.11 "foreclosure" |
| Credit bureau reporting | C-4.1-01 | 8106.1 "credit" | | | |
| Bailee letters | C1-2-05 | | | | |
| Servicing transfers | A2-7-01 | 7101.1 "transfer" | III.A.1.b "Transfer" | | |
| Escrow | B-1-01 | 8201.1 "Escrow" | III.A.1.g "Escrow" | | |
| Property preservation | | 8601.6 "preserv" | III.A.2.r "Preservation" | | 18.7 |

## How to use the map
1. Find the user's topic in the map. For each agency that applies, call `lookup_citation` with the citation in the map, then `find_in_section` with the terms shown in quotes. These are the agency's own words, and they may differ from the user's ("individual deposits" is FHA's term for large deposits).
2. The subsection shown (for example II.A.4.c.v) is where the answer usually sits; cite the subsection the passage actually comes from.
3. A blank cell, a topic not in the map, a `not_found` or an `ambiguous` result: fall back to `search_regs` (step 1 of Steps below). Never treat a blank cell as "the agency has no rule".

## Steps (topic not in the map)
1. Call `search_regs` with the topic in the regulator's vocabulary ("Single Family Default Monitoring System", "partial claim", "loss mitigation"). Set `family` when known (hud for FHA, fnma, fhlmc, va, usda, gnma).
2. When the user asks about a specific code or deadline (for example "Status Code 42" or "DDS Code 68"), use `find_in_section` on the matching section with that code as a term.
3. Read the answering passages, or page the whole section with `get_obligation` until `next_offset` is null.
4. Servicing sections are often changed by Mortgagee Letters. If `currency` is superseded-in-part, quote the Mortgagee Letter for the replaced provisions and this text for the rest.

## Output
- Quote each relevant passage verbatim with its `canonical_citation` and a link to `page_url`.
- State any `currency` warning and its dates.
- Summary after the quotes, labeled "Summary". Mention the research-only `notice` once per conversation.

## Do not
- Do not tell the user which code to report for a specific loan. Quote the rule that defines each code.
- Do not answer from memory; if the corpus doesn't address it, say so.
- Explicit user instructions take priority over this skill.
