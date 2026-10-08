# Execution loop

## Intake and task selection

Use the shared state/contract schema. Inspect source access, authority, source freshness, current diff and work ownership before action. Missing irrelevant fields may be NOT_APPLICABLE with reason; required unknowns are blockers. A report about a different baseline cannot advance the current task.

Select the smallest dependency-ready change with the highest agreed priority. Explain WHY_NOW from the approved plan, not a newly invented roadmap. Preserve the existing order unless the owner authorizes a change. Do not expand a bug report into a refactor or tool migration.

TASK_READY requires: accepted source slice; closed task-relevant Class 1; bounded Class 2/3; known baseline and permitted files; required inputs; the active method status and authority when material; feasible representation where applicable; selected assurance mode; direct acceptance oracle(s); declared acceptance environment when measurement depends on it; test/evidence/review plan; checkpoint/rollback; explicit completion and stop conditions. Record TASK_BLOCKED otherwise. An independent task may proceed only if authorized and actually unaffected.

## State transitions

| State | Evidence required to enter / leave |
|---|---|
| PLANNED | Candidate task and dependency source recorded. |
| TASK_READY | Readiness checks passed for specific baseline/manifest. |
| AGENT_BRIEFED | Actual delivery/receipt acknowledged; prompt prepared alone remains TASK_READY. |
| IMPLEMENTING | Observed run or attributable agent/user confirmation; no invented background execution. |
| AGENT_REPORT_RECEIVED | Preserve raw report, author, attempt and time; unsolicited reports may enter here directly with baseline unknown. |
| EVIDENCE_VALIDATION | Associate claims with actual inspected artifacts/runs; unknown baseline blocks acceptance, not safe report inspection. |
| SPECIALIST_REVIEW | Lead assesses domain result against target, not intent. |
| INDEPENDENT_REVIEW | Record reviewer identity/context, non-involvement and findings; pending if unavailable. |
| OWNER_REVIEW | Required key milestone/Class-1/external authority approval record; otherwise N/A with reason. |
| PASS | All task criteria met for final state through the declared oracle and environment, no unresolved required gate; checkpoint registered. A material implementer report cannot enter PASS without the required evaluator/authority gate. |

Do not invent earlier transitions when consuming a report midway through a session. Keep observed and inferred state separate.

## Repair, interruption and concurrency

- Each repair is a new ATTEMPT_ID under the same task, with previous failure evidence and bounded changes. Define retry/time/cost and, when useful, materially different hypothesis/variant limits. After the bound, stop parameter search and route to root-cause diagnosis, representation review, specification review or owner decision instead of continuing microvalue changes.
- Track approved Class-2 decisions, file changes, results, current visual status, failures, risks and next safe action after each attempt. Commit only when authorized and according to project rules; never stage unrelated files.
- On source/baseline drift pause affected acceptance. Compare actual changes, rebase the task contract with authority and rerun affected checks. Never overwrite others' work.
- On uncertain dispatch/timeout inspect run status before retry. Never duplicate a deployment or migration. Late output from SUPERSEDED attempts cannot update current state.
- On cancellation preserve state; do not launch follow-up work. Continued monitoring requires an explicitly supported and authorized recurring mechanism.
- Source conflict → Class 1 stop dependent work. Infeasible representation or another evidenced canonical reopen trigger → preserve the closed decision, mark the trigger and route method/representation review before comparing alternatives. Otherwise repair or calibrate inside the closed method. Failed tests → FAIL/defect route. Introduced regression → REGRESSION. Incorrect specification → SPEC_DEFECT; no implementer rewrite under cover of repair.
- Deployment is a separate gate: explicit target/environment, authority, tested revision, secrets handling, backup/rollback, review and observability. “Deploy” may authorize the intended action but does not fill missing target or waive technical gates.
- A material intermediate gate may route to `$verify-implementation-checkpoint` for read-only ratification. The controller remains responsible for state and next-task routing; the verifier neither repairs nor automatically advances the phase.
- Choose session boundaries by logical state: material gate, architecture transition, diagnosis, independent-review handoff, source replacement or demonstrated context degradation. Do not rotate sessions merely because a generic token/time threshold was reached.

## Manual mode

When the controller cannot access the external agent or repository, say so. Deliver an exact copyable task packet and request the smallest necessary report/evidence. Do not say “Claude is running”, “sent”, “installed” or “verified” from prompt preparation. Never ask for passwords or secret values; use redacted paths/configuration and secure local handling.
