# Coding-agent execution model

Version 1.2. Provider-neutral operating policy; provider mechanics live in verified provider profiles.

## Ownership and authority

The project orchestrator owns outcomes, dependencies and project integration. The harness architect owns the repository-specific operating layer under [coding-agent-harness-model.md](coding-agent-harness-model.md). The execution controller owns the bounded agent loop, context, task readiness, report validation and next-task routing. The domain implementation skill owns the change method. The implementer produces artifacts; qualified reviewers accept evidence. A new role label does not make an implementer independent.

Use the existing [decision-authority model](decision-authority-model.md), [professional-discretion policy](professional-discretion-policy.md), [specialist-review model](specialist-review-model.md) and [risk-adaptive assurance model](risk-adaptive-assurance-model.md). Unresolved Class 1 stops dependent work, not unrelated safe work. Class 2 needs named lead, target, bounds, reversibility, evidence and review. Class 3 remains internal engineering inside the contract. Neither implies authority to change tools, dependencies, approved architecture, brand, security or scope. An owner checkpoint cannot turn a failed technical gate into PASS.

## Execution state

Record project, phase, gate, repository/worktree, branch, revision, working-tree changes and ownership, last approved checkpoint, current failures, active specification manifest, open Class-1 decisions, risks, agent, session, context health, harness version and next task. Mark unknowns explicitly. Do not invent a revision for a non-Git project: use an approved snapshot identity and explain the limitation.

Bind each task attempt to `TASK_ID`, `ATTEMPT_ID`, source-manifest version/hash, baseline revision plus dirty-tree snapshot, EXPECTED_OUTPUT_STATE, evidence IDs and approval records. EXPECTED_OUTPUT_STATE defines the permitted change relative to baseline; do not invent a future generated commit hash. Record the actual final revision/snapshot separately in the report and bind inspected evidence to it. Recheck baseline and scope before dispatch and acceptance. Concurrent changes, stale reports or changed sources invalidate affected readiness/evidence. Do not overwrite user edits or replay non-idempotent actions after an uncertain result.

## Contract compatibility

Extend, do not replace, [task-execution-contract.md](task-execution-contract.md). The coding contract additionally carries WHY_NOW, current state/phase/gate, baseline, permitted files, session strategy, owner checkpoint and agent report requirements. Its aliases map as follows:

| Coding contract | Shared task contract |
|---|---|
| AUTHORITATIVE_SOURCES | SOURCES |
| FIXED_CLASS_1 | FIXED |
| CLASS_2_AUTHORITY / CLASS_3_AUTHORITY | CLASS_2_DISCRETION / CLASS_3_DISCRETION |
| PROHIBITED_CHANGES | PROHIBITED |
| REQUIRED_EVIDENCE | EVIDENCE |
| VISUAL_CHECKPOINT | LOCAL_CHECKPOINT (visual portion) |
| DEFINITION_OF_DONE | PASS_CONDITION |
| STOP_CONDITIONS | STOP_CONDITION |
| ROLLBACK_POINT | ROLLBACK |
| EXPECTED_REPORT | OUTPUT |

Keep ACTIVE_SKILL, LEAD_ROLE, SUPPORT_ROLES, REVIEW_ROLES and DEPENDENCIES. Record the proportionate ASSURANCE_MODE, direct ACCEPTANCE_ORACLES and only measurement-relevant ACCEPTANCE_ENVIRONMENT. If aliases appear, their meanings must agree; conflict is a specification defect, not a reason to choose one silently. Mark genuinely irrelevant fields NOT_APPLICABLE with justification, never omit critical unknowns.

## Context and session

Use the canonical [Context Package](context-package.md) for source selection and [session lifecycle](session-lifecycle.md) for health, compaction, continuation and clean resumption. Preserve the repository/attempt identity above. These shared policies replace duplicated generic session rules here; provider-specific mechanisms remain in the applicable provider profile.

## Evidence integrity and acceptance

For every material claim record CLAIM, EVIDENCE, VERIFICATION_STATUS, DECISION_CLASS, ACCEPTANCE_STATUS. VERIFIED means inspected/reproduced evidence actually establishes that scoped claim for this baseline. SUPPORTED means relevant but incomplete/indirect evidence. UNVERIFIED means no adequate inspection. CONTRADICTED means evidence opposes it. NOT_APPLICABLE needs a scoped rationale. A pasted assertion, filename or green status alone is not proof.

For critical changes apply where relevant:

`WRITE → READ_BACK → SERVED_OR_RUNTIME_STATE_VERIFY → REVISION_OR_CONFIG_VERIFY → REAL_OUTPUT → MEASURE_WHEN_MEANINGFUL → CLAIM`

No claim such as implemented, applied, fixed, rendered or passed is stronger than the inspected evidence. Prefer a direct real-system oracle to agent-authored expected or observed truth; do not allow a producer to control both sides of a material acceptance comparison. If evidence contradicts an earlier claim, mark `CONTRADICTED` and revalidate downstream conclusions that depended on it before allowing them to stand.

Technical and perceptual gates are separate. Numeric PASS plus observed visual FAIL is overall FAIL. Required missing evidence prevents acceptance. The builder may self-test and report, but cannot finally ratify its own material gate. Reviewers must be independent of the implementation and the critical decisions they accept; fresh context alone does not guarantee independence. If unavailable, record review pending and do not self-certify critical work. A trivial `NORMAL` task may justify a separate review stage as NOT_APPLICABLE.

## Loop and outcome

PLANNED → TASK_READY → AGENT_BRIEFED → IMPLEMENTING → AGENT_REPORT_RECEIVED → EVIDENCE_VALIDATION → SPECIALIST_REVIEW → INDEPENDENT_REVIEW → OWNER_REVIEW (when required) → PASS.

Every transition needs evidence. A prepared prompt is not a dispatched task. Without a connector, provide a manual handoff and wait for actual receipt/report. Select the smallest assurance mode that covers the actual failure impact; do not apply high-risk or perceptual ceremony to routine low-risk work. A scoped small task may record a noncritical review stage NOT_APPLICABLE with rationale; never waive required independent/security/release review. Local task PASS is not project completion or deployment authority.

| Outcome | Next safe action |
|---|---|
| PASS | Update verified state; select next dependency-ready task. |
| FAIL | Repair the same bounded task, preserving failed evidence. |
| BLOCKED | Ask the exact missing owner/source/tool question; continue only independent authorized work. |
| SPEC_DEFECT | Route to specification owner; revalidate affected contracts after approval. |
| REPRESENTATION_FAIL | Stop detail patches; run representation feasibility/proof review. |
| REGRESSION | Defect workflow and affected regression gates; rollback only with authority. |
| SUPERSEDED | Preserve attempt and reason; prevent late results from updating active state. |

Set a bounded attempt/time/cost budget appropriate to the authorized task. For calibration or repair, define a reasonable limit on materially different hypotheses or variants when the search space could loop. On exhaustion, stop parameter search and route by evidence to root-cause diagnosis, representation review, specification review or owner decision. Do not disguise tiny value changes as new hypotheses, loop indefinitely or silently buy capacity.

For a material between-gate ratification, route read-only verification through [implementation-checkpoint-verification.md](implementation-checkpoint-verification.md) and `$verify-implementation-checkpoint`. Trivial low-risk tasks do not require ceremonial intermediate review. No background monitoring, agent launch, repository harness installation, external publication or deployment is implied by this model.
