# Blink plugin for ChatGPT

The package OpenAI's plugin portal takes as a ZIP: `plugin.json` (Agent Plugins 1.0.0, ChatGPT listing under `extensions.com.openai`), `mcp.json` pointing at `https://blink.new/mcp`, the onboarding skill and the icons.

Build and check it:

```bash
bun scripts/build-chatgpt-plugin.mjs
```

The script validates every limit OpenAI's upload and final submission enforce, then writes `plugins/chatgpt/dist/blink-<version>.zip`. Bump `version` for every upload; the portal refuses an unchanged version. `name` must stay the package name the portal assigned to Blink (`app-6ab030de77e08191a3e87f8b18234f78`); the portal refuses any other. Reviewer credentials are entered in the portal, never in this folder.

Server behaviour, tools and review notes: [docs/claude-connector.md](../../docs/claude-connector.md).
