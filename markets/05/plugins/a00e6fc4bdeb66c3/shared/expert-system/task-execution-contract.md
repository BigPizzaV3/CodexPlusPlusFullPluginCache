# Task execution contract

Every material implementation work package records:

Use the shared [Context Package](context-package.md) as a task-sized view of this contract, not a second specification. Existing aliases/references may supply its applicable fields; do not duplicate approved truth. Simple non-material work does not require this full form.

```text
TASK_ID
OBJECTIVE
ACTIVE_SKILL
LEAD_ROLE
SUPPORT_ROLES
REVIEW_ROLES
SOURCES
FIXED
TARGETS
BOUNDS
CLASS_2_DISCRETION
CLASS_3_DISCRETION
PROHIBITED
METHOD_LOCK
REPRESENTATION_STRATEGY
PRODUCTION_LINEAGE
CALIBRATION_CHECKPOINT
DEPENDENCIES
CAPABILITY_CONTEXT
ASSURANCE_MODE
TESTS
EVIDENCE
ACCEPTANCE_ORACLES
ACCEPTANCE_ENVIRONMENT
LOCAL_CHECKPOINT
PASS_CONDITION
STOP_CONDITION
ITERATION_BOUND
ROLLBACK
OUTPUT
```

The contract must be portable without hidden chat context. Sources include exact identifiers, versions, status, permitted sections, precedence, and read order. `PRODUCTION_LINEAGE` records Source Master, Publishing/Delivery Target and Runtime Representation only when this distinction materially affects the task; otherwise use `NOT_APPLICABLE`. `CALIBRATION_CHECKPOINT` identifies the applicable authorized checkpoint and protected scope or `NOT_APPLICABLE`. Select `ASSURANCE_MODE` from the shared [risk-adaptive assurance model](risk-adaptive-assurance-model.md); combine modes only when multiple material risk dimensions exist. `ACCEPTANCE_ORACLES` names the closest authorized sources of actual truth for material claims. `ACCEPTANCE_ENVIRONMENT` records only measurement-relevant identity or a justified `NOT_APPLICABLE`. `ITERATION_BOUND` is required only when repair/calibration could become an open-ended search; state materially different hypothesis/variant, time or cost limits and the escalation route. The task cannot start if a required Class-1 decision, source, permission, environment, rollback path, or acceptance method is absent.

`METHOD_LOCK` carries the applicable compact view from [decision authority](decision-authority-model.md), resolved by the builder before execution. Use an exact accessible decision record or include its scoped contents; a bare `METHOD_CLOSED` label is insufficient. Omit for tasks without an applicable closed method and retain any material OPEN decision as a readiness dependency. Existing `METHOD_DECISION` fields may alias this view when they carry the same meaning; do not maintain duplicate records.

For technical execution read the [environment prerequisite gate](provider-capability-routing.md) and the [task-start decision](session-lifecycle.md). `CAPABILITY_CONTEXT` is their task-sized prerequisite/result view, not a second registry. Existing DEPENDENCIES, SOURCES, ACCEPTANCE_ENVIRONMENT and permission fields may supply its meanings by exact reference. Carry relevant method/guidance freshness with METHOD_LOCK, not hardcoded CURRENT/CLOSED labels. Before dependent execution verify required capabilities are task-sufficient in the actual recipient environment; missing/unknown required capability blocks execution, not reopens the method. This shared entrypoint applies to domain skills without copying the policy into them.
