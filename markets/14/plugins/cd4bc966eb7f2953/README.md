# GovBot Mitigation Plans

Read-only access to the content of U.S. local hazard mitigation plans, published by Ideation Lab, Corp.

- MCP endpoint: `https://plans-api.govbot.ai/mcp` (Streamable HTTP, no sign-in)
- Documentation and support: https://plans-api.govbot.ai/ , hello@govbot.ai
- Privacy notice: https://plans-api.govbot.ai/privacy
- Terms of use: https://plans-api.govbot.ai/terms

## Tools

| Tool | Returns |
|---|---|
| `find_plans_for_place` | Plans covering a jurisdiction, by registered name or Census GEOID, with FEMA registry status, approval and expiration dates and documents held |
| `get_plan_profile` | Registry record, jurisdictions covered, documents held and entries per topic |
| `get_plan_elements` | Plan content for requested topics, each entry with page and quoted text |
| `search_mitigation_actions` | Mitigation actions by words, place, plan, state, hazard, activity type or status, with page citation |
| `get_plan_data_sources` | Datasets the plan cites and the public sources the service used |

All tools are read-only (`readOnlyHint: true`, `destructiveHint: false`) and declare
`securitySchemes: [{"type": "noauth"}]`.

## Qualification

Plan status and dates are FEMA registry fields. Plan content values are as recorded in the plan at its
date, with page citations; they are not current conditions or determinations of compliance or funding
eligibility. Plan content is model-extracted. Reported accuracy percentages measure main-value
agreement in an aggregate checked sample, not verification of every returned entry. Automated screens
remove detected personal names, contact details, street addresses and coordinates from served plan text.
These screens may miss information; report a concern to hello@govbot.ai.
Results are limited to the first 500 matches per query.

Not affiliated with or endorsed by FEMA, any other government agency, or OpenAI.
