# GovBot County Hazard Intelligence

An independent, read-only county information plugin from Ideation Lab, Corp. Three skills organize existing GovBot records into sourced county hazard profiles, NFIP/CRS and resilience context, and mitigation-planning overviews.

GovBot resolves place names to Census county GEOIDs, matches FEMA plan-registry records, and combines checked, dated source holdings with live public-data reads and per-source provenance. FEMA, Census, NWS and OpenFEMA public data are used subject to their source terms. Access requires no sign-in. GovBot is not affiliated with or endorsed by FEMA, any government agency or OpenAI.

The configured MCP endpoint is `https://county.govbot.ai/mcp`. Deployment evidence and remaining client checks are recorded in the source checkout handoff; this package makes no claim of directory approval.

The gateway exposes exactly five tools:

| Tool | Purpose |
| --- | --- |
| `resolve_place` | Return Census place/county identity candidates and plan registry matches. |
| `get_county_brief` | Retrieve separate identity, planning, NFIP, study, resilience and disaster groups. |
| `get_nfip_community_status` | Read county-linked or exact-CID community participation and CRS records. |
| `get_county_resilience_profile` | Read county CRCI indicators with source/vintage qualifications. |
| `list_county_flood_studies` | Page through held study/stream metadata for a county. |

Locations must be resolved before selecting county records. The skills preserve source, supplied URLs, retrieval date, vintage, geographic grain, pagination, missingness and source-specific limitations. NFIP participation does not establish individual coverage; CRS class does not establish insurance eligibility. Planning and historical evidence cannot establish present safety. Study holdings do not establish regulatory status or complete FEMA coverage. This plugin does not calculate premiums or make property-level flood determinations.

## Local development

Use Node.js 24 or later and Python 3. From a source checkout:

```sh
npm ci
npm test
node scripts/validate-package.mjs
python3 scripts/build-package.py
```

Tests use synthetic fixtures unless explicitly labelled otherwise. The deployed upstream tool-list snapshot is read-only contract evidence. Neither fixture tests nor a public upstream probe establish an IAM-private deployment or ChatGPT client acceptance.

The runtime starts with `npm start` after the required environment is configured. It fails closed without a reviewed upstream endpoint/audience and exact allowed hosts. The public gateway sends short-lived Google ID tokens to its configured internal source route using a dedicated identity; the observed source frontend is restricted by ingress, while downstream private services retain IAM protections. No inbound caller credential is forwarded to the backend. Local tests inject an upstream function and need no cloud credentials.

The portable plugin consists of root `plugin.json`, `mcp.json`, `skills/` and `assets/`. The reproducible build writes `dist/govbot-county-hazard-intelligence.zip`, its SHA-256 checksum and a file manifest. It contains no server credentials. The ZIP uses the county-specific remote endpoint; it does not contain cloud runtime code or credentials.

## Review and release

In the source checkout, read `docs/HANDOFF.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/ARCHITECTURE.md`, `docs/TEST_RESULTS.md`, `docs/DEPLOYMENT.md` and `docs/OPENAI_SUBMISSION.md`. `submission/` contains eight reviewer scenarios and the walkthrough/checklist. Product documentation, support, privacy and terms are served by the county gateway. The deploying session must verify their public reachability and align operational retention with the published policy.

The Claude deployment session owns the separate `govbot-county-hazards` service. Code and package work in this checkout does not authorize cloud changes or public submission. Domain verification, public hosted checks, real-client reviewer cases and owner-approved listing/demo material remain distinct release checks. Existing GovBot services, datasets and pending submissions are protected.

Product and support: [GovBot County Hazards](https://county.govbot.ai/), hello@govbot.ai. [Privacy](https://county.govbot.ai/privacy) · [Terms](https://county.govbot.ai/terms).
