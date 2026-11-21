# CaDoMi.ai OpenAI Plugin

This package connects OpenAI plugin-capable clients to the CaDoMi.ai remote MCP server.

## MCP Server

- Production endpoint: `https://api.cadomi.ai/mcp`
- Transport: streamable HTTP
- Authentication: OAuth discovery from the MCP server, with bearer-token support for automation

## Capabilities

The MCP server exposes CaDoMi tools for reading and writing product, sprint, story, capacity, and rubric data as the authenticated user. The server enforces the same organization scoping and permission checks as the CaDoMi web application.

Read examples include sprint summaries, sprint stories, backlog stories, product lookup, story search, team members, and rubric assessments.

Write examples include creating stories, creating and updating sprints, updating capacity, updating and moving stories, creating and updating products, and submitting rubric assessments.

## Public Links

- Support: https://www.cadomi.ai/support
- Privacy policy: https://www.cadomi.ai/privacy-policy
- Terms of service: https://www.cadomi.ai/terms

## Files

- `plugin.json` is the portable Agent Plugins manifest.
- `mcp.json` declares the remote CaDoMi MCP server.
- `.codex-plugin/plugin.json` and `.mcp.json` provide a compatibility overlay for Codex-style plugin loaders.
