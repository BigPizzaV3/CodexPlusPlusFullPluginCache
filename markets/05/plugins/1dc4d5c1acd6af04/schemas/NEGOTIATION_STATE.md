# NEGOTIATION_STATE.md

**Status:** Canonical interface schema  
**Version:** 1.0  
**Date:** 1 September 2026  
**Authority:** `01_NEGOTIATION_AGENT_ARCHITECTURE.md` and `02_NEGOTIATION_BEHAVIOUR_CONTRACT.md`

## Purpose

Define the canonical persistent state owned by the negotiation orchestrator. Specialist skills may read bounded views of this state and propose patches. They do not persist it directly.

This schema is **[DESIGN]**.

---

# 1. Core invariants

1. One canonical state exists per tracked negotiation.
2. State changes are versioned.
3. Material history is append-only.
4. Options inside an agreement are separate from alternatives to agreement.
5. BATNA is separate from Notional BATNA.
6. Counterpart motives, interests, authority, constraints and likely reactions carry evidence status where material.
7. Targets and acceptance criteria cannot move silently.
8. Role-play output does not become evidence automatically.
9. Deal-review outcome is independent of advocacy.
10. A specialist cannot close the negotiation or mark a deal accepted.

---

# 2. Enumerations

```yaml
evidence_status:
  - KNOWN
  - SUPPORTED_INFERENCE
  - HYPOTHESIS
  - UNKNOWN

analysis_depth:
  - LIGHT
  - STANDARD
  - FULL

lifecycle_stage:
  - NEW
  - TRIAGE
  - QUICK_ADVICE
  - PREPARING
  - STRATEGY_READY
  - ENGAGED
  - IMPASSE
  - OFFER_RECEIVED
  - DEAL_REVIEW
  - PAUSED
  - CLOSED
  - NO_DEAL

topic_status:
  - open
  - provisionally_agreed
  - agreed
  - withdrawn

deal_review_status:
  - not_required
  - required
  - in_progress
  - pass
  - fail
  - conditional
  - insufficient_information
```

---

# 3. Canonical schema

```yaml
negotiation:
  meta:
    negotiation_id: string
    title: string
    state_version: integer
    lifecycle_stage: lifecycle_stage
    analysis_depth: analysis_depth
    status: active | paused | closed | no_deal
    created_at: datetime
    updated_at: datetime

  objective:
    user_stated_objective: string | null
    strategic_objective: string | null
    desired_outcome: string | null
    success_definition: string | null
    relationship_importance: low | medium | high | unknown
    reversibility: high | medium | low | unknown

  parties:
    user:
      role: string | null
      authority: string | null
      constraints: [string]
    counterpart:
      organisation: string | null
      visible_contact: string | null
      stated_role: string | null
      authority_status:
        value: string | null
        evidence_status: evidence_status
        evidence_refs: [string]
    other_parties:
      - party_id: string
        name_or_role: string
        organisation: string | null
        relationship_to_negotiation: string | null

  evidence_register:
    items:
      - evidence_id: string
        proposition: string
        evidence_status: evidence_status
        basis: string | null
        source_ref: string | null
        materiality: low | medium | high
        last_reviewed: datetime | null
    contradictions:
      - contradiction_id: string
        proposition_a_ref: string
        proposition_b_ref: string
        status: open | resolved
        resolution: string | null
    unresolved_material_unknowns:
      - unknown_id: string
        question: string
        decision_impact: string
        priority: 1 | 2 | 3

  positions:
    user_positions:
      - topic_ref: string | null
        position: string
        source_ref: string | null
    counterpart_positions:
      - topic_ref: string | null
        position: string
        evidence_status: evidence_status
        source_ref: string | null

  interests:
    user:
      - interest_id: string
        interest: string
        priority: critical | high | medium | low | unknown
        evidence_status: evidence_status
        basis: string | null
    counterpart:
      - interest_id: string
        interest: string
        priority: critical | high | medium | low | unknown
        evidence_status: evidence_status
        basis: string | null
    common:
      - interest_id: string
        interest: string
        specificity_test: string | null
        evidence_status: evidence_status
        basis: string | null

  facts_and_research:
    established_facts:
      - fact_id: string
        fact: string
        source_ref: string | null
    research_questions:
      - research_id: string
        question: string
        why_it_matters: string
        expected_decision_impact: string
        status: open | answered | obsolete
        answer: string | null
        evidence_ref: string | null

  options:
    in_agreement:
      - option_id: string
        option: string
        topics_affected: [string]
        expected_value_user: string | null
        expected_value_counterpart: string | null
        evidence_status: evidence_status
    rejected_options:
      - option_id: string
        option: string
        reason_rejected: string
        timestamp: datetime | null

  topics_targets_tradeoffs:
    topics:
      - topic_id: string
        topic: string
        priority: critical | high | medium | low
        current_position_user: string | null
        current_position_counterpart: string | null
        best_target:
          value: string | null
          rationale: string | null
          evidence_status: evidence_status
        minimum_acceptable:
          value: string | null
          rationale: string | null
          evidence_status: evidence_status
        opening_position: string | null
        tradeoffs_within_topic: [string]
        cross_topic_trade_links: [string]
        status: topic_status
    cross_topic_tradeoffs:
      - trade_id: string
        give: string
        receive: string
        rationale: string
        status: proposed | offered | accepted | rejected | withdrawn
        risk_notes: string | null

  alternatives:
    user:
      batna:
        description: string | null
        value: string | null
        evidence_status: evidence_status
        evidence_refs: [string]
      watna:
        description: string | null
        evidence_status: evidence_status
      improvements:
        - improvement: string
          status: possible | in_progress | achieved | rejected
      notional_batna:
        description: string | null
        probability: string | null
        timing: string | null
        cost: string | null
        downside: string | null
        evidence_status: evidence_status
        status: not_used | provisional | validated_for_decision_support
    counterpart:
      batna:
        description: string | null
        evidence_status: evidence_status
        evidence_refs: [string]
      watna:
        description: string | null
        evidence_status: evidence_status
      constraints: [string]
      estimated_dependency_on_agreement:
        value: string | null
        evidence_status: evidence_status

  independent_criteria:
    - criterion_id: string
      criterion: string
      relevance: string
      likely_counterpart_credibility: low | medium | high | unknown
      evidence_ref: string | null
      evidence_status: evidence_status

  stakeholders:
    - stakeholder_id: string
      person_or_role: string
      organisation: string | null
      formal_authority: string | null
      practical_influence: low | medium | high | unknown
      interests: [string]
      stance: supportive | neutral | resistant | mixed | unknown
      relationship_to_visible_counterpart: string | null
      evidence_status: evidence_status
      evidence_refs: [string]
      possible_engagement: string | null
      engagement_risk: string | null

  process:
    current_channel: string | null
    meeting_setting: string | null
    timing_constraints: [string]
    deadlines:
      - deadline: string
        evidence_status: evidence_status
        source_ref: string | null
    sequence:
      current_step: string | null
      proposed_steps: [string]
    agenda: [string]
    process_risks: [string]

  rapport_reactions_responses:
    relationship_state: string | null
    likely_reactions:
      - reaction_id: string
        reaction: string
        evidence_status: evidence_status
        prepared_response: string | null
    interaction_notes: [string]

  proposals:
    opening_offer: string | null
    least_acceptable_package: string | null
    creative_package: string | null
    current_user_offer: string | null
    current_counterpart_offer: string | null
    proposal_history:
      - proposal_id: string
        party: user | counterpart
        proposal: string
        timestamp: datetime | null
        source_ref: string | null

  concessions:
    ledger:
      - concession_id: string
        timestamp: datetime | null
        party: user | counterpart
        topic: string
        from: string | null
        to: string | null
        stated_reason: string | null
        requested_exchange: string | null
        received_exchange: string | null
        conditional: boolean
        reciprocal: true | false | unknown
        strategic_assessment: string | null
        source_event_id: string | null

  precommitment:
    created: boolean
    created_at: datetime | null
    acceptance_criteria:
      - criterion_id: string
        criterion: string
        importance: critical | important | desirable
        threshold: string | null
        evidence_basis: string | null
    disqualifiers: [string]
    relationship_requirements: [string]
    fairness_or_independent_criteria_requirements: [string]
    implementation_risk_limits: [string]
    later_changes:
      - change_id: string
        criterion_id: string
        previous_value: string | null
        new_value: string | null
        new_evidence: string | null
        reason: string
        approved_by_user: boolean
        timestamp: datetime | null

  strategy:
    current_strategy: string | null
    strategic_rationale: string | null
    leverage_sources: [string]
    vulnerabilities: [string]
    current_priority: string | null
    recommended_next_move: string | null
    moves_to_avoid: [string]
    confidence: low | medium | high | unknown
    assumptions: [string]

  roleplay:
    last_snapshot_version: integer | null
    red_team_findings:
      - finding_id: string
        finding: string
        reconciliation_status: ACCEPT | TEST | REJECT | DEFER
    accepted_findings: [string]
    rejected_findings: [string]

  deal_review:
    status: deal_review_status
    offer_reviewed: string | null
    interest_test: pass | fail | conditional | unknown | not_run
    batna_test: pass | fail | conditional | unknown | not_run
    independent_criteria_test: pass | fail | conditional | unknown | not_run
    hidden_timebomb_test: pass | fail | conditional | unknown | not_run
    priority_topic_test: pass | fail | conditional | unknown | not_run
    relationship_test: pass | fail | conditional | unknown | not_run
    implementation_test: pass | fail | conditional | unknown | not_run
    precommitment_test: pass | fail | conditional | unknown | not_run
    conditions: [string]
    recommendation: accept | counter | reject | get_information | null
    reviewer_rationale: string | null
    override:
      occurred: boolean
      user_reason: string | null
      new_evidence: string | null
      timestamp: datetime | null

  history:
    material_events:
      - event_id: string
        timestamp: datetime
        type: string
        summary: string
        source_ref: string | null
        state_changes: [string]
        rationale: string | null
```

---

# 4. Minimum state by analysis depth

## LIGHT

Required only as needed: objective, current positions, material interests, material unknown, current offer if any, and recommended next move. No persistent file is required by default.

## STANDARD

Where continuity is material, persist at least: meta, objective, evidence register, positions, interests, TTT, alternatives, material stakeholders, proposals, concessions, strategy and history.

## FULL

Use the full relevant schema, including pre-commitment where a later acceptance decision is expected.

---

# 5. Material-state-change triggers

The orchestrator must surface a change to the user in STANDARD/FULL mode where a state update materially changes strategy, user BATNA, a critical/high target, minimum acceptable position, material authority assessment, or deal-review outcome.

---

# 6. Validation errors

Reject or flag a patch that attempts to:
- insert a BATNA under options;
- insert an agreement option under alternatives;
- change a pre-commitment threshold without a logged change;
- delete a concession;
- promote evidence without basis;
- mark role-play output as KNOWN solely because it appeared in simulation;
- overwrite a newer state version;
- close the negotiation without an explicit user/material event.
