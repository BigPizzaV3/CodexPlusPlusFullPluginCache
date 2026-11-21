# Salsmart portable plugin

This package connects a compatible host to the free, read-only Salsmart MCP service at `https://salsmart.com/mcp`. It contains a portable root `plugin.json`, `mcp.json`, listing images and review case plans.

**Status:** prepared for testing and directory submission. This package has not been approved or published in the OpenAI Plugins Directory. Installing the package manually does not mean it has directory approval.

Package version 1.0.1 clarifies the grocery-comparison listing text and uses the directory's **Other** category. Official directory listings for Instacart and Klarna Shopping Search use that category. Product comparison and source-checking behavior are unchanged.

## What it does

- `search_products`: search by Hebrew or English product name, manufacturer or barcode; return up to 20 matching products and actual branch offers in ILS.
- `get_data_status`: report current source coverage, fresh/stale counts and source timestamps.
- An optional Hebrew MCP Apps interface shows search results inside supporting hosts. Text-only MCP clients still receive the results.

No sign-in, API key or payment is required for these MCP tools. Search shares the public website's fair-use allowance: 60 requests per minute and 500 per UTC day per network address. A host's shared network address can share that allowance across users.

Coverage is partial. A returned retailer price is not a live stock check or a nationwide lowest-price guarantee. Preserve unknown fields, cite source URLs, and distinguish retailer price-change time from fetch time.

## Connection and authentication

Use Streamable HTTP with endpoint `https://salsmart.com/mcp`. Choose **No authentication** in the OpenAI submission portal. This package contains no credentials, fixed authorization headers or OAuth configuration.

The currently published canonical `mcp.schema.json` rejects server-level extension objects. Therefore `mcp.json` omits the documentation's optional `extensions.com.openai.auth` declaration and stays valid against the canonical schema. No-auth is configured in the portal.

## Review materials and remaining steps

`plugin.json` includes exactly five positive and three negative case plans. Expected behavior describes what should happen; it is not a record that a human review run passed. Run the cases in the target ChatGPT host and record actual outcomes before submission.

The three included screenshots are actual 1168×900 captures of the production Salsmart preview host at `https://salsmart.com/mcp-preview`, showing live milk, coffee and pasta searches. They demonstrate the Salsmart widget and MCP service; they are not captures of ChatGPT or Claude and do not establish compatibility certification or approval by either platform. Package copies are encoded as PNG; source captures remain unchanged.

`review.demo_recording_url` points to an actual short production-preview screencast at `https://salsmart.com/agent-demo/mcp-preview.mp4`. It demonstrates the widget flow, not execution of all eight review cases in the target ChatGPT host. Remaining review work includes domain verification using the portal's exact challenge, verified developer identity, checking listing metadata, running the case plans in the target host, and a complete review walkthrough when target-host access is available. Then upload, resolve automated findings, submit, and publish only after approval.

Support: https://salsmart.com/support · Privacy: https://salsmart.com/privacy · Terms: https://salsmart.com/terms · Connection help: https://salsmart.com/connect

## Rebuild

From the Salsmart project directory, run `node scripts/package-openai-plugin.mjs`. The script validates both JSON files against fetched canonical schemas, renders the owned favicon to 512×512 PNG, includes up to three real captures from `public/agent-screenshots` as PNG assets at least 1000 pixels wide, and creates `public/downloads/salsmart-plugin.zip` with manifests at ZIP root. It checks dimensions and encoded image size, and does not alter the source captures. Use `--offline` to validate against previously saved schema copies.
