---
key: qa-adequacy
type: measurement
measurement_key: qa_adequacy
dimension: Responsiveness
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#signal-stack; CardHelpProvider.tsx#qa-analysis; registry"
last_verified: "2026-07-18"
---

# Q-A Adequacy

## What it measures

Whether questions actually got answered. Scored as an evasion score from 0 to 100 over the call's question-answer exchanges: higher means more question-dodging detected. It reads both directions, so it covers how fully your questions were answered and how fully you answered theirs. Research anchor: the question-response system in American English conversation (Stivers 2010).

## Where you see it

The Q-A Adequacy tile on the Signal Stack (Deep Dive tab), with the per-exchange detail in the Questions and Answers card and the QA Segments panel.

## How to read your number

- Direction: lower is better (less evasion).
- Signal Stack thresholds (exploratory v1 defaults, not yet calibrated against outcomes): above 60 signals active deflection; above 50 means questions were not fully answered and the QA Segments panel is worth reviewing to identify which ones.
- Unanswered questions are follow-up material: each one is a thread you can reopen.
- Combined reads from the card: high evasion plus high divergence plus a hedging certainty profile is the signature of a counterpart who is not bought in.

## What moves it

- Your side: answering the asked question in your first sentence before adding context (see [[responsiveness]]); resisting the pivot to your favorite topic.
- Their side, influenced by you: smaller, sharper questions get answered more fully than stacked or compound ones (see [[questions-asked]]); a held pause after asking gives the full answer room to arrive.
- Reopening the dodge: "coming back to what I asked earlier..." converts a detected evasion into a recovered answer.

## Drills

- Answer-first rep: for one call, answer every direct question in your first sentence. Verify against the evasion read next session. See [[drills-library]].
- The reopen: pick one unanswered question from your last session's QA panel and reopen it on the follow-up call.

## FAQ

**Their evasion score is high. What do I do with that?**
Treat it as a map of what they were not ready to answer. Those topics usually need a smaller question, more safety, or a different stakeholder, not more pressure.

**Does a polite deflection count as evasion?**
The measure reads response completeness, not rudeness. A graceful "let me come back to that" still leaves the question unanswered, and the coach treats it as an open thread, not an offense.

## Related

[[responsiveness]] · [[questions-asked]] · [[adjacency-pairs]] · [[discourse-markers]] · [[divergence-detection]]
