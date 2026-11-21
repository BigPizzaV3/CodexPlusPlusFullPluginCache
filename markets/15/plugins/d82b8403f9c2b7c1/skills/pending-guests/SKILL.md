---
name: pending-guests
description: List guests still pending RSVP and draft reminder text. Use for quién falta, pendientes, follow-ups, or reminder drafts.
---

# Pending guests

Help the organizer follow up with guests who have not confirmed.

## Steps

1. Resolve `evento_id` via `list_events` if needed.
2. Call `list_guests` with `status: "Pendiente"`.
3. List guest display names (and party size if present).
4. Optionally draft a short reminder message the user can copy — do **not** claim it was sent.

## Rules

- Never invent guest names.
- Do not expose or request phone numbers (tools do not return them).
- Do not send WhatsApp or email; drafting text only.
