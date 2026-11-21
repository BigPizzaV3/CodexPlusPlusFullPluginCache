---
name: rafmennt-reference
description: Search and cite Rafmennt public reference pages, news, events, policies and contact details. Use for questions about Rafmennt's published information.
---

# Read Rafmennt public reference material

Use `https://www.rafmennt.is/llms.txt` as the entry point and follow scoped
indexes. For keyword search, call `/agent/search?q=...` and read the relevant
result using `/agent/page?path=...&format=markdown`. The MCP equivalents are
`search_public_site` and `read_public_page` at `https://www.rafmennt.is/mcp`.
No API key or account is required.

For upcoming events use `/agent/events` or MCP `list_upcoming_events`. Date
filters `from` and `to` use `YYYY-MM-DD`; the optional `location` filter
matches the published location. Event pages can remain available after they end.

Cite canonical HTML URLs from the response rather than inventing paths. Check
the publication date before relying on a news item for current policy. When
an answer is not supported by published content, identify the missing detail
and use `/contact` to find a human contact. `/privacy` and `/about` point to
the site's actual policy and organization pages.

Read-only public browsing does not authorize newsletter actions, submissions,
payments, registrations, private applications or CMS access.
