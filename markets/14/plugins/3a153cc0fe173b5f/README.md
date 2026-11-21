# GovBot Environmental Site Context

Portable OpenAI plugin display name **GovBot Environmental Context**, version1.0.0. Prepare source-linked wetland, FWS habitat and EPA facility-record briefs for a public research point.

This independent repository reads public agency endpoints directly. It does not call or change any published GovBot/Claude service. Source-client/tool groundwork is adapted under MIT from the read-only GovBot Environmental Site Context reference; the OpenAI gateway/package pattern is adapted from the approved Tides implementation into this separate source tree.

## Three skills
- `wetland-records-brief`: mapped NWI record context with imagery provenance and map limits.
- `habitat-records-brief`: distinguish FWS final/proposed records, citations and unknown fields.
- `environmental-site-context-brief`: retain independent NWI/FWS/EPA scopes, record dates and unavailable sections; explain one exact EPA Registry ID when requested.

## Source and use limits
NWI is not a field delineation or jurisdictional determination. FWS map data exclude NOAA Fisheries habitat and do not replace Federal Register legal descriptions. EPA ECHO records are not contamination findings or independent final compliance determinations. Search results are not PhaseI/II assessments, permits, legal clearances or safety certificates. Missing/empty/unavailable are distinct and never establish absence or safety. Only public research points and public12digitRegistryIDs are needed; no homeaddress, files, login or payment.

## Local commands
`npm ci --ignore-scripts`; `npm test`; `npm run validate:package`; `npm run package`; `npm run probe:sources` (read-only live agency calls); `npm run probe:local` (temporarylocalhost SDK).

Proposed no-auth MCP: `https://environment-api.govbot.ai/mcp`. Website guide: `https://govbot.ai/plugins/environmental-site-context.html`. These are planned endpoints, not a deployment claim. `docs/REGISTRATION.json` is explicitly UNREGISTERED. Root owns hosting, registration/private import, actual ChatGPT tests/video, website publication and final materials preview. No submission is authorized.

The portable archive contains only plugin metadata, MCP URL, these3skills, README, MIT license and a reusable GovBot logo. It contains no runtime code, credentials, agency records or cloud configuration. Actual privateChatGPT app adapter will be a separate root-owned artifact after registration.

Questions: hello@govbot.ai. Independent product of Ideation Lab, Corp.; not an official government or OpenAI product.
