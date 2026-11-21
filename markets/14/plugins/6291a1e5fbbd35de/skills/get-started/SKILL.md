---
name: get-started
description: Answer questions from the company's own databases connected in AnythingMCP, read-only. Use when the user asks about their business data (customers, orders, revenue, stock, shipments) or which databases are available.
---

# Answer questions from your company's databases

1. Call `anythingmcp_list_databases` to see which databases this connection can query and their engine.
2. Before the first query on a database, call `anythingmcp_get_workspace_guide` for what its tables and fields mean, then `anythingmcp_get_database_schema` for the exact table and column names. Use `anythingmcp_get_query_examples` when unsure about the dialect (row limits, quoting, dates).
3. Answer with `anythingmcp_query_database`: one SELECT statement per call. Filter and aggregate in SQL; results stop at 1,000 rows.
4. Show the result as a short answer or a table, and say which database it came from.

Rules:
- The plugin only reads. If the user asks to change data, say that this plugin cannot do it.
- Never ask for passwords, connection strings or API keys. Databases are added in the AnythingMCP dashboard (`anythingmcp_get_configuration_url`).
- If no database is connected, explain how to add one with `anythingmcp_get_configuration_url`.
