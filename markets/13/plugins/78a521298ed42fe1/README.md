# Just Travel portable plugin package template

The package layout follows the current OpenAI plugin and Skills documentation:

- `plugin.json` — portable plugin metadata.
- `mcp.json` — one Streamable HTTP MCP server entry.
- `skills/*/SKILL.md` — Skills with YAML `name` and `description` frontmatter.
- `evals/` — local prompt corpus and offline trace evaluator; this is project
  evaluation material, not a listing metadata extension.
- `assets/logo.png` — square listing and composer icon (the site's arrow mark,
  padded to 300x300).

References for this layout:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://agent-plugins.org/schemas/1.0.0/mcp.schema.json

`mcp.json` points at the production endpoint `https://mcp.justtravel.io/mcp`.
Run the standalone ASGI app locally from the repository root with
`venv\Scripts\python.exe -m uvicorn api.chatgpt.runtime:app --port 8001`.
The default `CHATGPT_MCP_ENABLED=false` serves an empty tool registry; the
standalone app is not mounted by `api.main`. The OAuth bridge and the
`/connect/chatgpt` consent page are described in `docs/chatgpt-integration.md`.

`plugin.json` carries the OpenAI listing metadata under
`extensions.com.openai.interface`: display name, subtitle, long description,
category, website, support, privacy and terms URLs, three starter prompts,
brand colors, and the icon. Keep the long description limited to what the nine
MCP tools actually do (search, validate, save and load trips); bookings happen on
the provider's site, not inside ChatGPT. OpenAI's upload check rejects pricing,
subscription offers and promotions in the listing, so leave out words like
"free", plan names and price claims. Reviewer credentials and test cases go
in the OpenAI Platform dashboard, never in this package.

Both manifests pass Draft 2020-12 JSON Schema validation against the referenced
schemas. This confirms manifest structure only. Production runtime settings,
migration state, and public activation are tracked in the go-live checklist in
`docs/chatgpt-integration.md`.
