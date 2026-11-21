# Monotype Fonts — ChatGPT / Codex plugin

Portable Agent Plugins package for the Monotype Fonts MCP server at
`https://mcp.monotype.com/mcp`.

```
monotype-fonts/
├── plugin.json                     portable manifest + OpenAI presentation (extensions.com.openai)
├── mcp.json                        remote streamable-HTTP MCP server, OAuth
└── skills/
    └── monotype-fonts/SKILL.md     font matching / asset workflow
```

## Authentication
`mcp.json` uses a static, pre-registered OAuth client configured as a public
(native) client:

```json
"auth": {
  "type": "oauth",
  "client": {
    "mode": "provided",
    "clientId": "<Monotype client ID>",
    "tokenEndpointAuthMethod": "none"
  }
}
```

- `tokenEndpointAuthMethod: "none"` means no client secret is used, so the
  portal will not ask for one.
- Register the callback URL shown in the ChatGPT connection flow as an allowed
  redirect URI on this client.
- Authorization and token endpoints come from OAuth discovery. If discovery
  doesn't provide them, add `authorizationUrl` and `tokenUrl` overrides inside
  `auth`.

## Test locally (ChatGPT desktop app)
1. Copy this folder to `~/.codex/plugins/monotype-fonts`.
2. Create `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "monotype-local",
  "interface": { "displayName": "Monotype (local)" },
  "plugins": [
    {
      "name": "monotype-fonts",
      "source": { "source": "local", "path": "./.codex/plugins/monotype-fonts" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity"
    }
  ]
}
```

3. Restart the ChatGPT desktop app, open the Plugins Directory, choose
   "Monotype (local)" and install.

## Before public submission
- Add `privacyPolicyURL` and `termsOfServiceURL` to `extensions.com.openai.interface`.
- Add official assets under `./assets/` and reference them as `composerIcon`,
  `logo` and `screenshots`.
- Confirm `brandColor` and `category`.
