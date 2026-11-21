# Jus Mundi Legal Research — public plugin package

This is the portable plugin package intended for the OpenAI Plugins submission portal. It connects to the production Jus Mundi Assistant MCP endpoint and contains the legal research skill. It contains no access token or client secret; users authenticate through the MCP server's OAuth authorization flow. Public listing URLs and starter prompts have been populated from the Microsoft Copilot package supplied in this repository.

## Server behavior verified from this repository

- The server uses MCP Streamable HTTP and registers its handler at the configured server root.
- The default production resource URI documented by the MCP API reference is `https://mcp.jusmundi.com`.
- The server publishes `/.well-known/oauth-protected-resource` with a configured Keycloak authorization server and the `mcp:tools:legal_research` scope.
- The server challenges requests with Bearer authentication, validates the JWT signature, resource audience, and scope, and performs a Keycloak UMA permission check before research.
- `legal_research` persists the interaction and records usage and billing. Its `readOnlyHint` is therefore `false`; the server marks it open-world and non-destructive.

## OpenAI public review checks still required

The endpoint and OAuth flow must be checked against the live production configuration. The repository does not establish these Keycloak settings:

1. The OIDC discovery document advertises authorization-code PKCE with `S256` and supported client authentication/registration (CIMD, DCR, or an OpenAI-pre-registered client).
2. Keycloak accepts and preserves the MCP `resource` parameter, and the issued access token has the MCP resource URI in its audience.
3. The registered client permits the exact redirect URI shown by the OpenAI Plugins dashboard.
4. The tool metadata advertises OAuth security schemes in the form required by OpenAI's plugin auth UI. The current `legal_research` registration in this repository does not explicitly set per-tool `securitySchemes`; check whether the server advertises a default security scheme and add an explicit OAuth2 scheme if it does not.

The supplied Microsoft package provides the correct Jus Mundi logo and composer icon, as well as the website, privacy policy, and terms URLs used in this manifest. The support URL points to Jus Mundi's AI/MCP integrations page; confirm that it is the appropriate support destination for this listing.

## API use

For a direct Responses API integration, the application remains responsible for obtaining and refreshing the user's Keycloak access token and supplying it in the MCP tool's `authorization` field. This is separate from the public plugin's interactive OAuth sign-in flow.
