---
name: jci-sk-portal-tools
description: Use the JCI SK Portal MCP server's tools — one per real operation (list-content, get-content, search-content, list-corpus, glob-corpus, read-corpus, grep-corpus, create-content-note, remember-note, forget-note, submit-feedback, my-permissions) — to browse/search JCI South Key chapter content — bylaws/constitution (CBL), policy manual (PM), protocol, and other stored chapter documents and notes — explore that content by virtual folder path, read a specific document, remember a short personal preference, or submit feedback on an answer. Use this whenever a user asks about JCI South Key chapter administration, bylaws/constitution/policy content, chapter document lookup, or wants to save a note/preference or give feedback.
---

# JCI SK Portal tools

JCI SK Portal exposes one individually-named MCP tool per real operation —
not a generic dispatcher you pass a "capability" key to. Your MCP client's
own `tools/list` call already tells you exactly which tools exist and their
input shape; this file explains how to use them well, not what they are.
**You may not see every tool named below** — a tool you lack permission for
is simply absent from your own `tools/list` (not shown as disabled). Call
`my-permissions` at any time to see your own current access and why a tool
is/isn't available to you.

## Read-only vs. write

Every tool declares an explicit `readOnlyHint` annotation — `true` for
anything that only browses/searches/reads, `false` for anything that
creates or changes data. `forget-note` additionally declares
`destructiveHint: true` (a real, irreversible delete of your own memory
note) — every other write tool is purely additive.

## Real tool set (as of 2026-10-23 — see
references/mcp-capabilities.md for the full, literal schema pulled from the
server's own seeder)

**Content** — the original flat get/search/create-note set:
- `list-content` — browse stored content items, optionally by folder/type/tag.
- `get-content` — fetch one item in full by id.
- `search-content` — full-text search over titles, text bodies, and file names.
- `create-content-note` (requires the `content.create` permission — if you
  don't hold it, this tool won't appear in your own tools/list at all) —
  create a new text content item.

**Corpus explore** — an explore-first, virtual-file-tree pattern over the
same stored content, for when you need to navigate by structure rather than
search by keyword:
- `list-corpus` — list entries under a virtual path (start with `/`).
- `glob-corpus` — find paths matching a glob pattern.
- `read-corpus` — read a text file by path, line-numbered, with
  offset/limit for long files. Read the full clause/section around a match,
  not just the matching line.
- `grep-corpus` — regex search across stored text, `path:line: text` per
  hit. Try a few spellings/synonyms before concluding something isn't
  covered — an empty result should be taken at face value, not guessed
  around.

**Per-user memory** — self-scoped to the caller, never takes a user id as a
parameter:
- `remember-note` — save a short note to the caller's OWN memory (e.g. a
  wording preference). Never save personal data about someone else here.
- `forget-note` — delete one of the caller's own memory notes by id. Real,
  irreversible.

**Feedback** — `submit-feedback`: record feedback on an answer/interaction
for admin review (optional query reference, 1-5 rating, comment).

**Introspection** — `my-permissions`: report which of the tools above the
signed-in caller currently has access to, and why (e.g. a missing
permission) for ones they don't. Call this to check your own access rather
than assuming a tool is or isn't available.

## How a typical request should actually flow

1. For a direct lookup ("what does the CBL say about X" / "find the
   succession policy"), prefer `grep-corpus`/`glob-corpus` over
   `search-content` when the user is asking about STRUCTURED chapter
   documents (CBL/PM) — these are explicitly path-organized
   (`/cbl/...`, `/pm/...`) and `read-corpus` lets you pull the FULL
   surrounding clause, not just a search snippet.
2. Use `search-content`/`list-content` for general, less structured content
   (announcements, general notes) where a virtual path isn't the natural
   shape.
3. Never fabricate a chapter policy/bylaw answer from general knowledge —
   if a read-only call returns nothing, say so plainly rather than guessing.
4. Only call a write tool when the user has actually asked for a
   note/preference/feedback to be saved — never save something speculative
   on their behalf.

## Auth

Every call runs as the real, OAuth-authenticated JCI SK Portal member who
connected this plugin — not as an anonymous or admin identity. What a given
member can do is exactly their own role's permissions in the portal (checked
server-side on every write call, and reflected in which tools even appear in
`tools/list`); this skill doesn't need to re-implement that check, just
expect a clean refusal (or a missing tool) if a member lacks a permission.
