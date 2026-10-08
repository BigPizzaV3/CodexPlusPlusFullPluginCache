# Genseo Agent Plugin

Connect an AI assistant to Genseo through the public Streamable HTTP MCP endpoint at `https://api.genseo.co/mcp`.

The server exposes project-scoped AI visibility KPIs, trends, tracked prompts, competitors, cited sources, and quota alongside SEO audit, keyword, content, publishing, and webhook workflows.

## Public installation

The public connection uses OAuth 2.1 Authorization Code with PKCE and refresh tokens. Install or add Genseo from the platform's plugin/connector UI, sign in to Genseo, review the requested scopes, and approve the connection. No API key should be entered for a public installation.

After connecting:

1. Call `genseo_me` and `genseo_projects_list`.
2. Ask the user to choose exactly one accessible `project_id`.
3. Include that `project_id` in every project operation.
4. Respect membership, selected-project, expiration, viewer, and Agent Autonomy restrictions.

OAuth-connected agents cannot manage billing, team access, credentials, or delete projects.

## Developer and CI fallback

For non-interactive development or CI only, create a project-bound Genseo API key with the minimum required scopes and configure the MCP client to send `Authorization: Bearer $GENSEO_API_KEY`. Never commit the key or add it to a public manifest.

## Package layout

- `plugin.json` and `mcp.json`: portable Agent Plugins 1.0 package.
- `.codex-plugin/plugin.json`: Codex compatibility manifest using the OAuth-first `.mcp.json` connection.
- `.claude-plugin/plugin.json`: Claude compatibility manifest.
- `.cursor-plugin/plugin.json`: Cursor compatibility manifest.
- `.mcp.json`: Claude, Cursor, and Grok-compatible remote MCP declaration.
- `skills/`: safe project-selection and setup workflows.

Support: support@genseo.co · [Privacy](https://www.genseo.co/legal/privacy-policy) · [Terms](https://www.genseo.co/legal/terms)
