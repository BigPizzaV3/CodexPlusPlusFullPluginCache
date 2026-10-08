# 03_DECISION_LOG.md

**Status:** Active architecture decision record  
**Version:** 1.0  
**Date:** 1 September 2026

This file records approved design decisions for the Freeman-based Negotiation Adviser. It does not change the research authority in `00_FREEMAN_RESEARCH_BASE.md`.

---

## ADR-001 — Thin stateful orchestrator
**Decision:** APPROVED  
Use a thin stateful orchestrator with modular specialist skills rather than one monolithic skill or a persistent multi-agent swarm.

## ADR-002 — Canonical state ownership
**Decision:** APPROVED  
Only the orchestrator persists canonical negotiation state. Specialist skills operate on versioned state views and return proposed patches.

## ADR-003 — Snapshot plus material event history
**Decision:** APPROVED  
Maintain a compact current-state snapshot plus append-only material history.

## ADR-004 — Proportional reasoning
**Decision:** APPROVED  
Use LIGHT / STANDARD / FULL analysis depth. Do not invoke the full Freeman stack for simple cases.

## ADR-005 — Question policy
**Decision:** APPROVED  
Ask only questions with plausible material decision impact. Do not interrogate the user through the full I FORESAW IT checklist unless requested or genuinely necessary.

## ADR-006 — Persistence model
**Decision:** APPROVED — Hybrid  
Use conversation state for LIGHT negotiations. Use explicit persistent negotiation state for material STANDARD/FULL negotiations where continuity matters.

## ADR-007 — State visibility
**Decision:** APPROVED  
Keep working state primarily internal. Surface concise state summaries on request and at material milestones.

## ADR-008 — Deal-review gate
**Decision:** APPROVED — Hard recommendation gate  
A failed material independent deal review prevents the agent from recommending acceptance. The user may knowingly override.

## ADR-009 — Specialist execution
**Decision:** APPROVED  
Sequential by default. Permit selective parallel analysis only where genuinely independent FULL-mode analysis justifies the extra cost.

## ADR-010 — High-stakes classification
**Decision:** APPROVED  
Use consequence-based triage rather than a fixed monetary threshold.

## ADR-011 — Notional BATNA
**Decision:** APPROVED — Provisional use  
Permit Notional BATNA only as explicitly uncertainty-aware decision support until the primary procedure is more fully researched.

## ADR-012 — Incomplete Freeman named tools
**Decision:** APPROVED  
Where primary research is incomplete, retain the supported principle but do not claim an invented exact Freeman procedure.

## ADR-013 — Material strategic changes
**Decision:** APPROVED  
In STANDARD/FULL negotiations, the adviser must surface any material change to strategy, BATNA, target, walk-away position, decision-maker/authority assessment or deal-review outcome, with the reason for the change.

## ADR-014 — No pseudo-scientific scoring
**Decision:** APPROVED  
Use structured qualitative decision gates unless later evidence supports validated quantitative scoring.

## ADR-015 — Research provenance
**Decision:** APPROVED  
Preserve `[FREEMAN]`, `[EXTERNAL]`, `[SYNTHESIS]` and `[DESIGN]` provenance in development artefacts and specialist interfaces.

---

---

## ADR-016 — Challenge-language assertiveness

**Decision:** APPROVED — Option B  
Use direct but proportionate challenge language. Where there is a real strategic issue, the adviser may say "I wouldn't do this yet" or equivalent and explain briefly. Do not use forceful warnings routinely where the issue is minor.

---

## ADR-017 — Visibility of Freeman method names

**Decision:** APPROVED — Option B  
Use Freeman methods internally by default. Name I FORESAW IT, TTT and other frameworks when useful for training, audit, explanation or when the user asks to see the method. Do not burden ordinary advice with unnecessary framework labels.

---

## ADR-018 — Persistent state in STANDARD negotiations

**Decision:** APPROVED — Option B  
Create an explicit persistent state artefact for STANDARD negotiations when the matter is material or expected to continue across multiple exchanges. Do not create one automatically for every STANDARD case.

---

## Current status

- `00_FREEMAN_RESEARCH_BASE.md` — canonical research authority.
- `01_NEGOTIATION_AGENT_ARCHITECTURE.md` — approved architecture baseline v1.0.
- `02_NEGOTIATION_BEHAVIOUR_CONTRACT.md` — approved behaviour baseline v1.0.
- Canonical schemas — created as interface baseline v1.0 before individual skills.

---

## ADR-019 — Optional specialist deliverable field

**Status:** CONFORMANCE CORRECTION — 1 September 2026  
**Decision:** Add an optional `deliverable` field to the common specialist response for bounded artefacts such as F07 drafts and F06 role-play output.

**Reason:** The approved architecture assigns F07 responsibility for usable communication, but the v1.0 common response schema had no explicit field for that output. Using `recommendations` as a draft container would blur analysis and deliverable semantics. This correction restores the approved F07 boundary and does not change Freeman research, agent authority or state ownership.

---

## Current implementation status

As of 1 September 2026:
- F01–F08 specialist skill documents exist;
- specialist acceptance scenarios exist;
- orchestrator, routing rules, state-update rules and agent system prompt exist;
- common response schema v1.0.1 includes the optional deliverable field required by F07;
- behavioural isolated-model RED/GREEN testing remains open before deployment-ready status.

---

## Validation package status — 1 September 2026

No architecture decision changed. Independent behavioural validation is now specified by:
- `CODEX_BEHAVIOURAL_VALIDATION_PROMPT.md`;
- `tests/BEHAVIOURAL_TEST_HARNESS.md`;
- `tests/ADVERSARIAL_CROSS_SKILL_ACCEPTANCE.md`;
- `tests/BEHAVIOURAL_RESULTS_TEMPLATE.md`.

The system remains a **release candidate, not deployment-ready**, until isolated-model RED/GREEN testing satisfies the documented gate.
