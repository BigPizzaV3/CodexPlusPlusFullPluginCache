---
name: action-buttons
description: Adding, editing or deleting record-view action buttons (delete, copy, navigate, run workflow, show message, add comment, create/update record) — per-action-type value examples.
---

# Action buttons on record views

A record view has two button rows, selected with the `location` parameter:
- `"record"` (default): the record buttons, shown on the record page (and on collection rows when `display.collection` is true). Any action type.
- `"navigation"`: the collection's top row, above the list. Only NAVIGATE and LOGIN_PUBLIC_USER can be authored there — no `display`, and record-dependent actions (DELETE, UPDATE, CREATE, ADD_COMMENT, ON_DEMAND) are rejected.

Manage both with:

- `upsert_action_button`: set `location`, then omit `actionButtonId` to CREATE a button or pass an id to UPDATE it. On update, omitted fields keep their value, and `actions` is the complete final list (see "Updating the actions of an existing button" below) — read the button, edit its `actions`, and send the whole list back.
- `delete_action_button`: removes a button by id and can't be undone, so only remove a button the user asked to delete; pass the same `location`.
- Get current buttons and their ids from `get_page` with `include: ["actionButtons"]` — it returns `actionButtons` (the record row) and `navigationButtons` (the top row).
- `display` controls where a record button shows: `{ "collection": true }` also shows it on collection rows (new buttons default to the record page only).
- Buttons INSIDE page sections (TITLE, DETAILS, NOTICE, ACTION_BUTTONS, COLLECTION) are SEPARATE storage — they belong to the sections editor (delegate to `sections`). A record view may already have an ACTION_BUTTONS section, which the sections editor can edit but cannot create; check `get_page` with `include: ["sections"]` before deciding where a button should go.

Action buttons run one or more actions when clicked. Values are written in the authoring format below — field, workflow and page references are validated and expanded on save, and every button/action gets a stable server id.

## Where action buttons live

1. **Navigation buttons** — a collection's top row (above the list). Only navigation-style actions work here: NAVIGATE and LOGIN_PUBLIC_USER are authorable.
2. **Record buttons** — the record object's button row: shown next to each record on the collection page and at the top of the record view (`display` picks where).
3. **Section buttons** — TITLE, DETAILS, NOTICE, ACTION_BUTTONS and COLLECTION sections each carry their own buttons.

These are separate storage locations — a page can have buttons in several of them at once, so read the current state before choosing where to add one.

## Button envelope

```json
{
  "buttonText": "Send invoice",
  "execution": "ONE_CLICK",
  "appearance": "primary",
  "icon": "Send",
  "notification": { "enabled": true, "text": "Invoice sent" },
  "actions": [{ "type": "ON_DEMAND", "workflow": "Send Invoice" }]
}
```

- `buttonText` is PLAIN TEXT only — never a segment array or a field reference.
- The other text values (`title`, `description`, `tooltip`, `notification.text`, message/body texts) accept a plain string or a segment array mixing static text and field references: `[{ "text": "Owner: " }, { "data": { "path": "owner.name" } }]`.
- `execution`: `MODAL` opens a confirmation dialog (`title`/`description`, and the form for CREATE/UPDATE); `ONE_CLICK` runs immediately. Defaults to MODAL when any action confirms or collects input (CREATE, UPDATE, DELETE, ADD_COMMENT, SHOW_MESSAGE), else ONE_CLICK.
- `visibilityRules` gate who sees the button, in the same shape as section visibility rules: `roleRule` (`WITH_ROLES` / `WITHOUT_ROLES`) with `roles` (role names or reference ids — stored and read back as reference ids), `type` (`INTERNAL` / `CLIENT`), `auth` (`LOGGED_IN` / `NOT_LOGGED_IN`), `deviceRule` (`DESKTOP` / `MOBILE`), `publicAppVisibility` (`PRIVATE` / `VISITOR` / `ALL`), `spaces` (space ids) and `customRules` — OR-of-AND condition groups whose `field` is a field on the button's table (by name, or by path through relationships such as `owner.email`) or a logged-in-user reference such as `{ "source": "LOGGED_IN_USER", "value": "role.name" }`. On an update the whole object is replaced, so send every rule to keep; `null` clears them. Unknown keys are kept and reported as a warning.
- Builder-only action types (VIEW, IFRAME, SCAN_BARCODE) cannot be authored; existing ones pass through edits untouched.

## Per-type examples

**DELETE** — deletes the record in scope (confirm via MODAL):
```json
{ "type": "DELETE" }
```

**COPY** — copies a field's value to the clipboard:
```json
{ "type": "COPY", "fieldPath": "email" }
```

**NAVIGATE** — link to a page, the page's new-record form, a URL, an email or a phone number:
```json
{ "type": "NAVIGATE", "navigate": { "pageIdentifier": "Projects" } }
{ "type": "NAVIGATE", "navigate": { "pageIdentifier": "Projects", "pageTarget": "newForm" } }
{ "type": "NAVIGATE", "navigate": { "url": "https://docs.example.com", "newTab": true } }
{ "type": "NAVIGATE", "navigate": { "email": [{ "data": { "path": "email" } }], "subject": "Hello" } }
```
Links to a specific record page are not supported — link to the view page instead.

**ON_DEMAND** — runs an ON_DEMAND workflow on the record; pass the workflow's name (it must belong to the record's table):
```json
{ "type": "ON_DEMAND", "workflow": "Send Invoice" }
```

**SHOW_MESSAGE** — displays a message in the dialog (MODAL execution only):
```json
{ "type": "SHOW_MESSAGE", "showMessage": { "message": "Contact support to change this", "buttonText": "Got it" } }
```

**ADD_COMMENT** — posts a comment (or internal note); `body` presets the text and is required for ONE_CLICK. `field` (a relationship) posts the comment on that linked record instead of the current one; the body still references the current record either way:
```json
{ "type": "ADD_COMMENT", "addComment": { "note": true, "body": "Escalated" } }
{ "type": "ADD_COMMENT", "field": "employee", "addComment": { "body": "Reviewed" } }
```

**LOGIN_PUBLIC_USER** — opens the login dialog for public (not-signed-in) users. Zero config; must be the button's FIRST action, runs as MODAL, and the app needs public access enabled:
```json
{ "type": "LOGIN_PUBLIC_USER" }
```

**CREATE / UPDATE** — creates a related record or updates the record in scope. `field` names a relationship on the record's table (the action then targets that related table; omit it to act on the record's own table). `formFields` reference the TARGET table's fields:
```json
{ "type": "CREATE", "field": "tasksCollection", "formFields": ["taskName", { "name": "dueDate", "required": true }], "redirect": false }
{ "type": "UPDATE", "formFields": [{ "name": "status", "hidden": true, "value": "Approved" }] }
```
A form field takes the same config as a field of the view's new-record form: `label`, `hidden`, `value`, `defaultValue`, `required`, `requiredConditions`, `conditions`, `placeholder`, `helpText`, `readOnly`, `width`, `optionsConfig` and `orderBy`.
A `value` or `defaultValue` can copy another field of the same form instead of a static value — the source field must also be in `formFields` (it can be hidden), must not take its own value from the form, and a relationship is read one hop deep:
```json
{ "type": "UPDATE", "formFields": [{ "name": "email", "hidden": true }, { "name": "contactEmail", "hidden": true, "value": { "source": "FORM_VALUE", "value": "email" } }] }
```
With ONE_CLICK execution there is no form, so every `formFields` entry needs `"hidden": true` and a preset `"value"`, and adding a key that only matters on a visible form (`required`, `requiredConditions`, `conditions`, `defaultValue`, `placeholder`, `helpText`, `width`, `readOnly`, `optionsConfig`, `orderBy`) is rejected. Such keys already stored on a field (set in the builder) are kept when you send them back.

**Updating the actions of an existing button** — `actions` is the button's COMPLETE final list, matched to the stored actions by `id`:
- Start from the button as read (every action carries its `id`) and edit that; never send only the action you are changing.
- An action whose `id` matches a stored action of the same `type` is merged onto it (changing the `type` replaces the action instead): keys you omit keep their stored value (`formFields`, `redirect`, `workflow`, …) and `null` clears a key. Send nested objects (`navigate`, `copy`, `showMessage`, `addComment`) whole.
- `formFields` merge the same way, matched by field `name`: keys you omit on a field are kept and `null` clears one. Form sections and custom components sent back by name are kept exactly as stored.
- **An action or form field missing from the array you send is REMOVED.**
- An action without an `id` is added as a new action. An `id` that is not on the button is rejected.
- Builder-made actions (VIEW, IFRAME, SCAN_BARCODE) are sent back as read to keep them; they cannot be created or changed here.

## Button keys
- `buttonText` — Button label — plain text only. Required when creating.
- `execution` — MODAL shows a confirmation dialog (with the form for CREATE/UPDATE); ONE_CLICK runs immediately. Defaults by action type.
- `appearance`
- `icon` — Tabler icon name (e.g. "Copy", "Send").
- `tooltip`
- `title` — MODAL execution: dialog heading.
- `description` — MODAL execution: dialog body text.
- `notification` — Success toast shown after the action runs.
- `display` — Where a record button shows: on collection rows and/or the record page.
- `visibilityRules` — Who sees the button: `roleRule` + `roles` (names or reference ids), `type` (INTERNAL/CLIENT), `deviceRule`, and `customRules` (OR of AND groups whose `field` is a field name, a path through relationships like "owner.email", or a logged-in-user reference { "source": "LOGGED_IN_USER", "value": "role.name" }). Read back as stored, roles as reference ids. On an update the whole object is replaced, so send every rule to keep; null clears them. Unknown keys are kept and reported as a warning.
- `actions` — The steps the button runs. Required when creating. On an update it is the COMPLETE final list, matched to the stored actions by `id` — an action missing from it is removed (omit `actions` to keep them all).

## Action keys by type
- `DELETE`
  - `field`
- `COPY`
  - `fieldPath` — Shorthand: name (or dot-path) of the field whose value is copied to the clipboard.
  - `copy` — Full form: the copied text as a segment array.
- `NAVIGATE`
  - `navigate` — Required when adding the action; omit on a matched action to keep it.
- `ON_DEMAND`
  - `field`
  - `workflow` — The ON_DEMAND workflow to run: its name or referenceId. Must belong to the action's table. Required when adding the action; omit on a matched action to keep it.
- `SHOW_MESSAGE`
  - `showMessage` — Required when adding the action; omit on a matched action to keep it.
- `ADD_COMMENT`
  - `field` — Relationship field naming the linked record the comment is posted on. Omit to comment on the current record. (The body text still references the current record either way.)
  - `addComment`
- `CREATE`
  - `field` — Relationship field naming the table the new record is created in (linked back to the current record). Omit to create in the current table.
  - `formFields` — Form fields shown in the modal (or preset when ONE_CLICK, where every entry needs hidden + value).
  - `redirect` — Navigate to the new record after creating it.
- `UPDATE`
  - `field`
  - `formFields` — Form fields shown in the modal (or preset when ONE_CLICK, where every entry needs hidden + value).
- `LOGIN_PUBLIC_USER`
