---
key: psychological-safety
type: measurement
measurement_key: psychological_safety
dimension: Trust Building
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#session-safety-contribution; registry (drift note: primitive-based implementation)"
last_verified: "2026-07-18"
---

# Session Safety Contribution

## What it measures

Your running behavioral-safety profile: a 0-100 score averaged across every session you have analyzed, built from four observable conversational primitives: backchannels per minute, embedded acknowledgments per minute, repairs per minute, and your emotional acknowledgment score. Each session shows its delta against your running average. To be precise about what this is: the score measures acknowledgment-and-repair density, the observable substrate associated with conversations where people can ask questions, admit mistakes, and challenge ideas (the research lineage is Edmondson 1999). It is a behavioral signature, not a survey instrument.

## Where you see it

The Session Safety Contribution card: your running score with a confidence tier, this session's regulation band, the four primitive rows with running averages and deltas, and a de-escalation rate when friction occurred.

## How to read your number

- Guidance ranges from the card: backchannels around 0.2-0.5 per minute is typical for an engaged listener; embedded acks around 0.3-0.6 per minute is healthy; some repairs are good, too many can signal friction in that stretch.
- Read the pattern across all four rows, not a single delta. Sharply below your average on backchannels AND embedded acks usually means monologue mode; find where it started on the Emotional Timeline.
- The score stabilizes after about 10 analyzed sessions; earlier readings are provisional.
- Boundary the card itself draws: do NOT use this score to evaluate or compare other people. It is a per-user behavioral signature, not a job-performance metric.

## What moves it

- The four primitives, directly: acknowledging while others speak, embedding acknowledgment in your contributions, repairing misunderstandings, naming emotions when they appear.
- Deliberate experiments: the card recommends A/B testing your own behavior across calls; if a deliberate change (more clarifying questions, say) shows up as a positive delta, you have evidence the habit is taking.

## Drills

- Pick one primitive per week and run its drill: backchannel reps, acknowledge-and-add, the explicit check-in, acknowledge-then-answer. See [[drills-library]].

## FAQ

**Is this the full published safety construct?**
No, and the product does not claim so. It measures the observable substrate: acknowledgment and repair density. That honesty is what makes the number coachable.

**Can my manager see my safety score?**
Individual analysis goes to you. Managers see team aggregates only, with a minimum of 4 contributors. See [[manager-visibility]] and [[privacy-and-your-data]].

**Why did one intense call barely move it?**
It is a running average across your history, so single sessions nudge rather than swing it. The per-session deltas are where one call's story shows up.

## Related

[[trust-building]] · [[backchannel]] · [[embedded-acknowledgments]] · [[repair-attempts]] · [[emotional-regulation]] · [[manager-visibility]]
