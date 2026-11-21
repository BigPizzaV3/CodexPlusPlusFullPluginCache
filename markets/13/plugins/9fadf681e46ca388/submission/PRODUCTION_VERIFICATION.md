# Production verification runbook

Run this after deploying the Functions and Hosting changes. These checks do not
replace a full reviewer-workspace test.

## 1. OAuth discovery

```powershell
Invoke-RestMethod https://moodlenstodo.com/.well-known/oauth-protected-resource
Invoke-RestMethod https://moodlenstodo.com/.well-known/oauth-protected-resource/api/mcp
Invoke-RestMethod https://moodlenstodo.com/.well-known/oauth-authorization-server
```

Verify that the resource is exactly
`https://moodlenstodo.com/api/mcp`, the issuer is exactly
`https://moodlenstodo.com`, and the metadata advertises S256 PKCE, DCR, the
authorization endpoint, and the token endpoint. Protected-resource metadata
should advertise only the minimal `tasks` scope; authorization-server metadata
should advertise every supported scope.

## 2. Dynamic Client Registration

This creates a public test-client record. Use non-sensitive metadata.

```powershell
$registration = @{
  redirect_uris = @('https://claude.ai/api/mcp/auth_callback')
  client_name = 'MoodLens submission smoke test'
  token_endpoint_auth_method = 'none'
  grant_types = @('authorization_code', 'refresh_token')
  response_types = @('code')
} | ConvertTo-Json

Invoke-RestMethod `
  -Method Post `
  -Uri https://moodlenstodo.com/api/oauth/register `
  -ContentType 'application/json' `
  -Body $registration
```

The response must include a `client_id` and must not include a client secret.

## 3. Public MCP discovery

Use MCP Inspector or send `initialize` and `tools/list` with protocol headers.
Both should succeed without a credential. Confirm every tool has:

- a title;
- a narrow description;
- `readOnlyHint`;
- `destructiveHint`;
- the expected OAuth scopes.

## 4. HTTP authentication challenge

Call a protected tool without authorization. The HTTP response must be `401`
and its `WWW-Authenticate` header must contain:

- `resource_metadata="https://moodlenstodo.com/.well-known/oauth-protected-resource"`;
- the exact scopes required by that tool;
- `error="invalid_token"`.

For a singular `tools/call`, also confirm the response body contains the same
challenge under `_meta["mcp/www_authenticate"]`.

## 5. End-to-end OAuth

From fresh ChatGPT and Claude connections:

1. Add `https://moodlenstodo.com/api/mcp`.
2. Start one read tool and complete MoodLens sign-in.
3. Select the dedicated reviewer workspace.
4. Verify the consent screen displays the expected client and scopes.
5. Complete the read.
6. Start a write tool, approve it, and verify only the intended record changes.
7. Let the access token expire or use a controlled short-lived test, then
   verify refresh succeeds when the exact MCP `resource` is included.
8. Reuse the rotated refresh token in a controlled test and verify the token
   family is atomically revoked and its access tokens are rejected.

Never paste tokens into chat or commit them. Keep temporary tokens in
process-local environment variables and clear them after the test.

## 6. Isolation and replay checks

- Try a workspace identifier outside the reviewer workspace and verify access
  is denied without revealing private records.
- Present an MCP-bound access token directly to `/api/external` and verify it
  is rejected.
- Verify server logs contain no raw access token, refresh token, authorization
  code, client secret, or API key.

## 7. Functional review

Run every tool in `TEST_CASES.md`, then exercise the remaining tools at least
once with valid parameters. Record expected IDs and cleanup actions in the
private reviewer notes, not in this repository.
