# Claude Connectors Directory checklist

## Locally complete

- [x] Remote MCP server uses a stable HTTPS Streamable HTTP URL.
- [x] OAuth protected-resource and authorization-server metadata are routed.
- [x] Dynamic Client Registration accepts public clients without a client
  secret.
- [x] Every MCP authorization-code flow requires S256 PKCE and the exact MCP
  `resource`; refresh requests require the same resource.
- [x] Refresh tokens rotate, and detected reuse atomically revokes the token
  family.
- [x] Rotated refresh records remain available until their original expiry,
  and MCP request throttling follows the stable token family.
- [x] Protected calls return an HTTP `401` challenge with
  `WWW-Authenticate`; insufficient scopes return `403`.
- [x] ChatGPT receives the same challenge in tool-result
  `_meta["mcp/www_authenticate"]`.
- [x] Initialization and tool listing remain available for lazy
  authentication.
- [x] Every tool has a human title and read/write safety annotations.
- [x] Read and write operations are exposed as separate, purpose-built tools;
  there is no catch-all HTTP request tool.
- [x] MCP bearer credentials are validated once and are not forwarded to the
  internal MoodLens API executor.
- [x] Public documentation, privacy policy, support details, and a 512px icon
  are identified.

## Required after deployment

- [ ] Confirm all OAuth discovery URLs return `200` from production.
- [ ] Confirm an unauthenticated protected tool call returns `401` with the
  production protected-resource metadata URL.
- [ ] Connect from a fresh Claude custom connector using
  `https://moodlenstodo.com/api/mcp`.
- [ ] Complete OAuth through the hosted Claude callback and verify refresh.
- [ ] Exercise all tools with valid sample data using MCP Inspector or Claude.
- [ ] Confirm every valid tool call returns a useful response and every invalid
  input returns an actionable error.
- [ ] Confirm no response exposes credentials, stack traces, or data from a
  different workspace.

## Portal and reviewer requirements

- [ ] Use a Claude Team or Enterprise organization.
- [ ] Confirm the submitter is an Owner/Primary Owner or has Directory
  management access.
- [ ] Create a fully populated, non-sensitive reviewer workspace and test
  account.
- [ ] Enter reviewer credentials and setup steps only in the portal's secure
  fields.
- [ ] Confirm the permanent listing slug before publishing.
- [ ] Complete the data-handling and seven compliance acknowledgments with the
  responsible business or legal owner.
- [ ] Confirm whether any regulated health data or sponsored content is in
  scope; do not guess.
- [ ] Submit through Claude.ai Admin settings, then track feedback in the
  submissions dashboard.

Claude officially supports DCR out of the box. If directory traffic becomes
large, evaluate CIMD or Anthropic-held client credentials to avoid creating a
new DCR record for every fresh connection.
