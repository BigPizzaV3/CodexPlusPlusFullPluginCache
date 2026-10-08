---
name: validate-idea
description: Test an existing business or product idea against Trend Seeker's market evidence. Use when the user has a defined concept and wants evidence, adjacent demand, risks, or validation gaps.
---

# Validate a business idea

Evaluate the user's concept against Trend Seeker data. This is an evidence review, not a prediction that the business will succeed or fail.

## Frame the concept

Extract the target user, problem, proposed solution, geography or industry constraints, and business model when supplied. If a critical detail is missing, state the assumption you use rather than silently filling it in.

## Gather evidence

1. Call `search_business_ideas` with the core user problem. Search by the problem people experience, not only by the proposed product name.
2. If needed, make one narrower search for the target audience or workflow. Deduplicate candidates by business idea ID.
3. Use `get_business_idea` for the closest candidates.
4. Use `get_supporting_evidence` for the strongest two or three candidates. Preserve source URLs and publication dates.

Don't treat a lack of Trend Seeker results as proof that there is no demand. It only means this dataset didn't return matching evidence.

## Assess the idea

Classify the result as one of:

- `supported`: direct evidence matches both the audience and problem.
- `adjacent evidence`: demand exists, but the audience, problem, or solution differs materially.
- `weak evidence`: few or low-confidence matches were returned.

Explain the classification using retrieved facts. Include:

- The closest matching opportunities.
- Evidence for the problem, with dated source links.
- Relevant scores or confidence tiers and their scale.
- Important contradictions or mismatches.
- What the dataset cannot establish.
- Three concrete customer-research or market tests that would reduce the largest uncertainties.

Don't invent a market size, competitor claim, revenue estimate, or numeric probability of success. Clearly label all inference. Use other external research tools only when the user asks for broader research beyond Trend Seeker.
