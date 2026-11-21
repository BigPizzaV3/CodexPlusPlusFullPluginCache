---
key: backchannel
type: measurement
measurement_key: backchannel
dimension: Active Listening
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#backchannel-labs; CardHelpProvider.tsx#session-safety-contribution; CardHelpProvider.tsx#listening-style; registry"
last_verified: "2026-07-18"
---

# Backchannel

## What it measures

Short utterances a listener inserts to signal attention without taking the floor: "mm-hmm", "right", "yeah", "I see". Counted as a total, a per-minute rate, and by timing class. Every candidate passes a two-tier classifier: a strict tier (high-confidence allowlist plus timing rules) and a soft tier (valid but less certain). Research anchor: listeners as co-narrators (Bavelas, Coates and Johnson 2000).

## Where you see it

The Backchannel measurement card, the backchannels-per-minute row on the Session Safety Contribution card, and the Listening Style card (backchannel rate is one of its observable inputs).

## How to read your number

- Typical engaged-listener rate: about 0.2-0.5 backchannels per minute (Session Safety card guidance).
- Timing classes: On-Time (within 900ms of the prior speaker finishing) is the most rapport-relevant; Overlap (started before they finished) can signal eagerness or impatience, context matters; Late (900-2500ms) may indicate distraction. Candidates with gaps beyond 2500ms are dropped entirely.
- A rate near zero usually means you were in a dominant speaking mode; check [[talk-time-and-turns]] before reading it as poor listening.
- Strict count is near-certain; a low strict count with a high soft count means the signals were marginal, so treat the total as directional.

## What moves it

- Up: actually yielding the floor (you cannot backchannel while monologuing), and brief verbal acknowledgment while the other person develops a thought.
- The rejection-reason breakdown explains gaps: "part of a longer turn" rejections are expected and harmless; "not in allowlist" means you acknowledged with unusual phrasing the detector does not recognize.
- Related but different: acknowledgment embedded in a full sentence is counted separately as [[embedded-acknowledgments]].

## Drills

- Listener reps: on your next call, when the other side explains something for more than 20 seconds, give one short acknowledgment token and stay silent otherwise. Verify the per-minute rate next session. See [[drills-library]].

## FAQ

**Do backchannels count as filler words?**
No. Backchannel utterances are excluded from filler counts by design.

**Can I overdo it?**
Overlapping backchannels in bursts can read as hurrying the speaker. On-Time is the class to grow.

**Why did my "totally fair" not count?**
Evaluative phrases and longer responses fall outside the backchannel allowlist; many land instead as embedded acknowledgments or reflections, which are measured separately.

## Related

[[active-listening]] · [[embedded-acknowledgments]] · [[psychological-safety]] · [[talk-time-and-turns]] · [[drills-library]]
