# Ventrata

Manage your Ventrata account through your AI assistant.
The plugin supports authorized backoffice staff administering products,
bookings and reports. This is not a consumer storefront or booking service:
customers do not use this plugin to shop, check out or make bookings.
One server at `https://api.ventrata.com/mcp` exposes Ventrata's Resource
operations across available regions using your existing Ventrata permissions,
including bookings, backoffice purchases, balance collection, refunds and
stored-card references, while excluding passwords, PINs, API secrets, raw card
data and credential-bearing payloads (configure credentials in Dashboard).

In Dashboard's user menu, choose **Copy AI connection prompt** and paste it into
your AI assistant. The [setup guide](https://api.ventrata.com/graphql/docs/mcp)
covers ChatGPT, Claude and Antigravity installation, read-only connections,
domain toolsets, registered OAuth clients, permissions, data handling and revocation.
Use your own Ventrata sign-in; never put credentials in chat or project files.

Use the [ChatGPT archive](https://api.ventrata.com/mcp/ventrata-chatgpt.zip),
[Claude archive](https://api.ventrata.com/mcp/ventrata-claude.zip) or
[Antigravity archive](https://api.ventrata.com/mcp/ventrata-antigravity.zip) for your assistant.
All three select the full catalogue with `?toolsets=all` and contain Ventrata Ltd
metadata, the logo and MCP configuration, with no
skills or executable code. ChatGPT web needs an archive referencing your own
cloud MCP connection; Claude web needs a permitted workspace connector;
Antigravity loads `plugin.json` and `mcp_config.json` from your plugins directory.
Follow the setup guide above. Host interfaces may override the author or logo display.
The server supplies its own workflow instructions.

For server-enforced read-only access, connect to `https://api.ventrata.com/mcp?readonly=true`
(or narrow your client scopes to `mcp:read`). By default the server exposes the core
`catalog`, `sales`, `distribution` and `organization` toolsets; pass `?toolsets=`
(including `operations`, `finance`, `marketing`, `pos`, `cms` or `all`) or
`?resources=` to select a custom catalogue.

Clients must support sessionless MCP 2026-07-28 and the `Mcp-Param-Region` header
mapping. Account users and partner administrators authenticate through WorkOS;
account users require **MCP Enabled** on their user profile. Partner-admin access is
unaffected by that flag; staff use the internal API. Deployment and OAuth
configuration are documented in Dashboard's `docs/mcp.md`.

Start with **Show the Ventrata suppliers I can access in each region.** The
[agent guide](https://api.ventrata.com/graphql/docs/agents) explains queries,
reports and safe recovery of writes. MCP exposes no bulk actions or preview tools.
Restorable records have archive/restore tools; permanent deletions use delete
tools, and transaction voiding preserves the transaction's history.
Package components use `package_include` / `package_includes` tool names,
including `create_package_include`, `archive_package_include` and
`restore_package_include`. Weekday and month enums use full names such as
`MONDAY` and `JANUARY`.
For help, visit
[Ventrata support](https://support.ventrata.com/en/).
