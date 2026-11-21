# AeroPlan IQ Connect — OpenAI upload package v1.0.0

This is a portable **Agent Plugins 1.0** package. Upload this ZIP as one OpenAI Plugins draft. It contains a single remote HTTPS MCP server declaration and no credentials or app bindings.

- Main MCP resource: `https://app.drone-perspective.com/mcp`
- Authentication: Supabase-managed OAuth 2.1 via discovered issuer, Dynamic Client Registration (`dcr`) selected for the portal configuration; verify the issuer's DCR toggle and exact callback during portal connection. Public tool discovery is permitted; customer operation tools require authentication.
- Identity scopes: `openid` and `email`. Separate optional AeroPlan draft grants are managed by AeroPlan and NOT represented as arbitrary OAuth scopes.
- The official 192px source logo was retrieved from GitHub `public/aeroplan-connect-official-logo.webp` at main, then faithfully resampled to listing PNG sizes; no logo substitute or new illustration was generated.

**Important: This ZIP is prepared for draft upload, not yet certified ready to click `Submit for review`.** The verified public terms URL, reviewer-only test account, accessible real demo recording, currently published AI-specific privacy coverage and live portal connection/scans must still be addressed. The portal might also require business verification, publisher-target country selection, commerce disclosures and domain challenge. None can be established by packaging alone.

This ZIP excludes the application's proprietary source code, database contents and secrets.
