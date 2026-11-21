---
name: filters
description: 'Scoping what a collection view loads: hard-coded custom filters (the condition-group format, per-field-type operators, dynamic values) and the relative filter that follows a relationship from the signed-in user ("only my records"). Load before setting or changing either, and to pick between them.'
---

# List filters (the relative filter + custom filters)

A list has two always-on filters, both invisible to app users (unlike filter fields):
- The **relative filter** answers WHOSE records: the signed-in user's, or — for a list section on a record view — the page's record's. It is a path from that parent record to a multi-relationship field holding the list's records, where every hop before the last is a single relationship. The last field is either a reverse multi relationship — the `…Collection` fields ("tasksCollection", "team.projectsCollection") — or a forward multi relationship ("company.projects"). The list becomes the parent's related collection, so a record created or imported from it is linked to the parent automatically.
- **Custom filters** answer WHICH records: conditions on the list's own fields (field · operator · value), ANDed within a group and ORed across groups. A value may be static, a relative date, or a field of the parent record — but the parent is only something to compare against, and nothing gets linked.

When the ask scopes the list to the parent ("my projects", "this employee's requests"), use the relative filter if a path exists, rather than a custom condition whose value references the signed-in user or the page's record. Custom filters cover the rest: field values ("approved", "due this week"), OR ("mine or unassigned"), a comparison against a field of the parent ("same department as me"), or a list whose table has no single-relationship path from the parent. Use both when the ask does both — the conditions narrow the related records. Neither is a security boundary: the records stay reachable through other pages and the API, so restrict the table's permissions when the goal is access control.

Both live in upsert_view's `customFilters` group. On a top-level collection view the only context record is the signed-in user (there is no surrounding record); record-view list sections, which the sections agent configures in this same format, can also anchor at the page's record. Access control is upsert_permission's job, not a filter's.

## Relative filter — `customFilters.relativeFilter`

`{ "relativeFilter": { "path": "…" } }`: a relationship path from the SIGNED-IN USER's record to a multi-relationship field holding the view's records — the field itself ("projectsCollection") or single-relationship hops first ("company.projectsCollection"). `null` removes it. A read echoes it as `viewSettings.customFilters.relativeFilter`.

## Custom filters — `customFilters.filters`

`{ "customFilters": { "filters": [ … ] } }` REPLACES the whole set on every call, so read the current rows first (`filters` or `viewSettings.customFilters` from get_page) and send back every row the view should keep — rows you return unchanged are kept as they are.

Hard-coded filters narrow what a list shows for everyone; app users never see or remove them (unlike filter fields).

Format — condition groups, outer array ORed, inner arrays ANDed. `[]` clears every filter.
```json
[[
  { "fieldName": "status", "operator": "IN", "value": { "source": "STATIC", "value": ["OPEN", "IN_PROGRESS"] } },
  { "fieldName": "owner", "operator": "EQUAL", "value": { "source": "LOGGED_IN_USER" } }
]]
```

- `fieldName`: an internal field name from the LIST's table schema, plus `id`, `uuid`, `createdAt` and `updatedAt`, which schema reads omit but stay filterable.
- `operator` by field type — TEXT: EQUAL, NOT_EQUAL, CONTAINS, DOES_NOT_CONTAIN, EMPTY, NOT_EMPTY · INTEGER/DECIMAL/DURATION: EQUAL, NOT_EQUAL, GREATER, GREATER_OR_EQUAL, LESS, LESS_OR_EQUAL, EMPTY, NOT_EMPTY, IN, NOT_IN · DATE: EQUAL, NOT_EQUAL, AFTER, BEFORE, AFTER_OR_EQUAL, BEFORE_OR_EQUAL, EMPTY, NOT_EMPTY · BOOLEAN: TRUE, FALSE · SINGLE_OPTION/single relationship: EQUAL, NOT_EQUAL, EMPTY, NOT_EMPTY, IN, NOT_IN · MULTIPLE_OPTION/multi relationship: EMPTY, NOT_EMPTY, IN, NOT_IN · ARRAY: CONTAINS, DOES_NOT_CONTAIN, EMPTY, NOT_EMPTY.
- `value`: omit it for EMPTY/NOT_EMPTY/TRUE/FALSE, otherwise pass one of
  - `{ "source": "STATIC", "value": … }` — a literal; an array for IN/NOT_IN; internal option names for option fields; ISO 8601 for dates.
  - `{ "source": "LOGGED_IN_USER" }` — the signed-in user. Omit `path` when the filtered field is a user relationship ("only my records"); pass a user field path ("email", "manager.email") to compare a scalar field against it.
  - `{ "source": "CURRENT_RECORD", "path": "…" }` — a field of the record the surrounding record view shows (list sections inside a record view only). Reference a related record by the relationship field's own name, e.g. "userAccount", never "userAccount.id".
  - `{ "source": "RELATIVE_DATE", "token": "…" }` — DATE fields only. Tokens: today.now, today.start, today.end, week.start, week.end, month.start, month.end, year.start, year.end, or custom.<hour|day|week|month|quarter|year>.<ago|from>.<whole number>.

Filters read back as they are stored: `field` is the internal filter key (a relationship's is `<name>Id`), `result` holds the value or values, and a reference reads as `{ "id", "path" }` — `auth-wrapper` is the signed-in user, `<viewId>:VIEW` the surrounding record, `values` a relative date. Send rows back exactly as you read them to keep them, so you can change one row and leave the rest alone. Every row you send is validated either way, and a value only the app can read — a literal mixed with a reference — is kept as it is.

Rules specific to top-level collection views:
- CURRENT_RECORD is unavailable (there is no surrounding record); it only works in record-view list sections.
- A view cannot combine OR groups with the search box — disable `filterFields.search` first, or express the filters as one AND group.
