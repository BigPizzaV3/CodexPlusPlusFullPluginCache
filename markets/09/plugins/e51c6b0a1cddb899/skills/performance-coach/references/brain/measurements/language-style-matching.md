---
key: language-style-matching
type: measurement
measurement_key: lsm
dimension: Mirroring
customer_visible: true
provenance: traceable
source: "CardHelpProvider.tsx#language-sync; CardHelpProvider.tsx#lsm-timeline; CardHelpProvider.tsx#multiparty-lsm; registry"
last_verified: "2026-07-20"
---

# Language Style Matching (LSM)

## What it measures

How similarly two speakers use language patterns: function-word alignment (pronouns, articles), auxiliary verb matching (is, are, have), pronoun usage similarity (I, we, you), and conjunction patterns (and, but, or). Scored 0 to 1. Because it tracks function words rather than topic words, it measures HOW you speak together, not what you spoke about. Research anchor: Linguistic Style Matching in social interaction (Niederhoffer and Pennebaker 2002).

## Where you see it

The Language Sync (LSM) card, the LSM Timeline (2-minute windows across the call), the always-on LSM sparkline behind the Communication Timeline swimlanes, and the pairwise LSM heatmap in All Parties LSM and Dynamics for multi-party calls.

## How to read your number

- Language Sync card bands: 0.70 and above is strong alignment (high rapport); 0.50-0.70 is moderate (normal); below 0.50 is low alignment (disconnect). Scores naturally fluctuate, so read trends, not single points.
- Multi-party heatmap bands: 0.80 and above strong, 0.65-0.79 good, 0.50-0.64 moderate, below 0.50 low, per speaker pair.
- Timeline reading: a rising line means building rapport; dips after objections are normal, watch for the recovery; sustained 0.70 or above means strong rapport maintained; a sparkline falling in the second half means your language patterns diverged after a good start.
- Reliability notes from the cards: more balanced word counts give more reliable LSM; a guardrail badge means a score was capped because the sample was too short; early alignment is described as predicting conversation success, and higher LSM correlates with better outcomes (correlational language, never a promise).

## What moves it

- Mirroring their pronoun frame: adopting "we/us" when they use it.
- Reusing their key words instead of swapping in your own vocabulary (see [[mirroring]]).
- Matching sentence complexity: short declaratives get short declaratives.
- It happens unconsciously in good conversations; active listening and adapting raise it. This is style matching, not content parroting.

## Drills

- Echo-as-question: repeat their last two or three key words as a question, then wait. See [[drills-library]].
- Pronoun mirroring: for one call, consciously match their we-versus-I framing and check the LSM timeline afterward.

## FAQ

**Is a low LSM score my fault?**
It is a two-person number. One side can raise it meaningfully, and your trend across sessions shows whether your adaptation work is landing (see [[entrainment]] for the cross-session view).

**Does LSM mean we agreed?**
No. It means your styles converged. Two people can disagree in perfectly matched language, and that is often the healthiest version of disagreement.

## Research depth

High LSM is not automatically healthy rapport. Convergence can be mutual alignment or unilateral accommodation (power). See [[research-risks]] (alignment ambiguity, over-accommodation) and [[power-dynamics]]. Directional LSM is proposed, not a customer teachable until graduated ([[labs-and-boundaries]]).

## Related

[[mirroring]] · [[entrainment]] · [[speech-rate-modulation]] · [[recovery-episodes]] · [[drills-library]] · [[research-risks]]
