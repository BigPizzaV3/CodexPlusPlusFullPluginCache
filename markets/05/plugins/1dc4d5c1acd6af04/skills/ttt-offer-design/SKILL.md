---
name: ttt-offer-design
description: Use when a negotiation needs Topics, Targets and Trade-offs, an opening or counter-offer package, concession design, or alternatives within an agreement rather than a BATNA analysis.
---

# TTT Offer Design

## Overview

Turn state into **Topics, Targets and Trade-offs (TTT)** and offer packages. Freeman's TTT uses ambitious but realistic targets, least acceptable boundaries and two trade types; it is a play card, not a script. [F03]

**Authority:** `00_FREEMAN_RESEARCH_BASE.md` → `01_NEGOTIATION_AGENT_ARCHITECTURE.md` → `02_NEGOTIATION_BEHAVIOUR_CONTRACT.md`.

**Interface:** accept `schemas/SKILL_REQUEST.md`; return `schemas/SKILL_RESPONSE.md`. Never persist state directly.

## When to use

Use to define or refresh topics, targets, trades, opening/counter packages, least acceptable packages or conditional movement.

Do not own detailed BATNA/leverage analysis (F03), final drafting (F07), independent acceptance (F08), or role-play (F06).

## Core model

| Element | Rule |
|---|---|
| **Topics** | Identify negotiable issues; price/fee is not automatically the whole negotiation. |
| **Best target** | Ambitious but realistic, with rationale/evidence. A user wish is not automatically a researched target. |
| **Least acceptable boundary** | Preserve the established boundary; never move it silently. |
| **Cross-topic trade** | Exchange movement on one topic for value on another. |
| **Within-topic trade** | Find another way to satisfy the interest within the same topic. |

## Method

1. **Validate state.** Use the supplied version, interests, positions, evidence, priorities, BATNA summary and concession history. Flag material contradictions.
2. **Map topics/priorities.** Preserve `agreed` topics unless deliberately reopened. Add topics only when state supports them; do not invent counterpart priorities.
3. **Set/test targets.** Require a basis for best targets and least acceptable boundaries. If BATNA is needed but unknown, identify the limitation and route detailed analysis to F03.
4. **Search for trades.** Look for cross-topic and within-topic trades before unilateral movement. Never store an agreement trade as BATNA.
5. **Design supported packages:**
   - **opening package** near supported best targets, with no arbitrary numerical cushion;
   - **least acceptable package** respecting critical boundaries;
   - **creative package** using supported tradeable topics where useful.
6. **Check concessions.** State why movement helps, what should return, whether a boundary is crossed, and whether conditional movement is preferable. Unilateral movement is allowed when the state supports a strategic reason.
7. **Return proposals.** Explain give/receive logic and risks. Flag proposed target/floor changes through `material_change_candidate`.

## Safeguards

- Never invent prices, percentages, market anchors, target rationales or counterpart valuations.
- Preserve evidence labels for material assumptions about counterpart value.
- Do not sacrifice a critical topic for a lower-priority gain without surfacing a deliberate boundary change.
- Do not use arbitrary utility scores or pseudo-precision.
- Do not silently re-trade an `agreed` topic.
- Prefer supported trades to giveaways; do not manufacture reciprocity.

## Output

Return canonical `skill_response`: conclusion/confidence, findings, recommendations, permitted state patches, questions, warnings/conflicts and `material_change_candidate` where required.

For every finding, keep the two enums separate: `research_provenance` is only `FREEMAN | EXTERNAL | SYNTHESIS | DESIGN`; `evidence_status` is only `KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN | null`. Never place an evidence-status value in `research_provenance` or a methodology value in `evidence_status`.

F02 proposes; the orchestrator reconciles/persists. F07 drafts wording. F08 decides material deal acceptance.

## Stop condition

Stop when a supportable TTT map and enough package choices exist for the next move. Do not generate variants merely to appear creative.
