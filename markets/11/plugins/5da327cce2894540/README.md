# Overview plugin source

Contains the portable manifest, brand asset and data interpretation skill. The remote MCP implementation lives in `src/server/plugin` and the existing Next.js app's `/api/mcp` route. See [deployment instructions](../../docs/operations/public-chatgpt-plugin.md).

This source is not yet an installable remote-data release: a verified deployed endpoint is required. After deployment verification, run `npm run plugin:package -- --endpoint <verified HTTPS endpoint>` to produce a separate package containing `mcp.json`. The script checks MCP initialization/tool discovery before packaging. It does not upload, submit or publish the plugin.

Publisher verification, support/privacy/publication metadata and actual ChatGPT connection acceptance remain separate release steps. The source implements the approved shared allowance of 40 calls per user per 12 hours; public review remains pending.
