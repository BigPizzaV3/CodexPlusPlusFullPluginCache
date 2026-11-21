# Unified MCP migration

| Endpoint | Tools | Standalone OAuth audience |
| --- | --- | --- |
| `/mcp` | `account_*` and `insights_*` | `https://api.extract.to/mcp` |
| `/mcp-account` | Existing account names | `https://api.extract.to/mcp-account` |
| `/mcp-analyze` | Existing analysis names and compatibility wrappers | `https://api.extract.to/mcp-analyze` |

Authorization/token endpoints remain `/oauth2/authorize` and `/oauth2/token`.
New unified grants are account-scoped and explicitly list all three same-server
MCP audiences. One token can be reused across these endpoints without another
authorization. Endpoint-specific grants retain their original audience; endpoint
validators do not accept arbitrary tokens or credentials from another environment. Connector-bound clients authorize through
`/mcp-analyze`; existing connector-bound `/mcp` tokens cannot call account tools.
Existing tokens never gain scopes or roles. Legacy `/mcp` names are a breaking
inventory change: refresh tools or migrate Insights-only clients to `/mcp-analyze`.

Follow the three cumulative [ordered releases](releases.md): add `/mcp-analyze`
and migrate standalone clients first, activate the unified `/mcp` backend second,
and publish the unified manifests and skills together after backend acceptance. Remove old default
registrations and refresh discovery; never keep duplicate dependency registrations.

PR #2717's local bridge and exchange-only grant are superseded once real-client
acceptance passes. This implementation retains its consented-account revalidation
and token cache headers, without the unrelated account-activation change.
Gemini packaging and OAuth issuer-response improvements ship separately from
`add-gemini-extension-updates`, after the unified backend and shared skills.

One login means one authorization per client installation/session, not shared
credentials across products. Provider OAuth consent remains separate. Access tokens last 12 hours. Clients supporting the `refresh_token` grant can renew
automatically; refresh sessions last up to 30 days idle and 90 days total by default.
Existing access-token-only installations must reauthorize once to receive a refresh
token; legacy registrations or registrations that omitted refresh support must be updated. Reconnect once after deploying shared grants: existing tokens and pending
pre-rollout authorization codes keep their original audiences and scopes.

Keep one default `extract` registration. Separate integration entries can have
separate client-managed credential stores and prompt independently even with a
shared server grant. Do not install both local and production variants when only
one environment is intended; those environments cannot share authentication.

Before release, run the evaluation and client acceptance procedure in
[evaluations](evaluations/README.md). Local protocol tests alone do not prove that
a particular desktop host opens only one browser authorization tab.
