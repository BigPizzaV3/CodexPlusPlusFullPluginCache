---
name: glubler
description: Use when the user wants to search the Glubler catalog, save or batch-save websites into a Glubler collection, create, rename, or delete collections, remove a saved link, or view the contents of a public Glubler.
---

# Glubler

Glubler stores websites in curated collections called Glublers. This plugin talks to the
Glubler MCP server; every action below maps to one server tool.

## Choosing the tool

| The user wants to... | Tool |
| --- | --- |
| Find websites, tools, games hubs, or news already in the Glubler catalog | `search_glubler_catalog` |
| See their own collections and how many websites each holds | `list_my_glublers` |
| Confirm which Glubler account is connected | `who_am_i` |
| See the websites and subglublers inside one collection | `get_glubler_details` |
| Read a public collection by owner and slug | `get_public_glubler` |
| Start a new collection | `create_glubler` |
| Save one website into a collection | `glue_website` |
| Save many websites into a collection at once | `glue_websites_batch` |
| Rename a collection or change its URL slug | `rename_glubler` |
| Remove one saved website from a collection | `unglue_website` |
| Delete a collection and everything inside it | `delete_glubler` |

## How to work

- To save a website, you need the target collection. If the user did not name one, list their
  collections with `list_my_glublers` and ask which one to use, or create a new one with
  `create_glubler` when they ask for a fresh list.
- `create_glubler` accepts an optional `parentGlublerId` for a nested subglubler and an optional
  `slugName`. Pass a slug only when the user asks for a specific URL.
- `glue_websites_batch` takes an array of URLs and saves them all in one call. Prefer it over
  repeated `glue_website` calls whenever the user gives several links. Sites that are not in
  the Glubler catalog yet are fetched automatically: Glubler retrieves the page metadata and
  the real favicon, then adds the site to the collection.
- Glubler scrapes metadata and the real favicon for sites that are not in its catalog yet, so
  saving a new site can take a moment.
- Destructive tools (`delete_glubler`, `unglue_website`) remove content permanently. Confirm the
  specific collection or link with the user before calling them.
- `search_glubler_catalog` returns at most 7 results, and a query that matches nothing simply
  returns an empty list. Report that honestly instead of inventing websites.

## Authentication

Reading the public catalog and public collections works without signing in. Actions on the user's
own account (listing, creating, gluing, renaming, deleting) require the connected Glubler account.
If a tool returns an authentication error, ask the user to connect their Glubler account rather than
retrying the same call.
