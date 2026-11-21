# ReMCP existing App — MCP and translations

This is an update of **app-6aaaba1295a4819195a4987e18e43428**, not a new plugin.

`.codex-plugin/plugin.json` explicitly preserves `"mcpServers": "./.mcp.json"`.
The active Codex compatibility file `.mcp.json` declares the original remote HTTP MCP endpoint `https://remcp.site/mcp` and contains no `$schema`. No separate portable `mcp.json` is bundled, preventing conflicting plugin formats. OAuth is configured by the existing OpenAI connection; **do not place any credentials or synthetic MCP keys in this archive**.

Four original skills and gray brand images are included. Localized operator and publishing instructions are included under `locales/` for English, Russian, Ukrainian and Polish. The canonical technical metadata remains in English to match tool descriptions.

This archive cannot independently update the icon of a registered OpenAI App or publish changed backend tool descriptions. Refresh the authorized MCP discovery after the corresponding server deployment; only OpenAI can approve publication.

## Format verification

This archive uses the supported **Codex compatibility format**: `.codex-plugin/plugin.json`, `.mcp.json`, `skills/` and `assets/`. It does not mix a portable Agent Plugins `mcp.json` into the legacy package.
