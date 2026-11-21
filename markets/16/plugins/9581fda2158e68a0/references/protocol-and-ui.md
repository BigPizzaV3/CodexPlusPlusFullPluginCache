# MCP and MCP Apps current implementation reference

## Authoritative sources — check fresh before implementation
- MCP specification: https://modelcontextprotocol.io/specification/
- MCP TypeScript SDK **v2 current**: https://ts.sdk.modelcontextprotocol.io/v2/
- MCP v2 first server: https://ts.sdk.modelcontextprotocol.io/v2/get-started/first-server
- MCP Apps extension and examples: https://github.com/modelcontextprotocol/ext-apps
- MCP Apps UI quickstart: https://github.com/modelcontextprotocol/ext-apps/blob/main/docs/quickstart.md
- MCP Apps API: https://apps.extensions.modelcontextprotocol.io/
- OpenAI MCP Apps guide: https://developers.openai.com/plugins/build/app-quickstart

## Version compatibility
As of November 2026, `@modelcontextprotocol/server` is the stable v2 TypeScript server package and implements newer MCP specs. v1 used `@modelcontextprotocol/sdk/server/mcp.js`; do not mix those import paths across versions. Check installed versions and `@modelcontextprotocol/ext-apps` compatibility before generating code.

For a new v2 local server, the documented pattern is `McpServer` from `@modelcontextprotocol/server`, `serveStdio` from `@modelcontextprotocol/server/stdio`, Zod v4, and `server.registerTool(...)`. Remote servers should use the documented Streamable HTTP serving pattern, not old SSE templates.

## UI requirements
- Optional MCP Apps UI via `ui://` resource; provide useful tool-only result even without host UI support.
- Link tool to resource using `_meta.ui.resourceUri` and register matching resource. The current official ext-apps helpers are `registerAppTool`, `registerAppResource`, `RESOURCE_MIME_TYPE`.
- HTML MIME profile: `text/html;profile=mcp-app`. Check host capability negotiation.
- Use documented bridge/postMessage communication. Do not assume direct parent DOM access.
- Declare narrow connect/resource CSP domains; no blanket wildcards.
- Authorization is always enforced by server, including tools the UI calls.

## Tiny linkage shape (illustrative, not a complete server)
```ts
const resourceUri = 'ui://tasks/view.html';
registerAppTool(server, 'list_tasks', {
  title: 'List tasks',
  description: 'List current tasks',
  inputSchema: z.object({}),
  _meta: { ui: { resourceUri } },
}, async () => ({ content: [{ type: 'text', text: JSON.stringify({ tasks: [] }) }] }));
registerAppResource(server, resourceUri, resourceUri,
  { mimeType: RESOURCE_MIME_TYPE },
  async () => ({ contents: [{ uri: resourceUri, mimeType: RESOURCE_MIME_TYPE, text: html }] }));
```
Confirm actual API compatibility with installed libraries and run a real MCP client test before using this in production.
