# DUE Brand Deal Commercials — plugin package

Public, no-account plugin with exactly one MCP server: `https://brieftopaid.app/mcp-public` (only `check_brand_deal_commercials`). Authentication `none` is declared in `mcp.json`; review cases are in `plugin.json`.

## Contents
- `plugin.json` — portable identity at the root; OpenAI presentation, `skills` and `mcpServers` pointers under `extensions.com.openai`.
- `mcp.json` — the single streamable-http server.
- `skills/brand-deal-commercials/SKILL.md` — workflow for checking pasted terms.
- `assets/due-icon-512.png` — DUE icon (512×512 PNG).
- `REVIEW.md`, `SUBMISSION.md`.

## Package

```sh
cd distribution/due-brand-deal-commercials && zip -X -r ../../public/downloads/due-brand-deal-commercials-0.2.3.zip plugin.json mcp.json skills assets README.md REVIEW.md SUBMISSION.md
```

No credentials, hooks or app IDs belong in this package.
