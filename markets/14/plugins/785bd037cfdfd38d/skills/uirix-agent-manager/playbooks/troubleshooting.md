# Troubleshooting: from the symptom to the fact

Topic `troubleshooting` · version 2026-10-03 · served by `uirix_guide({ "topic": "troubleshooting" })`.

The complaints owners bring and the read that settles each: the agent does not know something, invents, did not send the lead, the widget does not show, calls fail or hang up, a build or a refresh failed, a webhook did not arrive, money ran out. Facts first, one fix at a time, then the proof.

```
GUIDE troubleshooting: from the symptom to the fact

GOAL
A complaint becomes a fact the server states, the fact becomes one fix the owner approves, and the fix is proven before the owner is told it is solved.

FACTS THAT MISLEAD
- The agent answers from the knowledge SUMMARY, never from the documents. "I added the document" without the paid refresh (reindex_kb) changes nothing. get_kb_status: pending_sources and the summary version.
- A capability switched on is not a capability that works: the setup review says per channel whether the tool runs (works / stub / no_handler / not_offered) and whether its detail is set. The agent may tell the customer it did something the platform never did.
- No lead e-mail does not mean no lead: list_outcomes shows what the agent recorded; the e-mail depends on the notification address and switch (finding notification_email_missing).
- A conversation with a wrong answer is the evidence, not a feeling: get_conversation shows the exact words, the tool turns and the summary's agent_quality issues.
- "The agent hung up" on an outbound call is in the transcript: get_conversation of the call; the profile's script decides the ending (call_profiles).
- A webhook that "did not arrive" has a delivery row: list_deliveries by endpoint and status says delivered, pending (retrying) or failed with the receiver's answer.
- Money: get_account says whether calls can be placed and why not, what is left of today's limits, and the balance. A paused agent is often a balance.

READ FIRST
get_agent_setup (findings first), then the read the symptom calls for below. Never fix before the fact is read.

SYMPTOMS AND THE READ THAT SETTLES THEM
- "It does not know X" / "it says the wrong price": get_kb_summary (is X there, correct?), get_kb_status (pending sources, stale summary), one get_conversation where it happened. Fix: knowledge playbook (add the fact or correct the summary, then the paid refresh), or a rule in the instructions when the fact is there and the agent ignores it (improve playbook).
- "It invents things" / "it promises what we do not do": the conversation first. Then: a capability switched on that does not work (capability_not_operational), a focus topic the business has no knowledge for, or a tone too eager. Fix: switch the capability off, add knowledge, a rule (improve playbook).
- "We did not get the lead": list_outcomes for the day (did the agent record it?), then the setup review's notification finding. Recorded and no e-mail: the address or the switch (update_agent_setup notifications). Not recorded: the lead action is off, blocked by a missing detail, or not offered on that channel (setup review).
- "The widget does not show": get_widget (on, token, domains include the site, install code), then whether the code is on the page (the owner checks). Fix: channels playbook.
- "The build failed" / "the agent is stuck": get_build_status (step, error). A build interrupted long ago: the setup review says so (agent_not_built or build interrupted). Fix: rebuild playbook, from the step that failed.
- "The refresh did nothing": get_kb_status.last_job and its error; a summary over its size with many long documents. Fix: knowledge playbook.
- "Calls fail" / "nobody is called": get_account (can_place_calls, calls_blocked_reason, limits), the agent's phone number (setup review), then get_call of one call (status, error) or the campaign report. Fix: the reason named: balance, no number, a profile finding (get_profile), a window that excludes now.
- "The agent hung up" / "it was rude on the call": get_conversation of the call, the profile's script and findings (get_profile). Fix: call_profiles playbook (goodbye rule, voicemail line, opening line).
- "The webhook did not arrive": list_deliveries filtered by endpoint and status. Fix: automations playbook (the receiver's error, replay, re-enable).
- "A connected tool errors": get_briefing tool_problems (failed actions with counts and sample conversations), then the setup review of that capability (detail, connector). Fix: the detail or the connector, then a test.
- "It is slow / quality dropped": get_briefing quality and training; weekly_review playbook.
- "It stopped answering at all": get_account (balance, status), get_agent_setup (enabled, build), get_widget (enabled).

APPLY
One fix at a time, from the playbook the symptom points to, after the owner's yes for anything paid or overwriting. Say which fact you found before you propose it.

VERIFY
The same read that showed the fact shows it gone, and a test_chat (or a test call, when the owner agrees to the cost) reproduces the original complaint and now passes. Only then say "solved".

MONEY
Paid, only as the fix and after the owner's yes: reindex_kb (the knowledge refresh); a rebuild or a test call are paid too and belong to their playbooks. Metered like a chat: test_chat. Free: get_agent_setup, get_briefing, get_conversation, list_conversations, get_kb_status, get_kb_summary, get_build_status, get_widget, get_account, list_deliveries, get_call, get_profile, list_outcomes, update_agent_setup, uirix_guide.

MISTAKES TO PREVENT
- Fixing from the complaint without the conversation or the status that proves it.
- Rebuilding the agent as a first move.
- "Solved" without the proving test.
- Blaming the model when a capability is switched off, a detail is empty or the balance is out.
- Reading a transcript to the owner at length: the one wrong sentence and the fact behind it.

STOP WHEN
The fact behind the complaint is named, the fix is applied with the owner's yes, and the proof is in hand.
```
