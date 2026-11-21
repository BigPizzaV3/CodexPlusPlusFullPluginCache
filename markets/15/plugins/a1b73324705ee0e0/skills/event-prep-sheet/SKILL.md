---
name: event-prep-sheet
description: Build a prep sheet for the coming days' events from Excellent — host, timing, rooms, party size, seating, the event's custom fields, the menu the documents state (and where they disagree), what's still owed, and the staff on shift — and, when asked, seat a table or fill in a custom field, each change undoable. Use for "prep sheet for this week's events", "what do we need to know for Saturday's wedding", "BEO rundown", "seat the Smith party at table 4", "mark the Adler wedding as nut-free".
---

# Event prep sheet

This skill reads, and on request seats tables and fills in an event's custom fields, each change undoable. To
draft a missing or stale BEO, proposal or contract, use the `build-event-documents` skill.

## 1. Collect

1. `agenda` — default 7 days, or the window the person names (`from`, `days`, `location`). Take every event in
   `dates`.
2. For each event, `get_event` with its `event_id`. Use:
   - the event's date, time window, party size, venue and rooms;
   - its contacts, host first;
   - the menu: the contract's or proposal's menu of record and each BEO's, and the `differences` where they
     disagree;
   - its documents with status and signature;
   - its money: each invoice's total, paid and balance, and installments still owed.
3. For each event, `event_setup` with its `event_id`: the floor-plan tables in its booked rooms (label, room,
   capacity, and the seats and seating label assigned for this event) and the group's event custom fields
   (label, type, whether required, and this event's value).
4. For staffing, `schedule_week` (or `schedule_today` for a single day) at that venue. If the schedule module
   is not switched on, skip staffing and say so.

## 2. Write one sheet per event

- **Header**: title, date and time at the venue's clock, venue and rooms, party size.
- **Host and contacts**: name, role, how to reach them.
- **Menu**: the menu of record; then a clear **Menu mismatch** list if any document disagrees.
- **Seating**: each seated table with its label and seats, and the seats assigned against the party size.
- **Details**: each custom field with its value (for example dietary needs, a cake order, a parking count).
- **Paperwork**: contract signed or not, latest BEO version and status.
- **Money**: total, paid, balance, next installment due. If `price_tbc_count` is above zero,
  `total_is_partial` is true or `rates_pending` is true, say the total is not final; never quote it as the
  whole price.
- **Staffing**: who is on during the event by role, open shifts, uncovered stretches.
- **Watch-outs**: unsigned contract, menu mismatch, balance due before the date, open shifts, fewer seats
  assigned than guests, a required custom field with no value.

Amounts arrive in minor units (cents): divide by 100. Mark sample data (`is_sample: true`).

Offer, don't do: fixes happen in Excellent by a person (chasing a signature, finalizing a document). If an
event has no BEO, or its BEO disagrees with the contract, offer to draft a fresh one with the
`build-event-documents` skill.

## 3. Seat a table or set a field (if asked)

**Before every change,** say exactly what you will change — the table or field, the old value and the new
one — and wait for a yes, unless the person already asked for that exact change. **After every change,** give
the `change_id` it returned and say it can be undone.

- **Seating:** `set_table_seats` with the `event_id`, the `table_id` from `event_setup`, `seats` (0 clears the
  table) and an optional `label` ("Smith party"; left out, the table keeps its label). It is refused past the
  table's capacity and for a table outside the event's booked rooms. After seating, read back the seats
  assigned against the party size.
- **Custom field:** `set_event_custom_field` with the `event_id`, the field's key from `event_setup` as
  `field`, and `value` as text matching the field's type — text, a number, `true` or `false`, a `YYYY-MM-DD`
  date, or one of a select field's options. Leave `value` out to clear it; every other field keeps its value.

Safety: the sheet only reads. A table's seats or a custom field change only on the person's yes, and each
change returns a `change_id` that `undo` puts back, once, for 30 days unless the record has changed since.
Nothing is sent, signed, charged or deleted.
