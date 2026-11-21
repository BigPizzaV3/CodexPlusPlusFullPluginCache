# Flint Agent Plugin

Build and manage websites with [Flint](https://flint.com)'s AI website builder from your AI agent: Claude Code, Codex, ChatGPT, Cursor, Gemini CLI, Google Antigravity, Grok, and Muse.

## Features

- **Chat with the Flint agent** to modify your Flint sites — add pages, update content, redesign sections — and answer its questions in the same chat
- **List your sites** across all connected organizations
- **Publish sites** to production when you're ready to go live

Every agent connects to the same hosted MCP server, `https://mcp.tryflint.com/mcp`, and signs you in with your Flint account the first time it calls a tool. Your Flint organization must be on the Starter plan or above.

## Installation

### Claude Code

```
/plugin install flint
```

Or from this repository's marketplace:

```
/plugin install flint --marketplace tryflint/agent-plugin
```

Then run `/mcp`, select Flint, and choose "Authenticate".

### Codex

```
codex plugin marketplace add tryflint/agent-plugin
codex plugin add flint@flint
codex mcp login flint
```

### Cursor

Install Flint from the [Cursor Marketplace](https://cursor.com/marketplace), or import this repository under Dashboard → Plugins & MCPs → Team Marketplaces.

### Gemini CLI

```
gemini extensions install https://github.com/tryflint/agent-plugin
```

### Grok Build

Grok Build reads Claude Code marketplaces, so the Claude Code marketplace command above works there too.

### Muse Code

Muse Code loads the skill from this plugin, but it won't sign in to a plugin's MCP server. Add the server to `~/.config/muse/settings.json`:

```json
{ "mcpServers": { "flint": { "type": "streamable-http", "url": "https://mcp.tryflint.com/mcp" } } }
```

Then run `muse mcp login flint`.

### Other MCP clients

Add a custom connector pointing at `https://mcp.tryflint.com/mcp` and sign in with Flint. This works in ChatGPT, Claude.ai, grok.com, and Grok Bot.

## Usage

Once authenticated, just ask your agent to work on your Flint site:

> "Add a pricing page with three tiers to my site"

> "Update the hero section to say 'Welcome to the Future'"

> "Publish my site"

In Claude Code you can also use the `/flint:edit-site` skill directly:

```
/flint:edit-site Add a contact form with name, email, and message fields
```

## Tips

- **Describe goals, not implementation** — Flint is an expert designer and produces better results when given creative freedom over layout, styling, and component structure
- **Pass through reference material** — if you have code snippets, embed scripts, or examples, include them and Flint will incorporate them
- **Be specific when you want to be** — requests like "make the header black" or "use a three-column grid" are honored directly

## Support

- Documentation: https://flint.com/docs/claude-code-plugin
- Email: support@tryflint.com

## Privacy Policy

https://flint.com/privacy-policy
