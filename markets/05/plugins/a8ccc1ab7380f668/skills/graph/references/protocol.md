# Graph Mode Protocol

## Contents

- Run lifecycle
- Node contract
- State ledger
- Checkpoint rules
- Terminal consistency

## Run lifecycle

Use `PLANNING` and `RUNNING` while work is active. Finish with exactly one of:

- `COMPLETE`: every required path passed or was conditionally skipped, with required evidence.
- `BLOCKED`: progress cannot continue because a dependency or prerequisite is unavailable.
- `NEEDS_APPROVAL`: the next material node requires user authority.
- `FAILED`: attempted work did not satisfy its gate and the repair allowance is exhausted.

Do not use `BLOCKED` for mere difficulty or uncertainty that can still be investigated safely.

## Node contract

Each runtime node must contain:

| Field | Contract |
| --- | --- |
| `id` | Unique lowercase identifier for this runtime attempt. |
| `title` | Short human-readable purpose. |
| `kind` | `scope`, `explore`, `execute`, `verify`, `review`, `synthesize`, `approve`, `monitor`, or `repair`. |
| `role` | `main`, `explorer`, `worker`, `reviewer`, `tool`, or `human`. |
| `access` | `read-only`, `workspace-write`, `external-write`, or `destructive`. |
| `status` | Current node status. |
| `status_history` | Ordered states beginning with `PENDING` and ending at `status`. |
| `depends_on` | Runtime node IDs that must resolve first. |
| `expected_output` | Concrete artifact, decision, or evidence packet expected. |
| `evidence_required` | Whether `PASSED` requires non-empty evidence. |
| `evidence` | Concise references to tests, files, sources, outputs, or approvals. |
| `attempt` | Count of actual `RUNNING` entries. |
| `max_attempts` | Maximum attempts for this runtime node. |
| `approval` | `not-required`, `required`, `granted`, or `denied`. |

Node statuses are `PENDING`, `READY`, `RUNNING`, `PASSED`, `FAILED`, `BLOCKED`, `NEEDS_APPROVAL`, and `SKIPPED`.

## State ledger

Use this checkpoint shape:

```json
{
  "schema_version": 1,
  "run_id": "graph-20260719-example",
  "task": "Audit the project against its plan",
  "status": "RUNNING",
  "nodes": [
    {
      "id": "scope",
      "title": "Resolve audit scope",
      "kind": "scope",
      "role": "main",
      "access": "read-only",
      "status": "PASSED",
      "status_history": ["PENDING", "READY", "RUNNING", "PASSED"],
      "depends_on": [],
      "expected_output": "Bounded audit target and source list",
      "evidence_required": true,
      "evidence": ["User request and repository plan identified"],
      "attempt": 1,
      "max_attempts": 1,
      "approval": "not-required"
    }
  ]
}
```

At each join, retain only information needed to route, verify, resume, and report. Keep noisy command output in node evidence artifacts rather than the main ledger.

## Checkpoint rules

Use file-backed state only when the run is long, scheduled, resumable, or likely to cross context compaction. Before writing inside a Git repository:

1. Resolve a candidate such as `.codex/graph-runs/<run-id>/state.json`.
2. Confirm the parent path is already ignored with `git check-ignore`.
3. Do not modify `.gitignore` or repository policy merely to store state.
4. Validate the file after every structural graph change and before claiming it is resumable.

If these conditions fail, use a compact state capsule in the task instead.

## Terminal consistency

- `COMPLETE` requires every node to be `PASSED` or `SKIPPED`, at least one passed node, and all evidence gates satisfied.
- `BLOCKED` requires at least one blocked node.
- `NEEDS_APPROVAL` requires at least one node waiting for approval.
- `FAILED` requires at least one failed node.
- A node cannot become `READY`, `RUNNING`, or `PASSED` until every dependency is `PASSED` or `SKIPPED`.
- `external-write` and `destructive` nodes cannot become `READY`, `RUNNING`, or `PASSED` until approval is `granted`.
