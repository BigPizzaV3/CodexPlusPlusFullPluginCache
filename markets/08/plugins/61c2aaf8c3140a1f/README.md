# Causalytics OpenAI plugin

Plugin package connecting ChatGPT and Codex to the Causalytics MCP server.

## Layout

```
openai-plugin/
├── plugin.json              # portable manifest (root, agent-plugins schema)
├── mcp.json                 # remote streamable-http MCP server config
├── .app.json                # registered MCP app mapping (plugin_asdk_app_…)
├── .codex-plugin/
│   └── plugin.json          # compatibility fallback
├── assets/
│   ├── causalytics-icon.png # composer icon (drop in before submitting)
│   └── causalytics-logo.png # listing logo (drop in before submitting)
└── skills/
    └── causalytics-overview/
        └── SKILL.md
```

## Install locally for testing

The marketplace file at `../.agents/plugins/marketplace.json` points here.

1. Restart the ChatGPT desktop app.
2. Open the Plugins Directory, find the "Causalytics local" source.
3. Install the plugin and authenticate via the OAuth flow.

## Submit to OpenAI

1. Drop the final `causalytics-icon.png` and `causalytics-logo.png` into
   `assets/`.
2. Confirm `termsOfServiceURL` in `plugin.json` and
   `.codex-plugin/plugin.json` points at a live terms page.
3. Submit the folder through the plugin submission portal.