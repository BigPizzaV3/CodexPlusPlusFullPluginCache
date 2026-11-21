---
key: topic-shift
type: measurement
measurement_key: topic_shift
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#signal-stack; registry"
last_verified: "2026-07-18"
---

# Topic Flow (Topic Shift)

## What it measures

Lexical cohesion between consecutive turns: how much each turn shares vocabulary and topic with the one before it. Scored 0 to 1, shown as a percentage. Higher means the conversation stayed on one topic; lower means more topic movement. Research anchor: the speaker-identity topic-segmentation model line (Nguyen, Boyd-Graber, Resnik et al. 2014).

## Where you see it

The Topic Flow tile on the Signal Stack (Deep Dive tab). Topic-change ownership also feeds the Topic Intro Rate in [[agency-orientation]] and topic control reads in [[power-dynamics]].

## How to read your number

- The product states this explicitly: there is no validated good-or-bad threshold yet, so read it as descriptive, not a verdict.
- High cohesion suits deep-dive calls; lower cohesion suits agenda-driven meetings that legitimately cover many items. Fit to purpose is the read.
- Pair it with [[divergence-detection]]: if divergence is high, the topic view shows where the conversation lost alignment.
- Compare across your own sessions of the same type: a discovery call that jumps topics every few turns rarely gets deep enough for real discovery.

## What moves it

- Follow-up chains: asking the next question about the same thread instead of opening a new one (see [[questions-asked]]).
- Topic repairs: returning to the dropped thread after a digression.
- Deliberate transitions: closing one topic aloud before opening the next keeps movement purposeful rather than scattered.
- What lowers it unhelpfully: pivoting off their answers to your agenda, and stacking new topics before old ones resolve.

## Drills

- Three-deep: on your next discovery call, take one topic three follow-up questions deep before allowing any topic change. See [[drills-library]].

## FAQ

**Is jumping topics always a problem?**
No. Status meetings and agenda reviews are built to move. The signal earns attention when topic movement replaces depth on a call whose purpose was depth.

**Who moved the topics, them or me?**
This tile is session-level; the Topic Intro Rate in [[agency-orientation]] attributes topic changes to the focus speaker, which answers the ownership question.

## Related

[[divergence-detection]] · [[questions-asked]] · [[agency-orientation]] · [[power-dynamics]] · [[grice-maxims]]
