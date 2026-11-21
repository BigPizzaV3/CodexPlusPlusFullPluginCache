# BlindOracle Agent Trust — OpenAI plugin package (source)

Portable Agent Plugins layout (developers.openai.com/plugins/build/plugins, read 2026-10-04).
Build + lint + ZIP with `python3 scripts/openai_plugin_package.py build` from the project root;
the ZIP lands in `dist/openai-plugin/` (gitignored). Operator runbook: `../SUBMISSION.md`.

The MCP server it points at is the live `/v1/mcp/chatgpt` surface
(`distribution/mcp_chatgpt_routes.py`, profile `config/mcp_profiles/chatgpt.json`,
`listing_mode=directory`). Nothing in this package is a secret.
