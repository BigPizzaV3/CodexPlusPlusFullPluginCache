---
name: move-the-pipeline
description: Move leads and events along Excellent's pipeline in plain words — set a lead's status, snooze or assign it, move an event to tentative, confirmed, completed or lost, change its guest count, title, host or rooms, turn a room hold into an event — each change undoable. Use for "move this lead to tentative", "confirm the Adler wedding", "mark the gala lost", "snooze this inquiry until Monday", "assign the Kim lead to Maria", "they're 80 now, not 60", "the Kim hold on the terrace is a booking now", "Dana Kim and Dana Kim-Lee are different people".
---

# Move the pipeline

This skill changes leads and events in Excellent, one narrow change at a time, each undoable. It never sends
anything to a guest, takes a payment or deletes a record.

**Before every change,** say exactly what you will change — the record, the old value and the new one — and
wait for a yes, unless the person already asked for that exact change. **After every change,** give the
`change_id` it returned and say it can be undone.

## 1. Find the record

`search` what the person names (`kind: "lead"` or `"event"`), or `get_event` when you have the id. For an
event, read back its title, date, stage, guest count and room before changing it.

## 2. Make the change

| The person says | Tool |
|---|---|
| "mark this inquiry contacted / qualified / lost" | `set_lead_status` (`new`, `contacted`, `qualified`, `lost`) |
| "snooze it until Monday" | `snooze_lead` with `until` (an ISO instant; leave it out to unsnooze) |
| "give it to Maria" / "I'll take this one" | `assign_lead` (`user_id` of a team member; leave it out for the person themselves) |
| "this lead is real, make it an event" | `convert_lead_to_event` |
| "move it to tentative / confirm it / it's done / we lost it" | `set_event_status` |
| "they're 80 now" | `set_event_guest_count` |
| "call it the Adler–Kim wedding" | `rename_event` |
| "the host is Dana Kim now" | `set_event_host` (`party_id` of a contact, or `host_name` + `host_email`) |
| "add the planner, Jo, to the event" | `add_event_contact` (`party_id`, `role`) |
| "move them to the Garden Room, 6 to 11" | `book_room` |
| "they want the Hall too, for dinner" | `set_event_rooms` (every extra room as `{ space }`; the list replaces the current extra rooms) |
| "the Kim hold on the terrace is a booking now" | `convert_hold_to_event` (`hold_id` from `space_availability` or `agenda`; optional `title`, `party_size`) |
| "Dana Kim and Dana Kim-Lee are different people" | `dismiss_duplicate_contacts` (two to twenty `{ party_id }`; nothing is merged or changed on them) |

A lead moved to an event's stage goes through `convert_lead_to_event` first, then `set_event_status`.
Converting a hold makes a tentative event in the hold's room and window, its holder the host; the holds queued
behind it move up. It is refused while another hold is ahead of it, and once it has been released or has
lapsed.

If a change is refused — a hold on the room, a double booking, a block, capacity — say why in plain words and
offer what would work. Never retry around a refusal.

## 3. Wrap up

List each change with its `change_id`. If the person asks to take one back, use `undo` with that id (see the
`undo-a-change` skill).

Safety: each change is made only on the person's yes and returns a `change_id` that `undo` puts back, once, for
30 days unless the record has changed since. Nothing is sent to a guest, charged or deleted.
