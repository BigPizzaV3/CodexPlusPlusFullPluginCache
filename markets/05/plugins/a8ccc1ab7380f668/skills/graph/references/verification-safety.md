# Verification and Safety

## Contents

- Evidence hierarchy
- Independent review
- Access and approval
- Failure behavior
- Run report

## Evidence hierarchy

Prefer the strongest evidence available for the claim:

1. Deterministic checks: tests, builds, schemas, exact queries, reproducible commands.
2. Runtime observation: launch, reproduction, browser or UI validation, service response.
3. Source reconciliation: direct inspection of code, plans, records, or primary sources.
4. Independent agent review: skeptical evaluation of artifact and evidence.
5. Model assertion: useful for routing, never sufficient by itself for completion.

Match evidence to the requested outcome. Unit tests do not prove production deployment; a build does not prove end-to-end behavior; a checklist does not prove implementation.

## Independent review

- Give the reviewer the original contract, artifact, and raw evidence.
- Ask for concrete defects, missing proof, and scope violations.
- Keep review read-only.
- Reinvestigate disputed claims once when evidence can resolve them.
- Do not ask the reviewer to rubber-stamp a predetermined verdict.

## Access and approval

| Access | Default behavior |
| --- | --- |
| `read-only` | Run when in scope and permitted. |
| `workspace-write` | Run when the user's requested outcome authorizes local changes. |
| `external-write` | Require explicit request authority or pause at `NEEDS_APPROVAL`. |
| `destructive` | Resolve exact targets and require explicit authorization. |

Approval is node-specific. Approval for one external target does not authorize another target or broader scope. Subagents inherit the parent environment but must follow the narrower access contract assigned to their node.

## Failure behavior

- Preserve raw failure evidence.
- Distinguish code failure, environment failure, missing authority, missing tool, and inconclusive evidence.
- Try a safe alternative when it remains within scope.
- Use one targeted repair round by default.
- Finish `BLOCKED` when an external prerequisite prevents progress.
- Finish `FAILED` when attempted work exhausts its allowed repair and still fails the requested gate.
- Finish `NEEDS_APPROVAL` when progress is possible only after new user authority.

## Run report

Use this compact structure:

```text
Terminal state: COMPLETE | BLOCKED | NEEDS_APPROVAL | FAILED
Executed path: ...
Evidence: ...
Changes/actions: ...
Skipped or unresolved: ...
Remaining uncertainty: ...
User action: ...
```

Omit empty sections, but never omit unresolved work or uncertainty that affects the verdict.
