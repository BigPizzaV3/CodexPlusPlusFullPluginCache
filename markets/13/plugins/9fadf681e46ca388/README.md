# MoodLens To-Do plugin

This is the universal ChatGPT and Codex plugin package for the MoodLens To-Do
remote MCP server.

## Package contents

- `.codex-plugin/plugin.json` contains public plugin metadata, review cases,
  release notes, and packaged icon paths.
- `.mcp.json` connects the package to the production Streamable HTTP MCP
  endpoint using OAuth with Dynamic Client Registration.
- `assets/icon.png` is the square listing and composer icon.
- `submission/` contains reviewer-facing listing text, test cases, release
  notes, OpenAI and Claude listing copy, production verification steps, and the
  remaining submission checklists.

This is intentionally an MCP-only plugin. OpenAI supports MCP-only submissions,
and the current server does not require a bundled skill or custom UI to expose
its tools.

## Endpoint

`https://moodlenstodo.com/api/mcp`

Opening this URL as a normal browser page can return a JSON-RPC error about
`text/event-stream`. That is expected because the URL is an MCP transport
endpoint, not a website.

## Authentication

Do not place API keys, OAuth secrets, demo credentials, or reviewer credentials
in this directory. Authentication details and any demo account belong in the
OpenAI submission portal's secure fields.

Before public submission, the remote endpoint must pass the OAuth, tool
metadata, and review checks in `submission/CHECKLIST.md`,
`submission/CLAUDE_CHECKLIST.md`, and
`submission/PRODUCTION_VERIFICATION.md`.

## Validation

From the repository root, run:

```powershell
Get-Content -Raw plugins\moodlens-todo\.codex-plugin\plugin.json | ConvertFrom-Json | Out-Null
Get-Content -Raw plugins\moodlens-todo\.mcp.json | ConvertFrom-Json | Out-Null
```

These commands verify that both JSON files parse. The OpenAI submission portal
performs the authoritative package, metadata, endpoint, and policy validation.
