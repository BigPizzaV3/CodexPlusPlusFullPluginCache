---
name: compare-opportunities
description: Compare two to five business opportunities using Trend Seeker data and supporting evidence. Use when the user is choosing between ideas, niches, or opportunity IDs.
---

# Compare business opportunities

Compare two to five opportunities on a consistent evidence basis.

## Resolve the candidates

- If the user supplies Trend Seeker business idea IDs, use them directly.
- If the user supplies names or descriptions, use `search_business_ideas` to resolve each one. When a description maps to multiple materially different candidates, show the ambiguity before choosing.
- Don't substitute a merely similar idea without telling the user.

## Retrieve comparable data

1. Call `compare_business_ideas` with the resolved IDs.
2. Call `get_supporting_evidence` for each candidate.
3. Compare only fields available across the candidates. Mark missing data instead of treating it as zero.

Use these dimensions when supported by the returned data:

- Target audience and problem specificity.
- Evidence strength and number of supporting posts.
- Validation score and confidence tier.
- Evidence recency.
- Why-now rationale.
- Solution clarity and unresolved assumptions.

## Report

Start with a compact comparison table. Follow it with the strongest case for each option, the main risk for each option, and a recommendation tied to the user's stated priorities. Include dated source links for the evidence that drives the recommendation.

Treat Trend Seeker scores as research signals, not forecasts. Don't create a composite score or weighting unless the user requests one. Clearly separate retrieved facts from inference, and never invent missing metrics or evidence. Use other external research tools only when the user asks for broader research beyond Trend Seeker.
