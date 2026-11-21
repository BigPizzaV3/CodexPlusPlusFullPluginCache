---
name: records
description: 'Reading, searching, creating, updating and deleting the records of a connected Noloco app: discovery first (list_projects, list_tables, get_table_schema), the read and write scopes, the data-admin access every call carries, filters, cursors, worked examples and what to do when a call fails. Load before the first data call on an app.'
---

# Working with records in a Noloco app

A Noloco app (a **project**, the `projectName` argument) holds **tables** of **records**; a table's **fields** have a type (text, number, date, single or multi select, relationship, formula, lookup, rollup, file). Every tool except `list_projects` and `load_skill` takes a `projectName`, and every tool answers with text: on success a message and, when there is data, a JSON block (also in `structuredContent`); a failed call is an error result whose text says what went wrong and, when there is one, what to do instead. Act on that suggestion rather than retrying the same call.

## Discover before you act

Project, table and field names are specific to each app and cannot be guessed. Inventing a `tableName` or a field name is the most common cause of a failed call. Work from discovery outward:

1. `list_projects`: the apps this connection may use and the exact `projectName` of each. When it returns one app, use it without asking.
2. `list_tables`: the tables of that app and their exact `tableName`. Pass `nameFilters` (case-insensitive substrings, several at once) to find related tables in one call.
3. `get_table_schema`: a table's fields, their types and select option values. Pass `fieldNames` (substrings) on a wide table to keep the response small. Read it before filtering, sorting or writing.
4. `list_records` and `get_record` to read; `create_record`, `update_record` and `delete_record` to write.

## Reading

- `list_records` takes `tableName` plus optional `filter`, `sort` (`{ field, direction: ASC | DESC }`), `first` (1 to 100, default 25), `after` and `before` (cursors), `include` (relationship fields to expand) and `fieldNames` (the columns to return). It returns `records`, `totalCount` and `pageInfo`.
- `get_record` takes `tableName` and `recordId`, plus optional `include` and `fieldNames`.
- Keep requests narrow. Filter with `filter` (value operators `equals, not, contains, gt, gte, lt, lte, in, notIn`; relationship operators `some, none, every`), return only the columns you need with `fieldNames`, and expand only the relationships you need with `include`.
- Page with cursors: request `first` (at most 100); while `pageInfo.hasNextPage` is true, call again with `after: pageInfo.endCursor`. `totalCount` tells the table size up front.

## Writing

- `create_record` takes `tableName` and `data` (a field to value map; `id`, `uuid` and timestamps are generated). It returns the new `recordId` and runs the app's automations.
- `update_record` takes `tableName`, `recordId` and `data` with only the fields that change. Repeating it leaves the values as they are but runs the app's update automations again, so read the record back with `get_record` before retrying a call whose result you did not see.
- `delete_record` takes `tableName` and `recordId`. It is permanent.
- Confirm a destructive or ambiguous write with the user first, and prefer the narrowest change.

## Scopes and access

Access is granted per app at sign-in as `mcp:read` or `mcp:read` plus `mcp:write`; `list_projects` reports the scopes held on each app. A write that fails for insufficient scope means the app is connected read-only: tell the user they can re-run the Noloco consent flow to grant write access, and do not retry.

Every tool acts with the connecting user's data admin role and bypasses the app's row-level and field-level permissions, reads included. Results are not what an app user sees, so never describe them that way. What is still enforced: the granted scope, a live data-admin check on every call, Noloco's data validation (required fields, field types, relationship rules) and the plan's API rate limits.

Some apps expose their own connector URL (`…/mcp/apps/<app>`). There, the tools act as the signed-in app user within their role: there is no `list_projects` and no `projectName` argument, and records or fields the user cannot see in the app are not returned.

## Worked examples

**Answer a question about data.** "How many deals did we close this quarter?": `list_tables` with `nameFilters: ["deal"]`; `get_table_schema` with `fieldNames: ["stage", "close", "amount"]` to confirm the stage options and the close date field; `list_records` with a `filter` on the stage and the close date, `fieldNames: ["amount"]` and `first: 100`, reading `totalCount` and paging with `after` when there is more.

**Make a targeted change.** "Mark deal 482 as Won": `get_table_schema` to confirm the stage field and that "Won" is one of its options; confirm the change with the user; `update_record` with `recordId: 482` and `data: { stage: "Won" }`.

**Walk a whole table.** `list_records` with `first: 100`, then `after: pageInfo.endCursor` while `pageInfo.hasNextPage` is true.

## When a call fails

- Table or record not found: re-run `list_tables` or `list_records` for the exact names and ids.
- Insufficient scope: the app is read-only for this connection; ask the user to re-consent with write access.
- Cannot view and manage all data: ask an admin of the project for a role that can view and manage all data, then retry.

For questions about Noloco as a product (how to build or configure an app, what a feature does), use the Noloco guides at https://guides.noloco.io/ rather than guessing.
