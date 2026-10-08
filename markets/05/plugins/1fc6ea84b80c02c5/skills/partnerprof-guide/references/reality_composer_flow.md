# PartnerProf Reality Composer 1.0

The guided web UI no longer builds the production compute input from free text, a chatbot decision, or text hashing. The new Composer uses only explicit choices from the versioned catalogue in `config/reality_composer_catalog.json`.

## User flow

1. Problem family
2. Space / field geometry
3. Variables selected from the catalogue
4. Explicit constraints, relations, invariants, and declared goal(s)
5. Initial state of every variable (`free`, `fixed`, `observed`, `bounded`)
6. Numeric ranges and units
7. Full review and explicit approval
8. Deterministic NumPy-vector generation + reference equation display
9. Start / compute through `core.CML -> core_privat/CML -> core_privat/CML_A`
10. Result explanation (valid zero, or one or more admissible realized states; a terminal state is admissible only when it is the declared goal, otherwise continuation must remain)
11. Existing-result certification and optional SMTP delivery

Only the active input step is visible. Completed steps remain navigable from the right-side progress map. Any change after approval invalidates the old vector approval.

## Deterministic encoding

Schema: `PartnerProf-Reality/1.0`

Exact public transport is a bounded `float64` vector in the configured 64..16384 dimension range. The minimum dimension is derived from the explicit schema blocks present in the approved field; unused positions of the chosen bounded slice are explicit zero, not silent padding of source data.

- header: 16 slots
- variable blocks: 12 slots per selected state
- constraint blocks: 8 slots per explicit constraint
- relation blocks: 8 slots per explicit relation
- invariant blocks: 8 slots per explicit invariant
- goal blocks: 8 slots per explicitly confirmed declared goal
- layer blocks: 16 slots per local-reality layer
- remaining positions of the approved bounded slice: explicit schema zero

Units are converted to canonical units before vector assembly. Equivalent physical values such as `2.5 m` and `250 cm` therefore produce the same computational vector when all other semantics are the same. The original entered unit remains in the audit structure for provenance.

The Composer records:

- schema version
- normalized structured field
- source-field SHA3-512
- canonical semantic SHA3-512
- exact NumPy-vector SHA3-512
- variable/constraint/relation/invariant/goal count
- vector non-zero count and preview
- explicit statements that text projection and AI interpretation were not used

`/api/v2/composer/execute` composes the field again immediately before compute and compares its vector hash with the hash approved by the user. A changed field is rejected and must be reviewed again.

## Reference equation

The Composer displays one conventional reference equation for the selected problem family. It is documentation only. It does **not** control `core.CML` and does **not** control `CML_A`.

## Certification

Certification is performed only after a CML result exists. `certify_existing` does not replay the computation. The certificate now includes the Composer input-field audit and the displayed reference-equation metadata.

## E-mail

`/api/v2/send_report` sends the persisted run history and, for the certification bundle, the certificate JSON and SHA3 file through SMTP. SMTP is configured with `EVO_SMTP_*` variables. If no mail transport is configured, the endpoint returns an explicit error and does not claim that mail was queued or sent.

## Operator manifest

The Composer follows `docs/EVO_OPERATOR_MANIFEST.md`: `EvO_t(R_t,H_t,C,G) -> A_t`. Constraints and invariants belong to fixed field conditions `C`; declared `goals` represent `G` and are encoded separately. A goal does not mutate the rules.

## Canonical EvO → Worker contract (2026-08-23)

The composer now treats goal admissibility as an existential property of the current realized field:

`E_EvO(G|H_t)=1 iff exists Gamma: R_t ~> G`.

`exists Gamma` is **not** an instruction for EvO to materialize or optimize Gamma. It only means that a coherent continuation exists from the current realized reality to the declared goal.

The request may carry `question.mode` with one of:

- `ADMISSIBILITY`
- `REALIZATION`
- `CONFLICT_DIAGNOSTIC`
- `NEAREST_ADMISSIBLE_GOAL`
- `FULL_CYCLE`

and an optional `optimization.objective` (`none`, `time`, `energy`, `cost`, `risk`, `distance`, `custom`). The question/optimization request is semantically separate from the EvO field vector. A Worker request is deferred until EvO returns admissible.

Negative results are not collapsed into one meaning. `DIRECT_CONFLICT` means explicit local `C_k(G)=0`. `UNREACHABLE_FROM_CURRENT_REALITY` means the isolated goal is locally legal but no coherent continuation exists from the realized history/current reality. Diagnostics follow `FAIL(G)=(C_fail,V_fail,H_break)` and unexposed components remain null/empty rather than being inferred.
