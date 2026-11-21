# Minz for ChatGPT (Codex plugin)

Skills that turn your Minz workspace data into briefs and summaries inside ChatGPT. The skills use the Minz connector (`https://mcp.minz.ai/mcp`), declared in `.mcp.json` and referenced from `.codex-plugin/plugin.json` (`mcpServers`). Do not remove it: ChatGPT rejects packages that drop the plugin's MCP connection; you sign in with your Minz account.

Version 0.3.0 adds the `actions` skill for write tools; 0.2.0 made **English the default language**. The assistant replies in the language the user writes in, so Vietnamese questions still get Vietnamese answers. The skills cover all 60 functions of catalog 1.9.0 (the connector lists 62 tools: these plus `search_functions` and `describe_functions`); the list is in `skills/*/references/verified-capabilities.md`.

## Skills

| Skill | Use it to |
|---|---|
| `crm-assistant` | Look up companies, contacts, leads, opportunities, quotes, contracts, products, care tickets, pipeline summary and health |
| `work-overview` | Tasks, calendar, activities and notes for a period; overdue and upcoming items |
| `minzspend-tracker` | MinzSpend expenses and settlement/reimbursement reports |
| `deal-coaching` | Compare a deal with recently won deals, win patterns, quotes and KPI progress |
| `my-inbox` | Approvals, requests, notifications and documents waiting on you |
| `workspace-explorer` | Operations cases and SLA, company directory, omni inbox, team chat targets, OKR, document register |
| `actions` | Create/update tasks, calendar events (create, change, delete, RSVP), OKR check-ins and drafts, deal follow, team chat messages. Always previews and asks for confirmation first |
| `call-prep`, `pipeline-review`, `my-week`, `expense-review` | Short briefs, shared with the Claude plugin |

## What the plugin does and does not do

- **Reads by default, writes only with confirmation.** Only the `actions` skill calls the 10 write tools. It shows the exact change and waits for a yes before each call, and each write tool needs its own `.write` scope that you grant when connecting. There is no tool to approve expenses or workflow tasks.
- **Your permissions.** Results follow your Minz workspace membership, sharing rules and scopes.
- **Facts and judgment kept apart.** Every report states period, timezone, scope and data limits.

`tests/` holds offline mock scenarios (fake data) used to review skill behavior; they are not an end-to-end test.

Support: support@minz.ai. Privacy: <https://minz.ai/privacy>.
