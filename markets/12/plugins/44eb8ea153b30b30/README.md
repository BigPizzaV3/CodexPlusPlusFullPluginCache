# Recipe One for AI assistants

<img src="assets/recipe-one-icon.png" alt="Recipe One" width="64" align="right">

Bring [Recipe One](https://www.recipeone.app) into Claude, ChatGPT, Cursor, Grok Bot and other AI assistants: save recipes from links, find what to cook in your own library, plan the week and send the ingredients to your grocery list. Everything syncs with the Recipe One app on iPhone and Android.

This repository is the plugin package: the connection to the Recipe One MCP server and a meal-planning skill. The server itself is hosted by Recipe One; there is nothing to run.

- **Server:** `https://mcp.recipeone.app/mcp` (remote MCP, Streamable HTTP, OAuth sign-in)
- **Docs:** https://www.recipeone.app/docs
- **Privacy:** https://www.recipeone.app/privacy
- **Support:** support@recipeone.app

## What you can do

Without an account:

- Turn a recipe from the chat into a recipe card and scale it to any number of servings.
- Plan a week of meals and get one combined shopping list.

With a free Recipe One account (Google, Apple or email):

- Import a recipe from a website, Instagram, TikTok, YouTube, Facebook or Pinterest link.
- Search your saved recipes ("what can I cook tonight with chicken?").
- Save recipes you create in the chat, edit and organize them into cookbooks.
- Add recipes to your meal plan and their ingredients to your grocery list.

## Install

**Claude Code**

```sh
/plugin marketplace add recipeone/recipe-one
/plugin install recipe-one@recipe-one
```

Or add only the server: `claude mcp add --transport http recipe-one https://mcp.recipeone.app/mcp`

**Claude (web, desktop, mobile):** Customize → Connectors → Add custom connector, and paste `https://mcp.recipeone.app/mcp`.

**Cursor:** install Recipe One from the Cursor marketplace, or add the server to `mcp.json`:

```json
{ "mcpServers": { "recipe-one": { "url": "https://mcp.recipeone.app/mcp" } } }
```

**ChatGPT:** Plugins → Add → Add custom MCP server, and paste the server address.

## What is in this repository

| File | Read by |
| --- | --- |
| `plugin.json`, `mcp.json` | Agent Plugins hosts (ChatGPT, Cursor) |
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.mcp.json` | Claude Code and Claude |
| `.codex-plugin/plugin.json` | Codex |
| `skills/meal-planning/SKILL.md` | all hosts that support skills |

## License

The plugin files in this repository are MIT licensed. Recipe One, its app and its server are not part of this license.
