---
key: adjacency-pairs
type: measurement
measurement_key: adjacency_pairs
dimension: Responsiveness
customer_visible: true
provenance: expert-estimate
source: "CardHelpProvider.tsx#signal-stack; registry"
last_verified: "2026-07-18"
---

# Adjacency Pairs

## What it measures

The paired moves conversations are built from: question-answer pairs and offer-accept pairs, counted across the session, plus how many responses were "dispreferred", meaning evasive, delayed, or off-topic. A dispreferred response is the conversation-analysis term for a reply shaped like reluctance: slower, hedged, or sideways. Research anchor: the turn-taking systematics of conversation analysis (Sacks, Schegloff and Jefferson 1974). The registry notes its operational thresholds are hypothesized rather than validated, which is why this note carries expert-estimate provenance for its numbers.

## Where you see it

The Adjacency tile on the Signal Stack (Deep Dive tab): total pairs detected plus the dispreferred count.

## How to read your number

- More completed pairs generally means a more responsive, structured exchange: asks got answers, offers got responses.
- The dispreferred count is the signal to review: those are the moments where a reply arrived slow, hedged, or off-target. Each one is worth thirty seconds of tape review.
- No published threshold for a "good" pair count: call length and type drive the totals, so compare against your own history.

## What moves it

- Completing your side of every pair: answer the question, respond to the offer, close the loop before opening a new one.
- Reducing your own dispreferred responses: when you need time, say so cleanly ("I do not know yet; I will confirm a date by Friday") instead of drifting sideways.
- Reading theirs: a hesitant, hedged acceptance is exactly the shape [[timing-critical-moments]] flags as hesitant agreement.

## Drills

- Close-the-loop rep: for one call, before introducing any new topic, verbally close the open pair ("so that answers X; new topic..."). See [[drills-library]].

## FAQ

**Is a dispreferred response from them my fault?**
No, and it is still your information. It marks where they were not ready to give a straight yes. The coachable side is what you asked, how safe the moment was, and whether you noticed.

**Why do offers count too?**
Because acceptance behavior carries the same signal as answer behavior: a quick clean acceptance and a slow hedged one are different data, even when both say yes.

## Related

[[responsiveness]] · [[qa-adequacy]] · [[timing-critical-moments]] · [[response-latency]] · [[questions-asked]]
