---
name: update-guests
description: Create or update Invitio guests — RSVP status, attendance check-in, name, and party size. Use when the user asks to confirm a guest, mark no-show, check in, rename, or add a guest.
---

# Update guests

Change guest RSVP and details using write tools.

## Steps

1. Resolve the event with `list_events` if needed.
2. Resolve the guest with `list_guests` (filter by status/name) unless the user already gave `guest_id`.
3. Choose the right tool:
   - RSVP only → `update_guest_status`
   - Name / adults / children / checked_in / status → `update_guest`
   - New guest → `create_guest`
4. Confirm the updated guest JSON to the user.

## Rules

- Prefer MCP tools; never invent guest IDs or claim a change without a successful tool result.
- Do not request or store phone numbers (tools do not accept them).
- Lector collaborators can list guests but cannot write — if a write fails for permissions, explain that.
- Do not send WhatsApp or email.
