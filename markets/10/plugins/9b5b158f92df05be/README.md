# Peskio ChatGPT plugin

Package for the ChatGPT / Codex plugin directory. Server: `https://peskio.com/mcp` (apps/web/src/app/mcp,
dark unless `MCP_ENABLED=1`). Spec: `docs/superpowers/specs/2026-09-30-chatgpt-plugin-mcp-design.md`.

- `plugin.json` — portable manifest; OpenAI presentation under `extensions.com.openai.interface`.
- `mcp.json` — the remote MCP server (discovered automatically at the package root). There is deliberately no
  `.app.json`: ZIPs with app references cannot be submitted (submission docs, 2026-10-02); the app is set up in the dashboard.
- `skills/` — `plan-fishing-trip`, `check-tides` (plan B adds `plan-dive`).
- `test-prompts.md` — golden set; run before every submission.
- `assets/` — icon, logo, screenshots (official brand assets only).

OpenAI documents no local validator CLI (submission docs, checked 2026-10-02); the checks are the portal's own
upload validation and `apps/web/test/plugin-package.test.ts`, which pins the file names (`plugin.json`,
`mcp.json`, `skills/*/SKILL.md`, `assets/icon.png`, `assets/logo.png`). If Codex's `@plugin-creator` skill is available,
run it against this folder as a dry run and reconcile any field it renames into `plugin.json`.
