# MCP server

The project provides two transports over the same core logic:

- Local stdio (`src/stdio.js`) for development and unit/protocol checks.
- Remote Streamable HTTP (`src/worker.js`) using Cloudflare Agents SDK `createMcpHandler`.

## Local stdio

```bash
node src/stdio.js
```

The process accepts one JSON-RPC message per line and responds on stdout. Diagnostics go to stderr.

## Cloudflare Worker — Streamable HTTP

From this directory:

```bash
npm install
npx wrangler login
npx wrangler deploy
```

The Worker exposes the MCP endpoint at `POST /mcp` through `createMcpHandler`, and `GET /health` for a health response. `createMcpHandler` is Cloudflare's recommended handler for new stateless Streamable HTTP MCP servers.

After deployment, test the actual deployed revision using MCP Inspector with the Streamable HTTP transport. Verify initialize, tools/list, all tools/call operations, and error handling. Do not treat the earlier legacy JSON-RPC HTTP tests as proof that this updated transport has been deployed.

## MCP tools

- `validate_product_brief`
- `validate_production_output`
- `build_production_manifest`

## Notes

The stdio entrypoint imports only the shared core and remains dependency-free. The Worker entrypoint requires `agents`, `@modelcontextprotocol/server`, and `zod`. The Worker uses the stateless Streamable HTTP handler; no protocol-level session storage is configured. The service does not implement OAuth because its current tools process only user-supplied brief data and do not access private third-party accounts.
