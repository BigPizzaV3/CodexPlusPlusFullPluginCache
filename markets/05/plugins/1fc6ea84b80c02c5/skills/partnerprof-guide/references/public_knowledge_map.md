# PartnerProf knowledge map

Use `GET /api/v3/knowledge-map` for the machine-readable version. It is also
published to ChatGPT as `partnerprof_knowledge_map`, so an assistant can decide
whether PartnerProf fits before asking a user to prepare a task.

PartnerProf is a quantum-inspired paradigm for declared-state admissibility and
realization assessment. It can remove states ruled out by the supplied
constraints before a conventional exhaustive or downstream calculation. This is
not a claim of quantum advantage, global optimality, faster execution, or a
scientific, legal, medical, or causal conclusion.

## Non-prediction and deterministic realization

EvO does not predict a future realization. Before computation, the input is only
a declared field of possibilities, dependencies and constraints. Its hash proves
the identity of that declaration; it cannot identify, preselect or certify a
concrete future result.

Before a result, for a non-empty declared candidate field:

```text
|Omega_declared| >= 1
```

This says only that possibilities were declared. The admissible subset may still
be empty, non-empty or unresolved. After EvO publishes one selected realization:

```text
|Omega_realized,published| = 1
```

Only that published `REALIZED_STATE` is a concrete deterministic result event and
may enter the realized history of the next chronon. The equation does not claim
that only one admissible state exists in the whole field.

Therefore determinism is not a property of the input, future, target, input hash
or input certificate. It is a property bound to an already realized and published
state. A possibility, candidate, unresolved state or desired target must never be
written into history as if it had occurred.

A generic forward `goal_distance` is intentionally prohibited: it would suggest
that a concrete future realization is already selected and merely being
approached. PartnerProf instead reports categorical admissibility and explicit
goal checks evaluated on a published realization.

## What belongs in the state field

The state field describes only the reality needed to decide whether a coherent
realization can exist. It is not a classical measurement record. Do not add a
relative value merely because it helps describe the system or because it is
available from an external model.

The field contains state identities or symbols, actual directed or undirected
dependencies, admissibility constraints and invariants, published realized
history, and the explicitly requested target. A numeric value belongs in the
field only when the exact value itself defines a state, a real admissibility
boundary, an invariant, or the target.

Relative amplitudes, correlations, descriptive coupling strengths, means,
scores, ranks, confidence values and observer-relative summaries stay outside
the field by default. The same applies to length, energy, frequency, time,
distance or precision when they serve only as a classical measuring scale.
Declare what is connected to what, including a real direction, without
inventing how strongly it is connected.

Use this exception test: if removing or changing the exact value would change
the declared admissibility boundary, state identity, invariant or target, it
belongs in the field. Otherwise retain it only as post-result comparison or
interpretation metadata. An observable derived from a published
`REALIZED_STATE` is interpreted after realization, or declared independently in
a later chronon; it is never inserted retroactively into the prepared input.

PartnerProf therefore asks whether a realization exists in the declared
reality, not whether the requester has a sufficiently detailed measuring scale
with which to describe it.

## Termination and error

An ordinary realization has no preselected `max_steps`. The number of chronons
needed is not known before evolution. It terminates when the requested state is
realized, a direct declared conflict is established, no coherent continuation
exists from realized history, or another terminal state is explicitly defined
by the field.

A fixed step count is accepted only as an explicitly bounded technical test.
Exhausting that test produces `UNRESOLVED_WITHIN_DECLARED_SLICE`; it never proves
that realization is impossible. Infrastructure timeout, watchdog and resource
protection remain outside the state field. Their intervention is a technical
interruption, not a physical or admissibility event.

A validated error or mismatch can supply new information about states,
dependencies, constraints or the expected realization:

```text
error -> new constraint or information -> updated admissible field -> next evolution
```

If no error, conflict or unresolved difference changes admissibility in one
local direction, that direction has no new informational impulse. This is a
local stability statement, not a claim that the whole system stops evolving.
Software, network and infrastructure failures are not evolutionary evidence
unless independently validated and deliberately declared as field information.

## Random Circuit Sampling input

For `problem_family=random_circuit_sampling`, use the strict
`PartnerProf-RCS/1.0` object. It carries a stable `circuit_id`, `qubit_count`,
`circuit_depth`, an ordered `gate_sequence`, and an optional
`output_bitstring` whose role is explicitly `observed`, `target`, or
`realized_history`.

Each gate declares its layer, vocabulary name and exact qubit indices. Only
parameterized gates may carry parameters, because those parameters form part of
the gate identity. The live task manifest is authoritative for exact arity,
parameter count and parameter order. In particular, `PHASED_X(p,t)` requires
`[phase_exponent_p_half_turns, exponent_t_half_turns]`; it represents
`Z^-p X^t Z^p` with `global_shift=0`. `PHASED_XZ(x,z,a)` adds the final Z exponent. OpenQASM/Qiskit
rotation parameters and `FSIM(theta,phi)` use radians.

The canonical `*_POW` families preserve Cirq's exact phase convention and
therefore require both `[exponent_half_turns, global_shift]`. Omitting the
global shift or comparing only up to global phase is not an exact circuit
identity conversion. Common import names are normalized only through the
published alias table (`ID`, `P`, `CPHASE`, `CNOT`, `TOFFOLI`, `FREDKIN`);
unpublished aliases are rejected.

The canonical fixed-width vocabulary covers global phase, standard one-qubit
rotations, controlled and interaction gates, and fixed 3–5-qubit controlled
gates. Gates require exactly their declared number of qubit indices. Every declared
layer must be represented (use `I` for an identity operation), and a qubit may
participate in at most one gate in a layer. PartnerProf canonicalizes this structure, computes and
optionally verifies `circuit_sha3_512`, and constructs the contiguous
`numpy.float64` state field itself. The user or AI never supplies a manually
vectorized RCS field.

The initial state is `|0...0>` in the computational basis. Any other preparation
must be expressed by canonical gates at the beginning of the sequence. Qubit
argument order remains part of identity, including control/target order. Values
are not reduced modulo a period. A random seed or ensemble label cannot replace
the concrete gate realization. `circuit_sha3_512` binds the circuit; the
role-labelled output bitstring is separately bound by the complete input
certificate and cannot predict the published realized result.

`MEASURE` is represented by the separately role-labelled computational-basis
`output_bitstring`, not disguised as a unitary gate. `RESET`, `BARRIER`, `DELAY`,
pulse/calibration instructions, classical control, arbitrary matrices, channels,
variadic controls and opaque custom gates are not silently converted. They must
either receive a future dedicated contract or be explicitly decomposed into the
published canonical vocabulary before submission.

The RCS result concerns the admissibility of that exact declared circuit
identity and bitstring role. It is not a quantum-hardware sample, fidelity or
probability estimate, nor proof of quantum advantage.

Normative vocabulary references are the official
[Cirq gate semantics](https://quantumai.google/cirq/build/gates),
[Cirq `PhasedXPowGate`](https://quantumai.google/reference/python/cirq/PhasedXPowGate),
[OpenQASM standard library](https://openqasm.com/language/standard_library.html),
and [Qiskit circuit library](https://quantum.cloud.ibm.com/docs/en/api/qiskit/circuit_library).
They define source-operation semantics; the live PartnerProf task manifest
remains authoritative for the accepted RCS/1.0 subset and parameter ordering.

For a large public Cirq source, call `POST /api/v3/rcs-sources/prepare` with
exactly `source_url` and an independently obtained `expected_sha3_512`. The URL
is input evidence, not a PartnerProf API endpoint. The server accepts only a
direct HTTPS `.py` file on its published host allow-list, rejects redirects and
verifies the hash before parsing. It never imports or executes the source:
an AST allow-list reads only `QUBIT_ORDER`, literal `Circuit` moments and the
published Cirq gate forms. Any additional statement or unsupported operation
rejects the entire file. A successful response returns source/circuit hashes,
counts, automatic dimension, input certificate and `prepared_task_id`; execution
still requires a later explicit confirmation.

## Run visualization rule

Whenever execution returns a `run_id`, a client must immediately read that
run's `status` and `progress`, render the available public samples, and retrieve
`result` after a terminal event. It must not wait for a separate user request.
Only samples returned by the progress endpoint may be plotted.

For a field-terminal run, the required chronon count is unknown. Its graph uses
published chronon/event order and elapsed time. A null `progress_fraction` is
correct and must not be replaced by an estimated percentage. The terminal event
is labelled distinctly when published.

## Select the mode

| Need | Mode | Meaning |
| --- | --- | --- |
| Is this declared state possible under these conditions? | `ADMISSIBILITY` | The field is fixed; the operator assesses its declared admissibility. |
| Find one admissible state under stated conditions. | `REALIZATION` | A returned `REALIZED_STATE` is not automatically an optimum or target success. |
| Explain a direct contradiction in stated conditions. | `CONFLICT_DIAGNOSTIC` | Reports declared conflicts only. |
| Assess a target from the current reality. | `NEAREST_ADMISSIBLE_GOAL` | The target must be explicit; an outside reference never becomes one implicitly. |
| Run the selected public realization contract. | `FULL_CYCLE` | Read the returned termination and goal checks separately. |
| Continue a simulation. | Continuation lifecycle after realization | This is not an input mode. A valid realization becomes historical direction for its successor; it is not a repeated statistical trial. |

## Input and execution

The manual form and API use the same catalog terms. Fetch the task manifest,
then submit exactly three parts: `computational_reality`, `request`, and
`external_comparison`. Unknown fields are rejected.

1. `POST /api/v3/tasks/prepare` returns accepted counts, declared compute slice,
   external-reference boundary, hashes, and `prepared_task_id`.
2. The user reviews this result.
3. For a short direct integration, `POST /api/v3/tasks/run` accepts only the ID
   and `confirm_execution: true`.
4. For web, ChatGPT, MCP and long runs, prefer `POST /api/v3/tasks/start`. It
   returns a persistent, unguessable `run_id` immediately. Retain it and read:
   `GET /api/v3/runs/{run_id}/status`, `/progress`, and `/result`.

The prepared ID is non-listable and held for one hour in volatile memory.
Restarting the service expires a task that has not started. The asynchronous run
record and its sanitized public result are persistent and non-listable. Client
disconnection does not cancel server computation. CPU load and aggregate queue
depth must never be used as proof that a particular run completed.

Progress points contain chronon/step, elapsed time, categorical state and goal
status and unsatisfied explicit-check count. `progress_fraction` is null for an
ordinary field-terminal run because its required chronon count is unknown. A
fraction exists only for an explicitly bounded technical test and is never a
probability, confidence measure, scientific-validity score, goal distance, or
completion forecast. PartnerProf intentionally does not publish a generic
`goal_distance`: EvO goal admissibility is defined by coherent continuation from
realized history, not by an invented scalar distance.

No private CML source, internal matrices, raw vectors, or protected working trace
is returned by the lifecycle endpoints.

## External references and limits

IBM values and other external references belong in `external_comparison`. They
are post-result comparison metadata. They do not enter the compute vector or
stop a run unless the user explicitly declares an equivalent goal in `request`.

Always read `evo_contract.goal_reached`, `goal_checks`, and
`evolution.termination`. An ordinary realization has no inferred fixed step
count. Exhaustion of an explicitly bounded technical test or intervention by an
infrastructure watchdog does not prove that no better or admissible state
exists.

## Published visible samples

`GET /api/v3/knowledge-map` lists every current published preset and its
ordinary public demo-run endpoint. A sample response visibly reports its input
contract, state, declared goals, termination, result audit, and certification.
It intentionally does not expose protected CML working steps.

Current structured JSON, the manual Reality Matrix, strict DIMACS-CNF, and
bounded NPZ manifest/data-pair ingestion are supported. Large-input routes bind
the exact declared source to an input certificate before confirmed execution.
