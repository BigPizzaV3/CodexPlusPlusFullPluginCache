# Coding-agent task contract

Fill required fields from sources. NOT_APPLICABLE needs a reason. Unknown task-critical fields mean TASK_BLOCKED, not invented values. This extends the shared task contract; aliases must agree.

```text
TASK_ID:
ATTEMPT_ID:
OBJECTIVE:
WHY_NOW:
CURRENT_STATE:
CURRENT_PHASE:
CURRENT_GATE:
BASELINE: repository/worktree, branch, revision, dirty-tree snapshot and ownership
EXPECTED_OUTPUT_STATE: permitted delta from baseline; actual generated final revision/hash recorded later, never invented
AUTHORITATIVE_SOURCES: manifest version/hash, source IDs/paths, allowed sections, precedence, recipient access
UPSTREAM_ARTIFACT_CONTEXT: authority/truth status, artifact type, bounded scope and provenance when produced by another worker; N/A with reason
ACTIVE_SKILL:
LEAD_ROLE:
SUPPORT_ROLES:
REVIEW_ROLES:
DEPENDENCIES:
CAPABILITY_CONTEXT: task-sized prerequisite/result view from the shared task contract, with actual recipient environment evidence or explicit unresolved gap
FIXED_CLASS_1:
TARGETS:
BOUNDS:
CLASS_2_AUTHORITY: named lead, reversible choices, decision log, evidence/review
CLASS_3_AUTHORITY:
PROHIBITED_CHANGES:
PERMITTED_FILES_OR_AREAS:
METHOD_DECISION: OPEN decision/readiness dependency, or the applicable scoped METHOD_LOCK from the shared task contract resolved by the receiver; N/A with reason when no material method choice exists
METHOD_GUIDANCE_FRESHNESS: current result and exact method-record reference, not an assumed CURRENT label
REPRESENTATION_STRATEGY: approved proof or explicit N/A
PRODUCTION_LINEAGE: Source Master, Publishing/Delivery Target and Runtime Representation when material, or N/A with reason
CALIBRATION_CHECKPOINT: applicable authorized checkpoint plus protected scope, or N/A with reason
TESTS: actual commands/procedures, environments, criteria, required outcomes
ASSURANCE_MODE: NORMAL | MATERIAL | HIGH_RISK | PERCEPTUAL_OWNER_CRITICAL with reason
ACCEPTANCE_ORACLES: direct non-circular observations that determine each material claim
ACCEPTANCE_ENVIRONMENT: exact environment/state relevant to measurement, or N/A with reason
REQUIRED_EVIDENCE: IDs, logs/captures, baseline/final-state identity
TRANSCRIPT_STATUS: AVAILABLE with location/scope | TRANSCRIPT_UNAVAILABLE | N/A with reason
VISUAL_CHECKPOINT:
INDEPENDENT_REVIEW: owner, independence, scope, criteria or justified N/A
OWNER_CHECKPOINT: trigger and authority required, or N/A
STOP_CONDITIONS:
ROLLBACK_POINT: scope, known restore method, authorization
DEFINITION_OF_DONE:
EXPECTED_REPORT:
AGENT_PROVIDER_MODEL_MODE: observed or unknown
CONTEXT_HEALTH: HEALTHY / DEGRADED / CONTAMINATED / RESET_REQUIRED with evidence, or UNKNOWN before assessment
SESSION_STRATEGY: CONTINUE_CURRENT_SESSION | START_FRESH_SESSION with reason; UNKNOWN until sufficient context evidence is available
CONTEXT_MANIFEST: included sources and excluded historical/irrelevant context
HARNESS_VERSION:
ATTEMPT_TIME_COST_LIMIT:
ITERATION_BOUND: materially different hypotheses/variants and escalation route, or N/A with reason
DISPATCH_STATUS: prepared | delivered | acknowledged | unknown
```

## Copyable execution prompt

Implement only TASK_ID/ATTEMPT_ID against the declared baseline and attached accessible contract. Confirm source/working-tree identity first. Follow ACTIVE_SKILL and the lead's bounded authority; preserve protected files and unrelated edits. Execute an applicable METHOD_CLOSED decision and do not restart tool, stack, representation or workflow exploration without a documented canonical reopen trigger. Do not resolve Class-1 gaps, add features, change tools/frameworks or deploy without explicit authority. Report conflicts before dependent edits. Produce the specified evidence and report; do not self-certify required independent review. Stop at the defined checkpoint. If any referenced contract/source is inaccessible, identify it and wait rather than reconstructing it from memory.

EXPECTED_REPORT must include task/attempt, actual final revision/dirty tree, changed files, material Class-2 choices and rationale, actual tests/commands/results, evidence IDs, target/perceptual status, deviations, failures, risks, proposed next step and approvals still needed. Keep claims separate from validated results.
