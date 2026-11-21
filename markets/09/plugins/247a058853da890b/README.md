# AdStellar plugin for ChatGPT and Codex

A portable [Agent Plugins](https://developers.openai.com/plugins/) package that
connects ChatGPT and Codex to the production AdStellar MCP server at
`https://app.adstellar.ai/api/mcp` and bundles four skills for the main
workflows (ad copy, creative generation, performance analysis, launch drafts).

The package contains no server code. Tools, authentication and tenant scoping
live in `apps/web/lib/mcp/**` and `apps/web/pages/api/mcp.ts`; this folder is
only the manifest, the MCP server mapping and the skills.

## Layout

```
plugins/adstellar/
├── plugin.json      # identity + OpenAI install-surface metadata
├── mcp.json         # streamable-http mapping to app.adstellar.ai/api/mcp
├── assets/          # composer icon (square) and logo
└── skills/<name>/SKILL.md + agents/openai.yaml
```

`.agents/plugins/marketplace.json` at the repo root exposes this folder as a
local marketplace so the plugin shows up in the Plugins Directory of the
ChatGPT desktop app when this repo is open in Work mode.

## Test locally

1. In ChatGPT open Settings > Security and login and turn on Developer mode.
2. Go to chatgpt.com/plugins, press the plus button and register the MCP server
   with the URL `https://app.adstellar.ai/api/mcp`. ChatGPT discovers the OAuth
   metadata, registers itself via dynamic client registration, and sends you to
   the AdStellar consent screen to pick a team and scopes.
3. Copy the connection id from the browser URL (it starts with
   `plugin_asdk_app`). To bind this package to that registered connection, add
   a root `.app.json` produced by `@plugin-creator` for that id and point
   `extensions.com.openai.apps` at `./.app.json`.
4. Restart the ChatGPT desktop app, install "AdStellar" from the local source
   in the Plugins Directory, and try the starter prompts in `plugin.json`.

## Submit to the directory

The portal (developers.openai.com/plugins/deploy/submission) needs, beyond this
package:

- **Domain verification.** The portal issues a token that must be served at
  `https://app.adstellar.ai/.well-known/openai-apps-challenge`. Set the
  `OPENAI_APPS_CHALLENGE_TOKEN` env var in Vercel to that exact value; the route
  returns 404 while it is unset.
- **Demo credentials.** A working AdStellar account with no MFA, email or SMS
  step, on an active plan, with at least one connected ad account and some AI
  credits, so reviewers can exercise every tool.
- **Test cases.** At least 5 positive and 3 negative prompts. The starter
  prompts and each skill's "Do not" section are a good source.
- **Metadata.** The category, capabilities and legal URLs in `plugin.json` are
  the defaults; adjust them in the portal if the directory offers a better
  category than Productivity.

## Validate before submitting

The manifests must satisfy the Agent Plugins 1.0.0 JSON schemas (the portal
rejects packages that don't). From the repo root:

```bash
curl -sO https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
curl -sO https://agent-plugins.org/schemas/1.0.0/mcp.schema.json
npx -y ajv-cli@5 validate --spec=draft2020 -s plugin.schema.json -d plugins/adstellar/plugin.json
npx -y ajv-cli@5 validate --spec=draft2020 -s mcp.schema.json -d plugins/adstellar/mcp.json
```

`apps/web/__tests__/integrations/chatgpt-plugin.test.ts` checks that every tool
and parameter a skill mentions exists on the server, so a tool rename fails CI
before it can ship a stale skill.

Tool metadata reviewers check (titles, `annotations`, per-tool
`securitySchemes`) is emitted by the server from `apps/web/lib/mcp/protocol.ts`
and each tool definition; changing a tool there changes what the portal scans.
