# Incumbent and market research

Goal: size a market and brief an incumbent or competitor from award evidence.

## Steps

1. Calibrate with `g2x_calibrate_session` so the market matches the user's company and codes.
2. Define the measure. Agree the NAICS or PSC, agency, fiscal years and whether the number is obligations, potential value or ceiling. Never mix them in one total.
3. Count and aggregate on the server. Call `g2x_query` with `{"command": "help"}`, then the source help, then a bounded query, for example `{"command": "awards aggregate --by awarding_agency --naics 541512 --fy 2025"}`. Carry the exact total into your answer. If the answer is saved as a workbook, link it and say what it covers. Do not add up a first page and call it the market. Protests data needs Starter Team and up.
4. Rank the performers. Call `g2x_rank_companies` for the same scope, for example `{"naics": ["541519"], "fiscal_years": [2024, 2025], "limit": 10}`. Each search counts toward the daily Directory searches.
5. Brief the incumbent. Resolve it with `g2x_search_companies`. Read `g2x_company_contract_history` with `expiring_within_days` for the work at risk, `g2x_socioeconomic_status` for certifications and `g2x_get_graph_neighborhood` for public relationships. Keep corporate family members separate.
6. Check the vehicle. Call `g2x_vehicle_usage` for holders on record and obligated task orders. Say the figures are partial and are not the ceiling.
7. Test claims. Use `g2x_company_evidence` for cited past performance. Use `g2x_company_signals` or `g2x_company_web_profile` only when public statements matter; each spends a metered lookup.

## What to tell the user

Lead with the market number, its measure, filters and period. Follow with the ranked table in prose, the incumbent brief, supporting G2X links, and any exclusion that would change the conclusion. Label a sample as a sample. A missing record does not prove no award exists.
