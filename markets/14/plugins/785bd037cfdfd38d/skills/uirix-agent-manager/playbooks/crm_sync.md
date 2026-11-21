# Leads and call results between UiriX and a CRM

Topic `crm_sync` · version 2026-10-03 · served by `uirix_guide({ "topic": "crm_sync" })`.

The CRM loops in this chat: new leads and outcomes into the CRM as contacts, notes and tasks, and the result of a single call written back onto the CRM record. Field mapping, duplicates, marks, batches, the speed-to-lead call. Calling a CRM list is a campaign, set up in the UiriX dashboard.

```
GUIDE crm_sync: leads, lists and results between UiriX and the owner's CRM

GOAL
Every lead the agent takes lands in the CRM once, with what the customer said and a task for a person. A call the agent places for a lead lands back on the right record. Calling a list the business keeps in the CRM is a campaign, set up in the UiriX dashboard or from Claude. Nothing is typed twice and nothing is sent twice.

FACTS THAT MISLEAD
- A UiriX lead is an outcome row (list_outcomes), not a row in a leads table. It carries contact (name, phone, e-mail, company), details (interest, notes, items), the conversation id and a short summary. The full transcript is in get_conversation.
- The contact fields are what the customer said. A missing e-mail is missing; do not invent one for the CRM.
- One outcome per conversation and action, with the corrected details when the agent recorded it twice. Do not create two CRM contacts for one conversation.
- The link between the two systems is the mark: mark_synced on the outcome with destination = the CRM's label (one label, always the same spelling, e.g. "hubspot") and external_id = the CRM record id. list_outcomes with not_synced_to = that label is exactly the work left.
- Many CRMs accept about ten records per request. Batch, and report progress.

READ FIRST
- Whether the CRM is connected in this chat and whether it can create and update contacts, notes, tasks and deals.
- list_outcomes(agent_id or account, not_synced_to "<label>", type lead or every actionable type): what is new since the last run.

ASK
1. The CRM label to use for the marks (once; keep it forever).
2. The mapping: UiriX name, phone, e-mail, company, interest, notes, summary, conversation link -> which CRM fields; whether to add a note with the summary and a task for a person, and for whom.
3. For a list out of the CRM: say that calling it is a campaign, set up in the UiriX dashboard or from Claude.

APPLY: loop 1, new leads into the CRM
1. list_outcomes with not_synced_to = label. Say how many and of which types.
2. For each (trial on the first two, then batches): search the CRM by e-mail, then by phone. Found: update what is new and add a note with the summary, the channel, the date and the conversation link. Not found: create the contact with the mapped fields, then the note. Add a task for the person who follows up when the owner asked for tasks.
3. mark_synced after each successful write: destination label, external_id = CRM record id, external_url when the CRM gives one. On a failure: status "failed" and the reason.
4. Report created / updated / failed with ids. Offer the routine "leads of the night" (routines).

APPLY: loop 2, a CRM list into a campaign
Not in this chat: importing a list and calling it is a campaign, set up in the UiriX dashboard or from Claude. Say so in one line, and never dial the list with single calls.

APPLY: loop 3, results back to the CRM
1. The result of a single call (speed to lead) is its conversation: get_conversation, with the summary, what was agreed (promises, dates, amounts) and what is left to do. A campaign's results are read in the UiriX dashboard.
2. Write to the lead's record: a note with the summary and the outcome, a field or a deal stage when the owner mapped one, a task for the follow-up. "Do not call again": the CRM's do-not-call flag, and add_dnc when the agent did not add the number itself.
3. Report what was written and where.

APPLY: speed to lead
A new CRM lead that should be called within minutes: create_call for one person (single_call playbook) with the lead's facts in the briefing, then loop 3 for its result. A whole segment every morning is a campaign, not a loop of calls.

VERIFY
list_outcomes with the not_synced_to filter again: empty but for the failures. Open one CRM record and compare.

MONEY
Paid, explicit yes first: create_call places one real call. Free: list_outcomes, get_conversation, mark_synced, add_dnc, uirix_guide.

MISTAKES TO PREVENT
- Creating a CRM contact without searching first.
- A label spelled two ways ("HubSpot", "hubspot"): the server lower-cases labels, but "hub_spot" and "hubspot" are two destinations.
- Writing the whole transcript into the CRM note. The summary and the link are enough.
- Dialling a CRM list with create_call per row.
- Reporting "synced" for rows whose write failed.

STOP WHEN
No open outcome is left without a mark for the CRM, except the failures the owner knows about.
```
