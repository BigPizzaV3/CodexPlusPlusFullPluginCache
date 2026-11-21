---
name: candidate-screening
description: "Compare candidate evidence with an agreed role scorecard, identify missing information, and prepare a recruiter review without making automatic hiring decisions."
license: MIT
metadata:
  version: "0.2.4"
---

# Candidate screening

## Inputs

Use the selected job brief, the agreed scorecard, and candidate-provided or authorized records. Record the source and date for each profile. If the scorecard is missing, establish criteria before evaluating people.

## Procedure

1. Resolve identity and duplicate records. Do not join two people just because their names match.
2. Extract job-related evidence for each criterion. Preserve short source references so the recruiter can verify the claim. Distinguish “led,” “contributed,” and “observed” where the source supports that distinction.
3. Apply the agreed anchors only where evidence exists. Mark missing evidence as “not assessed.” A CV omission is not a negative finding.
4. Identify contradictions and write neutral clarification questions. Avoid speculative explanations for employment gaps or career changes.
5. Summarize strengths, unresolved requirements, and the next evidence needed. If a stored match score exists, label its source and keep it separate from the evidence assessment.
6. Return an assessment for human review. Do not automatically reject, advance, or rank candidates based on protected characteristics, health, family circumstances, ethnicity, religion, age, or inferred personality.

## Output

For each candidate: record identifier; criterion-by-criterion evidence table; supported rating or not assessed; source; strengths; uncertainties; and targeted follow-up questions. Include a concise recruiter-review summary, not a final employment decision.

## Example

Requirement: ownership of production reliability. CV evidence: “Built dashboards for three services.” Assessment: observability contribution evidenced; incident leadership not assessed. Follow-up: “Tell us about an incident you personally investigated, the action you took, and what changed afterward.” Do not rewrite the CV as “owned reliability across three services.”

## Quality check

Could another reviewer trace every conclusion to a source? Did missing information stay unknown? Were the same criteria used across candidates? Are any stored or model-generated scores being mistaken for facts?

## With Vitae

Use live `search_ats_candidates`, `get_candidate`, and `get_candidate_resume` after selecting the correct record. Read the job through `get_job`. A recruiter-approved stage change is a separate action with a verified application identifier and the server's approval boundary. Do not move stages as a side effect of writing this report.

## Completion and handoff

Give the recruiter the evidence and questions. Continue to `candidate-outreach` or `interview-kit` only according to the recruiter's decision and the candidate's current stage.
