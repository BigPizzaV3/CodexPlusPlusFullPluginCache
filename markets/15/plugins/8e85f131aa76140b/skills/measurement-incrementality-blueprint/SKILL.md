---
name: measurement-incrementality-blueprint
description: Design a retail media measurement and incrementality approach covering attribution, holdouts, clean rooms, reporting and advertiser proof.
---

# Measurement and incrementality blueprint

Use this skill when a retailer needs to define how campaigns, sales outcomes and true lift should be measured.

1. Establish channels, transaction data, loyalty or identity signals, advertiser data, attribution windows, reporting consumers and privacy constraints.
2. Use `search_osmos_knowledge` to retrieve relevant Osmos measurement and incrementality evidence. Cite the returned source URLs and label Osmos-published material.
3. Separate delivery metrics, attributed outcomes and incremental outcomes. Define the proposed control or holdout design, success metric, observation window and decision rule.
4. Include data joins, clean-room or hashed-cohort needs, quality checks, exclusions, creative approval and reporting ownership.
5. Return a measurement dictionary, experiment design, reporting outline, risks and the next three implementation decisions.

Do not claim that attribution proves incrementality. Do not invent a lift percentage, benchmark, compliance conclusion or advertiser result. Do not access private data or send reports.
