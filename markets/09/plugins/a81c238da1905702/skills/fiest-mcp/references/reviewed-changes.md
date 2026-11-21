# Reviewed changes through Fiest MCP

Tool availability depends on consent, current role/page access, restaurant
features, and deployment gates. A skill does not enable any of these. Use the
actual connection's tool schemas, exact returned targets, and current versions.
Even read-only planning tools can require a write scope and an enabled workflow.

## Menus and catalog imports

Read `list_menus` and `find_menu_items` to resolve menu/item UUIDs. For an import,
read `get_catalog_import_guide` and `get_catalog_creation_capabilities`; inspect
an existing target with `get_catalog_import_target`. Normalize the source into
the supported create-only model, preserving options and other semantics. Ask
about missing facts or unsupported structures instead of flattening them.

Call `plan_menu_import` and show the exact target, entities, counts, warnings,
and omissions. Apply only the unchanged approved plan through
`apply_menu_import`, with its plan hash and UUID idempotency key. Reconcile an
uncertain result with `get_menu_import_result`. Imports remain inactive drafts;
activation is a separate approved change.

`create_menu` creates one inactive draft. `add_existing_items_to_menu` attaches
reviewed existing items to an inactive draft. For a targeted edit, inspect
`get_draft_menu_item_edit_target`, then use `update_draft_menu_item` with its
opaque current version and only the approved fields. Shared or live items are
not eligible for direct draft editing. Changed versions need another inspection.

`set_active_menu` and `set_online_menu` change the POS or online menu. Read the
current selection and exact target immediately before proposing activation.
Review counts and all schema-required preconditions. Approval to import or edit
never also approves activation. Re-read state after an uncertain response.

## Menu schedules

`get_menu_schedule` shows which menu runs when on each channel: `online` is
online ordering and the Fiest app, `pos` the POS tills (only when
`posFollowsSchedule` is true). Every time is the restaurant's own local time
in its returned `timeZone`, never the user's; say so when you state times.
Each channel has a usual menu; weekly windows put another menu on for part of
the week, and a date switch makes a menu the usual menu from a date on.

Read the schedule, then show the exact change in plain words (channel, menu
name, days, local times, entry replaced or removed) and wait for approval.
Choose the separate tool exposed by the connection for the approved change:

| Change | Tool |
| --- | --- |
| Add a weekly window or future date switch | `add_menu_schedule_entry` |
| Replace one existing entry | `update_menu_schedule_entry` |
| Remove one existing entry | `remove_menu_schedule_entry` |
| Change a channel's usual menu | `set_usual_menu` |
| Switch a channel's live menu until the next changeover | `switch_menu_now` |
| Enable or disable POS schedule following | `set_pos_schedule_following` |

Use the selected tool's input schema, `confirmed=true` and one retained UUID
`idempotencyKey`, with only returned `menuPublicId` and entry `id` values.
Replacing an entry replaces its whole contents, so preserve fields the user
did not ask to change. Carry the reviewed live or usual menu in
`expectedCurrentMenuPublicId` or `expectedUsualMenuPublicId` when required.
If it changed, `staleState` requires another read and approval.
`switch_menu_now` holds only until the next scheduled changeover; to make a
change last, change the usual menu or the entries. Use `update_menu_schedule`
only for an older connection that exposes it without the matching separate
tool; it retains the same approval and retry rules. A refused change changed
nothing. After a timeout, retry the identical request through the same tool
with the same key, or read the schedule first. Read it again afterwards to
confirm the result.

## Tasks

Read `get_task_workspace` with `view=all` and `status=all` for exact targets
before editing or reconciling. Follow `nextOffset` with the unchanged revision
when more rows are available. Use only returned assignee IDs and editing flags.
Tasks must be enabled for the restaurant and MCP environment; writes need their
separate task-write scope and workflow gate.

`create_task` creates a task or anytime/date/daily/weekly routine.
`update_task` replaces a complete task draft, so preserve every field the user
has not asked to change. Times are restaurant-local; distinguish event time
from a due-by deadline. Protected routines require the restaurant owner.

`set_task_completion` completes or reopens today's eligible occurrence. It
cannot complete a future task or routine that is not due today.
`delete_task` removes one task or recurring definition, stopping future work
while retaining historical records. Show the selected task and recurrence.

After approval, pass `expectedRevision`, the restaurant-local day,
`confirmed=true`, and one retained UUID idempotency key. A revision/day change
needs a fresh workspace and approval. After a timeout, re-read and retry only
the identical request with the same key.

## Opening hours

Read `get_opening_hours` and review the complete seven-day schedule, including
closed days, split shifts, and overnight closing. `replace_opening_hours`
requires the current version hash, complete week, confirmation, and a UUID
idempotency key. Replacement does not change schedule mode. A Google-managed
schedule cannot be replaced here. Re-read after stale or uncertain results.

## Payment-method corrections

This changes bookkeeping allocation, not a charge, refund, sale, VAT amount,
or provider settlement. Read `get_payment_correction_workspace` for a business
day or bounded calendar month, and choose the exact source payment identity.
A parent tab may contain several payments; never guess its intended leg.

For a correction, call `preview_payment_correction`, then apply the approved
preview through `apply_payment_correction`. For an undo, call
`preview_undo_payment_correction`, then apply through `undo_payment_correction`.
Follow the actual input schemas, including the required action. An older
connection may expose undo preview only through `preview_payment_correction`
with `action=undo`; use that compatibility path only when its schema supports
it and the separate undo-preview tool is absent.

Show the before/after report and reason, then wait for explicit approval before
either apply tool. Preserve fingerprint, revision, expiry, input, confirmation,
and a UUID idempotency key. Changed or incomplete evidence needs review; never
invent VAT or source amounts.

Read accounting and payment reports again afterwards. A stale, voided, or
changed original source may prevent undo. An undo reverses only the allocation
transfer, not the underlying sale or payment-provider record. Missing or disabled
correction access is not a reason to change an order through another interface.
