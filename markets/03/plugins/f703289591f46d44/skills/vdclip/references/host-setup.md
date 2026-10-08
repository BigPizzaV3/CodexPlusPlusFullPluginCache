# Host setup

Production MCP endpoint: `https://mcp.vdclip.com/mcp`

Authentication is OAuth, handled by the host on the first tool call. There is no API key.
Never write an access token into a repository file — use the host's credential store.

## Installing

| Host | How |
| --- | --- |
| Claude Code | `/plugin marketplace add vdclip/vdclip-skills`, then `/plugin install vdclip@vdclip-skills` |
| Codex CLI / app | `codex plugin marketplace add vdclip/vdclip-skills`, then `codex plugin add vdclip@vdclip-skills`. Skills load on a new session, not the current one. |
| Claude.ai / Cowork | Build the zip with `./build.sh` and upload `dist/vdclip.zip` under Settings → Customize → Skills (Pro and above), then add the MCP server as a custom connector |
| `npx skills` hosts | `npx skills add vdclip/vdclip-skills` |
| `.agents/skills` discovery | `ln -s "$PWD/vdclip-skills/skills/vdclip" ~/.agents/skills/vdclip` |

The Claude Code and Codex plugins ship `.mcp.json`, so the server is configured for you.
Every other path needs it added by hand:

```json
{
  "mcpServers": {
    "vdclip": { "type": "http", "url": "https://mcp.vdclip.com/mcp" }
  }
}
```

## When a tool is missing

The connector advertises only the tools the session's OAuth scopes grant. A tool absent
from `tools/list` is a scope or a pause, not a bug — ask the user to reconnect and grant the
scope, and check [recovery.md](recovery.md) before assuming the feature is gone.
