# HelpTester plugin package

This folder is the ChatGPT / Codex plugin (Agent Plugins 1.0.0 format) for HelpTester.
It is built into `dist/helptester-plugin.zip` by `npm run build:plugin` in `chatgpt-app/`.

- `plugin.json`      portable manifest + OpenAI listing/review metadata (`extensions.com.openai`)
- `mcp.json`         remote MCP server (Streamable HTTP) that serves the tools and widgets
- `.codex-plugin/`   compatibility manifest for older Codex clients
- `.mcp.json`        compatibility MCP config for older Codex clients
- `skills/helptester/SKILL.md`  instructions for the assistant on when to use which tool
- `assets/`          icon, logo, screenshots (copied in by the build)

The MCP server itself lives in `../server` and must be hosted publicly over HTTPS at the
URL declared in `mcp.json` (default `https://apps.helptester.com/mcp`). Override with
`MCP_URL=https://... npm run build:plugin`.
