---
name: hiring-scorecard
description: "Build a job-related evaluation scorecard with evidence criteria and anchored ratings before screening or interviews."
license: MIT
metadata:
  version: "0.2.4"
---

# Hiring scorecard

## Inputs

Use an agreed job brief and the hiring manager's desired outcomes. If requirements conflict, identify the decision needed before assigning weights. Ask which capabilities are essential on entry and which can be learned.

## Procedure

1. Select distinct criteria tied to the work. Avoid counting the same capability through several proxies such as years, title, and employer prestige.
2. For each criterion, define the evidence source: work example, portfolio, structured interview, or agreed exercise. Record whether the evidence is available now or must be gathered later.
3. Write criterion-specific anchors on a simple four-point scale: 1 = evidence below the agreed requirement; 2 = partial evidence; 3 = meets the requirement; 4 = exceeds it in a relevant way. Use “not assessed” for missing evidence, never zero.
4. If weighting is useful, agree weights with the hiring owner and make them sum to 100. Do not invent numerical precision or reuse unapproved weights across roles.
5. Identify genuine prerequisites separately. A missing CV detail is not proof that a prerequisite is absent; it becomes a follow-up question.
6. Agree which interview or assessment will collect each remaining piece of evidence. Use the same core criteria for all candidates for this role.

## Output

Return a table: criterion, job outcome, evidence needed, rating anchors, optional agreed weight, assessor, and assessment stage. Include the scoring rules and unresolved calibration decisions.

## Example

Criterion: incident analysis. Meets requirement: explains a production incident, the diagnostic steps, the root cause, and a prevention change with observed results. Exceeds requirement: also demonstrates improvement across several services or teams. Not assessed: the CV only says “supported production.”

## Quality check

Every rating must be reproducible from evidence. Exclude protected characteristics and proxies unrelated to the work. Avoid personality labels, school prestige, unexplained “fit,” and career-gap penalties. Scores organize evidence; they do not make an automatic hiring or rejection decision.

## With Vitae

Read the selected job through live tools if available. Do not confuse candidate/job skill taxonomy tools with this evaluation framework. Unless a verified tool supports storing this exact scorecard, return the document for the recruiter to attach or enter. Never claim it was saved without a successful response.

## Completion and handoff

The hiring owner calibrates the scorecard before `candidate-screening` or `interview-kit` uses it. Record its version so later reviews do not silently apply changed criteria to earlier candidates.
