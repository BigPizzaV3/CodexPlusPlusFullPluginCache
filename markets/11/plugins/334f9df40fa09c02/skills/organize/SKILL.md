---
name: organize
description: Organize the user's Albo library into collections and maintain collection-specific memories. Use when the user asks to create a collection, add or remove saved items, or remember constraints for a collection.
---

# Organize Albo

Keep the user's saved items and collection context organized with the Albo MCP tools.

## Workflow

1. Use `listCollections` (and `getCollection` for its items) before changing a named collection. Reuse an existing collection when its title matches rather than creating a duplicate.
2. Use `createCollection`, `addCollectionItems` or `removeCollectionItems`. For a new personal recommendation shortlist, explicitly use `visibility: "private"` unless the user requests another audience. Preserve whether each ID is an `extract` or an `import` when known.
3. Removing an item from a collection does not delete it from the user's Albo library. State that distinction when it matters to the request.
4. Use `readCollectionMemory` to inspect durable collection context before planning or reorganizing it.
5. Use `saveCollectionMemory` to save or correct a stable collection-specific constraint, and `deleteCollectionMemory` to remove an outdated one. Do not turn transient chat details into memory.
6. Summarize exactly what changed, including the collection and number of affected items.

## Boundaries

- Do not claim to delete a saved item from the library; the public tools only unlink items from collections.
- Ask for clarification when multiple collections have plausible matching names and choosing one would change user data.
- Do not make a private collection public unless the user explicitly asks for that visibility.
