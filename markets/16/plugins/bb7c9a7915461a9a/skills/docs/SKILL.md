---
name: docs
description: Write and organise product documentation on a Frexy website at /docs: pages as Markdown files, their order and groups, an API reference from an OpenAPI file, and the docs' own pages with search. Use when the person asks for documentation, a help centre, guides or an API reference on their site.
---

# Docs

Read `get_development_standards` with topic `docs` first: it holds the full contract.

1. **A page is a file**: `content/docs/<path>.md` written with `write_files`. The
   path is its address: `content/docs/guides/setup.md` is `/docs/guides/setup`.
   A header can give `title`, `description`, `group`, `order` and `status`.
2. **Order** lives in the pages' `group` and `order`, or in one
   `content/docs/docs.json`. Frexy builds the list, the previous and next links,
   search and the sitemap from the files: never write those by hand.
3. **API reference.** `content/docs/openapi.json` becomes a page for every operation.
4. **Markdown** with headings, steps, callouts (`> [!tip]`), tables, code and
   pictures; the components the standard names (Note, Steps, Tabs, CardGroup) work.
5. **The docs' design** is `public/docs/index.html` and `public/docs/[slug].html`.
   The person usually starts them from a design in Studio's Docs section; change
   them like any page, keeping every `{{token}}`.
6. A folder of docs they keep in a repository is brought in from a terminal
   (Claude Code or Codex), not here: write the pages they ask for instead.
7. `deploy_preview`, `get_deployment`, then give them the page's link.
