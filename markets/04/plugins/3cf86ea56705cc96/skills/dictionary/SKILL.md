---
name: dictionary
description: Read, add, update, delete, or additively import manual items in a user's VoiceCursor dictionary through the OAuth MCP. Use for VoiceCursor word or mapping management on macOS, iOS, Android, or explicit default.
---

# VoiceCursor Dictionary

Use the bundled `voicecursor_dictionary` MCP server. If the connection requests
authentication, let the user complete the VoiceCursor Clerk OAuth consent flow.

## Reads

- Use `list_dictionaries` to discover available language and OS targets.
- Use `get_dictionary_items` only with one exact language and OS.
- Never claim that this plugin reads or modifies the operating system's native
  user dictionary. It manages the user's VoiceCursor dictionaries, which
  VoiceCursor clients consume on their platforms.

## Mutations

Every create, update, delete, and import uses its matching prepare/commit pair.

1. Obtain the exact language and exactly one target OS: `ios`, `mac`, `android`,
   or `default`.
2. Never infer the OS from the current computer, project, client, prior usage,
   or a generic request. Use `default` only when the user explicitly says it.
3. Call the matching prepare tool with the complete proposed mutation.
4. Show the complete returned plan and `confirmation_prompt`. The user's
   original mutation request is not post-prepare confirmation.
5. Wait for the user to explicitly confirm the exact OS shown in the plan.
6. Call only the matching commit tool, once, with the token and that same OS as
   `confirmed_os`.

Use these pairs:

- create: `prepare_dictionary_item_write` / `commit_dictionary_item_write`;
- update: `prepare_dictionary_item_update` / `commit_dictionary_item_update`;
- delete: `prepare_dictionary_item_delete` / `commit_dictionary_item_delete`;
- import: `prepare_dictionary_items_import` / `commit_dictionary_items_import`.

For update and delete, first read the exact target and use its stable `item_id`.
Never target by a similar-looking word or mapping key. Only manual items are
mutable; item type cannot change. Word update changes its value. Mapping update
may change its key, value, or both.

Import accepts up to 100 `word`/`mapping` objects for one exact language and OS.
It is an atomic additive merge: it never deletes omitted entries, replaces a
dictionary, imports learning metadata, or silently overwrites a mapping.
Display every `create`, `unchanged`, and `conflict` result. A conflict produces
no committable plan.

If the user changes any plan field, discard the plan and prepare again. If
commit is ambiguous, stale, expired, already used, or rejected, do not retry the
token; read current state and prepare a fresh plan. Report `unchanged` as
success. Report `conflict` or `stale_plan` without claiming a mutation occurred.
