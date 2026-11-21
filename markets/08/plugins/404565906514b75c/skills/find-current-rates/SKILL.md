---
name: find-current-rates
description: Discover current public BrinkerAdvisor fixed-income records with search, then fetch a selected record by exact ID for freshness and provenance.
---

# Find current rates

Use this workflow when the user wants current BrinkerAdvisor records for a product, institution, term, or maturity.

1. Call `search` for every find, search, list, browse, lookup, or discovery request when no exact stable record ID is already known. Do not broaden a precise request without saying so.
2. Present the matching titles and canonical BrinkerAdvisor row links. Keep the returned stable IDs available for follow-up.
3. Call `fetch` only with an exact stable ID returned by `search` or supplied from a prior result, and only when the user wants that selected record's complete freshness and provenance.
4. Cite the canonical BrinkerAdvisor URL and distinguish it from the original provider or government source URL.

State the as-of date and yield convention. Never infer availability, insurance, tax treatment, suitability, or a transaction from a published rate.
