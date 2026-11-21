---
name: pretture-erp-get-started
description: Use Pretture ERP Analytics to run safe backend-calculated sales reports.
---

# Pretture ERP Analytics

Use this plugin when the user wants to summarize Pretture ERP sales, review sales breakdowns, apply sales filters, or include/exclude returns in backend-calculated sales metrics.

## How To Use The MCP Tools

1. Call `get_sales_analytics` for total sales KPIs over an inclusive date range.
2. Use the `group_by` argument for monthly, yearly, customer, product, store, location, category, subcategory, or size groupings.
3. Use the `filters` argument for exact-match sales filters such as customer, store, city, category, product, size, color, sales type, sales nature, or transaction type.
4. Use `include_returns=false` only when the user asks to exclude return rows; otherwise keep the backend's net-sales return handling.
5. Treat the backend response as the source of truth. Do not recalculate sales, returns, costs, counts, or profit from raw rows.
6. Do not ask users for ERP JWTs, API keys, OAuth tokens, or credentials in chat. Authentication is handled by the Pretture MCP server.

## User-Facing Behavior

- Use `get_sales_analytics` only for read-only sales analytics requests.
- If a user asks for unsupported ERP areas such as inventory or payments, explain that this plugin currently supports sales analytics only.
- Report errors honestly, including authentication, disabled API, validation, or upstream availability failures.
- Keep responses focused on business outcomes and cite the returned date range, grouping, and filters when relevant.

## Safety Boundaries

- Do not expose or request credentials.
- Do not perform payment, deletion, or destructive ERP actions.
- Do not infer private ERP records outside the connected user's authorized scope.
