---
name: batna-leverage
description: Use when a negotiation depends on fallback alternatives, walk-away credibility, bargaining power, weak-position strategy, counterpart dependency, or improving alternatives before making a material move.
---

# BATNA and Leverage

## Overview

Analyse alternatives **bilaterally** and identify supported leverage without reducing power to BATNA alone. Freeman's preparation examines each side's alternatives, WATNA, BATNA improvement and other sources of strength; a weak BATNA does not automatically mean a weak overall position. [F03]

**Authority:** `00_FREEMAN_RESEARCH_BASE.md` → approved architecture/behaviour.

**Interface:** accept `schemas/SKILL_REQUEST.md`; return `schemas/SKILL_RESPONSE.md`. Never persist state directly.

## When to use

Use when the orchestrator needs user/counterpart BATNA analysis, WATNA, alternative improvement, walk-away credibility, dependency analysis, weak-position strategy or leverage review.

Do not own package design (F02), detailed stakeholder mapping (F04), drafting (F07) or deal acceptance (F08).

## Core distinctions

- **BATNA:** best credible course if no agreement is reached.
- **WATNA:** credible worst alternative/outcome; never substitute it for BATNA.
- **BATNA improvement:** action that may strengthen the fallback; it is not achieved until evidenced.
- **Notional BATNA:** possible near-future fallback. Keep provisional and uncertainty-aware; never treat it as current BATNA. [F06]
- **Leverage:** may also arise from information, independent criteria, timing, counterpart constraints/dependency, process, stakeholders or value creation when supported by state. [F03]

## Method

1. **Validate alternatives.** For each candidate, test practical availability, timing, cost, feasibility and evidence. A named supplier/client/job is not automatically a BATNA.
2. **Analyse both sides.** Assess user and counterpart alternatives separately. Unknown counterpart BATNA/dependency stays `UNKNOWN` or evidence-labelled inference; do not infer power from one side alone.
3. **Separate BATNA/WATNA.** Record the best fallback and downside distinctly.
4. **Identify improvements.** Recommend actions that could strengthen alternatives; do not promote them before completion/evidence.
5. **Assess leverage broadly.** Use only supported leverage candidates. Do not convert rumours, assumed motives or unverified authority into strength.
6. **Test pressure moves.** If a threat/walk-away stance exceeds the credibility of the current alternative, warn the orchestrator and recommend another route or BATNA improvement.
7. **Handle Notional BATNA cautiously.** Capture probability, timing, cost and downside only from supplied evidence. Do not invent percentages, expected values or validated status.
8. **Return implications.** Propose evidence-backed patches/questions and set `material_change_candidate` when BATNA or leverage changes could alter strategy, target/floor or acceptance analysis.

## Safeguards

- No fictional fallback, arbitrary probability or pseudo-scientific leverage score.
- Weak BATNA does not justify automatic acceptance.
- Do not claim counterpart dependency without evidence.
- Do not bluff by inventing competing offers, deadlines or alternatives.
- If authority/stakeholder detail controls leverage, route the mapping to F04.
- If BATNA uncertainty prevents a reliable least acceptable boundary, tell F02/orchestrator rather than inventing one.

## Output

Return canonical `skill_response`: conclusion/confidence, findings with evidence/provenance, recommendations, permitted state patches, material questions, warnings/conflicts and `material_change_candidate`.

## Stop condition

Stop when alternatives and leverage are reliable enough to support the immediate strategic decision, with material uncertainty visible.
