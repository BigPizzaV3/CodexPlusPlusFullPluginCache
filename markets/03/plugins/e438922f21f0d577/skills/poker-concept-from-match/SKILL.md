---
name: poker-concept-from-match
description: Teach one poker concept through a concrete example from the user's current Poker app match when they ask to learn or understand ideas such as pot odds, position, ranges, effective stacks, stack-to-pot ratio, value betting, bluffing, or bet sizing. Use the model-visible ledger, stay focused on one concept, and avoid hidden-card spoilers unless requested.
---

# Poker Concept From Match

Teach one requested concept using a real decision from the current Poker widget's `modelContent`. Do not use `privateContent` or infer the undealt deck, burned cards, seeds, or random state.

## Inputs

- The concept the user wants to learn
- The current match ledger, including hands, cards, boards, positions, blinds, stacks, pots, actions, and outcomes
- An optional hand or decision the user wants used

If the concept is unclear, infer it from the user's wording when safe or ask one short question. If no suitable ledger is available, explain the concept briefly and state that a match-specific example requires the current rendered match. Do not start a new match unless the user asks to play.

## Workflow

1. Define the concept in plain language in one or two sentences.
2. Select the clearest relevant decision from the requested hand or current match. Prefer a completed decision with enough recorded context to demonstrate the concept.
3. Reconstruct only the facts needed for the lesson: street, position, user cards, public board, pot, effective stacks, prior action, and legal amounts.
4. Show the calculation when the concept is quantitative. For pot odds, distinguish call cost from total pot; for wagers, distinguish chips added from `amountTo`; for stack-to-pot ratio, state the stack and pot used.
5. Compare the actual choice with one useful alternative and explain the tradeoff using information available at that moment.
6. End with a compact rule of thumb and one question the user can ask themselves in a future hand.

## Hidden information

Treat non-showdown opponent cards as spoilers. Do not reveal or use them in the main lesson unless the user explicitly asks for a spoiler or perfect-information explanation. Showdown cards may be discussed normally.

If spoilers are requested, preserve the decision-time lesson and add hindsight separately; do not rewrite a sound decision as a mistake merely because hidden cards made it lose.

## Output

Use this compact structure:

1. Concept
2. Example from the match, citing the hand number
3. Calculation or reasoning
4. Actual choice versus one alternative
5. Rule of thumb

Keep the lesson focused on one concept unless the user explicitly requests a broader tutorial.

## Boundaries

- Keep examples educational and confined to play-money poker.
- Label equity, ranges, and behavioral reads as estimates unless directly established by the ledger or an explicit calculation.
- Do not claim solver output, live external data, or access to other match instances.
- Do not control the widget or alter gameplay.
