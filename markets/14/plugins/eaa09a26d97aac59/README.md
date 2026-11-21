# GovBot Disaster History

Historical public-record research using NOAA NCEI Storm Events and FEMA OpenFEMA. Six anonymous read-only tools support three workflows: disaster history briefs, recovery project records and county redacted flood claim summaries. Publisher links, dates, record grain, missingness and page boundaries remain visible.

Product guide: https://govbot.ai/plugins/disaster-history.html.

The OpenAI endpoint is `https://disasters-api.govbot.ai/mcp`. This independent implementation calls public FEMA APIs directly and reads its own hash-checked NOAA snapshot. It does not call a Claude connector or the shared GovBot gateway.

| Tool | Source and scope |
| --- | --- |
| `search_flood_events` | NOAA NCEI flood-related event records, held 1996–2025 snapshot; search, whole-query totals and paged examples |
| `get_flood_event` | One held NOAA record, event/episode narratives and publisher event link |
| `list_disaster_declarations` | FEMA Disaster Declarations Summaries v2, one designated-area record per declaration area |
| `list_public_assistance_projects` | FEMA Public Assistance Funded Projects Details v2, project records for a disaster |
| `list_nfip_flood_claims` | FEMA NFIP Claims v3, redacted claim records for a county and loss-year range |
| `list_hazard_mitigation_subapplications` | FEMA HMA Subapplications v2, state/program/fiscal-year records |

## Local use

Node 24 or later. Run `npm ci --ignore-scripts`, `npm test`, and `npm run verify:snapshot`. `npm start` binds to `127.0.0.1:8080`; configure `PORT` to use another port. No sign-in, API key or Google credential is required. `npm run verify:sources` makes six read-only examples, including four direct FEMA queries, and saves evidence under docs/evidence. It is not an offline test.

`GOVBOT_ALLOWED_HOSTS` is an exact comma-separated Host allowlist; production uses `disasters-api.govbot.ai`. `GOVBOT_ALLOWED_ORIGINS` defaults to `https://chatgpt.com,https://chat.openai.com`; absent Origin is accepted, other Origins rejected. `OPENAI_APPS_CHALLENGE` serves an exact portal-provided token on the new host; when unset, that route returns 404. `GOVBOT_TRUSTED_LB_IP` is optional and must only be set behind the new, restricted Google load balancer.

## Skills

- `disaster-record-brief`: county/state flood history with source narratives and declarations.
- `disaster-recovery-records`: declaration and recovery project research with distinct monetary/status fields.
- `county-flood-claim-records`: redacted claim-record examples with page, code and missing-value qualifications.

Record research uses the operations exposed by this plugin. No geocoding or street address is required. For an uncertain county code, the workflow asks for confirmation or uses a reliable official county-code source available in the environment; it never invents an identifier.

## Qualifications and privacy

These are historical records, not warnings or forecasts. NOAA event records, FEMA designated declaration areas, projects, subapplications and claims are different units of observation. A source may be unavailable or return no matches; neither establishes no event or loss. Storm damage estimates, project amounts, obligations, payments, insurance coverage and requested funding measure different things and are not interchangeable. Snapshot dates differ from retrieval dates. NOAA county filters select county-coded records only and exclude forecast-zone records, including historical zone-coded Flood records; there is no county/zone crosswalk. Damage subtotals preserve missing/unparsed counts and remain null when no reported estimate can be derived. FEMA pages can change between requests and the service offset ceiling is explicit; Public Assistance tie ordering is not established. The service provides no property, flood-zone, insurance, eligibility, safety, legal or engineering determination and does not reidentify redacted policyholders.

Tool arguments go only to this independent service and, for FEMA queries, the public FEMA API. NOAA lookups stay within the service's snapshot. The application has no persistent request/result store and does not log tool arguments or returned records. Successful public FEMA responses may be reused in bounded process memory for five minutes; their retrieval time is preserved. This service project currently retains ordinary request logs for 30 days and required administrative/system/access-transparency audit logs for 400 days. Those periods do not cover all provider/client logs or the separately hosted govbot.ai website. See https://disasters-api.govbot.ai/privacy for this service notice; ChatGPT/Codex handling follows the client's own policy. GovBot is not an official product of or endorsed by any government agency or OpenAI. Support: hello@govbot.ai.

## Build and release files

`npm run package` validates the portable manifests, skills, reviewer cases and allowlisted files, then creates a deterministic plugin ZIP. It does not include server code, data holdings, tests, evidence or deployment credentials. `deployment/` is the separate server container/cloud configuration. In the source repository, `docs/SUBMISSION.md` records deployment, client and portal checkpoints; check each evidence type separately. No cloud resource or submission is created by any npm script.

MIT license for this package code and instructions; source data retain their own publisher terms. The copied Storm Events data retain publisher attribution and immutable input provenance in `gateway/storm-record/`. This snapshot is source coverage, not a current hazard determination.
