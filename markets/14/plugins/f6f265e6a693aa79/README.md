# GovBot Soils

Prepare source-cited soil-survey briefs, explain USDA NRCS recorded land-use limitations and compare mapped soils across bounded public research areas. Developed by Ideation Lab, Corp.

This portable OpenAI plugin contains exactly three workflow skills and one independent no-auth MCP reference. It is in preparation: not submitted, approved or published. The local runtime reads fixed USDA NRCS Soil Data Access endpoints directly; no existing GovBot connector is an upstream dependency. No credentials or agency data are bundled.

## Three workflows
- soil-survey-brief: map units, components and horizons with survey dates and unknowns.
- land-use-limitations-brief: published NRCS ratings/reasons, distinct from site approval.
- area-soils-comparison: consistent bounded-area mapped shares and source context.

## Limits
Map-unit components are not spatially located at the supplied point. Preserve map scale, mixed components, source/version dates, units, missing/unrated values and conditional farmland wording. This is not a soil boring, percolation test, septic permit, flood/ponding determination, property-safety finding or engineering certification. A missing record does not mean a place is suitable or safe. NRCS publishes a nightly maintenance window; a service error is not a soil finding.

Source: [USDA NRCS Soil Data Access](https://sdmdataaccess.nrcs.usda.gov/) and [Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/). Source-backed operational facts, local checks, hosted checks and actual ChatGPT acceptance are separate evidence layers. No public demo is claimed before the actual recording and review.

Support: hello@govbot.ai. Privacy: https://soils-api.govbot.ai/privacy . Terms: https://soils-api.govbot.ai/terms . Do not send confidential information or private home addresses. Independent; not affiliated with or endorsed by USDA, NRCS, any government agency or OpenAI.

## Local development
Use Node24. Run `npm ci --ignore-scripts`, `npm test`, `npm run validate:package`, `npm run package`. Start `npm start` for localhost MCP. The canonical proposed host is https://soils-api.govbot.ai/mcp; hosted/DNS/registered app and actual ChatGPT testing remain root-owned release gates.
