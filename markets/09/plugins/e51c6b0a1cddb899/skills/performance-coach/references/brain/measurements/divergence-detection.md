---
key: divergence-detection
type: measurement
measurement_key: divergence_detection
customer_visible: true
provenance: expert-estimate
source: "CardHelpProvider.tsx#signal-stack; registry"
last_verified: "2026-07-18"
---

# Divergence Detection

## What it measures

How much the conversation drifted from shared goals: whether the two sides converged toward a common thread or split into parallel tracks. Scored 0 to 100, where low is healthy convergence. Research anchor: Communication Accommodation Theory (Giles, Taylor and Bourhis 1973), the research line on how speakers move toward or away from each other.

## Where you see it

The Divergence tile on the Signal Stack (Deep Dive tab), with the topic-level detail in [[topic-shift]].

## How to read your number

- Direction: lower is better. Signal Stack threshold (exploratory v1 default, not calibrated against outcomes): above 60 means the conversation is splitting rather than converging.
- Combined reads from the card: high divergence plus high question-evasion plus a hedging certainty profile is the signature of a counterpart who is not bought in.
- If divergence is high, check the Topic Shift view to see where alignment was lost, and check [[repair-attempts]]: rising divergence with low repairs means the conversation drifted and no one pulled it back.

## What moves it

- Topic repairs: steering back to the lost thread after a digression ("coming back to the rollout question...").
- Building on their last turn instead of pivoting to your agenda (see [[embedded-acknowledgments]] and [[questions-asked]]).
- Explicit convergence moves: summarizing shared ground before moving on ("so we agree the bottleneck is onboarding; next is timeline").
- What raises it: agenda-pushing past their cues, stacked topic changes, and letting side threads replace the goal.

## Drills

- The thread check: once per call, summarize the shared goal in one sentence and confirm it still holds. See [[drills-library]].
- One topic repair per call: notice a digression and steer back aloud.

## FAQ

**Is all divergence bad?**
No. Productive exploration wanders on purpose. The cost shows when the call ends split: no shared thread, no converged next step. Pair the number with whether your close landed (see [[clean-commitments]]).

**Who caused the divergence?**
The tile is session-level. The timeline and topic views show where it happened and after whose turns, which is more useful than assigning blame.

## Related

[[topic-shift]] · [[repair-attempts]] · [[qa-adequacy]] · [[counterpart-reciprocity]] · [[grice-maxims]]
