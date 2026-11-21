---
name: seating-and-door
description: Seating tables, guest-to-table assignment, check-in counts, guest name search, and basic event date/name updates for Invitio events.
---

# Seating and door day

Help with tables, check-in, finding guests, and light event edits.

## Steps

1. Resolve `evento_id` with `list_events` if needed.
2. Pick tools by intent:
   - Find someone → `search_guests`
   - Door stats → `get_checkin_summary` (and `update_guest` for `checked_in` if needed)
   - Tables → `list_mesas`; add with `create_mesa`; edit with `update_mesa`; remove with `delete_mesa`; seat guests with `assign_guest_to_mesa`
   - Rename / reschedule → `update_event` (name/date/time only)
3. Confirm results from tool JSON; do not invent table or guest IDs.

## Rules

- Never invent mesa or guest IDs.
- Writes need owner/admin/editor; lector is read-only.
- Do not send WhatsApp or email.
