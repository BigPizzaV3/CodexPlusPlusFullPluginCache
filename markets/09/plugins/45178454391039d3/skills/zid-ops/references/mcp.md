# MCP connections

## Which connection

| Client | How it connects |
| --- | --- |
| ChatGPT, through the Zid plugin | Signs in to Zid; nothing to paste. A tool answering `insufficient_scope` means the connection predates that tool: disconnect and reconnect Zid in the plugin's settings. |
| Claude, Cursor, Windsurf, Codex, n8n, Make, scripts | The store's personal MCP URL, from the Zid AI Connector app (أدوات الذكاء الاصطناعي) in the Zid dashboard. |

The personal URL works like a password: anyone holding it can run the store's
tools. It goes into the client's settings, never into a chat, a shared workflow
export or a screenshot. **Rotate secret** on the same page replaces it; every
client using the old URL stops working until it gets the new one.

## URL forms

Write the base as `<MCP_URL>` = `https://zam-mcp-server.zid.sa/mcp/<token>`.

| URL | Serves |
| --- | --- |
| `https://zam-mcp-server.zid.sa/mcp/v2/<token>` | The `zid_*` tools for store, reports, orders, products, customers, promotions and content |
| `…/mcp/v2/<token>?toolsets=shipping,inventory` | Adds the named areas: `shipping`, `inventory`, `catalog`, `campaigns`, `payments`, `settings`, `account`, `design`, `pos`, `marketplaces` |
| `…/mcp/v2/<token>?toolsets=all` | Every area above. The Zid skills use tools from `shipping`, `inventory`, `catalog`, `campaigns`, `payments`, `settings` and `account` |
| `https://zam-mcp-server.zid.sa/mcp/<token>` | Whichever tool set the store is on; older workflows built on capitalized tool names (Orders, Products) use this one |

Fewer areas keep the tool list short, which helps smaller models pick the right
tool. Transport is streamable HTTP at the URL itself.

## Client settings

- **Cursor**: MCP settings → add a server: `{"mcpServers": {"Zid": {"url": "<MCP_URL>"}}}`.
- **Windsurf**: Cascade → Add custom server: `{"mcpServers": {"Zid": {"serverUrl": "<MCP_URL>"}}}`.
- **Claude**: add a custom connector with the URL (a Claude organization owner adds it for the organization).
- **Codex**: in `~/.codex/config.toml`, a `[mcp_servers.zid]` table with `url = "<MCP_URL>"`.
- **n8n**: an AI Agent node with an MCP Client Tool node: Endpoint `<MCP_URL>`,
  Server Transport HTTP Streamable, Authentication None (the token is in the
  URL). Under Tools to Include, pick only the tools the workflow needs.
- **Scripts**: the MCP SDK's streamable HTTP client (`@modelcontextprotocol/sdk`
  in TypeScript, `mcp` in Python) with the URL read from an environment variable.

## How the tools behave

- `zid_<area>` tools read; `zid_<area>_manage` tools change the store. Every
  call names an `action`.
- A wrong or missing argument returns `invalid_arguments` with `missing` and
  `unexpected`; correct the call from those lists.
- A change that needs approval returns `confirmation_required` with the plan and
  a `plan_id`. Show the plan to the user; after they approve, the call with the
  same arguments and that `plan_id` applies it: once, within 10 minutes. `plan_used`, `plan_expired` and `plan_mismatch` come
  with a fresh `plan_id`. Repeating an applied call repeats the change, so check
  whether the first call landed before retrying.
- Lists are paged: pass `page` and the page size the action takes, and keep
  reading until a page comes back short.
- A `429` comes from Zid and names the seconds to wait; wait that long and run
  bulk work one call at a time.
- Refunds, payment status, wallet credits and debits, payment links, shipment
  cancellations, Zid plans and purchases, the app and theme markets, and
  anything that needs an OTP or API key stay in the Zid dashboard.
