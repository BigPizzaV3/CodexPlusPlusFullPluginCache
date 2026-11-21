---
key: repair-attempts
type: measurement
measurement_key: repair_attempts
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#repair-attempts; CardHelpProvider.tsx#session-safety-contribution; registry"
last_verified: "2026-07-18"
---

# Repair Attempts

## What it measures

Moments where a speaker recognized a communication breakdown (a misunderstanding, an awkward silence, a deflection) and actively tried to correct it. Three kinds are detected: initiation repairs (correcting your own utterance before finishing it: "I mean, what I'm trying to say is..."), response repairs (addressing a misunderstanding the other person signaled), and topic repairs (steering back to a lost thread after a digression). Each carries a confidence score for how clearly the repair was signaled versus inferred. Also tracked as repairs per minute on your safety profile. Research anchor: the preference for self-correction and the repair taxonomy in conversation analysis (Schegloff, Jefferson and Sacks 1977).

## Where you see it

The Repair Attempts card, the repairs-per-minute row on the Session Safety Contribution card, and repair clusters as a friction trigger in [[recovery-episodes]].

## How to read your number

- A moderate repair rate, not zero and not excessive, is the hallmark of an adaptive, present communicator.
- Zero repairs often means the speaker is not tracking misalignment: plowing through regardless.
- Too many repairs can signal anxiety about the material, thin preparation, or unclear thinking in that stretch.
- Successful repairs, the ones followed by the other person re-engaging, are the strongest indicator of conversational agility.
- Some repairs are good in themselves: they show humility and accuracy. Dense repairs in one segment mean that segment was confusing; review the transcript there.

## What moves it

- Noticing the signals that the conversation went off track: short replies, puzzled restatements, a stalled thread.
- Checking in explicitly ("did that answer what you actually asked?").
- Falsifier worth knowing: repair-request "sorry"s ("sorry, say that again?") are clarification mechanics, not apologies, and they do not count against you in apology-density coaching.
- Pairing signal: rising divergence with low repairs means the conversation drifted and nobody pulled it back (see [[divergence-detection]]).

## Drills

- The explicit check-in: once per call, after a complex explanation, ask a one-line comprehension check. See [[drills-library]].
- Review your highest-confidence repairs from the last session: those are your clearest course-correction moves, worth repeating on purpose.

## FAQ

**Is repairing myself mid-sentence bad?**
A self-correction that lands the clearer version is a skill. The concern is density: constant restarts in one stretch usually mark cognitive load, worth a look at what you were explaining (see the Delivery Confidence card and [[speech-rate-modulation]]).

**How is this different from Recovery Episodes?**
Repair Attempts counts the individual course-correction moves. [[recovery-episodes]] zooms out to whole friction arcs and whether they ended recovered, partial, or not recovered.

## Related

[[recovery-episodes]] · [[psychological-safety]] · [[active-listening]] · [[divergence-detection]] · [[drills-library]]
