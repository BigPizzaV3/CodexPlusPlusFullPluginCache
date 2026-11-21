---
key: grice-maxims
type: measurement
measurement_key: grice_maxims
customer_visible: true
provenance: expert-estimate
source: "CardHelpProvider.tsx#signal-stack; registry"
last_verified: "2026-07-18"
---

# Grice Maxims

## What it measures

The rate of cooperative-conversation violations across your turns, using the four classic maxims of conversation: quantity (say as much as needed, not more), quality (say what you have evidence for), relation (stay relevant to what was just said), and manner (be clear, avoid obscurity). Reported as a violation rate: the percentage of turns violating any maxim. Research anchor: "Logic and Conversation" (Grice 1975). The registry notes the violation thresholds are hypothesized rather than validated, hence expert-estimate provenance for the numbers.

## Where you see it

The Grice tile on the Signal Stack (Deep Dive tab), with a per-utterance breakdown in the Grice Maxims detail card.

## How to read your number

- Direction: lower is cleaner. Signal Stack guidance (exploratory v1 default): under 30% is relatively clean; higher suggests unclear or evasive communication.
- The maxim mix matters: quantity violations pair with monologue drift, relation violations pair with topic divergence, manner violations pair with unclear delivery, and quality violations deserve a hard look at what was claimed.
- If the rate is high, scroll to the detail card for the per-utterance breakdown rather than guessing which maxim drove it.

## What moves it

- Quantity: land the point in one sentence, then hand it back (see [[talk-time-and-turns]]).
- Relation: answer the asked question first; build on their last turn (see [[responsiveness]] and [[qa-adequacy]]).
- Manner: concrete words, shorter sentences, one idea per turn.
- Quality: claim what you can back; convert speculation into a clean conditional ("I'll confirm the number by Friday").

## Drills

- One-sentence-first: for one call, open every substantive reply with the single-sentence version of your point before any elaboration. See [[drills-library]].

## FAQ

**Are violations lies?**
Almost never. Most violations are over-talking, drifting, or vagueness, which are craft issues. The value of the maxim frame is that it names WHICH cooperative habit slipped.

**My style is expansive. Is that a violation?**
Style is yours. The read is against the conversation's needs: an invited deep-dive is not a quantity violation, and the coach checks whether the depth was requested before counting it.

## Related

[[qa-adequacy]] · [[divergence-detection]] · [[talk-time-and-turns]] · [[discourse-markers]] · [[topic-shift]]
