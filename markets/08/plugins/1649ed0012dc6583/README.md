# theprintspace plugin (Creative Hub)

Skills that teach an assistant how to order fine-art prints, framing and mounting from theprintspace through the Creative Hub MCP server (`https://order.creativehub.io/api/v1/mcp`, OAuth sign-in with a Creative Hub account). The MCP server was entered in the submission portal ("With MCP") for v1.0.0; from v1.1.0 the bundle must also declare it (`.mcp.json`, referenced by `mcpServers` in the manifest — the portal matches it to the existing connection by exact URL and refuses a package that omits it). The bundle carries the manifest, the MCP declaration, icons and three skills:

- `order-a-print` — the end-to-end workflow: image first, size, finish (asked, not assumed), country, one-call preview + price, address last, explicit yes, saved card or payment link.
- `get-artwork-in` — the five ways to get an image into the library, best first.
- `check-an-order` — status, payment link recovery, invoices, tracking.

Source of truth for the tools and rules: `MCP.md` in the artful-gallery repository.
