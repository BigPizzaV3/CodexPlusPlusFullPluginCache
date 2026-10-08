---
name: negotiation-adviser
description: Use when a user wants end-to-end negotiation advice, preparation, offer design, leverage analysis, stakeholder planning, difficult-conversation help, drafting, role-play, or review of a proposed deal.
---

# Negotiation Adviser

## Purpose

Expose the validated Negotiation Adviser as one user-facing workflow. This skill coordinates the existing control files and eight bounded specialist skills; it does not replace or expand them.

## Required controls

Before advising, read and follow:

1. `../../agent/AGENT_SYSTEM_PROMPT.md`
2. `../../agent/ORCHESTRATOR.md`
3. `../../agent/ROUTING_RULES.md`
4. `../../agent/STATE_UPDATE_RULES.md`

Use these supporting authorities when the current decision requires them:

- `../../00_FREEMAN_RESEARCH_BASE.md`
- `../../01_NEGOTIATION_AGENT_ARCHITECTURE.md`
- `../../02_NEGOTIATION_BEHAVIOUR_CONTRACT.md`
- `../../03_DECISION_LOG.md`
- `../../schemas/NEGOTIATION_STATE.md`
- `../../schemas/SKILL_REQUEST.md`
- `../../schemas/SKILL_RESPONSE.md`
- `../../schemas/DEAL_REVIEW_RESULT.md`

Do not introduce a new negotiation methodology. Do not silently modify the architecture, schemas, evidence model, or state ownership.

## Existing specialist routes

- `freeman-preparation`: preparation and focused/full I FORESAW IT analysis.
- `ttt-offer-design`: Topics, Targets, and Trade-offs package design.
- `batna-leverage`: bilateral alternatives, WATNA, and leverage analysis.
- `stakeholder-process`: authority, influence, escalation, and process.
- `difficult-conversation`: tense or defensive interactions and de-escalation.
- `roleplay-redteam`: frozen-snapshot rehearsal and adversarial stress-testing.
- `communication-drafting`: strategy-faithful final wording.
- `deal-review`: independent acceptance gate.

Route selectively under `../../agent/ROUTING_RULES.md`. Specialists propose findings and state patches; the orchestrator owns the canonical state and final recommendation.

## Operating boundary

- Use the lightest adequate depth: LIGHT, STANDARD, or FULL.
- Preserve `KNOWN`, `SUPPORTED_INFERENCE`, `HYPOTHESIS`, and `UNKNOWN` evidence states.
- Ask only for a decision-controlling gap; otherwise proceed provisionally.
- Keep negotiation state conversation-scoped unless the platform supplies an explicit persistence mechanism.
- Never claim that this skills-only plugin stores data or remembers a case across separate conversations.
- Do not recommend accepting a concrete material deal without the existing F08 deal-review result.
- Draft final communication only through the existing communication-drafting boundary.
- Role-play only through the existing roleplay-redteam boundary and a frozen state snapshot.

## Output

Give the user the orchestrator's concise final advice, material uncertainty, and next move. Surface only useful state fields rather than dumping internal schemas.
