---
name: get-started
description: First steps with SuperDB in ChatGPT. Use when the user connects SuperDB or asks what it can do with their database projects.
---

# Getting started with SuperDB

SuperDB is a managed Postgres backend (database, auth, storage and realtime) made in Brazil. This plugin talks to the user's SuperDB projects through the remote MCP server at https://mcp.superdb.com.br/mcp.

## How to help the user

1. Start by listing the projects the user authorized (`superdb_list_projects`). The connection only reaches the projects chosen on the SuperDB consent screen.
2. To understand a project, list its tables (`superdb_list_tables`) and describe the relevant ones (`superdb_describe_table`).
3. To answer questions about data, use `superdb_query_sql`. It runs in a READ ONLY transaction, so it never changes data.
4. To create or change tables, use `superdb_run_sql` only when the user asked for a change. Show the SQL first and keep row level security (RLS) on for new tables.
5. To review who can read or write a table, use `superdb_list_policies`.
6. Files live in Storage buckets: `superdb_list_buckets` and `superdb_create_bucket`.

## Rules

- Never run destructive SQL (DROP, DELETE, TRUNCATE, ALTER that removes data) without the user explicitly confirming it.
- If more than one project is authorized and the user did not say which, ask.
- Answer in the user's language. Most SuperDB users write in Portuguese.
