---
name: setup
description: Connect Dreamdata and verify account access after installing the Dreamdata plugin, or troubleshoot initial authentication and account selection.
---

# Set up Dreamdata

The plugin declares the shared MCP endpoint https://mcp.dreamdata.io/mcp in its root mcp.json. Users authenticate with their own Dreamdata login through OAuth 2.1 with SHA-256 PKCE. No existing custom connection or account-specific endpoint is required by this configuration.

## Connect and verify

If Dreamdata tools are available, call list_my_accounts to verify access. A successful response establishes connectivity; an installed plugin alone does not. If authentication is requested, direct the user through the host's Connect or sign-in flow. Never request passwords, tokens, or client secrets in chat or store them in plugin files.

If tools are unavailable, ask the user to enable the installed Dreamdata plugin and complete its MCP sign-in flow, then use a fresh chat if needed. Do not claim to create a connection without a supported host operation. Avoid creating a second custom connection when the bundled server can be authenticated.

For manual ChatGPT connection setup when the host cannot load the bundled server, follow the official Dreamdata instructions: use https://mcp.dreamdata.io/mcp, and clear OIDC enabled under Advanced OAuth settings > OpenID support before authenticating. Explain this as a fallback rather than an installation requirement.

Reading Dreamdata resources is required. Saving reports, audiences, and dashboards are separate optional grants. Explain these options based on the user's intended work; do not require write permissions for reading. OAuth consent does not authorize individual save operations. Let the user complete consent themselves.

Once connected, select the sole account automatically. If several accounts are available, use the user's stated account or ask them to choose. Do not store account selections in shared package files. Offer a relevant first task: analyze a saved report, inspect a company journey, or find companies for an audience. For reports, dashboards, and company journeys, use the [analytics skill](../dreamdata-analytics/SKILL.md). For audience discovery, querying, and saving, use the [activation skill](../dreamdata-activation/SKILL.md). Perform the task they choose using the available Dreamdata tools.

## Connection issues

- 401: reconnect to renew authentication.
- 403: verify the account against list_my_accounts; do not assume a missing scope is the cause.
- Missing save permission: explain the required optional grant. Dreamdata documents disconnecting and reconnecting to obtain newly available permissions; explicit-scope clients also need the scope added to their configuration. Do not disconnect automatically.
- Client not recognized: Dreamdata allowlists OAuth clients; direct the user to mcp-feedback@dreamdata.io.
- Server not enabled for the user: direct the user to their Dreamdata account owner or mcp-feedback@dreamdata.io.
- 502: report a Dreamdata service error, not a local configuration problem.

Reference: https://developer.dreamdata.io/mcp/mcp-server/
