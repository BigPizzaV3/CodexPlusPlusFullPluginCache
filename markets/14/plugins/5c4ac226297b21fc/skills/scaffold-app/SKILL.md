---
name: scaffold-app
description: 'Turning a project that has data but no useful pages into a usable app: which tables deserve a page, creating the tables and fields first when the data only exists as a description, one view per table in navigation order with its list fields, form and record page, the navigation itself, and what to check before handing over. Load before building an app from a connected source, from existing tables or from scratch.'
---

# Scaffolding a Noloco app from its data

The job: take a project that has data but no useful pages and leave it an app people can open and work in. One well-chosen view per table that matters, a record page behind each, a new-record form that asks for the right fields, and a navigation that starts with the table the team opens most. Load `build-views` with this skill: it chooses each view's layout and settings.

## 1. Survey before you plan

- `list_projects`: the `projectName`, and `canBuild` must be true.
- `list_tables`: every table with its `fieldsCount` and `primaryField`. A table synced from an external source (Airtable, Google Sheets, a database) carries a `source` naming that source's type; a Noloco table has none. `dataSources` lists those sources.
- `get_table_schema` on each table you will build for. Field types and option values decide the layout (a SINGLE_OPTION status field makes a BOARD, dates make a CALENDAR or TIMELINE), and relationships decide which related lists belong on a record page.
- `list_pages`: what the app already has. Never create a second view for a table that has one; configure the existing view with `upsert_view` and its `pageIdentifier` instead.
- `list_records` with `first: 1` on the main tables: a BOARD or CALENDAR of an empty table renders empty, so you need to know which tables have data.
- `list_version_history`: whether the app has ever been published, which decides the last step.

## 2. Decide what to build

Before the first write, decide in product words what each table gets, one line per table ("Deals: board by stage. Tasks: calendar by due date. Companies: cards."), plus the navigation order and anything you will skip. Writes take effect at once, so settle these choices up front: tables and fields have no draft, and on an app that has never been published app users see a page as soon as it is saved.

Which tables get a page:
- Every table the team works in day to day. A pure lookup table (statuses, categories, countries) gets none: its values are reached through the records that use them.
- From a connected source with many tables, pick at most 7 by these criteria and tell the user which tables you left out:
1. Core business entities users will view and update regularly
2. Tables with rich data (more fields typically means more important)
3. Prefer operational tables over pure lookup/reference tables (e.g. prefer "Projects" over "Project Statuses")
- Any table the user named comes first, in the plan and in the navigation.

## 3. The schema, only when the data is not there yet

When the user describes the app instead of pointing at tables, create Noloco tables first. Never add fields to a table with a `source`: its schema belongs to that source, so the field is added there and syncs in.
- `upsert_table` per table, parents before children (Companies before Deals) so relationship fields have a target.
- `upsert_field` per field. INTEGER or DECIMAL for numbers with the matching format in `typeOptions` (currency, percentage), DATE with a date or date-time format, SINGLE_OPTION with its `options` (a status field is what makes a BOARD and a STAGES section possible), OBJECT with the matching `format` (fullName for a person's name, phoneNumber for a phone number, address for an address), TEXT single-line by default and multi-line only for notes. A link to another table is `type: "<its tableName>"` with `relationship: MANY_TO_ONE` on the child table (Deals link to a Company); the reverse field appears on the parent by itself.
- `upsert_table` again with `primaryField` set to the name-like field once the fields exist, so a record is shown by its name wherever it is referenced.
- Sample records only on Noloco tables, and only when the user wants to see the app with data: a handful per table through `create_record`, named so they are obviously samples. A link field takes the related record's id, or a list of ids for a many link; an option field takes the option's stored name, its display in upper snake case ("In progress" is `IN_PROGRESS`); an OBJECT field takes an object with the sub-field keys `get_table_schema` reports. A connected source's rows live in that source; never write samples into it.

## 4. One view per table, in navigation order

`upsert_view` with `data.tableName` creates the view, its record page and its new-record form in one go, and takes the layout and every other setting in that same call. Create views one after another, never two in parallel, in the order the navigation should have: a new view lands at the end, and views created in parallel land in whatever order they finish. In the creating call set the layout and its companion settings (see `build-views`), `sort.orderBy` to the field users expect, `buttons.newButtonText` naming the record ("Add deal") and `filterFields.search` on tables users look things up in. On a TIMELINE, GANTT, CALENDAR, MAP, BOARD view also set `setup.recordTitle` to the name-like field; the other layouts reject it.

The view is named after its table and gets a random icon: follow up with `update_page_settings` for a fitting `icon` (a common Tabler icon name: Briefcase, Users, Calendar, Truck; an unknown name renders blank) and, when the table's name is not what users call the page, a `name`.

## 5. The list and the form

- `configure_view_fields`: a new view shows the table's first fields, which is rarely the best set. Keep the few high-signal fields (status, owner, date, amount), chosen from the schema you read in step 1; on a CARDS, BOARD or COLUMNS view put the image field first with `heroImage`. Where `setup.recordTitle` is set it is already the card's heading, so leave that field out of the list.
- `configure_form_fields`: the form starts with the table's first ten editable fields. Keep the ones a person fills in when creating the record, mark the essential ones `required` and drop the rest.
- One call per view and per tool, with every change in it. Changes merge onto the fields already there, so a field you drop stays until you pass `{ fieldName, enabled: false }` for it, and the complete `fieldOrder` lists every field still shown.

## 6. Record pages

A new view's record page starts with a sensible default: a STAGES section on the field a new BOARD is grouped by, or else on a single-option field named like a status, stage, phase or step (none when the table has neither), HIGHLIGHTS for its first numbers and dates, DETAILS for the other fields and lists of related records. Leave it on secondary tables. On the one or two tables the team opens most, hand the page to `sections` with the business context (what the team does, which fields matter day to day, which related records belong on the page) in one call per page. Never run two `sections` calls at the same time: each can take a few minutes and spends the team's AI credits.

## 7. Navigation

App users land on the first page of the navigation, so put the table they work in most first (`update_page_settings` with `position`). Group reference tables into a folder (`create_navigation_item` with `type: FOLDER`, then `parentPage` on each page) or hide a page with `hidden: true` when its records are only ever reached from other records. A placeholder page the app already had is deleted with `delete_page` only when the user asked for it: nothing asks for confirmation.

## 8. Check, then hand over

- `list_pages` once to confirm the pages, their order and their routes. A page whose layout depends on a field (BOARD, CALENDAR, TIMELINE, GANTT, MAP, CHECKLIST) deserves one `get_page` with `include: ["viewSettings"]` to confirm the field is set.
- `publish_project` only when the app has been published before (the version history from step 1): then the new pages wait in the draft until it runs. A never-published app already serves them. Say which case applies.
- A table with permissions off shows every record to every app user, who can also edit it; a table with permissions on shows a role nothing until it has a rule. `list_permissions` says which case each table is in. Leave access for a follow-up unless the user asked for it; `upsert_permission` sets a rule per table and role when they do, and turns that table's permissions on.
- Hand over in product words: each page and what it shows, what you skipped and why, and the natural next steps (roles and permissions for app users, workflows, a dashboard).
