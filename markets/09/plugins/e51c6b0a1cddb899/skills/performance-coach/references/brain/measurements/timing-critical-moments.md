---
key: timing-critical-moments
type: measurement
measurement_key: timing_critical_moments
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#timing-critical-moments; registry (graduated 2026-06-10)"
last_verified: "2026-07-18"
---

# Timing-Critical Moments

## What it measures

Five timing events where pacing and silence change the meaning of what was said. Response latency is normalized against each speaker's own session median, so video lag, connection delay, and individual rhythm do not inflate or suppress the signal. The five events:

1. **Hesitant agreement**: an acceptance slower and more hedged than that speaker's own typical response pace, shaped like a reluctant yes.
2. **Post-objection silence**: 2 to 10 seconds of dead air immediately after an objection, detected structurally.
3. **Held silence after a close** (post-close dwell): a deliberately held pause after asking for a decision, positive pacing.
4. **Long monologue**: your side holding the floor continuously past a 90-second floor.
5. **Customer story**: the other side sustaining the floor for 120 or more continuous seconds, a positive engagement signal.

Research anchor: preferred and dispreferred agreement formats (Pomerantz 1984) plus turn-taking timing research. Graduated to customer-visible on 2026-06-10; it runs in the live pipeline and Ask Coach can answer on it.

## Where you see it

Events on the Conversation Timeline, the Timing-Critical Moments review card, and Ask Coach answers about timing.

## How to read your number

- Each event shows the speaker, timestamp, the gap in milliseconds, and the ratio to that speaker's own session median response time.
- Badge colors follow the product palette: gold marks risk signals (hesitant agreement, long monologue), blue marks positive pacing (held silence after a close, customer story), silver marks structural silence (post-objection).
- Hesitant agreement and held-silence-after-close pass a conservative confirmation gate before appearing (fail-closed, so borderline candidates stay out); the other three are purely structural.
- The long-monologue and customer-story duration floors are exploratory v1 defaults.

## What moves it

- Fewer hesitant agreements from the other side: smaller asks, more safety before the ask, and noticing the hedge instead of steamrolling it ("you paused there; what part is not sitting right?").
- Post-objection silence becomes an asset when you let it breathe instead of rushing to fill it.
- Long monologues shrink with the land-and-hand habit (see [[talk-time-and-turns]]).
- Customer stories grow when your questions and silence make room for them.

## Drills

- The held close: ask for the decision, then hold the silence until they answer. See [[drills-library]].
- Hedge-catch: when you hear a slow hedged yes, name it kindly and reopen the concern rather than banking the false agreement.

## FAQ

**Is a flagged hesitant agreement proof they did not mean it?**
No. It is a timing-and-phrasing shape strongly associated with reluctance. Treat it as a prompt to check, not a verdict. You can also mark any event as accurate or wrong on the card; that feedback calibrates the gate.

**Why milliseconds?**
Because the same words arrive differently slow and hedged than quick and direct. Millisecond timing is where that difference lives.

## Related

[[response-latency]] · [[silence-mechanics]] · [[talk-time-and-turns]] · [[objection-structure]] · [[adjacency-pairs]] · [[engagement]]
