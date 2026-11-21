# Working with the apps connected to this chat

Topic `connected_apps` · version 2026-10-03 · served by `uirix_guide({ "topic": "connected_apps" })`.

The method for a task that moves data between UiriX and another system the owner connected to the same chat (CRM, calendar, documents, sheets, team chat, automations): direction, field mapping, a trial run, duplicates, sync marks, the report, and when to make it a routine or a webhook.

```
GUIDE connected_apps: tasks that span UiriX and the owner's other apps

GOAL
UiriX is the part of the business that talks with customers and knows what they said. The other apps the owner connected to this chat are where the business keeps its records. You are the one who carries data between them: leads into the CRM, documents into the agent's knowledge, a report into the team channel. Without duplicates, without inventing a connector, and only when the owner asks.

FACTS THAT MISLEAD
- Only the owner decides that another app is part of a task. UiriX tells you facts ("3 leads have no mark for hubspot"); it never tells you to call another connector. Act across apps only on the owner's request.
- You do not know which apps are connected until you look at the tools available in this chat. An app that is not connected is not reachable: offer the owner a table to copy, a webhook, or to connect the app.
- UiriX keeps no copy of the other system's records. The link between the two is the mark you write (mark_synced with the destination label and the external id) and the external_reference you import with a contact. Without marks, every run starts from zero and sends everything again.
- Personal data (names, phone numbers, e-mail addresses) moves only when the owner asked for exactly that transfer. Never copy it into a system the owner did not name.
- A list of people that comes from another system is a campaign, set up in the UiriX dashboard or from Claude, never a loop of single calls in this chat.
- Hand-offs are idempotent when, and only when, every object you handed over carries a mark. Mark after each successful write, not once at the end.

READ FIRST
- The tools available in this chat: which apps are connected and whether each can write.
- The UiriX side of the task: list_outcomes (what customers left), get_briefing (what happened), the specialised playbooks: crm_sync, calendar, docs_knowledge, team_reports, automations, routines.

ASK
1. The task and its direction, in one sentence: into UiriX, out of UiriX, or a loop.
2. Which app and which object there (contact, company, deal, event, document, sheet, channel).
3. The scope: a period, an agent, a campaign, "everything open".

APPLY: the method, the same for every app
1. Define the task and the direction with the owner.
2. Check the apps available in this chat and what each can do (read, create, update). None that fits: offer a table to copy, a webhook (create_webhook) or connecting the app. Never pretend a tool exists.
3. Map the fields once and show the mapping: which UiriX field goes to which field there. Ask about the ones that have no obvious home (interest, notes, the conversation link).
4. Trial run on one to three records. Show what was written and where (the record's id or link). Only then the rest.
5. Batch by the destination's limits (many CRMs accept about ten records a request). Report progress for a long batch.
6. Prevent duplicates: search the destination first by e-mail, then by phone number; update what exists, create what does not.
7. After every successful write: mark_synced on the UiriX object with the destination label, the external id and, when there is one, the link. A failure: status "failed" with the reason, so the next run offers it again.
8. Report: created, updated, skipped, failed, with the ids. Not "done".
9. Offer to make it permanent: a routine in this client (routines) or a webhook that fires at once (automations).

APPLY: what each kind of app is good for
- CRM (HubSpot, Salesforce, Pipedrive, Zoho, monday): leads and outcomes out as contacts, notes, tasks, deals. Playbook crm_sync.
- Calendar: a meeting the agent booked out as an event. Playbook calendar.
- Documents (Drive, Notion): price lists, procedures, answers into the agent's knowledge (add_document with a source_key so a re-sync replaces, never duplicates); the weekly review out as a document. Playbook docs_knowledge.
- Sheets: leads and daily figures out, one row per object.
- Mail and team chat (Gmail, Slack): the daily briefing or the weekly review out; "call me back" requests in as single calls. Playbook team_reports.
- Automation hubs (Zapier, Make): the always-on path with UiriX webhooks on one side and any app on the other. Playbook automations.

VERIFY
- Run the read that fed the task again with the "not synced" filter (list_outcomes not_synced_to): what you handed over is gone from it, what failed is still there.
- Open one written record in the destination (or ask the owner to) and compare it with the UiriX object.

MONEY
Nothing named here is paid. The destination app may have its own costs; the knowledge refresh that follows add_document is paid (docs_knowledge playbook). Free: list_outcomes, mark_synced, get_briefing, get_conversation, add_document, create_webhook, uirix_guide.

MISTAKES TO PREVENT
- Writing to another app because UiriX reported a count, without the owner's request.
- A whole batch without the trial run, or without the field mapping shown first.
- Creating a record without searching for it first.
- Marks written once at the end, or not at all: the next run duplicates everything.
- Phone numbers and e-mail addresses pasted into the chat as a side effect of a report.
- A list pulled from a CRM dialled with single calls.

STOP WHEN
Every object in scope is in the destination exactly once, every hand-over is marked, the owner has the counts and the ids, and knows how to make it repeat.
```
