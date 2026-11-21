---
name: causalytics-overview
description: Discover and use the Causalytics MCP tools to browse a user's LinkedIn contacts, companies, posts, and interactions.
---

# Causalytics overview

Causalytics allows to connect to the user's LinkedIn data. After the user has
authorized the Causalytics MCP server, the following tools are available.
Use them to help the user explore their network.

## Available tools

- `list_contacts` — List the user's LinkedIn connections. Accepts optional
  `limit` (1-100) and `offset` (0-1,000,000).
- `get_contact` — Get an enriched contact by ID. Requires `id` (UUID).
- `get_company` — Get an enriched company by ID. Requires `id` (UUID).
- `list_posts` — List recent LinkedIn posts for the user's team. Supports
  `limit`/`offset` pagination.
- `list_interactions` — List recent LinkedIn interactions. Supports
  `limit`/`offset` pagination.
- `list_activity` — List recent LinkedIn activity. Supports `limit`/offset`
  pagination.
- `list_messages` — List recent LinkedIn messages. Supports `limit`/offset`
  pagination.

## Usage notes

- Start by calling `list_contacts` to surface the user's network, then use
  `get_contact` to drill into a specific person and `get_company` for their
  employer.
- Pagination is 1-indexed by `limit`/`offset`; default page size is server
  controlled.
- IDs are UUIDs returned by `list_*` tools. Do not invent them.
- All data is read-only and scoped to the authorized user's team.
