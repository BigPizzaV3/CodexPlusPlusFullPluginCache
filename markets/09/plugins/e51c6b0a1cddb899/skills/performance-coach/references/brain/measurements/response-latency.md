---
key: response-latency
type: measurement
measurement_key: response_latency
dimension: Responsiveness
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#patience; HelpContentManager.ts#session-response-timing; CardHelpProvider.tsx#premium-scores; CardHelpProvider.tsx#multiparty-lsm; registry"
last_verified: "2026-07-18"
---

# Response Latency

Companion key documented here: `response_latency_matrix` (the per-speaker-pair version).

## What it measures

How long you wait before responding after the other person finishes speaking, in seconds or milliseconds, computed from utterance timing (your start time minus their end time). The matrix version (`response_latency_matrix`) computes the median response time for every responder-after-speaker pair in multi-party calls, with sample counts. Research anchor: cross-linguistic turn-taking research (Stivers et al. 2009) puts typical human gaps near 200ms, with delays past roughly 300-700ms reading as hesitant or dispreferred.

## Where you see it

The Patience card (Overview tab), Response Timing help, the pause-gap markers on the Communication Timeline, the Latency P50/P90 tiles in Premium Scores, and the Response Latency table inside All Parties LSM and Dynamics for multi-party calls.

## How to read your number

Direction: a middle zone is best; both extremes carry signal. Shipped copy states three overlapping bands, each cited, and they do not fully agree (flagged for founder reconciliation in the vault's gap ledger):

- Patience card: ideal 0.6-1.0 seconds; under 0.5s may seem like you are not listening; over 3.0s may create awkward silence.
- Response Timing help: optimal 0.5-2 seconds; too fast can seem rushed, too slow can seem checked out.
- Premium Scores: P50 (median) of 800-1500ms is conversational; over 3000ms reads as hesitation; a large P50-to-P90 gap means you occasionally froze, often on objections or hard questions.

Latency is also normalized against your own session median in timing events, so video lag and connection delay do not inflate the signal (see [[timing-critical-moments]]). In multi-party calls, consistently long latency from one person toward another can signal hesitation, formality, or a power asymmetry; the speaker others answer fastest is often the informal authority.

## What moves it

- Faster (toward crowding): preparing your answer while they still talk, jumping in under 0.5s, fear of silence.
- Slower (toward hesitation): multitasking, uncertainty, overload (a rising latency trend across sessions is one component of the overload signature, always a workload conversation, never a state-of-mind claim).
- Better: one breath before responding; deliberate 1.5-2.0s holds after high-stakes statements (a coaching guideline, see [[silence-mechanics]]).

## Drills

- The two-second gift: after any big statement from the other side, hold 1.5-2.0 seconds before responding. Verify in the next session's latency distribution. See [[drills-library]].
- Count "one-Mississippi" silently if you tend to jump in; prepare a response framework in advance if you tend to stall.

## FAQ

**Is my slow reply after a hard question a problem?**
Usually no. Thinking time after a direct, difficult question is deliberation, not distance. The coach checks what preceded a long gap before counting it against you.

**Why does my latency look different on video calls?**
Platform delay is real. Timing events are normalized against your own session median specifically so video lag does not read as hesitation.

**What is P90?**
Your slowest 10% of responses. A big gap between P50 and P90 means you are quick most of the time but occasionally freeze; those outliers often align with objections.

## Related

[[responsiveness]] · [[silence-mechanics]] · [[timing-critical-moments]] · [[power-dynamics]] · [[interruptions]] · [[drills-library]]
