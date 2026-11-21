# xTask plugin

This is the OpenAI Platform submission package for the xTask MCP integration.

## Contents

- `plugin.json` — portable Agent Plugins manifest and OpenAI listing metadata.
- `mcp.json` — the public streamable-HTTP MCP endpoint at `https://xtask.hu/mcp`.
- `skills/xtask-workspace/SKILL.md` — guidance for safe, consistent use of xTask tools.
- `assets/` — xTask icon files referenced by the listing metadata.

## Before public submission

The canonical listing metadata is in root `plugin.json`. Its English base listing follows
OpenAI's submission guidance; `extensions.com.openai.publication.translations.hu-HU`
contains the Hungarian subtitle and description. Starter prompts remain Hungarian.
As of the documentation checked on 2026-10-02, imported translations are retained but
do not yet change text displayed in the Plugins Directory or listing API responses.
See https://developers.openai.com/plugins/deploy/submission#translate-listing-text.
The compatibility manifest is for older local tooling; it does not override root metadata.
Review cases are proposed scenarios and must still be run using the review account.

1. Upload the ZIP through **With MCP** in OpenAI Platform.
2. Complete the domain-verification challenge at `/.well-known/openai-apps-challenge` on the MCP host.
3. Connect the MCP server and complete the OAuth flow; then review the discovered tools.
4. Add a reviewer-only test account and workspace in the dashboard. Do not put credentials in this package.
5. Add an accessible video walkthrough URL in the dashboard, run the five positive and three negative review cases, and submit for review.
