---
name: roof-storm-risk
description: >-
  Review hurricane history, hail exposure, wind risk, FEMA flood zones, evacuation
  zones, and sinkhole proximity by property address using GetRoofReport's storm-risk
  records. Use for "What is this home's hurricane and hail exposure?" or "Check
  the FEMA flood zone for this address." Address records currently cover Florida.
  Historical exposure does not establish current roof damage or provide a live
  weather alert.
---

# Storm and flood records

Call `get_risk_profile` with a supplied property locator. Use
`search_addresses` to disambiguate an address when needed and reuse the
selected permalink. Current property records cover Florida.

Summarize the available risk fields and link to `reportUrl`. Distinguish
historical exposure, flood-zone designations, and design wind speed from
observed current damage. Report missing values as unavailable.

These records do not diagnose roof damage, provide a current weather forecast,
or determine current evacuation instructions. Do not infer an active warning
or an insurance outcome from historical exposure.
