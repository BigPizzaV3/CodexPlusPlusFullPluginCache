# Implementation Runbook / MOP Module

Use for execution-ready procedures, real production changes/cutovers, migrations, upgrades, replacements, deployments, or other changes with ordered state transitions. Do not create a formal MOP for every troubleshooting remediation or simple corrective action.

Create the procedure only from approved or evidence-justified changes.

## Every meaningful change block or state transition must contain
- Purpose
- Entry conditions
- Risk / impact
- Exact actions or verified GUI paths/commands
- Expected resulting state
- Validation
- PASS criteria
- STOP / FAIL criteria
- Evidence to capture when useful
- Rollback / recovery where technically possible

Do not repeat the full metadata schema around every individual command within a controlled change block. Critical, irreversible, or high-blast-radius actions may require their own inline validation, stop condition, and rollback/recovery guidance.

## Sequencing
- Baseline/read-only checks first.
- One failure domain at a time.
- Validate after every meaningful transition.
- Delay destructive cleanup until the new state is stable.
- Separate migration from decommissioning.
- If rollback is impossible, explicitly call the path Recovery or Forward Fix.

Providing the procedure does not authorize execution. External state changes require an explicit user request and normal platform approval controls.
