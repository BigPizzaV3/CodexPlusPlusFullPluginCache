Historical supplied review; findings have not been reverified on 2026-10-14. Do not infer that the production server has been fixed.

# Current server OAuth acceptance items

Review snapshot: 2026-10-12. Local source: `supabase/functions/mcp/index.ts` in NotelyVoicePro, SHA256 `31c65f8817047a92519241b14d1f77dc064c40e7b05345731ed62740a5bc5ed6`. Public endpoint checks confirm discovery HTTP 200 and unauthenticated MCP HTTP 401 with a Bearer metadata challenge. These checks do not prove the full local source is deployed.

## Improvements confirmed in source

- Upstream credentials are read from environment variables; registration returns no client secret.
- Registration validates submitted callbacks and issues a signed downstream client ID.
- Authorization checks the registered callback; token exchange checks the original callback.
- Host PKCE S256 challenge/verifier binding is implemented.
- The public Supabase anonymous signing-key fallback has been removed.

## Remaining work before production approval

1. Require downstream `client_id` in authorization-code exchange. Its match is currently checked only when supplied (approximately lines 1657-1662).
2. Bind refresh tokens to their downstream client. Refresh currently permits a missing client ID, and checks registration rather than token ownership when one is supplied (approximately lines 1598-1627). Reject mismatched or missing clients.
3. Use only a dedicated `MCP_OAUTH_HMAC_SECRET`. The service-role-key fallback remains (approximately line 1332); fail closed without the dedicated key.
4. Confirm the previously exposed upstream secret was rotated. Removing it from source is insufficient; rotation must occur at the provider.
5. Verify code replay prevention, token resource/audience and scope enforcement, client revocation, per-user authorization/RLS, and refresh behavior with synthetic test accounts.
6. Verify complete login and the note tools across intended desktop/web/mobile hosts. Rejection tests must include missing/wrong PKCE, wrong/missing client, wrong callback, expired/replayed code, and mismatched refresh client.

The earlier successful library overview demonstrated account access, not security certification. This rebuild invokes no note tools or credential exchange. No secrets are shipped in the plugin. Server deployment, secret rotation, and production publication are separate owner-operated steps.
