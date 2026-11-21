---
name: wayfront-querying
description: Find, filter, sort, paginate, and summarize records in a connected Wayfront workspace. Use for reports, audits, record lookup, and questions spanning clients, orders, tickets, invoices, subscriptions, services, or forms; use the narrower setup skills for configuration changes.
---

# Wayfront Querying

Query only the part of the workspace needed for the user's question. Do not inventory every tool or fetch every record before starting.

## Query efficiently

Use `workspace-info` when the user asks which workspace or account is connected, or when unexpected permissions make the connection context relevant. Do not call it before every ordinary query.

Use the live schema for the chosen entity tool to confirm its current fields, actions, and workspace-specific status codes. Start with a filtered `list`, then use `show` only for records whose full detail matters.

For entities that support changes, queries use the separate `*-read` tool (for example, `order-read` or `service-read`). Those tools cannot write. Existing read-only tools such as `invoice-tool` and `subscription-tool` keep their names. Configuration changes use the corresponding `*-write` tool.

Most list actions accept:

- `filters`, such as `{"name":{"$contains":"Monitoring"}}` or `{"type":{"$eq":"intake"}}`;
- `sort`, such as `["created_at:desc"]`;
- `limit` and `page` for pagination.

Filter names are model-specific. Do not guess a field that is absent from the tool schema. Status filters use schema-defined numeric codes, not labels; the display labels can be customized by workspace.

Read the returned pagination object. Continue only while `current_page < last_page`; an empty page beyond `last_page` is a successful empty result, not an error. If the user asks for every matching record, paginate to completion. Otherwise state the time range, filter, or result limit used.

## Use the right identifier

Most entities use numeric IDs, but orders and tickets use their string `number`; invoice identifiers can also be strings. List first when the identifier is unknown and pass the exact identifier field named by the tool schema.

## Interpret access and errors

An empty result means no visible record matched the query. It does not prove that inaccessible records do not exist. If access is unexpectedly denied, call `workspace-info` and explain the connected workspace, staff role, relevant role-level capability, and any record-level scope that may still apply instead of repeatedly loosening filters.

When a filter or sort fails, compare it with the live schema and retry once with a supported field. Do not retry generic server errors in a loop. Preserve the original scope when correcting a query.

For configuration changes, load the relevant workflow skill before writing: `$wayfront-workspace-setup`, `$wayfront-service-setup`, or `$wayfront-form-setup`.

Use `search-wayfront-docs` for connection, permissions, product behavior, or interface instructions that are not answered by live workspace data. Retrieve a selected result with `get-wayfront-doc` when its full context is needed, and share its canonical source URL with the user.
