# Requirements checked 2026-10-01

- https://developers.openai.com/plugins/build/plugins — portable root manifests, discovery paths, remote HTTPS MCP.
- https://developers.openai.com/plugins/build/mcp-server — MCP tool/server guidance.
- https://developers.openai.com/plugins/build/auth — anonymous public stateless operations may use noauth; no OAuth/account system claimed.
- https://developers.openai.com/plugins/plugin-guidelines — individual operations, explicit annotations, privacy and narrow inputs.
- https://developers.openai.com/plugins/deploy/submission — initial ZIP includes MCP, identity/domain verification, five positive and three negative cases.
- https://developers.openai.com/plugins/deploy/submission-errors — current listing/archive/image limits.
- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://agent-plugins.org/schemas/1.0.0/mcp.schema.json

Official schema documents were fetched and validated with existing Ajv 2020; both passed. No legacy 2023 ai-plugin.json/OpenAPI package is used. Documentation currently conflicts on whether annotation justifications remain required: guidelines says no longer required while submission-errors still lists them. This package has explicit annotations; retain review rationale in READINESS and confirm portal behavior before submission.
