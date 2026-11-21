# BudgetSync plugin package

This directory uses the current portable Agent Plugins root format. `mcp.json` points at the locally verifiable development endpoint. It contains no credentials and no fabricated OpenAI registration IDs.

Start the server, validate it with Inspector, then build a deployment-specific private package:

```sh
PUBLIC_MCP_URL=https://YOUR_VERIFIED_HOST/mcp npm run mcp:package
```

The packaging script writes `dist/budgetsync-plugin/budgetsync` and a ZIP, verifies `/health` at that host, and replaces only the copied endpoint. Install that private package through the appropriate local plugin source, or register the verified remote MCP connection in ChatGPT developer mode. Public submission requires approved privacy/support URLs, publisher metadata and OpenAI review; no upload or publication is performed by this repository.

Available to every BudgetSync account, including Free. No paid subscription is required. Sign-in and consent are required to read your accessible budgets.
