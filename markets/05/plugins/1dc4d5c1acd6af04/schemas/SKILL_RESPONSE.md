# SKILL_RESPONSE.md

**Status:** Canonical specialist-output interface  
**Version:** 1.0.1  
**Date:** 1 September 2026

## Purpose

Define the response contract returned by specialist skills to the orchestrator. The specialist does not persist state directly.

This interface is **[DESIGN]**.

---

# 1. Response schema

```yaml
skill_response:
  skill_id: string
  request_id: string
  based_on_state_version: integer

  summary:
    conclusion: string
    confidence: low | medium | high | unknown

  findings:
    - finding_id: string
      finding: string
      importance: low | medium | high | critical
      research_provenance: FREEMAN | EXTERNAL | SYNTHESIS | DESIGN
      research_refs: [string]
      evidence_status: KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN | null
      evidence_refs: [string]

  recommendations:
    - recommendation_id: string
      recommendation: string
      rationale: string
      priority: low | medium | high | critical

  proposed_state_patch:
    - patch_id: string
      operation: ADD | UPDATE_WITH_EVIDENCE | SUPERSEDE | FLAG_CONTRADICTION
      path: string
      proposed_value: any
      basis: string
      evidence_refs: [string]

  questions:
    - question_id: string
      question: string
      priority: 1 | 2 | 3
      decision_impact: string
      blocking: boolean

  warnings:
    - warning_id: string
      warning: string
      severity: low | medium | high | critical

  conflicts_with_state:
    - conflict_id: string
      field_or_proposition: string
      current_state: string
      specialist_view: string
      reason: string

  deliverable:                       # optional
    kind: draft | talking_points | agenda | roleplay | other
    content: string

  material_change_candidate:
    triggered: boolean
    fields: [string]
    explanation: string | null
```

---

# 2. Output rules

- Hypotheses may be proposed but not promoted without evidence.
- AI architecture choices are `DESIGN`, not `FREEMAN`.
- Questions follow the materiality policy.
- State patches may `ADD`, `UPDATE_WITH_EVIDENCE`, `SUPERSEDE` or `FLAG_CONTRADICTION`.
- Specialists may not delete history, silently alter pre-commitment, accept a deal, close a negotiation or persist state directly.
- If output would materially change strategy, BATNA, target, floor, authority or deal review, set `material_change_candidate.triggered: true`.
- `deliverable` is optional and is used only where the specialist's bounded output is itself a usable artefact (notably F07 drafting and, where useful, F06 role-play). It does not authorise a strategy change.


---

# 3. Red-team reconciliation

Significant red-team findings are classified by the orchestrator as `ACCEPT`, `TEST`, `REJECT` or `DEFER`. Only reconciled `ACCEPT` findings may directly modify canonical strategy.
