---
name: prospecting
description: Find companies that match a target profile (region, industry, size, founding year, financials, website or email present) or companies similar to a reference company. Use for lead lists, supplier search, market screening, "find companies like X", "Firmen finden", "Zulieferer suchen", "Leads", "ähnliche Firmen".
---

Use this skill when the user wants a list of companies rather than information about one company.

## Workflow

1. Translate the request into `discover_companies` filters. Common filters: `countries` (ISO codes), `cities`, `postal_codes`, `industry_codes`, `statuses`, `legal_forms`, `company_size_min` / `company_size_max`, `founded_after` / `founded_before`, `revenue_min` / `revenue_max`, `has_website`, `has_email`. Use `query` for a free-text keyword such as a product.
   - For federal states or cantons, use `regions` when the recorded address data supports the requested region. Region data may be incomplete; disclose that limitation. Postal prefixes and a selection of cities are not equivalent to administrative boundaries: never silently substitute them or present their results as complete regional coverage. If reliable region filtering is unavailable, ask whether the user wants a specific city/postal area or an explicitly approximate search. Use `postal_codes` with a trailing `*` only for a requested or agreed postal-prefix search.
   - Industries: prefer NACE codes as used in the country's register, for example `C28` (machinery) for Austria.
2. If the target is unclear (no region or no industry), ask one short clarifying question before searching.
3. For "companies like X", resolve X with `search_company` and pass its uuid as `similar_to_uuid`; filters then narrow the similar companies.
4. Present the results as a table with name, city, legal form and status, and state the total number of matches for the applied filters. For an approximate search, name the actual city/postal scope and explain that the count is not the total for the requested region. If the response lists `ignored_filters`, tell the user which filter could not be applied and suggest an alternative instead of presenting the list as filtered. Offer to show the next page (`offset`) or to refine the filters.
5. Results with `ranking: "ai_similarity"` are AI-ranked: label them "(AI ranking)".
6. For details on a single company, continue with the company-profile workflow.

## Boundaries

- Keep pages small (default 25) and only fetch more when the user asks.
- If a region or country is not included in the user's plan, say so plainly without promoting upgrades.
- Answer in the user's language. Explicit user instructions take priority over this skill.
