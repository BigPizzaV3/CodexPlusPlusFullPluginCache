# What happened and what is waiting

Topic `daily_brief` · version 2026-10-23 · served by `uirix_guide({ "topic": "daily_brief" })`.

Reporting a day or a week of an agent to its owner from one read: conversations, leads and other outcomes, quality, what still waits for a person, money, and what needs attention. What each figure counts, and how to say it in a few lines.

```
GUIDE daily_brief: what happened, what is waiting, what needs attention

GOAL
The owner knows in one short answer what the agent did in a period, what still waits for a person, and whether anything needs attention. Every number is one the server counted.

FACTS THAT MISLEAD
- get_briefing resolves the period itself, in the account's time zone: never compute dates for it. The week starts on Sunday in Israel and on Monday elsewhere.
- When period.time_zone_source is "phone", "language" or "default" the zone was assumed. If you know the owner's zone, call again with it.
- A period still running (today, this week, this month) is compared with the same stretch of the one before, so "up 20%" is fair.
- total counts customer conversations. no_customer are the ones nobody spoke in: silence, voicemail, an answering system, a failed call. dashboard_sessions are the owner's own tests and are in no other figure.
- unresolved means the customer left without what they came for. A captured lead or a hand-over to a person is not unresolved.
- Leads, tickets and orders are counted from what the agent actually recorded, once per conversation.
- waiting looks back 30 days whatever the period: an old lead nobody handled is still waiting.
- needs_you (since 23 Oct 2026) lists the calls that stopped on a decision only the owner can take, whatever the period, until decide_call records the answer. Open the briefing with them, one line each, before the figures.
- Test conversations are in no figure.
- Money is in USD. days_left projects the balance at the spending of the last 7 days and is absent when nothing was spent.

READ FIRST
- get_briefing(period, agent_id): one call. Leave agent_id out for the whole account.
- Only when the owner asks for more: list_outcomes for the people behind a number, get_conversation for one conversation, get_metrics for a breakdown by day or by agent, get_usage for costs by month or channel.

ASK
Which period, only when the owner did not say: today is the default. Nothing else.

APPLY: the daily brief
1. get_briefing for the period.
2. Open with what needs a person: the attention items, critical first, then what is waiting: how many leads or requests nobody handled and the oldest, follow-ups that are due or overdue.
3. Then the numbers in one or two lines: conversations against the period before, by channel only when more than one is used, leads and other outcomes recorded, quality when conversations were rated.
4. Then training: when training.recommended is true say why in one line (training.reason) and offer the fix named there. When it is false say nothing, or one reassuring line.
5. Money only when it matters: a balance that lasts less than a week, paid actions that are blocked, or when asked.
6. Close with one offer, the most useful next step: go over the waiting leads, read the weakest conversation, fix the action that failed.

APPLY: what needs my attention
get_briefing for today. Report attention and waiting only, most severe first, each with what it costs the business and what you recommend. When the agent has setup findings that need fixing now, offer the setup review.
An attention item whose code starts with privacy_ is a privacy or call-compliance setting the account's calls require and that is not in place (the account's, whatever the agent): say it in one line and offer to go through it, get_privacy with the privacy playbook.

PRESENT
- About 8 lines. Numbers in the owner's words: "41 conversations, 6 new leads, 3 still waiting for a call back".
- No field names, and no ids except a conversation the owner asked about.
- A block marked unavailable was not read: say which permission is missing instead of reporting zero.
- A quiet period is an answer: "No conversations today so far."
- Never turn a small number into a trend: 2 against 1 is not "up 100%".

VERIFY
The figures come from one call: quote them as they are. When two figures seem to disagree (leads recorded in the period against leads waiting), say what each one counts.

MONEY
Free: every tool named here.

MISTAKES TO PREVENT
- Dates computed by you and passed to other tools to rebuild the briefing.
- A change proposed from one bad conversation.
- Customers' personal details listed when the owner asked only "how was today".
- Dashboard sessions or silent calls reported as customers.

STOP WHEN
The owner has the picture and knows the one thing worth doing next.
```
