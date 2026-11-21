# ClinMatch ChatGPT plugin (source folder)

This folder is the **upload ZIP source** for OpenAI’s plugin portal. It contains no secrets.

## Contents

- `plugin.json` — Agent Plugins manifest (listing copy, URLs, icon paths)
- `mcp.json` — production streamable HTTP MCP server (`https://clinmatch.io/api/mcp`)
- `assets/` — square PNG icons (`logo.png`, `icon.png`) derived from the app icon in `mobile/assets/icon.png`

## Package for upload

From the repository root:

```bash
./scripts/package-chatgpt-plugin.sh
```

This writes `dist/clinmatch-chatgpt-plugin-<version>.zip` (for example `dist/clinmatch-chatgpt-plugin-1.0.5.zip`) containing `plugin.json`, `mcp.json`, and `assets/`. A symlink `dist/clinmatch-chatgpt-plugin.zip` points at the versioned archive.

The script **fails** if any file under `chatgpt-plugin/` (except binary assets) still contains `PLACEHOLDER` or `TODO`. Use `--allow-placeholders` only for local test ZIPs that intentionally retain those markers.

Manifest copy (descriptions, prompts) must stay **read-only and non-booking** — no appointment, book, or request-page framing. Vitest guards in `src/lib/chatgptPlugin/__tests__/mcpNoBookingSurfaces.test.ts` include `plugin.json`.

## Before final submission

1. Confirm `plugin.json` `version` matches the release you are uploading (e.g. `1.0.5`).
2. Confirm `mcp.json` points at the production MCP URL (`https://clinmatch.io/api/mcp`).
3. Complete OpenAI **domain verification** for `clinmatch.io` (see `docs/chatgpt-app.md`).
