---
name: eventhex-response-style
description: How to respond when operating EventHex — id discipline, real links only, batch reporting, destructive-action confirmation.
---

# Response style — golden rules

How the AI client should behave and reply when using EventHex tools.

1. **Resolve ids first, never guess.** Every event-scoped tool needs an `eventId` from `list_events`. Same for `ticketId` (`list_tickets`), `speakerId` (`listSpeakers`), `sessionId` (`listSessions`), section ids (`list_sections`). If the user names an event ambiguously, list and confirm the match.
2. **Echo what you acted on.** When you create, update or delete something, state the event title and the ids involved (eventId, ticketId, …) in your reply, so the user can verify and reuse them.
3. **Never invent or guess URLs.** `create_event` returns `websiteUrl`; `publish_website` / `improve_website` return `url` — share that exact link. Otherwise call `get_event_domains(eventId)`. After creating or publishing a site, ALWAYS give the user the real link.
4. **Destructive actions need explicit user intent.** `delete_event`, `delete_ticket`, `delete_speaker`, `deleteSession`, `eventhex_resource` deletes — only when the user clearly asked for that exact deletion; restate what will be deleted before doing it. Never delete to "clean up" on your own.
5. **Batch tools report per item.** `create_speakers`, `create_sessions`, `createAgendaBatch` create each item independently — read the per-item results and report failures item by item, not "done".
6. **Don't assume currency or timezone.** Amounts are in the event's configured currency; session times use the event's timezone. State times/dates the way the tool returns them.
7. **Missing scope = tell the user which one.** On `Connector key missing required scope: X`, say the connector key lacks `X` and it must be enabled in EventHex connector settings — don't retry.
8. **Prefer dedicated tools.** Use `eventhex_resource` only for long-tail entities that have no dedicated tool.
9. **Check before you re-create.** Before creating events/tickets/speakers that may already exist, list first and update instead of duplicating.
10. **Data answers cite scope.** Analytics replies should say which event and which measure (e.g. "registrations, all participant types" vs "paid attendees") — `get_franchise_summary` counts ALL participant types.
