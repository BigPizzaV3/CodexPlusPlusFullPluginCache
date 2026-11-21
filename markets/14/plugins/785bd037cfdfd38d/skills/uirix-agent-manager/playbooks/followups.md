# Leads and follow-ups

Topic `followups` · version 2026-10-02 · served by `uirix_guide({ "topic": "followups" })`.

Going over what customers left with the agent and nobody handled yet: leads, tickets, orders, callback requests, promised follow-ups. Who is waiting, for what and since when, what to do first, and how to record what was handled so it is not offered again.

```
GUIDE followups: leads and requests that wait for a person

GOAL
Nobody who left details with the agent is forgotten. The owner sees who is waiting, for what and since when, decides what to do with each, and what was handled is recorded so it is not offered again.

FACTS THAT MISLEAD
- The platform has no lead list of its own. A lead, a ticket, an order, a message for accounting, a callback request: each is what the agent recorded during a conversation. list_outcomes reads them.
- One row per conversation and action. When the agent recorded it twice (a corrected phone number), the row carries the last version and recorded_times says so.
- contact is what the customer said. A field the customer did not give is empty. On a phone call caller_number is the line they called from: it may differ from the number they asked to be called on.
- open true means no mark says anyone handled it or recorded it anywhere. It does not mean nobody called: only that nobody said so here.
- A mark is the memory between sessions. Without it the same lead is offered again tomorrow.
- The lead e-mail the business receives is separate: an outcome can be open here although the e-mail was read.
- Meetings, transfers and RSVPs are outcomes too, for counting. They need no follow-up and are not in the waiting list.

READ FIRST
- list_outcomes(agent_id, open_only true): who is waiting, newest first. The default window is 30 days.
- get_conversation(conversation_id) before advising on one: the summary on the row is short.

ASK
Nothing to start. Per lead, only when the owner wants to act: "Did you already call her back?"

APPLY: go over what is waiting
1. list_outcomes with open_only true. Say how many, by type, and the oldest.
2. Present each in one or two lines, oldest first, at most 10: who (name, business), what they asked for, when, on which channel, and what the business owes them. Phone and e-mail when the owner is about to act, not as a list of personal data.
3. Recommend an order: a promised callback and an angry customer first, then leads by age.
4. For each one the owner says is done: mark_synced with destination "owner" and a short note (who handled it). For spam or a duplicate: status "skipped" with the reason.
5. Report what is left.

APPLY: follow-ups that were promised
get_briefing lists the follow-ups whose date is today or past (waiting.action_items_due). For each: read the conversation, say what was promised and to whom. When the owner confirms it was done, mark the conversation with mark_synced, destination "owner".

APPLY: a list for someone else
When the owner wants the list for a colleague: the same rows as a table (name, phone, what they want, when), in the owner's language, as a message they can copy. Write the marks only after the owner confirms the hand-over happened.

VERIFY
After marking: list_outcomes with open_only true again. The marked ones are gone and the count dropped by exactly that number.

MONEY
Free: every tool named here.

MISTAKES TO PREVENT
- Marking as handled something the owner only looked at.
- One mark for the whole list after a partial hand-over: mark what was done, leave the rest open.
- A lead reported as "new" because of its date when its row is already marked.
- Contact details pasted in bulk when the owner asked a general question.
- Advice on a lead from its row alone when the conversation says more.

STOP WHEN
Everyone waiting was handled, marked or consciously left, and the owner knows how many remain.
```
