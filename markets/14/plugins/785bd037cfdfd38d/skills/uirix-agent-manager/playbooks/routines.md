# Routines: scheduled tasks that use UiriX

Topic `routines` · version 2026-10-06 · served by `uirix_guide({ "topic": "routines" })`.

A task the owner repeats as a scheduled task of this client: the morning briefing, the night's leads into the CRM, the weekly review, a document sync. The rules of a run nobody watches (idempotent, bounded, no money, prepare and ask), the permissions, ready prompts.

```
GUIDE routines: scheduled tasks that use UiriX

GOAL
The owner's recurring work runs by itself in this client at the agreed time, does exactly what was agreed, never sends anything twice, never spends money without a yes, and leaves a short report the owner reads in the morning.

FACTS THAT MISLEAD
- A routine is a feature of the CLIENT (Claude scheduled tasks and Claude Code routines, ChatGPT scheduled tasks, Gemini scheduled actions), not of UiriX. UiriX sees ordinary tool calls. You write the prompt; the owner saves it in the client's scheduler.
- An unattended run stops or fails when a tool needs an approval the client did not grant. The owner must allow the UiriX reads (and mark_synced, add_document when the routine writes) in the client's settings, and the other app's tools the routine uses.
- A run that spends money unattended is a mistake even when the owner would have said yes: the routine prepares (a draft, a list, a briefing) and the owner approves in the chat.
- Idempotency comes from the marks and the keys: list_outcomes with not_synced_to, add_document with source_key. A routine without them duplicates.
- Bound every run: at most N objects per run (50 is a sane default), and say in the report when more remain.
- The period must be stated in the prompt (yesterday, last_7_days), and the time zone is the account's: get_briefing handles it.

READ FIRST
- The task done once by hand in this chat, with the owner, so the mapping and the rules are settled before they are frozen in a prompt.
- The client's scheduler and its permission settings (the owner shows them, or you describe where they are).

ASK
1. Which task, how often, at what local time.
2. The bound per run, and where the report goes (the chat of the run, a channel, a mail).
3. Which writes the routine may do by itself (marks, documents) and which it must only prepare.

APPLY: write the routine
1. Start from the ready prompt below, fill the agent, the labels, the period and the bound.
2. Add the rules every routine carries: read first, never spend money, never create without searching, mark every hand-over, stop at the bound, report counts and ids, say "nothing new" when there is nothing.
3. Give the owner the prompt and the list of permissions to grant in the client. Ask them to run it once by hand and show you the result.
4. Check the first run's report against the data (list_outcomes). Fix the prompt before the second run.

READY PROMPTS (fill the brackets)
- Morning briefing: "Call get_briefing for yesterday for agent [agt_...] (or the whole account). Write at most 8 lines in [language]: conversations and the change, leads and what waits for a person with names, what needs attention, money only if the balance is low. Send it to [channel or mail]. No tool names, no ids."
- Leads of the night into the CRM: "Call list_outcomes with not_synced_to [label], types lead and callback, for agent [agt_...], at most 50. For each: search the CRM by e-mail then phone; update or create the contact, add a note with the summary and the conversation link, add a task for [name]. After each success call mark_synced with destination [label] and the record id; on failure status failed with the reason. Report created / updated / failed with ids. Spend nothing."
- Weekly review: "Call get_briefing for last_week for agent [agt_...]. Write the review as in the weekly_review playbook: figures and the change, quality and what repeats, three conversations worth knowing (summaries), at most three fixes with who does what. Save it to [document] and post the link to [channel]. Change nothing on the agent."
- Document sync: "Read [document] in [app]. Compare with the UiriX document of source_key [key] (list_documents, its date). If it changed, call add_document with the same source_key and keep_verbatim [true/false], then tell the owner a refresh (reindex_kb, paid) is needed and do NOT run it. Report changed or unchanged."
- Who called today (personal assistant, evening): "Call get_briefing for today and list_conversations since this morning for agent [agt_...]. At most 6 lines in [language]: who called, what they wanted, how urgent, a callback number only when they left one. Offer a callback or an errand for each; place no call."
- My errands this week (personal assistant, Sunday morning): "Call list_errands with period this_week for agent [agt_...]. At most 6 lines in [language]: what is still pending (when, with whom), what happened (the result in one line each), what I must do or bring. Place no call."
- Who to call back (business, morning): "Call who_to_call_back for agent [agt_...]. At most 8 lines in [language]: who, why, since when. Place no call."

VERIFY
- The first run by hand: the report matches list_outcomes; the second run reports "nothing new" or only what is new.
- A week later: no duplicate in the destination, no object left unmarked that the routine handled.

MONEY
Paid, and never called from a routine: reindex_kb, create_call, call_for_me, rebuild_agent, build_profile. A routine prepares and asks. Free: get_briefing, list_outcomes, mark_synced, list_errands, list_conversations, add_document, list_documents, uirix_guide.

MISTAKES TO PREVENT
- A prompt without the not_synced_to filter or without marks.
- An unbounded run over a long backlog.
- A routine that calls reindex_kb, create_call, call_for_me, rebuild_agent or build_profile: a callback or an errand is offered in the report and placed only after the owner's yes in the chat.
- Freezing a task in a prompt before it was done once by hand.
- A report that says "done" without counts and ids.

STOP WHEN
The owner saved the routine, granted the permissions, saw one good run by hand, and knows what it may and may not do.
```
