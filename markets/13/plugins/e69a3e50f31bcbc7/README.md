# CurrencyGo plugin package

This package connects ChatGPT or Codex to the existing CurrencyGo MCP server at https://currencygo.app/mcp. It does not deploy a website or start a server on the user's computer. No CurrencyGo sign-in, API key or local dependencies are required.

## Import

Before importing this domain update, connect `currencygo.app` to the existing Vercel project and verify that https://currencygo.app/ and its MCP endpoint are reachable over HTTPS. Importing the package does not configure DNS or Vercel. Keep the existing connection until the new domain is ready.

Upload CurrencyGo-Plugin.zip to the plugin importer. The archive includes a portable Agent Plugins manifest, a Codex compatibility manifest, the remote MCP connection, one currency-conversion skill and the existing CurrencyGo logo.

For a public submission involving the remote server, use the portal's With MCP flow. This archive provides package and listing metadata; it is not evidence of review approval. Do not upload CurrencyGo-Ready.zip here: that separate archive contains the Next.js project for GitHub and Vercel.

## Test after importing

Start a new conversation and ask: Open the currency converter in my local currency. Confirm that the custom card actually renders, then edit an amount, manually select a currency and swap the pair. Example: Convert 250 USD to GBP with a 2% exchange fee.

The deployed server remains the source of the interface and tools. Updating this package alone does not update that server.

Keep the existing app's registered MCP URL, `https://currencygo.app/mcp`, unchanged. If it redirects to `www`, connect the root domain directly to Production in Vercel rather than changing this package's MCP URL.

## Public submission preparation still required

- Run the included five positive and three negative review cases against the final ChatGPT version; they are expectations, not recorded passes.
- Record and provide a reviewer-accessible demo. No recording URL has been invented or included.
- Confirm intended country availability in the portal; country targeting is intentionally omitted.
- Review the optional device-location button and coordinate-based tool inputs against current OpenAI location requirements before public submission.
- Complete applicable developer/domain verification, scans and declarations in the portal. No account IDs, reviewer credentials or legal attestations are packaged.

Website: https://currencygo.app/
Privacy: https://currencygo.app/privacy
Terms: https://currencygo.app/terms
Support: https://currencygo.app/support
