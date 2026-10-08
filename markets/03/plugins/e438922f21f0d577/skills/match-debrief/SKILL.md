---
name: match-debrief
description: Review and debrief a Poker app match when the user asks for a match recap, performance review, biggest mistakes, strengths, leaks, pivotal hands, or improvement priorities. Use only the current widget's model-visible match ledger, separate decision quality from results, and do not reveal non-showdown opponent cards unless the user requests spoilers.
---

# Match Debrief

Use the current Poker widget's `modelContent` as the source of truth. Do not use `privateContent` or infer the undealt deck, burned cards, seeds, or random state.

## Inputs

- The current match ledger, including difficulty, result, hands, cards, boards, stacks, actions, outcomes, and blind levels
- Any focus the user requests, such as aggression, bet sizing, preflop play, or a concise review

If no usable match ledger is available, say that a debrief requires the current rendered match and ask the user to open or return to it. Do not invoke `start-match` unless the user separately asks for a new match.

## Workflow

1. Confirm whether the match is complete or still in progress. Label an in-progress review as provisional.
2. Reconstruct the match arc from recorded stack changes, blind progression, and outcomes. Do not invent actions between ledger entries.
3. Identify the few hands that most affected the result or best demonstrate a repeated decision pattern. Do not equate the largest pot with the worst decision automatically.
4. Evaluate choices using only information legitimately available to the user at each decision: the user's cards, public board, position, prior actions, pot, stacks, and legal bounds.
5. Separate decision quality from the eventual cards and result. Call out uncertainty when opponent ranges or equity are estimates.
6. Find repeated strengths and improvement opportunities. Support each material observation with hand numbers and concrete actions.
7. Prioritize no more than three adjustments the user can apply in the next match.

## Hidden information

Treat opponent cards from non-showdown hands as spoilers even though they are model-visible. Do not reveal or use them to justify decision-time advice unless the user explicitly requests a perfect-information or spoiler review. Opponent cards shown at showdown may be discussed normally.

When spoilers are requested, keep the fair-play analysis primary and put hindsight from hidden cards in a clearly labeled separate section.

## Output

Provide:

1. A short match summary with result, difficulty, approximate turning points, and final stacks when present
2. Two or three strengths supported by hand references
3. Two or three improvement opportunities supported by hand references
4. Brief reviews of the pivotal hands
5. Three specific priorities for the next match

Scale detail to the match length and the user's request. Use chip amounts exactly as recorded and call raises "raise to" amounts when applicable.

## Boundaries

- Keep the discussion educational and specific to play-money poker.
- Do not claim access to matches from another widget, conversation, or session.
- Do not claim exact equity unless it is actually calculated from available information; otherwise use qualitative or explicitly approximate language.
- Do not control the widget, place blinds, take actions, or start another match on the user's behalf.
