---
name: job-intake
description: "Turn a recruiting vacancy or hiring-manager conversation into an agreed job brief, with requirements, constraints, and open questions."
license: MIT
metadata:
  version: "0.2.4"
---

# Job intake

## Inputs

Start with the vacancy, hiring-manager notes, and any approved job description. Identify the client, role, hiring owner, location/work arrangement, employment type, compensation range and currency, hiring timeline, and interview process. Ask only for missing facts that affect the brief; preserve unknowns instead of inventing answers.

## Procedure

1. Ask what the hire needs to accomplish in the first three and six months. Turn vague labels such as “rockstar” into observable work outcomes.
2. Separate must-have capabilities from preferences. For every must-have, record why it is needed and what evidence would demonstrate it. Challenge unnecessary credential or exact-title requirements with the hiring owner.
3. Record logistics separately from capability: location, working hours, travel, compensation, start date, and any role-specific authorization requirement supplied by the employer. Do not infer eligibility from nationality or names.
4. Capture the opportunity accurately: scope, team, reporting line, support, and progression. Mark any selling point that still needs confirmation.
5. Resolve contradictory sources with the hiring owner. Keep source and date alongside disputed claims.
6. Return the brief and a short decision list. An unconfirmed intake is a draft, not an approved vacancy.

## Output

Produce: role summary; expected outcomes; must-haves with evidence; preferences; working conditions; approved compensation; process and owners; candidate proposition; unresolved questions with decision owners. State which questions block sourcing and which can wait.

## Quality check

Can another recruiter explain success in the role without the original conversation? Are preferences clearly separated from requirements? Are salary, location, and process facts sourced? Avoid age, gender, family status, ethnicity, or “culture fit” proxies as selection criteria.

## Example

Input: “Senior backend engineer, must know our exact framework, own reliability.”

Draft outcome: “Within six months, reduce recurring production incidents and own the on-call improvement plan.” Evidence: a concrete example of diagnosing incidents and preventing recurrence. Open question for the manager: is the exact framework essential on day one, or can experience with comparable systems suffice?

## With Vitae

If connected, use live `list_jobs`/`get_job` and `list_clients`/`get_client` tools to identify the records. Never guess IDs. Prepare the brief before requesting a `create_job_draft` or update. Missing required API fields remain questions. Respect server approval responses and read back successful changes. Otherwise return a document the recruiter can enter in Vitae.

## Completion and handoff

Hand the approved requirements to `hiring-scorecard`; retain open questions and the hiring owner's approval state. Do not publish a vacancy or start a paid search merely because the brief is complete.
