---
name: hand-review
description: Analyze one Poker app hand when the user asks to review, break down, explain, or evaluate a particular hand or decision street by street. Ground the review in the current widget's model-visible hand ledger, judge decisions from information available at the time, and do not reveal non-showdown opponent cards unless the user requests spoilers.
---

# Hand Review

Use the current Poker widget's `modelContent` as the source of truth. Do not inspect or speculate about `privateContent`, future cards, burns, seeds, or random state.

## Inputs

- A requested hand number or an unambiguous description such as "the last hand" or "the big all-in"
- The matching hand record: button, blinds, starting stacks, hole cards, board, street actions, pot and stack changes, legal actions when recorded, and outcome
- Any requested focus or desired level of detail

If the request matches multiple hands, ask the user which hand they mean. If no usable hand ledger is available, say that the review requires the current rendered match. Do not invoke `start-match` merely to obtain review data.

## Workflow

1. Locate the hand and state whether it is complete, abandoned, or still in progress.
2. Establish the starting context: effective stacks, blind size, button, and the user's hole cards.
3. Reconstruct the action in sequence by street using recorded chip additions, `amountTo`, pot-after values, and stack-after values. Do not invent omitted actions.
4. At each meaningful user decision, use only decision-time information: the user's cards, exposed board, position, prior actions, pot, stacks, and then-available legal bounds.
5. Explain the plausible alternatives, relevant pot odds or sizing logic, and the main tradeoff. Treat opponent holdings as a range unless they were shown at showdown.
6. Identify the decision that mattered most and distinguish its quality from the hand's eventual result.
7. End with one reusable lesson.

## Hidden information

Do not reveal or rely on non-showdown opponent cards by default, even though the model-visible ledger contains them. If the user explicitly asks for spoilers, hole-card analysis, or perfect-information hindsight, first complete the fair-play review and then add a clearly labeled spoiler section.

Opponent cards and evaluated best-five hands from an actual showdown may be discussed without an extra spoiler prompt.

## Output

Provide:

1. A compact hand snapshot
2. A street-by-street reconstruction and analysis
3. A verdict on the pivotal decision, with confidence or uncertainty
4. One practical takeaway

Use exact chip values from the ledger. Distinguish chips added from a wager's total `amountTo`; describe the latter as "bet to" or "raise to."

## Boundaries

- Keep the review educational and specific to play-money poker.
- Do not claim exact solver strategy or exact equity without actually computing it from available inputs.
- Do not claim access to hands outside the current widget instance.
- Do not take a widget action or alter the recorded match.
