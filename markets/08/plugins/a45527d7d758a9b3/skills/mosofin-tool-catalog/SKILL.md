---
name: mosofin-tool-catalog
description: Use whenever MosoFin is connected and the user asks about their business numbers, workspaces, connected data sources, or saved MosoFin skills (QuickBooks, Xero, Stripe, Square, WooCommerce, BigCommerce, Google Ads and more). Read-only. Answer only from MosoFin tool results in this chat; never invent numbers.
---

# MosoFin

MosoFin gives read-only access to a business's connected data. It never changes anything in QuickBooks, Stripe, Google Ads, or any other platform.

## Before you start

MosoFin needs a signed-in account with an active subscription. If any tool returns a login, session, access, or subscription error, stop. Don't guess numbers. Tell the user:

> Please sign in at https://app.mosofin.com, check that your subscription is active and your data sources are connected, then try again.

## Steps

1. **Pick the workspace.** Call `list_workspaces` first, every time.
   - `confirmed`: tell the user which workspace you're using, by name.
   - `selection_required`: ask whether this is for one workspace or several, then call again with `workspace_ids` and `mode` (`single` or `multi`).
2. **Pick the company.** Call `get_agent_datasources` to see what's actually connected. If a platform has more than one company, ask which one by its `display_name`, then pass its `data_source_id` on every later call. Never show the id to the user.
3. **Find the tool.** Call `get_datasource_tools` with the `datasource` id. Only use tool names it returns.
   - `enabled`: call it.
   - `permission`: ask the user once, then call with `approved: true`.
   - `disabled`: don't call it.
   - Empty list: the connection isn't active. Ask the user to reconnect at https://app.mosofin.com.
4. **Get the numbers.** Call `invoke_datasource_api_tool`. Run independent reads in parallel (for example P&L, balance sheet, and A/R aging together).
5. **Answer** using the format below.

## Data sources

MosoFin adds connections over time, so the table below shows examples, not the full list.

- **What this user has connected:** always check `get_agent_datasources`. Its results win over this table.
- **What MosoFin supports:** the current list is at https://www.mosofin.com/connections. If the user asks about a platform that isn't connected, don't say MosoFin can't do it. Point them to that page, and to https://app.mosofin.com to connect it.

| `datasource` | Covers | Agent |
|---|---|---|
| `quickbooks`, `xero` | Accounting | `bea` |
| `stripe`, `square_payments` | Payments | `pax` |
| `woocommerce`, `bigcommerce` | Online stores | `otis` |
| `google_ads` | Advertising | `ada` |

**Google Ads:** report tools need `start_date` and `end_date` (`YYYY-MM-DD`). Money fields ending in `Micros` are divided by 1,000,000 once.

## Errors

| Error | What to do |
|---|---|
| `connection_unavailable` | Ask the user to reconnect at https://app.mosofin.com |
| `entity_required` | Ask which company, then retry with its `data_source_id` |
| `approval_required` | Ask the user, then retry with `approved: true` |
| `invalid_params` | Fix the dates or filters and retry |
| Login or subscription | Stop and send the user to https://app.mosofin.com |

## Saved skills

- `get_skills`: list saved workflows when the user asks, or when the request sounds like a repeat job.
- `get_my_skill`: only after the user picks one. Follow its `skill_md`.
- `create_skill`: the only write. It saves a MosoFin skill and changes nothing else. Use it only after the user has seen the answer and says yes, and ask where to save it: MosoFin, this app, or both.

## How to answer

1. Name the workspace and company.
2. Lead with the answer in plain English, then the key numbers.
3. Use only numbers from tool results in this chat where `mock` is `false`. If `mock` is `true`, say it's sample data.
4. If a call failed or came back empty, say so. Never fill gaps from general knowledge.
5. End with one line: `Data sources: <datasource> <tool> @ <fetched_at>, …`
