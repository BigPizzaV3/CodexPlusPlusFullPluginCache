---
name: get-started
description: First steps with Supahost — check what this connection can do, then show today's arrivals and the conversations waiting for a reply.
---

# Get started with Supahost

1. Call `check_permissions` first. It says which organization is connected and
   which tools this connection holds. Tell the host in one line.
2. Show today's arrivals with `search_bookings` (check-in date = today, in the
   organization's timezone), then the conversations waiting for a reply with
   `list_conversations`.
3. Offer next steps: draft a reply, create a cleaning task, or a revenue summary
   for this month.

Rules:

- Always confirm with the host before sending anything to a guest
  (`send_message`, scheduled messages (`send_scheduled_message_now`) or approved
  WhatsApp templates, broadcasts). Draft first with `draft_message` and show the
  text.
- Never invent a booking, guest, property, date or price. Read it from the
  tools; if nothing matches, say so.
- Payments, police/guest registration and smart-lock setup are not available in
  this connection. Point the host to the Supahost app for those.
