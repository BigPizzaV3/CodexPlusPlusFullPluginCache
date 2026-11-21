---
name: data-modeling
description: "Use to design, create or evolve the workspace's objects (their fields, choices and relations), install a template, or read and write their records."
---

# Designing the workspace's objects

An object is a stable business concept the workspace tracks: subscribers, contracts, cases, tasks. Each object is a real table; a record is one of its rows; a field is one of its columns. The workspace's objects as a whole are its structure. A template is a set of objects and fields provided by the platform, which a workspace installs and extends.

## Start from the business

First understand what is tracked, the decisions the user wants to make and the questions they will ask. An Excel file, a sheet or a PDF is a source of information, not a structure to reproduce.

- Create an object for a concept that has its own life (status, deadlines, owner) and that is listed, filtered or counted.
- Never create an object simply because a new document arrives: reuse the object that already represents the same concept.
- Do not duplicate information in several places and do not store a computable value without an explicit reason.

## Choosing fields

- text: A short text: a name, a number, a code. multiple:true holds several, each its own (a company's IBANs, a partner's other names): only values with no data of their own, permanent like the type.
- long_text: A free text, over several lines.
- integer: A whole quantity.
- number: A decimal quantity; a percentage is stored in points from 0 to 100.
- money: An amount, stored in cents in the <key>_cents column.
- date: A calendar day, as YYYY-MM-DD.
- datetime: A precise instant.
- boolean: A yes or no.
- choice: A closed list of values (status, category), multiple:true to pick several. Each value has a permanent key and a label.
- relation: Points at a member (kind member), a group (kind group) or a record of another object of the workspace (kind object, with its key). The <key>_id column holds the id pointed at. The inverse side is not declared: a subscriber's contracts are found through the relation of the contract object.
- email: An email address, validated and clickable. The platform finds a record's addresses by this type.
- phone: A phone number, stored in international format (+33612345678), validated and clickable. The platform finds a record's numbers by this type.
- A collection that has its own life (lines, deadlines, many contacts) becomes a related object, never a list in a field.
- files:true attaches several files to each record, { max: 1 } a single one.

## Keys and labels

- Object and field keys are English snake_case, whatever the user's language, 20 characters at most, and describe the meaning of the data: effective_date, monthly_premium. They are permanent: they name the table and the columns.
- What the workspace creates beside templates starts with x_: an object it creates (x_broker), and a field or a choice value it adds to a template's object (x_prev_insurer). The fields of an object the workspace created take no prefix. A template's keys never start with x_.
- Labels (label, label_plural, the labels of fields and choices) are in the user's language and can change at any time.
- title_field names the visible text field that names a record wherever it appears: a name, a number. Every object has one.
- required applies only to information truly essential to the concept. Unknown information stays empty: never invent a value missing from a source.

When several reasonable choices would durably change the workspace structure, ask for clarification. For a reversible detail, make a consistent choice.

# Changing the workspace structure

## Before creating

1. Call list_objects: it returns the workspace's objects with their complete definitions, and the proposed templates.
2. If a proposed template fits the need, install it rather than recreating its objects.
3. Reuse an object that already represents the same concept and evolve it; only create a new object for a new stable concept.

## Creating or evolving an object

configure_objects applies a change of the structure at once: the templates to install, then the objects to create or replace. Send every template and object of a change in one call, so the user sees and approves it as a whole, as a plan; objects created together may point at one another. Always send each object complete, all its fields included, starting from the definition returned by list_objects. Never describe the change in text beforehand: the approval shows it.

- The order of the fields list is the display order: keep it when sending the object back, move a field in the list to reorder it.
- Renaming an object, a field or a choice value: change only its label, never its key.
- Adding a field or a choice value: add it to the definition.
- A field's type does not change: for another type, add a new field.
- A field missing from the sent definition is deleted with its data: only remove a field on explicit request. A field or an object of a template cannot be deleted: disable it with is_hidden:true, its data remains.
- remove_object deletes an object created by the workspace with all its records: only on explicit request.

A refusal returns error with the reason: fix the definition and call the same tool again.

# Reading and writing records

Records are read and written with the data tools, like any other data of the workspace.

- inspect_data_model gives the exact name of an object's table and of its columns, with the label of each field. A table is named by its object's key and a column by its field's key; an amount is in <key>_cents, a relation in <key>_id. Always use the names it returns.
- query_data reads records in SQL: object tables are written without a schema, like the others.
- insert_rows creates records, update_rows updates them and delete_rows deletes them. owner_workspace_group_id, required, is the group that owns the record (an id of workspace_groups); the responsible member is the one who creates the record.
