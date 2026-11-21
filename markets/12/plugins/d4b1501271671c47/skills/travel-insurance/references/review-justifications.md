# Tool annotations and input scope

These justifications describe the updated MCP server source. Deploy that source
and rescan the endpoint before submitting: the ZIP does not deploy the server
or override the portal's scanned annotation values.

| Tool | Hint | Value | Justification |
| --- | --- | --- | --- |
| `get_travel_insurance_quote` | `readOnlyHint` | `true` | Calculates and retrieves quotes without creating or changing an insurance policy. Returning a purchase link does not execute a purchase. |
| `get_travel_insurance_quote` | `openWorldHint` | `true` | Sends quote criteria to the configured public TP API over HTTPS, outside a bounded private account or workspace. It does not accept arbitrary URLs or recipients. |
| `get_travel_insurance_quote` | `destructiveHint` | `false` | Does not buy policies, process payments, delete data, revoke access, or execute irreversible policy actions. |
| `check_api_health` | `readOnlyHint` | `true` | Retrieves the upstream health response without requesting quotes or changing policy data. |
| `check_api_health` | `openWorldHint` | `true` | Contacts the public TP API's fixed `/healthz` endpoint over HTTPS, outside a bounded private account or workspace. |
| `check_api_health` | `destructiveHint` | `false` | Does not buy policies, process payments, delete data, or change policies. |

## Necessary quote inputs

- Trip type and dates select single-trip versus annual cover and the coverage period.
- Destination country codes determine destination eligibility and pricing.
- Traveller ages determine eligibility and pricing; names and dates of birth are not requested.
- Optional cancellation and baggage amounts, excess, and activity-cover flags specify the requested cover.
- The health tool accepts no user inputs.

The server disables PostHog's injected `context` parameter and conversation-ID
parameter. It does not request conversation summaries, conversation history,
names, contact details, credentials, or payment details as tool inputs.
This change does not disable all operational analytics or logging; those remain
separate from the tool input schema and must be reflected in the actual privacy
disclosures. The annotations describe the tools' quote/status operations.

Regression tests inspect both advertised schemas and annotations with analytics
enabled and disabled, and call both tools without analytics context using mocked
upstream responses. These tests do not establish what the upstream provider
stores internally or guarantee review approval.
