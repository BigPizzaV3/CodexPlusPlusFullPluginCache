---
name: import-a-list
description: Bring a list into Excellent — contacts, menu items with prices, inquiries, past events, the staff roster or a plan of social posts — from a pasted table, a spreadsheet or a file, staged as an import for a person to check and commit in Excellent. Use for "import these contacts", "load our menu into Excellent", "bring over our past events from the old system", "add this staff list", "import this posting plan".
---

# Import a list

This skill stages imports only. Excellent reads the columns, checks every value and matches people already on
record; nothing is added to Excellent until a person commits the import on its review page.

## 1. Pick the target

| The rows are | Tool |
|---|---|
| contacts · menu items with prices · inquiries · past events | `draft_import` with `target` `contacts`, `menus`, `leads` or `events` |
| the staff roster | `draft_staff_import` |
| a plan of social posts | `draft_post_import` |

Each needs the permission its target needs in Excellent: Events for the first four, Craft for the staff
roster, Marketing (with the Marketing module switched on) for posts. If the rows mix kinds, split them into
one import per target.

## 2. Build the table

- One header row that names each column plainly, e.g. `name, email, phone, organization`. For staff: name,
  email, phone, role, venue, start date (any other column is kept as a roster column). For posts: channel,
  caption, photo link, when, location.
- One row per record, with the same separator on every row (comma, semicolon or tab) — pick one no value
  contains.
- Keep the person's values as given. Tidying is fine (split a "Name <email>" cell in two, drop blank lines and
  totals rows); filling in a missing email, price or date is not — leave the cell empty.
- At most 2,000 rows go into one import: split a longer list and say so.

Show the header, the first few rows and the row count, and wait for a yes.

## 3. Stage

Call the tool with the `table` (and the `target` for `draft_import`). Give back how many rows were staged and
the review link. If it is refused:

- the text doesn't read as a table, or no column holds each record's identity — fix the header row and stage
  again;
- no rows — the table had only a header;
- records on file (or the group's locations, for posts) could not be read — nothing was staged; try again in
  a moment.

## 4. Hand off

People already on record are offered as merges on the review page; the person decides each. A committed post
plan becomes posts awaiting approval in Portfolio → Marketing. End with: "This import is staged, not added.
Open it in Excellent to check each row, set aside what's wrong and commit it there."

Safety: an import is staged behind its review link; nothing is added to Excellent until a person commits it
there. Nothing is sent, changed or deleted from ChatGPT.
