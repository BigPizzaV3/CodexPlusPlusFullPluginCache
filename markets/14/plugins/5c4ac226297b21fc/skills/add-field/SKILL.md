---
name: add-field
description: 'Adding a field to a table and making it usable: on every view''s list and form, on the main record page, and in the permission rules that would hide it. Load whenever the user asks for a new field or column.'
---

# Adding a field and showing it

The job: add a field to a table and leave it usable: in the list, on the new-record form, and on the record page where it is read and edited. A new field appears on no page by itself. Each view keeps its own field lists for its list, its form and its record page, so every place the field belongs is changed here. Load `build-views` too when the field should drive a layout (a board grouped by it, a calendar on it).

## 1. Read before you write

- `list_tables`: a table with a `source` is synced from an external source (Airtable, Google Sheets, a database) and refuses new fields. Tell the user to add the field in that source; once it syncs in, steps 3 to 7 show it.
- `get_table_schema`: the table's fields. When the field already exists, show that one instead of creating a second.
- `list_pages` with `nameFilters: ["<tableName>"]`: the table's views are the pages whose `dataType` is the table. From here on pass a view's `id` as `pageIdentifier`: a table often has several views, and its name picks only one.
- `list_version_history`: whether the app has been published before, which decides the last step.

## 2. Create the field

`upsert_field` with its type and format. Its name is derived from `display` in camelCase: use the `name` the result returns, because the view tools accept only that name. Some kinds change the steps below:
- Calculated fields (a formula, a lookup, a rollup or an AI-generated value) hold a value nobody types in: they go on the list and the record page, never on the form.
- A link to another table also adds a field to that table, listing the records that point back. Show it on that table's record page, as a list of related records, only when the user asks.
- An image field can be the card picture on a layout that shows cards (step 4). A single-option field can group a board: that is a view setting, see `build-views`.

## 3. Decide where it goes

- The views the user named. When they named none: the list and the form of every view of the table, and the record page of the table's main view only, the one that comes first in the navigation. A record page is changed by a sub-agent that takes minutes and spends the team's AI credits per page, so leave the other record pages alone unless the user asks, and say which ones you left.
- Skip views without a field list: CHARTS, PIVOT_TABLE and SINGLE_RECORD.

## 4. The list and the form

Work through the views one after another, never two calls on the same view at once: each call rewrites that view's whole field list, so parallel calls overwrite each other.
- `configure_view_fields` with `{ fieldName, enabled: true }` adds the field at the end of the list. Pass `fieldOrder`, naming every field still shown, only to put it somewhere else. On a layout that shows cards, an image field becomes the card picture with `heroImage: true`, placed first.
- `configure_form_fields` the same way for the new-record form. Mark it `required` only when the user said so. Skip calculated fields.

## 5. The record page

The record page is where users read a record and, after pressing Edit, change it. There is no separate edit form, so a field missing from the record page cannot be changed on existing records except inline in a list column.
- One `sections` call with the main view's `id` as `page` and a task like "Add the <display> field to the main Details section, keeping every field already there". Never run two `sections` calls at the same time.
- `get_page` cannot show which fields a section holds: rely on the summary `sections` returns.

## 6. Permissions

When a table has permissions on, each rule lists the fields its roles may read, create and update. A new field is in none of them, so app users with those roles do not see it, while admins do, the builder preview included.
- `list_permissions` for the table. With permissions off (`permissionsEnabled: false`), every app user sees the field and there is nothing to do. With permissions on but no rules, the table shows app users nothing at all, so there is nothing to grant: say so in the hand-over.
- When a rule lists the table's other fields but not the new one, add the field to it with `upsert_permission`: the rule's `ruleId` and `fields: { "<name>": { ... } }` with the access the rule gives its other fields (`{ read: true }` where they are read-only, `{ read: true, create: true, update: true }` where its roles create and update records), changing nothing else in the rule. Leave a rule out when the request says its roles should not see the field.
- Say in the hand-over which rules now include the field and with what access, so the user can narrow it.

## 7. Publish and hand over

- The field itself is live at once. List, form and record-page changes are saved to the draft: when the app has been published before, they reach app users only after `publish_project`, which also releases every other pending change in the project, so ask before running it. A never-published app already serves them.
- Hand over in product words: the field, the pages it now shows on, the record pages you left alone, any permission rules you changed, and whether publishing is still needed.
