---
name: decision-support
description: Compare 2-8 concrete options when costs, benefits, risks or competing interests require judgement. Use for requests to weigh pros and cons, compare suppliers, assess launch timing, choose project or staffing plans, or check an AI agent's proposed action. Eevo evaluates consequences separately for each affected stakeholder and shows where interests agree or conflict. Also use when Eevo is requested explicitly. Not for factual lookups, taste-only choices, simple arithmetic, or decisions already settled by an explicit user rule.
---

# Decision support with Eevo

Eevo weighs a decision from the point of view of each stakeholder it affects: for each one it returns the option with the highest expected value, the probability that each option is the best, and whether the stakeholders agree. It never combines them into one verdict. Eevo supports a decision; it does not make it, and its answer is one input to the user's own judgement.

## When to use it

- A choice between 2 to 8 concrete, mutually exclusive options, where the right one depends on what follows from each option for the people or things it affects.
- Not for questions of fact or taste, for a case a rule the user has given already decides, or when each option's value follows from the given facts by plain arithmetic (two prices for the same thing): compute those instead.
- For narrow labels or ratings rather than a choice (how severe, how reversible, which category), use `eevo_classify`.

## Build the decision yourself

Do not ask the user to choose a mode or to list consequences, stakeholders or sizes before the first call; that is your job. Ask only when you cannot tell what is being decided or what the options are. Where something is uncertain, make a reasonable estimate, say in the consequence that it is one, and go ahead. Keep the facts the user gave, your own assumptions and Eevo's estimates distinguishable, and never turn missing evidence into a confident number.

1. **Context**: what is being decided and the facts that matter (constraints, deadlines, amounts, what is unknown). Eevo knows only what you give it; invent no facts.
2. **Options**: 2 to 8, as the user would phrase them.
3. **Consequences**: for each option, 2 to 6 concrete effects, one effect each: what changes, for whom and how much, marked as a benefit or a harm, with a short label. Do not list the same effect twice in different words.
   - Use one baseline for every option: what would happen if none of the options were taken, including risks that already exist. Describe each consequence as a change from that baseline that its option causes, not relative to another option, and do not list "keeps X as it is" or "avoids option A's cost" as a consequence: that is the other option's consequence seen from this side.
   - State amounts: how much, how many, for how long. When consequences are in different units (money, time, people, risk, emissions), also give each one's rough value to the stakeholder in one common unit, if a reasonable estimate exists.
4. **Stakeholders**: everyone the decision materially affects, not only the one the user names, typically 2 to 5: the organization, the affected customers, the affected team members, and the environment when the options differ environmentally.
5. Call `eevo_decide` **once** with all of them. Use the quicker Direct mode, without consequences, only when the user asks for a quick answer or the consequences cannot be named even roughly.

A Default mode decision that runs longer than about 40 seconds comes back as running: fetch it with `eevo_show_decision` about every 30 seconds rather than calling `eevo_decide` again.

Fill the decision's metadata with references the task already has (the issue, pull request or conversation), never with personal details or conversation content the decision does not need.

## Revise when the result shows a gap

Read the result against what you know. If it shows you left out or got wrong something material (a consequence, a size, a stakeholder, context, an option), call `eevo_decide` again with the whole corrected decision, `revises` set to the latest decision id and a revision note saying what was missed. Revise without asking first, never to steer the answer towards an option, and stop after two or three revisions to tell the user what remains uncertain.

## Present the result

- Say that you used Eevo, and for which stakeholders; if you revised, say why.
- One row per stakeholder: the best option and each option's probability. Name the consequences that drive each stakeholder's best option.
- Say where the stakeholders agree and where they conflict. Leave the trade-off between them to the user; a best option below about 50% is a close call.
- Call `eevo_show_decision` once with the final decision id to show the decision as a card.
- Remind the user that Eevo decided only from the context it was given, and name any missing fact that would separate the options.

## Record what happened

- Record whether you agree with the answer, per stakeholder, with `eevo_assess`. Settle which option you would choose before reading Eevo's numbers in detail.
- Once you know what was actually done, report it once with `eevo_report_chosen_decision`: the option carried out (or none) and whether an agent or a person decided. Never guess.
- Share a decision with the user's Eevo organization, or keep it to the user, with `eevo_share_decision` only when the user asks.
