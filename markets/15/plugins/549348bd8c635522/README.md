# FiraCrypto ChatGPT plugin

The plugin provides read-only, evidence-based security checks for public EVM token contracts and public wallet addresses. It does not connect to a wallet, take payments, sell reports, trade assets or give investment advice.

## Endpoint

`https://www.firacrypto.com/mcp` is a stateless streamable HTTP MCP server without sign-in. Code: `src/app/mcp/route.ts` and `src/lib/mcp/server.ts`.

The tools use GoPlus Security data, the same source used by the website's free token and address checks. They return a source and checked time. A missing record produces no score. The endpoint rate limits requests and sends only the public address and chain to GoPlus; temporary request metadata is described in the privacy policy.

## Review and release

1. Verify the production endpoint and the four listing URLs in `plugin.json`.
2. Connect the MCP server in ChatGPT, scan tools and run the positive and negative test cases in `plugin.json`.
3. Upload the complete `plugin/` directory as a ZIP through the OpenAI developer portal, complete domain verification and submit for review.
4. Approval does not publish automatically. Publish the approved version in the portal before adding a public listing link to the website.
