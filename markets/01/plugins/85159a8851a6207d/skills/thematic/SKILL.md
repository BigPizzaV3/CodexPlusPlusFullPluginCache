---
name: thematic
description: >-
  Use this skill to score or rank securities by MSCI thematic relevance, test whether holdings actually express a requested investment theme, or compare thematic exposure across names. Trigger for themes such as cybersecurity, robotics, digital health, fintech, future mobility, genomic innovation, space exploration, smart cities, defense/security, or related MSCI-published themes.
---

# MSCI thematic exposure scoring

Use published MSCI thematic relevance data to test thematic exposure claims at security level.

## Output

State the MSCI theme selected, explain any mapping from the user's wording, rank securities by score, and state the score's meaning and date. Never describe a relevance score as revenue percentage.

## Workflow

1. Search `search_index_datapoints` for the user's theme and inspect the available published thematic fields. Do not rely on a static remembered theme list when the live catalog can confirm availability.
2. If the user's language can map to more than one plausible MSCI theme, choose the closest supported field only when the mapping is defensible and state the choice. If no suitable theme exists, say so rather than silently proxying it.
3. Resolve each company/ticker/ISIN with `search_index_securities`. Resolve independent holdings in parallel when useful.
4. Fetch the selected security-level thematic field with `fetch_index_data`, obeying `constraints.notes` and date availability.
5. If the user asks for portfolio thematic exposure, combine the relevance scores with the user-supplied portfolio weights when available. If weights come from another MSCI index dataset, clearly identify that source and date.

## Presentation

- Rank descending unless the user requests another ordering.
- Identify each security as `<name> (<msci_security_code>)` when showing codes.
- State the selected theme and fetched date.
- Explain that a high relevance score reflects MSCI's thematic framework, not expected return, quality, or a recommendation.

## Guardrails

- Relevance score is not revenue percentage.
- Do not invent unsupported themes.
- Date every score; scores can change or be restated.
- If aggregating to portfolio level, show or describe the weighting method.
