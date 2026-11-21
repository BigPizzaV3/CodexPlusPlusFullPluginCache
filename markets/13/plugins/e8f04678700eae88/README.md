# QuotedPart plugin for Claude, ChatGPT and Codex

Price a CNC machined part from your AI assistant. Give it a STEP/IGES model or a PDF
drawing (or a link to one), a material and a quantity, and the QuotedPart tools price it with
your own shop's rates and return a price breakdown (material, machining, setups, programming,
finishing). Each estimate is saved as a quote in your QuotedPart account, and its link opens
the quote there, where you can adjust it and send it.

It needs an existing QuotedPart account, linked once: in Claude Code run `/mcp`, pick
`quotedpart` and choose Authenticate, then sign in to QuotedPart in the browser and allow it.
To unlink, open Integrations in QuotedPart and disconnect it under AI assistants.

## Install

```
/plugin marketplace add Helios-One-Oy/quotedpart-plugins
/plugin install quotedpart@quotedpart
```

or in one step on Claude Code 2.1.275 or later:

```
/plugin install quotedpart --marketplace Helios-One-Oy/quotedpart-plugins
```

## Codex and ChatGPT

The same folder is an Agent Plugins package (`plugin.json`, `mcp.json`, `skills/`), so Codex
installs it from this repo:

```
codex plugin marketplace add Helios-One-Oy/quotedpart-plugins
codex plugin add quotedpart@quotedpart
```

Or add only the MCP server: `codex mcp add quotedpart --url https://quotedpart.com/mcp`
(see `codex/config.toml`). Then link your account with `codex mcp login quotedpart`, which
opens QuotedPart's sign-in in the browser.

ChatGPT and other MCP clients that connect to `https://quotedpart.com/mcp` ask you to sign in
to QuotedPart the same way:

- Claude (web and desktop): https://claude.ai/customize/connectors → **Add custom connector** → `https://quotedpart.com/mcp` → **Connect**
- ChatGPT: https://chatgpt.com/plugins → **+** → **Add custom MCP server** → `https://quotedpart.com/mcp`, auth **OAuth** → sign in

Accounts on quotedpart.com can be linked; accounts on the Finnish site (fi.quotedpart.com) can't yet.

## Tools

| Tool | What it does |
| --- | --- |
| `list_shops` | Your shop: name, currency, units, and the rates, materials and markup it prices with |
| `list_materials` | Your shop's materials, optionally for one process |
| `estimate_price` | Price a STEP/IGES model and/or PDF drawing, saved as a quote in your account: cost lines, price breaks, lead time, quote link |
| `get_quote` | Current state of a quote (for example after a drawing read finishes) |
| `update_estimate` | Re-price a part on a quote with another material, quantity or process (on a quote with several parts, name the part or its line number) |
| `create_upload` | Upload URL for files too large to send inline |

The bundled `quote-a-part` skill describes the order to use them in.

## Server

The plugin connects to the hosted QuotedPart MCP server over streamable HTTP. To point
it at another server (a local one while developing), set `QUOTEDPART_MCP_URL` before
starting Claude Code:

```
QUOTEDPART_MCP_URL=http://127.0.0.1:8787/mcp claude
```

Codex does not expand variables in a plugin's `mcp.json`, so override the URL in config instead:

```
codex -c 'mcp_servers.quotedpart.url="http://127.0.0.1:8787/mcp"'
```

`estimate_price` fetches files from links (open-world), so Codex asks before calling it. A
non-interactive `codex exec` cannot ask; allow it up front with
`-c 'mcp_servers.quotedpart.tools.estimate_price.approval_mode="approve"'`. A local file reaches the server through `create_upload` and an HTTP PUT, so
`codex exec` also needs network access: `--sandbox workspace-write -c sandbox_workspace_write.network_access=true`.
`codex exec` cannot open a sign-in either, so link the account with `codex mcp login quotedpart` first.

## Privacy and terms

Parts you price are sent to QuotedPart and saved as quotes in your shop. Privacy:
https://quotedpart.com/privacy (AI assistants and MCP).
Terms: https://quotedpart.com/terms. Support: support@quotedpart.com.

## License

MIT, see [LICENSE](LICENSE). The license covers the files in this repository (manifests, skill, README, icon);
the QuotedPart service they connect to is covered by its terms of service.
