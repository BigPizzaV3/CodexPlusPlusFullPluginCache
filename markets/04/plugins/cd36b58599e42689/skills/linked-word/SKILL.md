---
name: linked-word
description: >
  Look up King James verses and chapters, Strong's Hebrew and Greek numbers,
  reverse-look up original words from an English KJV rendering, find verses that
  use a number, search the KJV text, and find section headings (topics). Use
  when the user asks for a Bible verse, Strong's number, Hebrew/Greek word
  study, a KJV phrase search, or a named topic such as the Sermon on the Mount.
---

# Linked Word

Use the Linked Word MCP tools (`https://www.linkedword.com/mcp`). Do not invent verses, Strong's numbers, or glosses. Cite the `url` each tool returns.

This server is KJV only. Do not use it for NIV, ESV, or other translations, or for pastoral advice.

## Which tool

| User wants | Tool |
|---|---|
| A verse or chapter | `get_passage` |
| Meaning of H7225 / G26 / "Strong's 25 Greek" | `get_strongs` |
| Which Hebrew/Greek words the KJV translates as *flesh* | `reverse_strongs` |
| Every verse that uses a Strong's number | `find_verses_by_strongs` |
| Find a phrase in the KJV ("still waters") | `search_verses` |
| A topic or heading ("Sermon on the Mount", "end times") | `search_topics` |
| Book abbreviation (Genesis → `gen`) | `list_books`, or [references/books.md](references/books.md) |

Do not use `search_verses` to find Strong's numbers. Do not use `get_strongs` when the user only has an English word — use `reverse_strongs` first. Do not use `search_topics` when the user asked for a specific verse reference.

## Book abbreviations

`get_passage` requires `book` as a lowercase abbreviation (`gen`, `1john`, `1chr`, `song`). If the name is not in [references/books.md](references/books.md), call `list_books`.

Numbered books have no space: `1sam`, `2kgs`, `1cor`, `1john`. Psalms is `ps`. Song of Solomon is `song`. James is `jas`. Philemon is `phlm`.

## Passages

```
get_passage({ book: "john", chapter: 3, verse: 16 })
get_passage({ book: "gen", chapter: 1 })
```

- Default: verse text (or a page of verses) plus one citation URL. No per-word Strong's data.
- Set `include_strongs: true` only if the user asked for Strong's numbers or word-level links.
- Chapters are paged. `page_size` defaults to **20**, maximum **100**. Genesis 1 has 31 verses — use `page_size: 31` for the whole chapter, or follow `next_page` when `has_more` is true.

## Strong's numbers

`get_strongs` takes `lang` (`h` or `g`) and `id` as an integer **without** the H/G prefix.

- `H7225` → `{ lang: "h", id: 7225 }`
- `G25` → `{ lang: "g", id: 25 }`

If the user says "Hebrew 566" use `lang: "h"`. Cite the returned URL. The English name or gloss is in the entry (transliteration + definition), not in `find_verses_by_strongs`.

## Reverse lookup (English → numbers)

```
reverse_strongs({ keywords: "flesh" })
reverse_strongs({ keywords: "love", lang: "g" })
```

Matches the **KJV usage/gloss** (the English word the KJV uses), not the long definition text. Returns `strongs` + a short `definition` only. Then call `get_strongs` for the full entry of one number.

Keywords must be at least 3 letters. Results are paged (default 20, max 100).

## Verses that use a number

```
find_verses_by_strongs({ lang: "h", id: 7225 })
```

Returns verse text and URLs, not the lexicon entry. The matching English word is inside the verse text but is not highlighted.

## KJV text search

```
search_verses({ query: "still waters" })
```

Full-text search of the English KJV. Ranked, paged. This does not search Strong's.

## Topics

```
search_topics({ query: "sermon on the mount" })
search_topics({ query: "end of the world" })
```

Matches section headings (pericopes) by keyword and meaning. Returns verse ranges and URLs, not the verse text. Follow with `get_passage` when the user wants the passage itself.

## Answers

- Quote the returned KJV text. Do not silently modernize it.
- Include the Linked Word URL for anything you cite.
- If `has_more` is true and the user wants the rest, call again with `page: next_page`.
- If a tool returns `error` (unknown book, missing verse), fix the abbreviation or reference and retry. Do not guess the verse.
