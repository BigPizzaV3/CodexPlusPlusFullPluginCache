# Bullflow OAuth connection

The host connects to `https://api.bullflow.io/mcp` over Streamable HTTP. An unauthenticated request returns HTTP 401 with a Bearer challenge pointing to protected-resource metadata. Let the host discover the authorization server and manage OAuth.

| Setting | Value |
| --- | --- |
| Resource and issuer | `https://api.bullflow.io` |
| Protected-resource metadata | `https://api.bullflow.io/.well-known/oauth-protected-resource` |
| MCP metadata alias | `https://api.bullflow.io/.well-known/oauth-protected-resource/mcp` |
| Authorization-server metadata | `https://api.bullflow.io/.well-known/oauth-authorization-server` |
| Authorization | `https://api.bullflow.io/oauth/authorize` |
| Token exchange and refresh | `https://api.bullflow.io/oauth/token` |
| Client registration | `https://api.bullflow.io/oauth/register` |
| Revocation | `https://api.bullflow.io/oauth/revoke` |

The flow uses authorization codes with S256 PKCE. The user signs in through Bullflow's normal sign-in page and approves the requested permissions. Access tokens are opaque bearer tokens and belong only in the Authorization header managed by the host.

## Permissions

- `api:read`: market-data tools and GEX setup streams.
- `alerts:read`: saved custom alerts, live alerts, and backtesting replays.
- `alerts:write`: create custom alerts.
- `offline_access`: rotating refresh tokens to stay connected; requires another granted permission.
- `openid` and `email`: account identity and verified email, when requested by the host for workspace domain restrictions. These permissions require consent and do not grant market-data or alert access.

Use current tool schemas and available tools after connecting. Never treat OAuth consent as a request to perform a write.

## Troubleshooting

- A connection requires a verified email, active API subscription, and accepted API usage policy.
- HTTP 401 with `invalid_token` can indicate expired or revoked credentials or lost subscription access. Let the host refresh or reconnect; do not attempt to recover tokens from local files.
- HTTP 403 with `insufficient_scope` identifies a missing permission. Reconnect through the host and obtain the user's consent.
- Token errors such as `invalid_grant` require reconnecting.
- HTTP 429 requires respecting `Retry-After`.
- Access tokens last 15 minutes. Approved offline connections last at most 30 days from consent. Refresh tokens rotate; the host must save replacements and must not reuse old tokens.
- Disconnect from **Bullflow API dashboard → Connected services**. Reconnecting requires a new consent flow.

The package contains no client credentials or tokens. Do not add static credentials to MCP configuration or expose authorization codes, access tokens, refresh tokens, or credential-bearing URLs in chat.
