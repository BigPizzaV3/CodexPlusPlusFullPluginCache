Jusnote ChatGPT plugin package — REVIEW WORDING REVISION

This package revises product descriptions and review-test expectations to avoid
promising behavior that has not yet been demonstrated.

Before submission:
1. Run Scan Tools against https://mcp.jusnote.com/insights and confirm every
   tool name in plugin.json against the exact names exposed by the public endpoint.
2. Execute each positive and negative test against a dedicated test tenant.
   Replace sample record references with records that actually exist in that tenant.
3. Confirm which operations are exposed by the server. Describe the connector as
   read-only only if all exposed operations have been verified to be retrieval-only.
4. Verify authorization behavior with accounts having different permissions.
5. Record the walkthrough using actual successful test results.
6. Keep client secrets, access tokens, and passwords out of this ZIP.

The package contains logo assets under assets/. OAuth is configured for DCR
discovery without a registrationUrl. This assumes the authorization server
publishes a valid registration_endpoint in its OAuth metadata and supports
the DCR flow expected by the platform.
