# TimeChimp plugin for OpenAI (ChatGPT & Codex)

Brings your TimeChimp data into ChatGPT and Codex through the TimeChimp MCP server:

**MCP server:** [https://mcp.timechimp.com/mcp](https://mcp.timechimp.com/mcp) (Streamable HTTP, OAuth sign-in with your TimeChimp account)

The plugin bundles:

- **MCP connection** to `https://mcp.timechimp.com/mcp`
- **Skill** `timechimp-mcp`, which tells the model when and how to use the TimeChimp tools (pagination, date handling, euro formatting)

All tools are read-only: the signed-in user's profile, users and their contracts, teams, hours, expenses, mileage, projects and their budgets, customers, company holidays, the planning and remaining availability.

## Layout

```
plugins/timechimp/
├── plugin.json              # Portable Agent Plugins manifest (+ extensions.com.openai)
├── mcp.json                 # Portable MCP config (streamable-http)
├── .codex-plugin/
│   └── plugin.json          # Codex compatibility manifest (older Codex builds)
├── .mcp.json                # Codex compatibility MCP config
├── skills/
│   └── timechimp-mcp/
│       └── SKILL.md         # Copied from tc-mcp-server/skills/timechimp-mcp
└── assets/
    └── icon.png
```

`../../.agents/plugins/marketplace.json` registers this plugin in a local marketplace for testing.

## Test locally

**Codex CLI**

```bash
codex plugin marketplace add /Users/dylanmauer/Documents/timechimp/mcp-plugin
```

Then open `codex`, run `/plugins`, install **TimeChimp** and sign in when prompted.

**ChatGPT desktop app**

1. Turn on Developer mode (Settings → Security and login).
2. Add this folder as a personal marketplace, restart the app.
3. Open the Plugins tab, pick the TimeChimp marketplace, install, and sign in when prompted.

## Keeping the skill in sync

`skills/timechimp-mcp/SKILL.md` is a copy of the skill in the `tc-mcp-server` repo. When the server's skill changes, copy it again:

```bash
cp ../../../tc-mcp-server/skills/timechimp-mcp/SKILL.md skills/timechimp-mcp/SKILL.md
```
