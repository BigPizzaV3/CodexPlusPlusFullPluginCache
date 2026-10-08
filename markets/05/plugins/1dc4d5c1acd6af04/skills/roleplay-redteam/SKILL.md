---
name: roleplay-redteam
description: Use when an important negotiation strategy, offer, meeting, or difficult conversation needs rehearsal against a credible resistant counterpart or independent stress-testing before execution.
---

# Role-play and Red Team

## Overview

Stress-test the current strategy using Freeman's role-play principle, with an AI isolation protocol that prevents simulated claims becoming facts. [F03]

**Interface:** accept a versioned `SKILL_REQUEST`; return `SKILL_RESPONSE`. Never persist state.

## Isolation rule

The supplied state snapshot is immutable during the exercise. Simulation output is **not evidence** about the real counterpart.

## Method

1. **Lock the snapshot.** Record `state_version`, current strategy, proposal, evidence and explicit assumptions.
2. **Adopt a credible counterpart.** Model the strongest plausible resistance supported by the state; do not create a cartoon villain or easy opponent.
3. **Stress-test.** Challenge weak assumptions, ambiguous terms, non-credible threats, exposed concessions and unattractive trades. Identify what a competent counterpart could ask for or attack.
4. **Separate simulation from analysis.** If a role-play transcript is useful, return it only as an optional `deliverable.kind: roleplay`.
5. **Debrief.** Return strongest counterarguments, weak assumptions, missing evidence, likely reactions and proposed tests/strategy changes. Simulated reactions remain hypotheses unless independently evidenced.
6. **Reconcile externally.** The orchestrator classifies significant findings `ACCEPT`, `TEST`, `REJECT` or `DEFER`. F06 does not write them directly into canonical state.
7. **Check staleness.** If the live state no longer matches `based_on_state_version`, warn rather than overwriting newer reasoning.

## Safeguards

- Attack the strategy, not the user personally.
- Do not provide reassurance theatre; resistance should be meaningful and plausible.
- Do not create new KNOWN facts from dialogue you generated.
- Do not make the final negotiation recommendation or deal-acceptance decision; F08 owns independent acceptance.
- Do not persist state or silently alter targets/BATNA.

## Stop condition

Stop when further rounds no longer reveal material new vulnerabilities, evidence gaps or response problems.
