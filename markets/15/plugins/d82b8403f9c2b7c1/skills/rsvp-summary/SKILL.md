---
name: rsvp-summary
description: Break down RSVP status for an Invitio event. Use for confirmados, pendientes, NoAsistira, asistencia, or RSVP summary requests.
---

# RSVP summary

Give a clear Confirmado / Pendiente / NoAsistira breakdown.

## Steps

1. If `evento_id` is unknown, call `list_events` and pick or clarify the event.
2. Call `get_event_summary` with that `evento_id`.
3. Present counts for confirmed, pending, and declined parties, plus total adults/children when available.

## Rules

- Only use tool data.
- If the user lacks access, explain that the event was not found or access was denied.
- Keep the answer concise and actionable.
