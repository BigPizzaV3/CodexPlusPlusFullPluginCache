---
name: extract-data-from-pages
description: Pull specific fields such as prices, names, dates or specifications out of one or more web pages as structured data. Use when the user wants values or a table rather than a summary, or the same fields from several pages.
---

Use this skill when the user wants particular values from web pages rather than the pages' full text.

1. Work out the fields the user wants and the pages that hold them. If the user has not given URLs, find them with `search`, or with `map` when they are on one site, and confirm the list with the user when it is long.
2. Call `extract` with the `urls` and either a `prompt` describing the fields or a JSON `schema` with them. Use a `schema` when the user wants a table with fixed columns or the same fields across several pages. Type numbers as numbers and keep fields that may be missing nullable.
3. Set `showSources` to true when several URLs are involved, so each value can be traced to its page. Set `showConfidence` to true when the user asks how sure the values are.
4. Present the result in the shape the user asked for, usually a table, with the source URL for each row.

When data is missing:

- Leave a field empty when the page does not state it, and say which fields were not found. Never fill a gap with a plausible value.
- If a page could not be read, list it separately instead of dropping it silently.

Do not:

- Use `extract` to answer a question about one value on one page. `scrape` that page and read the value instead.
- Extract from more pages than the user needs. Narrow the list first.

The user's explicit instructions take priority over this skill.
