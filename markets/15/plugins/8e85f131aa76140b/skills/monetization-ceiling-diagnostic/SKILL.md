---
name: monetization-ceiling-diagnostic
description: Diagnose a retailer's retail media monetization gaps and revenue levers using supplied answers, published Osmos evidence and explicit scenario assumptions.
---

# Monetization ceiling diagnostic

Use this skill when a retailer wants to understand what may be limiting retail media revenue or which levers to test next.

1. Collect only the retailer's stated vertical, region, channels, inventory, advertiser demand, measurement, operations and first-party-data context. Do not ask for an email or other contact details.
2. Use `assess_retail_media_health` when readiness answers are supplied. Report gaps, not an invented maturity score or peer percentile.
3. Use `lookup_retail_media_benchmarks` for published evidence and preserve its cohort, denominator, geography and period.
4. Use `estimate_rmn_revenue` only when the user supplies explicit stream assumptions. A GMV, traffic or store count alone is not a forecast.
5. Organize the answer as: current evidence, likely constraints, revenue levers, scenario range, dependencies, and next three actions.

All tools are open; show full results without asking for contact details. Never invent a ceiling, benchmark or financial outcome. Only if the user asks to speak with Osmos, offer the optional expert follow-up (work email only) through request_osmos_expert.
