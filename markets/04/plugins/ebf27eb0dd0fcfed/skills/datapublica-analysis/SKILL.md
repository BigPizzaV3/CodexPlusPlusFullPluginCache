---
name: datapublica-analysis
description: Discover and analyze current Danish companies, people, ownership, filings, financials, capital, investments, Gazelle data, geography, classifications, and risk data with Datapublica. Use semantic discovery or known-company similarity for company sourcing, direct tools for entities, and validated read-only SQL for multi-company analysis. Do not use for non-Danish entities, general news, market prices, legal advice, or unsupported predictions.
---

# Datapublica Analysis

Use Datapublica as the structured source for Danish business-register and Datapublica-derived data. Attribute data used in produced content with `Source: datapublica.dk`.

## Choose the path

- For one identified company, person, or unresolved participant, use the matching direct tool.
- If the stable identifier is unknown, call `search_companies`, `search_people`, or `search_participants` first. Never pass a display name where a stable identifier is required.
- Use `find_similar_companies` when one to five seed CVR numbers are known. Use `search_companies_semantically` to discover companies by company type, activities, products, services, or customer types.
- Keep geography, financials, size, and status out of free-text semantic queries. Request a sufficiently large candidate pool and filter its returned fields afterward. State that post-filtering cannot recover companies outside the candidate pool and that semantic rank is not an exhaustive market result.
- Prefer the specialized timeline, portfolio, capital-event, investment-feed, and Gazelle tools when they directly answer the question.
- Use custom SQL when the question spans multiple entities, needs filters or custom columns, or asks for rankings, comparisons, aggregations, or trends. Do not replace one analytical SQL query with repeated entity lookups.

## Run advanced SQL analysis

1. Call `get_sql_contract` and retain its exact `schemaVersion`.
2. When delivery is modular, call `get_sql_contract_module` for every required module and its declared dependencies. Available domains include company registry, people and ownership, financials and filings, risk and signals, classifications and geography, and capital and investments.
3. Author read-only SQL from the active contract. Use `translate_to_sql` only when the question cannot be converted confidently; it consumes natural-language credits and does not execute SQL.
4. Call `validate_sql` after authoring or changing SQL.
5. Call `execute_sql` with the validated SQL, exact schema version, and bounded `maxRows`. Reuse an idempotency key only when retrying the same logical request.

SQL may scan the full active dataset available to the user's plan even though the returned rows are bounded. Preserve currencies and financial reporting scopes; do not compare entity and consolidated-group statements as if they were the same population.

## Interpret results

- Never infer fields absent from tool output.
- Keep official Børsen Gazelle awards separate from Datapublica-computed screening results.
- Treat financial-distress signals as decision aids, not credit decisions or predictions.
- Disclose truncation, partial investor attribution, suppression reasons, and other material limitations.
- Treat a successful empty result as valid. If a tool returns `needs_clarification`, ask the user for the missing detail.
- Reload the contract after `schema_changed`; do not retry blindly after plan or quota errors.

## Representative requests

- Find SaaS companies, retrieve 200 semantic candidates, then keep companies in Copenhagen and preserve semantic rank.
- Find companies similar to CVR 34456348 based primarily on products and services.
- Find active software companies in Copenhagen and rank by latest entity-scope revenue growth.
- Show 50 Danish companies with highest latest revenue, keeping currencies and entity/group statements separate.
- Which people currently hold roles in more than five Danish companies?
- Compare company count and financial performance by industry and region.
- List recent priced investment rounds in DKK with implied investment and post-money valuation.
- Compare official Gazelle winners with Datapublica-computed candidates by industry.
- Which investors appear most often across priced capital events? Disclose attribution limitations.
- Find companies with declining revenue and elevated financial-distress signals without treating the scores as credit decisions.
