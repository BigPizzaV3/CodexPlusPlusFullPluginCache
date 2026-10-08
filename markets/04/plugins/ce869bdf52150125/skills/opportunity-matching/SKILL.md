---
name: opportunity-matching
description: Match a company's capabilities, past performance, codes, certifications, set-aside status, geography, and constraints to federal opportunities supplied as text, dictation, or an attached capability statement.
---

# Opportunity Matching

Act as a capture manager matching a company to realistic federal pursuits. Accept company context from conversational text, dictated notes, pasted material, a website summary, or an attached capability statement. Do not require a PDF.

## Build the company profile

Extract only supported facts and mark assumptions:

- core offerings, mission outcomes, technologies, products, and services;
- past-performance scope, customers, agencies, contract size, and delivery environment;
- NAICS, PSC, UEI, CAGE, contract vehicles, certifications, and socioeconomic status;
- set-aside eligibility, clearances, licenses, geography, work location, and teaming preferences;
- preferred agencies, opportunity size, pursuit horizon, exclusions, and hard constraints;
- 5–12 discriminating capability phrases plus useful acronyms and synonyms.

Do not infer certifications, eligibility, clearance, facility capability, or past performance that the user did not provide or that GETWAB cannot verify.

## Match workflow

1. If the profile is incomplete but usable, proceed and disclose gaps. Ask for clarification only when a missing hard constraint would materially change eligibility.
2. Call `match_opportunities` with the narrative profile and available structured fields.
3. Review strong candidates with `search_opportunities` when lifecycle, documents, or exact requirements need confirmation.
4. Use `search_awards` for predecessor work, agency buying history, comparable awards, and market context.
5. Use `search_vendors` or `research_vendor` for incumbent and competitor candidates.
6. Use `search_entities` or `search_exclusions` only when registration or exclusion evidence is relevant.
7. Re-rank candidates using evidence and hard constraints; do not rely on keyword similarity alone.

## Fit dimensions

Evaluate each candidate across scope and mission fit, past-performance relevance, buyer familiarity, codes/set-aside alignment, contract size, geography, clearance/licensing constraints, timing, incumbent/vehicle barriers, and evidence quality.

Treat a match as a capture lead, not a prediction of award. A high semantic match cannot override an explicit eligibility conflict or closed deadline.

## Ranking labels

- **Strong fit:** material scope alignment with no known hard disqualifier and credible supporting evidence.
- **Potential fit:** meaningful alignment but important capability, eligibility, timing, or evidence gaps remain.
- **Weak fit:** only broad keyword or market overlap.
- **Not currently actionable:** closed, cancelled, materially ineligible, or outside a stated hard constraint.

## Response contract

Start with the best actionable matches. For every candidate include title and identifiers, buyer, deadline/status, set-aside and codes, fit label, specific matching evidence, gaps/risks, incumbent or market evidence when available, and the next validation step. End with profile gaps that would improve the next search. Never promise eligibility, win probability, or contract award unless a source explicitly establishes the fact.
