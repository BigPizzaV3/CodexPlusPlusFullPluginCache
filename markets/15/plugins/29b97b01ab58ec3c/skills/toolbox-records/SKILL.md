---
name: toolbox-records
description: "Use when a FlatRate Pro technician asks to view their toolbox inventory, record an owned tool, or update a specific tool's condition, status, location, or purchase details."
---

# Toolbox records

Use the connected technician's inventory only. This is recordkeeping, not
purchasing, payments, loan enforcement, or proof that equipment is safe to use.
Explicit user instructions control which records and fields may change.

1. Call `listMyTools` for inventory questions or to identify a requested item.
   Report stored properties only; do not invent serial numbers, condition,
   calibration records, assignments, or checkout history.
2. Before an update, resolve the actual tool ID. Ask the user to distinguish
   duplicate names. Viewing inventory does not authorize a change.
3. For an explicitly requested new record, call `logTool` with the tool name
   and only supplied brand, cost/price, category, purchase date, or notes.
   Do not infer price or execute a purchase.
4. For an explicitly requested edit, call `updateTool` with that ID and only
   the supplied fields. `status` supports `available`, `checked_out`,
   `maintenance`, `retired`; `condition` supports `excellent`, `good`, `fair`,
   `needs_service`. "Needs service" is a condition, not a status.
5. Respect client write confirmations. State the server-confirmed changed
   fields and leave other properties untouched. Surface errors; do not retry
   non-idempotent `logTool` after an uncertain response without checking inventory.
6. Decline other-account inventory requests. If sign-in is needed, direct the
   user to client OAuth, never to credential sharing in chat.

Examples: "What's in my toolbox?" is read-only; "Move my wrench to Bay 2"
requires a unique item; "Buy a new scan tool" is outside this workflow.
