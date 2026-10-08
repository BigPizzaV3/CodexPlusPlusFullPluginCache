---
name: genseo-setup
description: Configure or troubleshoot the Genseo remote MCP connection for ChatGPT, Codex, Claude, Cursor, or Grok. Use when Genseo tools are disconnected, authentication is missing, or the user asks how to connect Genseo.
---

# Set up Genseo

1. Connect the remote server at `https://api.genseo.co/mcp` and complete the browser-based Genseo OAuth flow.
2. Review the requested scopes and approve the connector only if the client name and callback are expected.
3. Reload the plugin and open `/mcp` to verify the `genseo` server connection.
4. Call `genseo_me` and `genseo_projects_list`, then select one project before using another Genseo tool.

For non-interactive developer or CI use only, a project-bound `GENSEO_API_KEY` can be sent as a Bearer token. Never paste the key into chat, source files, public manifests, or version control. Public installations use OAuth 2.1.

For setup details, use [the Genseo developer documentation](https://docs.genseo.co/developers/overview). Contact `support@genseo.co` if authentication fails after creating a new key.
