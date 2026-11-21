---
name: vaiz-help
description: Answer "how does Vaiz work" questions from the built-in knowledge base — search help articles, FAQs, and tutorials, list and read MCP resources such as dictionaries and space overview data, and tell system documentation apart from user documents.
---

# Vaiz help and MCP resources

The Vaiz MCP server exposes Vaiz's own documentation alongside its tools: a searchable knowledge base of help articles and tutorials, plus read-only resources such as dictionaries (enumerations, field definitions) and space overview data. Use them to answer questions about Vaiz itself without guessing.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth (open the Vaiz connection and complete OAuth sign-in).

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz search_knowledge_base`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Two sources of truth

- **System documentation** — Vaiz's own help, FAQs, tutorials, and reference data. Read with `search_knowledge_base`, `list_resources`, and `read_resource`.
- **User content** — documents and tasks your team wrote. Read with `search_space`, `get_document`, `get_task`. `search_space` does not search system documentation, and `search_knowledge_base` does not search the workspace.

If the user asks "how do I do X in Vaiz", use system documentation. If they ask "what did we write about X", use user content. If they ask what they can do with Vaiz here, use `get_started` (see `vaiz-workspace`).

## Searching help

`search_knowledge_base(query)` — search help articles, FAQs, and tutorials (feature explanations, settings, integrations). Optional `limit`. Start here for most "how does Vaiz…" questions.

## Reading resources

1. `list_resources` — returns every available resource: dictionaries, space data, and the help index. Call it once per session and reuse the names.
2. `read_resource(resourceName)` — reads one resource by name, for example `vaiz-space-overview`. Knowledge base articles use the `vaiz-help-` prefix followed by the article name from the index.

Quote or summarize the article for the user and mention that it comes from the Vaiz help center; do not paraphrase from memory when an article is available.

## Good habits

- When a tool call fails with a validation error about an enum or field, check the relevant dictionary resource before retrying.
- For anything not covered by the knowledge base, point the user to the public help center and support.

Further reading:

- Help center: https://vaiz.com/help
- Connecting Vaiz to MCP: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp
- Support: https://vaiz.com/support
- https://vaiz.com
