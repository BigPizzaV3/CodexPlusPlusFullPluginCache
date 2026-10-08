# DEAL_REVIEW_RESULT.md

**Status:** Canonical independent-deal-review interface  
**Version:** 1.0  
**Date:** 1 September 2026  
**Research basis:** I FORESAW IT offer tests, Measures of Success, Deal Dashboard/pre-commitment [F03][F07][F08]  
**Architecture:** Independent F08 review gate

## Purpose

Define the structured result returned by the independent deal-review specialist before the orchestrator recommends acceptance of a material deal. This schema does not create a numerical "Freeman score".

---

# 1. Result schema

```yaml
deal_review_result:
  negotiation_id: string
  request_id: string
  based_on_state_version: integer
  offer_reviewed: string

  gate_result:
    status: PASS | CONDITIONAL | FAIL | INSUFFICIENT_INFORMATION
    recommendation: accept | counter | reject | get_information
    rationale: string

  tests:
    interests:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    batna:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    independent_criteria:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    hidden_timebombs:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    priority_topics:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    relationship:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    implementation:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN
      findings: [string]
      critical_failures: [string]
    precommitment:
      status: PASS | CONDITIONAL | FAIL | UNKNOWN | NOT_APPLICABLE
      findings: [string]
      critical_failures: [string]

  conditions_to_accept:
    - condition: string
      criticality: critical | important | desirable

  unresolved_material_unknowns:
    - unknown: string
      why_it_matters: string
      required_before_acceptance: boolean

  precommitment_variances:
    - criterion_id: string
      prior_threshold: string
      current_offer: string
      variance: string
      status: acceptable | unacceptable | requires_user_override

  evidence_warnings:
    - warning: string
      evidence_status: KNOWN | SUPPORTED_INFERENCE | HYPOTHESIS | UNKNOWN

  override_allowed: true
```

---

# 2. Gate logic

## PASS
No unresolved critical failure is identified on current evidence.

## CONDITIONAL
The deal may be acceptable if stated conditions are resolved. The orchestrator must not present it as unconditionally acceptable.

## FAIL
At least one critical criterion fails. Under ADR-008, the orchestrator may not recommend acceptance. The user may knowingly override.

## INSUFFICIENT_INFORMATION
A material acceptance question cannot be assessed responsibly. The normal recommendation is `get_information`, not a guessed pass/fail.

---

# 3. Independence rules

The reviewer must not be instructed to validate the orchestrator's preferred outcome. It should receive relevant state without advocacy such as "we worked hard to get here" unless that fact is itself materially relevant and presented neutrally.

---

# 4. No pseudo-precision

Do not output arbitrary percentages, total scores or claims that the 2026 Deal Dashboard statistically proves the result. Use transparent criterion-level judgements.

---

# 5. Override record

If the user accepts after `FAIL` or unresolved `CONDITIONAL`, canonical state preserves the previous gate result, user's reason, new evidence and timestamp.
