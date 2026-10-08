# PartnerProf Task Manifest API

`GET /api/v3/task-manifest` is the authoritative public contract for the
PartnerProf manual form, API clients, and ChatGPT. Read it before preparing a
task; do not infer variable names, units, operators, or result semantics.

## Three separate parts

| Part | Purpose | Compute effect |
| --- | --- | --- |
| `computational_reality` | Current state, typed variables, units, constraints, relations, invariants, coordinates, and history. | Encoded as the approved reality field. |
| `request` | Mode (`ADMISSIBILITY`, `REALIZATION`, or `FULL_CYCLE`), requested output, explicit goals, and optional worker request. | Defines what the returned state is evaluated against. |
| `external_comparison` | IBM or another external baseline and a post-result comparison method. | Never enters the EvO compute vector and never becomes a goal implicitly. |

## Prepare/run workflow

1. Read `/api/v3/task-manifest` and select only catalog-supported keys.
2. Send `task_manifest` to `POST /api/v3/tasks/prepare`.
3. Review the accepted counts, declared termination settings, external-reference
   boundary, and approval hashes.
4. Send only `prepared_task_id` and `confirm_execution: true` to
   `POST /api/v3/tasks/run`.

The prepared ID is an unguessable, non-listable capability held for one hour in
volatile server memory. A service restart expires it. The run endpoint cannot
receive a replacement field, vector, goal, or benchmark.

Unknown catalog keys, invalid units, states, operators, and malformed values
are rejected. They must never be silently discarded.

## Supported entry forms

- Structured JSON: smaller reality fields submitted as a `task_manifest`.
- Reality Matrix text: first read `GET /api/v3/matrix-text-contract`, then
  prepare through `POST /api/v3/matrix-tasks/prepare` and run its returned ID
  through `POST /api/v3/tasks/run`. This is the same line grammar as the
  manual `/api/v2/model/prepare-matrix` route.
- Published presets: inspect `/api/v2/composer/catalog`, then use the matching
  catalog values in a task manifest.

NPZ and DIMACS-CNF manifest/data-pair import are reserved contracts and are
not claimed as implemented until the manifest endpoint marks them supported.

## Interpreting a result

`REALIZED_STATE` means that CML published an admissible state in the declared
field. It does not by itself mean that an optimization goal was reached or that
an external IBM reference was exceeded. Read `goal_status`, `goal_checks`,
`evolution.termination`, and any external comparison independently.

The public output intentionally excludes private CML implementation paths,
operator matrices, internal working steps, and source code.
