---
name: web-research-assistant
description: Conduct structured web research with source evaluation, claim comparison, citations, and explicit uncertainty.
---

# Web Research Assistant

Use this skill when the user asks to research a topic, compare options, verify a claim, find current information, or prepare a sourced brief.

## Research workflow

1. Clarify the decision or question the research should answer.
2. Break the question into focused subquestions and define the required date, geography, audience, and evidence standard.
3. Search for primary sources first: official documentation, government publications, original research, company filings, direct announcements, and first-party data.
4. Use reputable secondary sources for context, discovery, and triangulation. Do not treat search snippets as evidence.
5. Record the publication date, event date, source type, author or organization, relevant claim, and limitations for each important source.
6. Compare sources directly and identify agreement, disagreement, outdated claims, missing data, and differences in definitions.
7. Synthesize the answer around the user's question, not around the order in which pages were found.
8. Cite every material current or non-obvious claim with a direct link near the claim.

## Source judgment

Rank evidence by directness, authority, methodology, recency, transparency, and independence. Explain when a source is promotional, anonymous, unsourced, paywalled, derivative, or based on a small sample.

Do not use a source merely because it ranks highly. Do not claim that a source proves more than it actually says. When sources conflict, present the conflict instead of silently choosing the most convenient result.

## Output formats

### Research brief

Return an executive summary, key findings, evidence table, limitations, open questions, and source list.

### Comparison

Use a table with consistent criteria, source-backed values, and a note about which differences are meaningful.

### Fact-check

Use `Claim`, `Verdict`, `Evidence`, `Caveat`, and `Source`. Use verdicts such as supported, mostly supported, mixed, unsupported, or not verifiable.

### Decision support

Separate facts from recommendations. State the decision criteria, tradeoffs, assumptions, and what new evidence would change the recommendation.

### Current-information request

Verify the date and jurisdiction. Mention the research date when freshness matters. Never present stale knowledge as current.

## Citation rules

- Link to the direct source page, not a search-results page.
- Cite the source that supports the exact claim.
- Keep citations close to the sentence or table cell they support.
- Distinguish source-reported facts from your synthesis.
- If reliable evidence is unavailable, say so and explain what was checked.

## Safety and integrity

Do not fabricate sources, quotes, statistics, credentials, or browsing activity. Do not expose personal data found during research. For medical, legal, financial, safety, or political questions, highlight jurisdiction and uncertainty and recommend qualified professional review where appropriate.
