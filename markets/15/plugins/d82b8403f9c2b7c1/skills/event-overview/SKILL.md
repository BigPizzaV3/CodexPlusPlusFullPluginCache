---
name: event-overview
description: Summarize the user's Invitio events or upcoming event. Use when they ask about my events, próximo evento, overview, or what events I have.
---

# Event overview

Help the user understand their Invitio events.

## Steps

1. Call `list_events`.
2. If there are no events, say so clearly.
3. If there are multiple events, prefer the soonest upcoming by `date` (or ask which event if dates are missing/ambiguous).
4. Call `get_event_summary` for the chosen `evento_id`.
5. Reply with a short bilingual-friendly summary: event name, date/time, plan, and RSVP totals.

## Rules

- Never invent events or guest counts — only use MCP tool results.
- Do not claim WhatsApp messages were sent.
- Owners and collaborators see only events they can access.
