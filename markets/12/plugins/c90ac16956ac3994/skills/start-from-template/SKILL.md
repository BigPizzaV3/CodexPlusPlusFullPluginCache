---
name: start-from-template
description: Find a LaTeX template in letX's library and start a letX project from it. Use when the user needs a starting point for a thesis, a journal or conference paper, a CV, a poster, a presentation or a report, or asks for a template by name, university or publisher.
---

# Start a letX project from a template

The user's instructions come first. If they name a template, use that one.

## Steps

1. Search with `search_templates`, using the user's own words: a university, a publisher such as
   IEEE or Springer, or a kind of document such as "thesis" or "resume". Add `category` only when
   the user names a kind of document that matches one.
2. Show the best few matches with their name, a one-line description and the template's page
   link. Ask which one they want, unless they already chose or only one fits.
3. If the user wants to know more about one, call `get_template` with its slug.
4. Create the project with `create_project_from_template` and the chosen slug.
5. Give the user the editor link from the result. If they want to start writing now, read
   `main.tex` with `read_project_file` and fill it in with `update_project_file`, sending the
   whole file each time.

## Never

- Never call a template an official university or publisher template unless its details say so.
- Never create more than one project for a single request.
- If nothing matches, say so, and suggest broader words (for example "thesis" instead of a
  department's name).
