# SKILL_REQUEST.md

**Status:** Canonical specialist-input interface  
**Version:** 1.0  
**Date:** 1 September 2026

## Purpose

Define the request contract between the negotiation orchestrator and a specialist skill. Specialist skills are normally stateless and reason only from the request and provided state view.

This interface is **[DESIGN]**.

---

# 1. Request schema

```yaml
skill_request:
  skill_id: string
  request_id: string
  negotiation_id: string
  state_version: integer

  context:
    lifecycle_stage: string
    analysis_depth: LIGHT | STANDARD | FULL
    user_request: string
    task: string

  state_view:
    included_sections: [string]
    data: object

  evidence_constraints:
    material_unknowns: [string]
    prohibited_assumptions: [string]
    required_evidence_labels: boolean

  research_context:
    allowed_methodology: [FREEMAN, EXTERNAL, SYNTHESIS, DESIGN]
    research_refs_available: [string]
    research_gap_warnings: [string]

  execution_constraints:
    may_ask_questions: boolean
    may_propose_state_patch: boolean
    may_draft_user_content: boolean
    may_roleplay: boolean
    may_make_acceptance_recommendation: boolean
    output_budget: short | medium | detailed
```

---

# 2. Required fields

Every request must include `skill_id`, `request_id`, `negotiation_id`, `state_version`, lifecycle stage, analysis depth, user request, task and state view.

---

# 3. State-view principle

Pass the smallest state view that allows the specialist to do its job safely.

For TTT, normally pass objective, interests, facts, topics, current positions, BATNA summary and existing concessions.

For deal review, pass current offer, interests, TTT, BATNA, independent criteria, pre-commitment, implementation risks and material evidence uncertainties. Do not tell the reviewer that the orchestrator already wants acceptance.

---

# 4. Stale-state control

A specialist result is valid only against `state_version`. If state changes before reconciliation, the orchestrator must check continued applicability.

---

# 5. Prohibited request patterns

Do not:
- instruct a specialist to validate a predetermined conclusion;
- omit material evidence uncertainty to make an answer easier;
- ask role-play to determine actual counterpart motives;
- ask drafting to decide commercial thresholds;
- ask another module to bypass the independent deal gate.
