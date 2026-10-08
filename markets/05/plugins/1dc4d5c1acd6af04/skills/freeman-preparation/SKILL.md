---
name: freeman-preparation
description: Use when preparing or refreshing a material negotiation, meeting, opening position, or strategy where interests, facts, options, alternatives, authority, process, criteria, or initial targets are incomplete or uncertain.
---

# Freeman Preparation

## Overview

Use **I FORESAW IT** as a preparation map, not a questionnaire. Apply only dimensions that can change the current decision and preserve uncertainty rather than inventing completeness. [F03]

**Authority:** `00_FREEMAN_RESEARCH_BASE.md` → `01_NEGOTIATION_AGENT_ARCHITECTURE.md` → `02_NEGOTIATION_BEHAVIOUR_CONTRACT.md`.

**Interface:** accept `schemas/SKILL_REQUEST.md`; return `schemas/SKILL_RESPONSE.md`. Never persist canonical state directly.

## Core map

| Element | Prepare |
|---|---|
| **Interests** | User, counterpart and specific common interests; separate interests from positions. |
| **Facts / financial research** | Established facts, missing evidence and decision-relevant research. |
| **Options** | Possible terms inside an agreement; never BATNAs. |
| **Rapport / reactions / responses** | Relationship, credible reactions and prepared responses; no simulation. |
| **Empathy / ethics** | Counterpart perspective and ethical boundaries. |
| **Setting / scheduling** | Channel, timing, deadlines, sequence, agenda and process risks. |
| **Alternatives** | User/counterpart alternatives, WATNAs and improvements; future possibilities stay provisional. |
| **Who** | Authority, influencers, allies, counterpart selection and stakeholder uncertainty. |
| **Independent criteria** | Credible external standards; self-asserted fairness is not independent evidence. |
| **Topics / targets / tradeoffs** | Initial topics and target gaps; detailed package design belongs to F02. |

## Method

1. **Validate state/version.** Flag contradictions or gaps that block reliable preparation.
2. **Use proportional depth.** STANDARD inspects only decision-relevant dimensions. FULL reviews every relevant dimension without inventing content.
3. **Protect evidence.** Material counterpart interests, motives, authority, constraints, reactions and alternatives remain `KNOWN`, `SUPPORTED_INFERENCE`, `HYPOTHESIS` or `UNKNOWN` according to basis.
4. **Protect semantics.** A position is not an interest. An agreement option is not an alternative. A hoped-for future opportunity is not a current BATNA.
5. **Ask only material questions.** A question must be capable of changing strategy, target/floor, BATNA, authority, process, trade or acceptance; do not dump the mnemonic as questions.
6. **Return supportable preparation now.** Non-blocking unknowns do not prevent useful findings/patches.
7. **Respect boundaries.** Do not produce the final communication, enter role-play, persist state, or make the independent acceptance decision.

## Safeguards

- Treat unsupported counterpart motive as hypothesis.
- “Company policy” is a reported statement until evidenced; do not assume the visible contact owns the decision.
- Reject vague common interests.
- Do not invent benchmarks, targets, floors, deadlines, authority or BATNAs.
- Material target/floor needs a rationale.
- Notional BATNA remains provisional; do not invent probabilities. [F06]
- Do not reconstruct unresolved named Freeman procedures from memory.

## Output

Return canonical `skill_response`: conclusion/confidence, findings with provenance/evidence status, recommendations, permitted proposed patches, prioritised questions, warnings, state conflicts and `material_change_candidate` where required.

## Stop condition

Stop when the orchestrator has enough supported information for the next strategic move. Do not fill fields merely to complete the framework.
