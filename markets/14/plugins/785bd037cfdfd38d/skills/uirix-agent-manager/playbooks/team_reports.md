# Reports to the team, requests from the team

Topic `team_reports` · version 2026-10-03 · served by `uirix_guide({ "topic": "team_reports" })`.

Sending what UiriX knows to where the team reads: the daily briefing or the weekly review into a channel, a mail or a document, a lead hand-over with a mark, an alert; and the other way: a "call this person back" request from the team becomes a call. What to include, what never to include.

```
GUIDE team_reports: reports to the team, requests from the team

GOAL
The people who act on what the agent hears get it where they already read, in a few lines, with what they must do. The owner does not copy numbers by hand, and a request the team writes in its channel becomes a call the agent places.

FACTS THAT MISLEAD
- A report is a text you write from get_briefing (and list_outcomes for the leads); UiriX has no report sender. The channel, mail or document tool is the one connected to this chat.
- The briefing is computed in the account's time zone and compared with the period before; use its figures as they are and name the period.
- Personal data in a team channel is a decision of the owner: by default a lead hand-over names the person and what they want, and puts the phone number only when the owner said the channel is for that.
- A hand-over without a mark is handed over twice tomorrow. mark_synced with destination = the channel's label ("slack", "team_mail") after the message was sent, or "owner" when the owner took it.
- An escalation alert is an event the agent produced (a human requested, an escalated conversation in the briefing). You see it when the briefing or the outcomes run; for the instant version offer a webhook (automations playbook).

READ FIRST
- get_briefing(period, agent_id or account): the figures, what waits, what needs attention.
- list_outcomes(open_only, not_synced_to "<channel label>") for a lead hand-over.
- get_conversation only for the conversations worth a line (an escalation, a complaint).

ASK
1. Where (which channel, address or document) and for whom (what they can act on).
2. What goes in: figures only, leads with contact details or without, the weekly fixes.
3. How often, and whether to make it a routine.

APPLY: the daily briefing to the team
1. get_briefing for yesterday (or today at the end of the day).
2. Write at most 8 short lines in the team's language: conversations and the comparison, leads and what waits for a person (names and what they want), quality in one line when it changed, what needs attention, money only when the balance is low. No tool names, no ids.
3. Send it with the connected tool. Report that it was sent and where.

APPLY: a lead hand-over
1. list_outcomes open_only, not_synced_to = the channel's label.
2. One line per lead: who, what they asked for, when, the conversation link; phone and e-mail only by the owner's rule. For a named colleague, a task in the tool the team uses.
3. After sending: mark_synced on each outcome with the channel's label and the message or task id. The next run offers only the new ones.

APPLY: the weekly review to the team
Run the weekly_review playbook, then send the page: the figures, three conversations worth knowing (summaries, not transcripts), at most three fixes with who does what. As a document when the owner keeps a place for it.

APPLY: a request from the team
"Call Dana back about the invoice" in the team channel: confirm with the owner that such requests may become calls (once, as a rule), then single_call playbook: create_call with the person, the number, the goal in the briefing, the explicit yes, get_call until it ends, the result back in the channel where the request came from.

VERIFY
- The message or document exists where the team reads (the tool's answer, or the owner's look).
- list_outcomes with not_synced_to = the label is empty after a hand-over.

MONEY
Paid, explicit yes first: create_call places a real call. Free: get_briefing, list_outcomes, get_conversation, mark_synced, get_call, uirix_guide.

MISTAKES TO PREVENT
- Pasting the whole briefing JSON or a transcript into the channel.
- Phone numbers in a channel the owner did not approve for them.
- A lead handed over twice because no mark was written.
- Figures for a period other than the one named.
- A call placed from a team message without the owner's rule for it.

STOP WHEN
The team has the report where it reads, every hand-over is marked, and the owner knows how to make it repeat.
```
