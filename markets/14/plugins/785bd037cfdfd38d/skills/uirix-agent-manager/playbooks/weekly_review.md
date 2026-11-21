# Weekly review

Topic `weekly_review` · version 2026-10-02 · served by `uirix_guide({ "topic": "weekly_review" })`.

A short, honest review of an agent's week for its owner: volume, results, quality with what repeats, three conversations worth knowing, and at most three fixes, each with its evidence and the place it is made.

```
GUIDE weekly_review: one page on the week, and up to three fixes

GOAL
Once a week the owner gets a short, honest review: what the agent handled, what it brought in, where it fell short, and at most three fixes worth making, each with its reason and where it is done.

FACTS THAT MISLEAD
- get_briefing with period last_week is the closed week (Sunday to Saturday in Israel, Monday to Sunday elsewhere) against the week before it. this_week is the week still running.
- Quality scores exist only for conversations summarised since the score was introduced: a small number of rated conversations is a fact to state, not a problem.
- The issues named on a conversation (unanswered_question, no_next_step and the others) are judged from the transcript by a model. They say where to read. They are not proof.
- A fix needs evidence from more than one conversation, or one failure that matters a lot: an action that failed, a wrong price.

READ FIRST
- get_briefing(period last_week, agent_id).
- The conversations it names as evidence: get_conversation, at most 10 in all. Start with the training signals, then the weakest conversations.
- get_agent_setup only when a fix touches the setup: an action that fails, a missing detail.

ASK
The closed week, or the week so far? Default: the closed week. One agent or all of them? Default: the current agent.

APPLY
1. get_briefing for the week.
2. Read the evidence: for each signal, two or three of its conversations. Note what the customer wanted and what the agent did.
3. Write the review, in this order:
   - Volume: conversations against the week before, by channel.
   - Results: leads, tickets, orders, meetings, and how many still wait for a person.
   - Quality: the average and how many were rated, then what repeats, in plain words, with one example.
   - Three conversations worth knowing: the best one, the worst one, the most unusual one. One line each.
   - Money: what was spent, and how long the balance lasts when it is short.
4. Propose at most three fixes, most valuable first. Each: what is wrong, what it costs the business, the fix, and where it is made:
   - a missing or wrong fact: Knowledge.
   - a behaviour: one improvement rule, under Improve the agent.
   - an action that failed or lacks a detail: Agent setup.
   - a change nobody tested: a run of the saved test questions.
5. Ask which fix to start with. One at a time.

PRESENT
- One screen: about 15 lines. No tables unless the owner asks.
- Numbers with their base: "quality 4.1 of 5 over 23 rated conversations".
- Say plainly when the week was good: "Nothing needs fixing this week."
- When the owner wants it for the team, give the same review as a message they can copy, without customers' personal details.

VERIFY
Every figure in the review appears in the briefing. Every fix names the conversations that support it.

MONEY
Free: every tool named here. A fix may cost (a knowledge refresh, a rebuild, a run of the test questions): say so when you propose it.

MISTAKES TO PREVENT
- More than three fixes, or a fix without evidence.
- A trend claimed from a handful of conversations.
- The whole briefing read out instead of a review.
- A change applied during the review without a yes.

STOP WHEN
The owner read the review and chose a fix to start with, or chose to change nothing.
```
