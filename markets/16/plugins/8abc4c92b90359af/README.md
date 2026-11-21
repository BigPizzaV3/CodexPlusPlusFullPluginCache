# WOWSERU AI AFFILIATE STORYBOARD

Independent plugin project by **WOWSERU**.

This package converts product briefs into an AI UGC affiliate production plan. It is separate from WOWSERU AI ANIMASI and contains no animation-plugin workflow.

## Package contents

- `plugin.json` — Agent Plugins 1.0 manifest and listing metadata.
- `mcp.json` — public Streamable HTTP MCP connection for the deployed Cloudflare Worker.
- `skills/ai-affiliate-storyboard/SKILL.md` — core workflow instructions.
- `mcp-server/` — local stdio server and Cloudflare Worker Streamable HTTP server.
- `test/` — five positive and three negative acceptance scenarios.
- `submission/` — draft listing, release notes, and reviewer materials.

## Local MCP core tests

Requirements: Node.js 18 or later. From `mcp-server/` run:

```bash
npm test
npm start
```

The stdio entrypoint remains dependency-free and is intended for local protocol/core testing. The root `mcp.json` is configured for the public remote MCP endpoint, not local stdio.

## Cloudflare Worker

The Worker uses Cloudflare Agents SDK `createMcpHandler` and the Model Context Protocol server SDK to expose Streamable HTTP at `/mcp`. The health route is `/health`. From `mcp-server/` run:

```bash
npm install
npx wrangler login
npx wrangler deploy
```

The configured public endpoint is `https://ai-affiliate-storyboard.infowowseru.workers.dev/mcp`. The deployed Worker passed production checks on 2026-11-01: `GET /health`, MCP `initialize`, `tools/list`, and `tools/call` for all three tools (`validate_product_brief`, `validate_production_output`, and `build_production_manifest`). The deployed Cloudflare version ID recorded during release was `4b31e74d-0fb1-4101-8ac5-ed24c8fc0b60`. Health route: `https://ai-affiliate-storyboard.infowowseru.workers.dev/health`.

The root `mcp.json` points to this public Streamable HTTP endpoint. The local stdio entrypoint remains available for development and core testing.

## Scope and limitations

The plugin produces prompts and structured production plans. It does not render images or videos, access product links without an enabled browsing capability, or verify product claims beyond supplied/retrieved evidence.

Public submission still requires completing the OpenAI portal workflow, domain verification, developer identity verification, required listing/review metadata, and a real reviewer demo recording.


## Submission identity

This archive is a **new plugin identity** (`wowseru-ai-affiliate-storyboard-remote`, version `1.0.0`). Submit it using the portal flow to create a new plugin draft. Do not upload it as a replacement/update to the existing plugin whose MCP server was configured as a command/stdio server. The remote MCP server is declared in the root `mcp.json` as Streamable HTTP and points to the already deployed, production-tested Cloudflare Worker.


## v1.0.5 annotation verification
The MCP `tools/list` response must expose an `annotations` object on each tool with explicit boolean values: `readOnlyHint: true`, `destructiveHint: false`, and `openWorldHint: false`. The automated regression test asserts these exact values. After updating the repository, deploy the Worker and re-run the OpenAI tool scan; changing this ZIP alone does not update the deployed endpoint.
