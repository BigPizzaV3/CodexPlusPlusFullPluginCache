---
name: get-started
description: First steps with TehProf Dialogs — see who is waiting for a reply, whom to call back and what is scheduled, then draft replies that go out only after the user confirms.
---

# Getting started with TehProf Dialogs

TehProf Dialogs is a shared inbox for WhatsApp, Telegram, MAX and phone calls. The connector works with
the signed-in user's own TehProf Dialogs account and sees exactly what that user sees.

1. Start with an overview: call `day_summary` for unanswered chats, missed calls and scheduled
   messages, or `conversations_unanswered` for who is waiting and for how long.
2. Open a conversation with `messages_read` before suggesting anything, and draft with
   `reply_suggest`. A draft is never sent by itself. A customer's voice note already transcribed in Dialogs
   reads as text; when its `transcript` says it is not, `voice_transcribe` turns it into text.
3. For callbacks use `calls_missed`; for the customer's CRM record and deal use the CRM tools; to look someone up in the CRM with no
   conversation open, `crm_search` finds contacts, companies, deals and leads and `crm_record` opens one (both read
   as the user's own CRM account). `crm_funnel_load` counts the deals sitting on each funnel stage right now and `crm_stage_deals` lists the deals on one stage (title, amount, responsible, link). `crm_customers_top` ranks the best customers by won deals and `manager_crm_work`
   shows each manager's CRM work (activities, overdue tasks, deals with no next step); both need the Analytics tab right.
4. Anything that reaches a customer or changes the CRM (`message_send`, templates, moving a deal,
   completing a conversation) is a destructive action: show the user what will happen and wait for
   an explicit "yes".

Answer in the user's language. Never invent customers, numbers or deals: if a tool returns nothing,
say so.
