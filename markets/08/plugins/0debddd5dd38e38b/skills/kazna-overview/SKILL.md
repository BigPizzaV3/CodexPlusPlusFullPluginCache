---
name: kazna-overview
description: Summarize the authenticated Kazna author cabinet using read-only MCP tools (channels, storefront profile, balance, recent orders).
---

# Kazna author overview

Use only the Kazna MCP server (`Kazna`). Do not invent data.

## Steps

1. Call `list_channels` and briefly summarize titles and platforms.
2. Call `get_storefront` for display name / bio / slug.
3. Call `billing_summary` for balances (available, pending, lifetime).
4. Call `list_orders` (or note if empty) and summarize recent order statuses.
5. Remind that pricing, product creation, checkout, and payouts stay on kazna.online — this plugin is read-only.

## Constraints

- Never claim you can create products, change prices, publish storefront items, or withdraw funds.
- If a tool is missing or auth fails, ask the user to reconnect Kazna OAuth.
