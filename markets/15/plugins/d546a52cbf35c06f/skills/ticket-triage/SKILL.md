---
name: ticket-triage
description: Triage an AssistLoop agent's support tickets. Use when the user asks which tickets need attention, wants a ticket summarized, assigned, reprioritized, closed or noted, or wants to email a ticket's customer.
metadata:
  short-description: Find, summarize and update support tickets
---

Help the user work through the support tickets of one AssistLoop agent.

1. Find the agent. If the user did not name one, call `list_agents` and ask which agent
   to use. Ticketing must be on for that agent; if it is off, say so and stop.
2. Find the tickets with `list_tickets`. Use its filters instead of reading every
   ticket: `status` (open, in_progress, resolved, closed), `priority` (low, medium,
   high), `assigned_to` (`me`, `unassigned`, or a teammate id) and `q` for words in the
   subject. Show each ticket's number, subject, status, priority and assignee.
3. For one ticket, call `get_ticket`, then `list_ticket_messages` for the conversation
   with the customer and `list_ticket_comments` for the team's internal notes. Summarize
   what the customer needs and what has already been done. Quote, do not invent.
4. To change a ticket, call `update_ticket` with only the fields that change: status,
   priority, subject or `assigned_to`. For a teammate, take the id from
   `list_ticket_assignees`; do not guess it from a name. Teammates are notified, the
   customer is not.
5. To leave a note for the team, call `add_ticket_comment`. Customers never see notes.
6. To email the customer, first make sure you have the right ticket. If more than one
   ticket matches what the user named, list them (number, subject, requester) and ask
   which one.
   - If the user's message contains the email text itself, after a colon or in quotes
     (for example "Email the customer on this ticket: ..."), call
     `reply_to_ticket_customer` right away with exactly that text. Do not add a greeting
     or sign-off or change its wording; if you would change anything, use the next case.
   - Otherwise, show your draft and call `reply_to_ticket_customer` only after the user
     approves the exact text.
   It is sent at once and cannot be taken back; tell the user which ticket and address it
   went to. If the ticket has no customer email address, say that the reply cannot be
   sent.

Create a ticket with `create_ticket` only when the user asks for a new one.
Report what each change returned. If a tool refuses (no access, ticketing off, a plan
limit), say what it said and stop; do not retry with other ids.
