---
name: get-started
description: First steps with TehProf Support — see open tickets, overdue SLA and the team's workload, read a ticket and draft an answer that goes to the customer only after the user confirms.
---

# Getting started with TehProf Support

TehProf Support is a helpdesk for service teams: tickets from WhatsApp, Telegram, email and
Bitrix24, SLA, a knowledge base and analytics. The connector works with the signed-in user's own
Support account and sees exactly what that user sees.

1. Start with an overview: `tickets_list` for open tickets, `analytics_sla` for overdue ones,
   `analytics_dashboard` for the team's day.
2. Open a ticket with `tickets_get` before suggesting anything; look for an answer with
   `knowledge_search`.
3. `tickets_note` adds an internal note that customers do not see.
4. Anything that reaches a customer or changes a ticket's state (`tickets_reply`, `tickets_complete`,
   reassigning, changing settings) is a destructive action: show the user what will happen and
   wait for an explicit "yes".

Answer in the user's language. Never invent tickets, customers or numbers: if a tool returns
nothing, say so.
