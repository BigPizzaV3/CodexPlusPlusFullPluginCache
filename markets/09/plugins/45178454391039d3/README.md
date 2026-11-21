# Zid Store Workspace

This package connects ChatGPT to the Zid merchant MCP service and its global
workspace app. The workspace supports English and Arabic and has ten tabs:
Home, Orders, Products, Abandoned Carts, Loyalty, Inventories, Shipping,
Discounts, Storefront and Store areas. The Orders and Products tabs can update
order statuses and products; Store areas lists what the plugin covers and sends
sample requests to the conversation; the other tabs are overviews.

The model gets the 21 earlier reviewed Zid tools and the `zid_<area>` tools of
the v2 surface (every toolset but money; see [scopes.md](scopes.md) for what is
left out). Both are listed until OpenAI approves the v2 tools; a later release
unlists the earlier ones and keeps them callable for existing chats.

The `OpenStoreWorkspace` tool registers Zid's global workspace entrypoint in the
ChatGPT sidebar after installation and merchant sign-in. Merchants do not need
to pin Zid from Explore.

Private browser previews use a separate developer flow: register the task
tunnel as a developer MCP app and attach it in Plugin Creator. Keep the
generated `.app.json` mapping as a private override; it is not part of the
merchant installation flow or portable package.

The portable `mcp.json` points to Zid's stable public HTTPS endpoint. Build the
portable ZIP with the repository-local default output:

```bash
node scripts/package-plugin.mjs
```

This writes `dist/zid-chatgpt-plugin.zip`. For a private local integration test,
run:

```bash
node scripts/package-plugin.mjs --url https://your-task-tunnel.example/mcp \
  --output /path/to/test-plugin.zip
```

The command writes a test-only package outside this folder. The override never
changes the source manifest or the portable package. Use `--output` to choose a
different output path.

The package contains no access tokens, Zid credentials, hooks, embedded app
references, or store data. Merchant sign-in and consent use the remote MCP OAuth
flow. Order and product changes made in the workspace show a confirmation step before they apply.
Changes the server marks for approval (most deletes, bulk changes, publishing
and sends, `src/registry/registry.ts`) through the `zid_<area>_manage` tools
apply only with the `plan_id` that `preview_change` returns.
Each authorization is bound to the signed-in Zid user ID and calls Zid with that
user's own tokens, so several staff members can connect the same store, each
with their own dashboard permissions.

OAuth permissions are listed in [scopes.md](scopes.md). Read access to the
overview analytics is limited to aggregate sales, order, visit, and conversion
metrics for a requested range of up to 90 days.

## Contents

- `plugin.json`: portable plugin manifest and ChatGPT presentation metadata.
- `mcp.json`: remote Streamable HTTP MCP server configuration.
- `skills/`: workflows for common store operations, one folder per skill with
  `SKILL.md` and optional `references/`. `test/plugin-skills.test.ts` fails when a
  skill names a tool or action the plugin does not list.
- `assets/zid-icon.png`: the square Zid mark for the listing and composer, in
  light and dark themes.
- `publication.translations["ar-SA"]`: the Arabic subtitle and description. The
  directory shows one display name in every language, so it is "Zid | زد".

The sidebar app HTML is built from `../web/` and served by the MCP resource; it
is not copied into this package.
