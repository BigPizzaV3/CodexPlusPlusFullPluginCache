# Public MCP contract

All calls use the authenticated connection's active SMEPost organization. Never send organization IDs, credentials or model-generated metrics as tool inputs.

| Tool | Inputs | Result and use |
| --- | --- | --- |
| `get_profile` | none | Opaque connected profile identifier and organization nickname only. Do not return email or personal name. Read-only. |
| `list_gsc_properties` | none | Organization name, connected properties and shared GSC access policy. Read-only; interacts with Google. |
| `get_gsc_opportunities` | optional `siteUrl`, `country`, `device`, `minImpressions` | Prioritized normalized opportunities, effective and comparison ranges, filters, access limitations and workspace link. Read-only; interacts with Google. |
| `get_gsc_page_insights` | required `pageUrl`; optional `siteUrl`, `country`, `device` | Performance and queries for one page under the connected property. Read-only; interacts with Google. |
| `save_gsc_opportunity` | required `opportunityId`, `siteUrl`; optional `filters`, `note` | Idempotent SMEPost write returning saved ID, status and exact workspace URL. Initial saves re-fetch Google evidence. Requires explicit user intent. |
| `create_content_brief` | required saved `opportunityId` | Idempotent SMEPost write returning the persistent brief, status and exact workspace URL. Requires explicit user intent. |

Opportunity IDs are opaque 32-character values supplied by the server. Do not construct them. Country uses a lowercase three-letter GSC code, such as `hkg`; device is `DESKTOP`, `MOBILE` or `TABLET`. Saving preserves the full returned filters object, including the impression threshold when present.

The server determines finalized date ranges and entitlement limits; these tools do not accept arbitrary start/end dates. Missing comparison data is unknown, not zero. CTR is a fraction; position improvements mean a lower numeric average position. A low-CTR expectation is an estimate, not guaranteed clicks. Cannibalization is a candidate requiring editorial judgment.

Google Search Console is read-only. Save and brief actions write only explicitly selected work into SMEPost. Neither action publishes content, creates a checkout, subscribes the user to marketing, nor enables automatic alerts.
