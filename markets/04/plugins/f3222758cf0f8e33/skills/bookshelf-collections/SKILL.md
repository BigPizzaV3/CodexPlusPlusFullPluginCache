---
name: bookshelf-collections
description: Organize existing Heyzine flipbooks in bookshelf collections. Use when users ask to list shelves, inspect contents, add, remove, or position flipbooks, update a social preview, or ask about bookshelf creation and ordering limits.
---

# Heyzine bookshelf collections

A bookshelf references existing flipbooks. Adding or removing membership does
not copy or delete the flipbook.

## Inputs and boundaries

- Identify a bookshelf and flipbook by id, public URL, short id, or an
  unambiguous title returned by the list tools.
- In membership tools, `id` is the bookshelf and `flipbook_id` is the
  flipbook. Never transpose them.
- There is no tool to create, delete, or reorder an existing bookshelf. Explain
  that those actions require the Heyzine bookshelf editor.
- If bookshelves are unavailable for the account, report the server's plan
  error. Do not invent a substitute collection.

## Resolve names

1. Call `heyzine_list_bookshelves` to resolve a shelf title.
2. Call `heyzine_list_flipbooks` to resolve a flipbook title.
3. Proceed on one clear match. If several entries plausibly match, show their
   titles, ids, and URLs and ask the user to choose. If none match, report that
   and stop.

Do not rely on a remembered list when the user asks about current membership.

## Inspect a bookshelf

Call `heyzine_list_bookshelf_flipbooks` with the bookshelf `id`. Preserve the
returned display order and positions when answering what visitors see.

## Add flipbooks

Call `heyzine_add_to_bookshelf` once for each flipbook with `id` and
`flipbook_id`. Pass optional `position` only when the user specifies placement;
it is zero-based. A flipbook may belong to several shelves.

For a batch request, list and resolve the matching flipbooks first. Add only
clear matches, then report the added count and any skipped or failed items.

## Remove flipbooks

Call `heyzine_remove_from_bookshelf` with the shelf `id` and `flipbook_id`. This
removes only the membership. If "remove" or "delete" could mean deleting the
flipbook itself, clarify before acting. Never call `heyzine_delete_flipbook`
for an unqualified shelf change.

## Update the social preview

`heyzine_set_bookshelf_social` controls how the shelf's link renders when
shared. Pass `id` plus only the requested `title`, `description`, and
`thumbnail` fields. `thumbnail` must be a public image URL. Do not invent
missing metadata.

## Report the result

After membership changes, list the shelf once to verify the current contents.
Return the bookshelf URL, the resulting count, and any failures. For a batch,
summarize counts instead of narrating every tool call.
