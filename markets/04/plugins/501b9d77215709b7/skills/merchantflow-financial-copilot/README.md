# MerchantFlow Financial Co-Pilot (skill bundle)

Guidance that teaches an AI assistant how to read MerchantFlow data like an
ecommerce operator: which tool answers which question, how the P&L waterfall is
built, and which shortcuts produce wrong numbers.

## Contents

| Path | What it is |
| --- | --- |
| `SKILL.md` | The skill itself. Load this first. |
| `references/tool-reference.md` | All 64 MCP tools, with scopes and parameters, generated from the live server. |

## Connect first

This bundle is guidance, not a connection. It is only useful alongside the
MerchantFlow MCP server:

- **Server URL:** `http://localhost:3000/api/mcp`
- **Transport:** JSON-RPC 2.0 over Streamable HTTP (POST only)
- **Auth:** `Authorization: Bearer <token>` - either a Personal Access Token
  (`mf_pat_...`, created at `/dashboard/settings/developer/mcp`) or an OAuth
  2.1 access token from the consent flow.

## Installing

**Claude** - upload this .zip as a skill, or drop the folder into your project
so `SKILL.md` sits at its root. Add the MCP server separately as a connector.

**Cursor / Windsurf / Copilot** - these read a single instruction file rather
than a bundle. Download the format built for your editor instead:
`/api/mcp/skill?format=cursor`, `?format=windsurf`, or `?format=vscode`.

**ChatGPT** - ChatGPT connects to MerchantFlow by MCP server URL, in Settings >
Connectors, using the URL above. It does not take a skill archive, so there is
nothing here to upload. Paste `SKILL.md` into a Project's custom instructions
if you want the same guidance applied to a conversation.

## Staying current

`references/tool-reference.md` is generated at download time. Re-download the
bundle after MerchantFlow ships new tools rather than editing it in place - and
in any disagreement, the live `tools/list` response wins.
