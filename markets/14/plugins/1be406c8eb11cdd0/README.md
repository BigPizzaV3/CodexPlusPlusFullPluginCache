# Pledge plugin for Claude, Codex and Cursor

Create, send and store contracts with your agent. The plugin connects your agent to your Pledge workspace (the MCP server at `https://www.pledge.no/api/mcp`) and adds the `new-contract` skill: the agent asks what kind of contract you need, who it's for, the value and who signs, saves a draft in Pledge, shows you the contract in the chat, and sends it for signing when you say so.

In clients that show MCP Apps (Claude, ChatGPT), the contract appears in the chat as an editable document: change the text in place, click a field to fill it in, select text to ask the agent for changes, then choose who signs and press Send. Elsewhere (Claude Code, Codex) the agent shows it as Markdown with a link to the draft.

The same folder is a Claude plugin (`.claude-plugin/plugin.json`), a Codex plugin (`.codex-plugin/plugin.json`) and a Cursor plugin (`.cursor-plugin/plugin.json`). All three use `skills/`; Claude and Codex read the server from `.mcp.json`, Cursor from its manifest.

Always use `https://www.pledge.no/api/mcp` (with www): `pledge.no` redirects to www, and clients that check the server's metadata (Codex does) refuse the sign-in otherwise.

## Install

The plugin is published at [github.com/Ur-Solutions/pledge-plugin](https://github.com/Ur-Solutions/pledge-plugin), with marketplace files at its root: `.claude-plugin/marketplace.json` for Claude, `.agents/plugins/marketplace.json` for Codex and `.cursor-plugin/marketplace.json` for Cursor.

Claude Code:

```bash
claude plugin marketplace add Ur-Solutions/pledge-plugin
claude plugin install pledge@pledge
```

Then run `/mcp` in Claude Code and sign in to Pledge.

Codex:

```bash
codex plugin marketplace add Ur-Solutions/pledge-plugin
codex plugin add pledge@pledge
codex mcp login pledge
```

Cursor: open Pledge's [one-click install](cursor://anysphere.cursor-deeplink/mcp/install?name=pledge&config=eyJ1cmwiOiAiaHR0cHM6Ly93d3cucGxlZGdlLm5vL2FwaS9tY3AifQ==), or add it to `~/.cursor/mcp.json`:

```json
{ "mcpServers": { "pledge": { "url": "https://www.pledge.no/api/mcp" } } }
```

Then sign in when Cursor asks (Settings → MCP shows Needs login until you do). The repository's `.cursor-plugin/marketplace.json` lists the plugin with its skill for Cursor's marketplace.

On claude.ai and in ChatGPT, add Pledge as a connector with the same URL. The flow also works there without the skill, because the server's instructions and its `new_contract` prompt describe it.

## Keep in step

This folder lives in Pledge's main repository (`plugins/pledge`) and is copied to the public pledge-plugin repository on release. The `new-contract` skill and the server's own flow text say the same thing in two places: change both together.

## What it sends and stores

The plugin contains two skills (`new-contract`, `get-started`) and the address of Pledge's MCP server, `https://www.pledge.no/api/mcp`. It runs no code on your machine. The agent sends tool calls to that server only, over HTTPS, signed in as you with OAuth; the server reads and changes the workspace you picked, as you could in Pledge, and logs each change on the contract. Pledge doesn't receive your conversations.

## Privacy and support

Privacy policy: https://www.pledge.no/privacy. Terms: https://www.pledge.no/terms. Help and setup: https://www.pledge.no/agents. Contact: contact@ursolutions.no.

