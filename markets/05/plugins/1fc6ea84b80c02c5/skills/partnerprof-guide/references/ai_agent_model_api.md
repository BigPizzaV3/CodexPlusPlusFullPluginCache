# EvO PartnerProf — Public API & IT Integration Guide

This document describes only the public integration contract. It intentionally does not document protected implementation paths, private module names, or internal routing.

## Current public workflow (ChatGPT and new clients)

1. For every new request, first read `GET /api/v3/knowledge-map`; do not decide
   fit, reject the request, or invent task questions from model memory.
2. Read `GET /api/v3/task-manifest` and use only its catalog terms.
3. Submit `computational_reality`, `request`, and `external_comparison` to
   `POST /api/v3/tasks/prepare`.
4. Review accepted counts, field-terminal policy, comparison boundary, hashes,
   and the returned `prepared_task_id`.
5. After explicit user confirmation, submit only that ID and
   `confirm_execution: true` to `POST /api/v3/tasks/start`.
6. Preserve the returned `run_id`. Poll `GET /api/v3/runs/{run_id}/status`, read
   graph data from `/progress`, and retrieve the terminal public result and
   certificate from `/result`.

Unknown manifest fields are rejected. The v3 ID is short-lived and held in
volatile server memory; a restart expires it. It prevents a client from
changing the reviewed field between preparation and execution.

`/api/v3/tasks/run` remains available as the compatible synchronous route. MCP,
ChatGPT and browser clients should use `/start`: it returns immediately and the
server continues work independently of the initiating HTTP connection. Starting
the same prepared ID again is idempotent and returns the same lifecycle ID.

Per-run status is authoritative. Never infer completion from process CPU usage,
an empty aggregate queue, or `/api/v1/status`. Do not set `max_steps` for an
ordinary realization: the necessary chronon count is unknown and termination is
defined by the field. `progress_fraction` is therefore null for such a run. It
is present only for an explicitly bounded technical test and then means only
consumption of that declared test slice. `admissibility` is categorical, and no
generic `goal_distance` is defined or emitted.

Whenever a call returns `run_id`, immediately call the run-specific `status`
and `progress` tools and render only their returned samples. After the terminal
event, retrieve `result`. For field-terminal work, plot chronon/event order and
elapsed time; never turn a null `progress_fraction` into an estimated 0–100%.

### Random Circuit Sampling vocabulary

For an RCS task, send `problem_family=random_circuit_sampling` and replace the
free-form state variables with one strict `PartnerProf-RCS/1.0` circuit object:

```json
{
  "task_manifest": {
    "computational_reality": {
      "problem_family": "random_circuit_sampling",
      "rcs_circuit": {
        "schema": "PartnerProf-RCS/1.0",
        "circuit_id": "rcs.example.2q",
        "qubit_count": 2,
        "circuit_depth": 2,
        "gate_sequence": [
          {"layer": 0, "gate": "H", "qubits": [0]},
          {"layer": 1, "gate": "CX", "qubits": [0, 1]}
        ],
        "output_bitstring": {"role": "target", "value": "00"}
      }
    },
    "request": {
      "mode": "ADMISSIBILITY",
      "requested_output": "circuit_admissibility_state"
    },
    "external_comparison": {}
  }
}
```

Do not add a numeric vector. PartnerProf validates and canonicalizes the exact
circuit identity, computes or verifies its SHA3-512 digest, selects a sufficient
dimension when none is declared, and creates the contiguous `numpy.float64`
field. The optional output bitstring must be labelled `observed`, `target`, or
`realized_history`; these roles are not interchangeable. Read
`/api/v3/task-manifest` before composing the request for the current gate,
arity, parameter, layer, and bitstring rules.

`PHASED_X(p,t)` is a native canonical entry with parameters ordered as
`[phase_exponent_p_half_turns, exponent_t_half_turns]`. Do not convert these two
exponents to radians. The equivalent identity is `Z^-p X^t Z^p`, with
`global_shift=0` fixed by this shorthand. Each canonical `*_POW` entry instead
requires `[exponent_half_turns, global_shift]` so exact phase identity is not
lost. Normalize import aliases only through `gate.accepted_aliases` returned by
the live manifest.

The published vocabulary covers exactly convertible fixed-width unitary/global
phase operations. Measurement is represented by the role-labelled
`output_bitstring`. Reset, barriers, delays, pulse instructions, classical
control, arbitrary unitary matrices, channels, variadic controls and opaque
custom gates are not accepted as gate names and are never guessed or silently
decomposed.

The resulting state event is evidence only within the declared structural RCS
field. It is not a hardware sample, probability or fidelity estimate, nor proof
of quantum advantage.

If the concrete public Cirq source is too large for `gate_sequence`, use
`partnerprof_prepare_rcs_source(source_url, expected_sha3_512)`. The source hash
is mandatory and must be known independently. PartnerProf verifies the fetched
bytes first, parses them without execution, rejects the complete input on an
unknown construct and returns a normal reviewable `prepared_task_id`. This tool
prepares only; it never implies permission to start the run.

## Legacy direct-field workflow

PartnerProf uses a two-phase structured input contract:

1. **Discover** the supported task types, variables, units, ranges, and presets.
2. **Prepare** one exact `composer_field` and receive its approval digest.
3. **Run** the identical `composer_field` together with that digest.
4. **Read** the public CML state, the separate goal status, the problem-specific explanation, and audit evidence.

The API is not a free-text word-problem interpreter. Missing numeric values, relations, invariants, and goals must not be invented by a client, AI tool, or agent.

## Discovery endpoints

- `GET /api/v2/task/catalog` — task and public entry-mode catalogue.
- `GET /api/v2/model/catalog` — structured field catalogue with variables, units, ranges, presets, and limits.
- `GET /api/v2/model/example/quantum-tunneling` — a complete runnable quantum tunnelling example.
- `GET /api/v2/model/openapi.json` — OpenAPI 3.1 contract.
- `GET /health` — public availability check.

## Example input

The quantum example endpoint returns a complete `composer_field`. Its preset includes numeric states, relations, target, compute slice, and **Default vector = 0.2**.

Use the returned `composer_field` unchanged:

```json
{
  "composer_field": {
    "problem_family": "quantum_tunneling",
    "geometry": "unbounded_slice",
    "dimension": 128,
    "variables": [
      {
        "key": "nuclear_distance",
        "state": "observed",
        "value": "8",
        "unit": "fm",
        "min": "1",
        "max": "20",
        "origin": "system_preset",
        "confirmed": true
      },
      {
        "key": "barrier_width",
        "state": "fixed",
        "value": "5",
        "unit": "fm",
        "min": "1",
        "max": "10",
        "origin": "system_preset",
        "confirmed": true
      },
      {
        "key": "barrier_energy",
        "state": "fixed",
        "value": "400",
        "unit": "keV",
        "min": "100",
        "max": "800",
        "origin": "system_preset",
        "confirmed": true
      },
      {
        "key": "temperature",
        "state": "observed",
        "value": "100000000",
        "unit": "K",
        "min": "10000000",
        "max": "200000000",
        "origin": "system_preset",
        "confirmed": true
      }
    ],
    "constraints": [],
    "relations": [
      {
        "source": "nuclear_distance",
        "target": "barrier_energy",
        "relation": "opposes",
        "weight": 1.0,
        "bidirectional": false,
        "origin": "system_preset",
        "confirmed": true
      },
      {
        "source": "barrier_width",
        "target": "nuclear_distance",
        "relation": "couples",
        "weight": 1.0,
        "bidirectional": true,
        "origin": "system_preset",
        "confirmed": true
      }
    ],
    "invariants": [],
    "goals": [
      {
        "variable": "nuclear_distance",
        "op": "<=",
        "value": "5",
        "unit": "fm",
        "confirmed": true
      }
    ],
    "question": {"mode": "ADMISSIBILITY"},
    "optimization": {"objective": "none", "custom": ""},
    "compute_slice": {
      "extent": 1e-13,
      "resolution": 1e-15,
      "step_size": 1e-15,
      "pixel_grain": 1e-15,
      "max_steps": 10000,
      "timeout_s": 60,
      "initial_perturbation": 0.2
    }
  }
}
```

The live example endpoint should be preferred over copying this static example because it always reflects the currently deployed public catalogue.

## Phase 1 — prepare

`POST /api/v2/model/prepare`

Content type: `application/json`

```json
{
  "composer_field": { "...": "exact structured field" }
}
```

The response returns the normalized field and:

```text
audit.vector_sha3_512
```

Store that value. It identifies the exact approved numeric input.

## Phase 2 — run

`POST /api/v2/model/run`

Send the identical field plus the approval digest:

```json
{
  "composer_field": { "...": "identical structured field" },
  "approved_vector_sha3_512": "<digest returned by prepare>"
}
```

If the field changed after preparation, the server returns HTTP 409. Prepare the changed field again instead of reusing the old digest.

## Reading the result

The public response should be read in this order:

- `state` — public CML realization state.
- `interpretation.verdict` — human-readable admissibility conclusion.
- `interpretation.goal_status` — whether the declared goal was actually proven; this is separate from admissibility.
- `interpretation.scenario` — what was calculated, exact inputs, deterministic input-derived checks, conclusion, and supporting evidence.
- `run_id` — stable run reference.
- `output_vector_sha3_512` — integrity digest of the exact returned vector.
- `certification` — evidence/certification state for the existing result.

A positive admissibility result is not automatically proof that the declared target has already been reached.

## HTTP behavior

- **200** — successful public request.
- **400** — invalid or incomplete structured input.
- **409** — the field no longer matches the approved digest.
- **429** — public compute capacity is busy. Retry the same request later without altering the approved field.
- **5xx** — service/runtime failure. Do not manufacture a replacement result.

## IT integration

### Reverse proxy

Preserve request bodies and `Content-Type`. When PartnerProf is mounted below a public URL prefix, forward `X-Forwarded-Prefix` so generated public links remain inside that mount.

### Health monitoring

Use:

```text
GET /health
```

Treat a non-2xx response as unavailable.

### Timeouts

The submitted compute slice and server policy define the accepted execution limits. The reverse proxy and client timeout must be long enough for an accepted run.

### Persistence on the client side

For every run, store at minimum:

- the approved structured input or its own immutable reference,
- `audit.vector_sha3_512` from preparation,
- `run_id`,
- `output_vector_sha3_512`,
- the returned verdict and goal status.

This is enough to prove which input was approved and which public result belongs to it without requiring access to protected implementation details.

## Rules for AI tools and agents

An AI or agent may:

- load the public catalogue,
- present allowed fields and units,
- validate completeness,
- serialize explicit user/measurement/dataset values,
- submit the prepared field,
- read and explain the public result.

It must not invent a missing numeric value, relation, invariant, or goal. If a value is unknown, keep it unknown/free according to the catalogue instead of estimating it.
