# Cello for Codex

Connect Codex to Cello to build, diagnose, and improve user-referral and partner programs.

## Included

- Hosted Cello MCP server: `https://mcp.cello.so/mcp`
- `cello-get-integration-guide`: tailored Cello integration plans
- `cello-integration-health-check`: live integration diagnostics
- `cello-get-program-performance`: referral-program performance analysis

## Local installation

Place this folder at `~/plugins/cello`, then add the following entry to the `plugins` array in `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "cello",
  "source": {
    "source": "local",
    "path": "./plugins/cello"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Reinstall the plugin from your personal marketplace, then open a new Codex task to use its MCP tools and skills.

## Authentication

The MCP endpoint may ask each user to authenticate with Cello when they install or first use the plugin.
