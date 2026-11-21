# OwnerRez for ChatGPT

This repository packages the [OwnerRez MCP server](https://api.ownerrez.com/mcp) for ChatGPT and Codex. The server is hosted separately. This package contains manifests, OwnerRez brand assets, and an account workflow skill; it contains no credentials.

The portable plugin uses `plugin.json` and `mcp.json`. `.codex-plugin/plugin.json` and `.mcp.json` provide the Codex compatibility format. The package name is `ownerrez`.

`mcp.json` sets `baseScopes` to `["read", "full"]`. Without it ChatGPT requests `read` alone, and the OwnerRez consent page then grants View only with no choice. With both scopes the consent page lets the customer choose, with View and make changes preselected.

## Build

Run PowerShell 7 from the repository root:

```powershell
pwsh -File ./scripts/pack.ps1
```

The script validates the manifests, referenced files, listing fields, review case counts, and icon dimensions. It writes `dist/ownerrez-chatgpt-plugin-<version>.zip`, with the version from `plugin.json`. The ZIP contains the portable manifests, assets, skill, README, and license. `dist/` is ignored by Git.

Tool names in the skill and the review test cases come from `agent-catalog/catalog.json` in `ownerrez/orez`. Renaming a tool there means a new ZIP.

## Review details entered in the portal

The demo account credentials stay out of this repository. The account must sign in from outside OwnerRez's network with no two-factor step, and its data must include at least one upcoming booking with a balance due, one open inquiry, one quote, and a guest whose last name replaces `<demo guest last name>` in the third positive test case. Remove the VIP tag from the next upcoming booking before each review submission.

The tool scan asks for a justification of each annotation. All nine tools set `openWorldHint: false` because each one reaches only the OwnerRez account the user authorized.

| Tool | readOnlyHint | destructiveHint | Justification |
|---|---|---|---|
| `entity_list` | true | false | Lists bookings, properties or guests from the connected account and changes nothing. |
| `entity_get` | true | false | Reads one record from the connected account by ID and changes nothing. |
| `search` | true | false | Searches the connected account's bookings, guests and properties by text and changes nothing. |
| `fetch` | true | false | Reads the record behind a `search` result and changes nothing. |
| `schema` | true | false | Returns the OwnerRez API v2 operation list and field shapes; reads no account data and changes nothing. |
| `api_get` | true | false | Sends only GET requests to the OwnerRez API v2 for the connected account and changes nothing. |
| `api_write` | false | true | Sends POST, PATCH, PUT or DELETE requests to the OwnerRez API v2, which create, change or delete account data. Refused unless the connection has Full access, which the customer chooses on the OwnerRez consent page and can lower to Read-only under Settings > Connected Apps. |
| `api_docs_search` | true | false | Searches OwnerRez's own API v2 documentation index; reads no account data. |
| `support_docs_search` | true | false | Searches OwnerRez's published support articles; reads no account data. |
