# EvO_PartnerProf

EvO_PartnerProf is the scientific PartnerProf service in EvO Logic.

## Runtime

- Service: `EvO_PartnerProf`
- Default bind: `127.0.0.1:19130`
- Public compute entry: `core.CML`
- Sole evolutionary operator: `CML_A`
- Matrix role: reality field
- Canonical EvO semantic: **evolutionary operator of admissible states over current reality**

## EvO operator semantic

**EvO je evoluční operátor přípustných stavů nad aktuální realitou.** Rules, conditions and invariants define the possible field and remain fixed. PartnerProf keeps the current realized reality (`R_t`), realized history/context (`H_t`), fixed conditions (`C`) and declared goal (`G`) semantically separate. A realized step must either satisfy `G` or preserve at least one admissible continuation. A terminal state before the goal is not a target realization.

Canonical equations are maintained in `docs/EVO_OPERATOR_MANIFEST.md` and exposed by `/api/v2/task/catalog`. Structured inputs may carry explicit `goals`; line-oriented Reality Matrix uses `GOAL ... confirmed`.

## Compute contract

The public/API boundary may accept JSON, text, form data, supported files, or an explicit numeric vector. Existing PartnerProf transformation code must terminate that public representation and create the numeric vector before CML execution.

The compute route is single and mandatory:

`api/app.py -> src/evo_runtime/vector_transform.py -> core/CML.py -> core_privat/CML.py -> core_privat/CML_A.py`

Rules:

- `api` and `src/evo_runtime` never import or open `core_privat` directly.
- There is no public `core/CML_A.py`.
- The other public `core/*` shell modules may route to their private counterparts; they must not implement substitute computation.
- CML/CML_A are never replaced by local matrix/Q/teamwork/replay solvers.
- CML_A accepts numeric vector transport only; JSON/dict/text/binary objects are rejected at the CML numeric boundary.
- The matrix is the reality field. It is not optimized, approximated, jittered, or evolved by PartnerProf runtime logic.
- Evolution belongs to `CML_A`, not to the matrix, runtime, API, or certification layer.
- A returned exact zero is a valid deterministic state: no realization is possible in the given field under the declared conditions and constraints.
- A singularity/non-finite state is preserved as information and is not substituted.
- Determinism is bound only after CML returns a state. It is never selected before realization.
- Certification binds evidence to an existing returned CML state. It does not replay or recompute CML/CML_A.
- Computational errors are not replaced with mock/default results.

Structured composer/model runs (including prepared public task runs) enforce
`compute_slice.timeout_s` across the task's engine calls in a dedicated spawned
process. The same engine serves all chronons of that task. Expiry terminates
and reaps that process before request capacity is returned. If no chronon
completed, the API returns HTTP 504 with `status: unresolved` and no substitute
state or certificate. If earlier chronons completed, they are returned with
`TIME_LIMIT_REACHED`; unfinished computation is not certified. Input composition,
final certification and process cleanup add time outside this compute budget.
Run-history JSON becomes visible only after its complete atomic write.

## Start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
./start.sh
```

GUI: `http://127.0.0.1:19130/`

## Primary API

- `GET /health`
- `POST /api/v2/interpret`
- `POST /api/v2/execute`
- `POST /api/v2/certify` — certifies an existing `run_id` without compute replay
- `POST /api/v2/send_report`

Legacy `/api/v1/*` compatibility endpoints remain transport wrappers only and must use the same CML route.

## Architecture verification

```bash
python scripts/check_architecture_contract.py
```

This gate verifies the public/private boundary, single CML route, numeric-only CML boundary, valid zero state, singularity preservation, matrix invariance under operator evolution, and absence of substitute matrix/Q solvers in `evo_runtime`.

### Canonical EvO / Worker contract (2026-08-23)

PartnerProf uses `E_EvO(G|H_t)=1 iff exists Gamma: R_t ~> G`. EvO answers **is the goal admissible from the current realized reality?**; `exists Gamma` is not a path-search instruction. Only after a positive EvO gate may a separate Worker optimize `Gamma* = argmin J(Gamma)`. The input contract keeps current reality, local realities, relations, constraints, invariants, realized history, goal, question mode and deferred Worker objective separate. Negative results distinguish direct conflict from unreachable-from-current-reality when the authoritative audit supports it.

### Chess manifestation start contract (2026-08-23)

A new live chess manifestation has one and only one manual move. The user realizes White's first legal move; its signed board delta is the required non-zero initial direction vector `v0 != 0` for EvO. This seed is passed through the normal `EvORuntimeEngine -> core.CML -> CML_A` route with move publication disabled. Stockfish then reacts as Black. From that opponent response onward, EvO owns White and continues only from the realized history and current reality. The user cannot make further moves. Chess rules remain invariant and the goal remains opponent checkmate.

Sequence:

`manual seed (White) -> EvO direction initialization -> Stockfish reaction (Black) -> EvO realization (White) -> Stockfish reaction -> ...`

The initial seed is not a Worker-selected move and not an EvO publication. It is the external non-zero direction required to establish the first realized history.


## 2026-08-23 chess first-move UI hotfix

The live chess board now starts directly in the manual initial-vector phase. No preliminary button click is required. The first White move can be entered click-to-click or by drag-and-drop. `Nová partie / znovu` resets to the same interactive initial reality. Chess assets are served no-store and the JS URL is cache-busted to avoid a stale read-only client after deployment. If the seed API rejects the first delta, the UI rolls back to the initial board and allows a retry instead of permanently locking the manifestation.

### Chess manifestation uses the generic CML gateway

Live chess is an application-level manifestation, not a special CML implementation. The application composes a 16384-dimensional numeric current-reality field and calls only `core.CML.CML.run(vector)`. It never calls `CML_A` directly and never sends JSON/settings/target commands behind the CML boundary.

The first manual White move is the non-zero initial direction seed. A persistent generic CML instance receives that vector. Stockfish then realizes the opponent move. The application integrates the new board, history and delta into the next numeric field and invokes the same CML instance again. CML's returned vector is projected onto the current legal-move basis; no external chess score, prediction tree or Hessenberg controller is added.

## 2026-08-23 — Persistent CML continuation field

Live chess now treats the numeric result of `core.CML.CML.run(vector)` as the evolved
field. A Stockfish move is integrated into that retained result as a newly realized
external change, and the merged numeric field is submitted again to the same
persistent CML object. The application does not direct prediction, Hessenberg,
evolution or selection and never calls CML_A directly. The non-zero realized DELTA
is the continuation signal; no JSON or scalar command crosses the CML boundary.

## 2026-08-23 — Chess current-reality simulation loop repair

The live chess reference loop no longer represents legal moves as equal 0/1 coordinates. `python-chess` is used only as immutable rule authority to enumerate the immediate candidate local realities. Every candidate occupies a 64-value transition block in the same 16384-D numeric field. The public compute boundary remains exactly `core.CML.CML.run(vector)`; PartnerProf does not call CML_A and does not send JSON, prediction, Hessenberg, optimization or selection instructions behind CML.

The result is interpreted only against the candidate blocks of the exact field that produced it. `NO_REALIZATION` is reserved for a zero candidate response. A unique returned candidate is committed. `MULTIPLE_ADMISSIBLE_STATES` is now a continuation state: the returned candidate blocks are recombined with the unchanged current-reality header and condensed evolved history and the field is sent to the same persistent CML again. The browser automatically requests that next evolution instead of terminating the game.

When one candidate is manifested, the resulting board is immediately recomposed into a committed field before `WAIT_EXTERNAL`. The candidate region is cleared while waiting and a deterministic linear projection of the full CML result is retained in the evolved-history channel. The subsequent Stockfish move is integrated as the next realized delta, new candidate local realities are composed, and the loop repeats. The complete realized path stays separately auditable; determinism is attributed to the returned/committed state rather than imposed before the result.


## 2026-08-23 — Non-zero historical direction on every chess CML call

Live chess now keeps the newly realized field change and the CML historical
direction as separate vector quantities. `DELTA[160..223]` carries the latest
realized change (including the opponent move). `HISTORICAL_DIRECTION[865..928]`
carries the non-zero direction from the previously committed CML realization and
is inserted explicitly into every subsequent `core.CML.CML.run(vector)` input.
The first manual White move initializes it; each later EvO/CML committed move
replaces it with that realization's signed board direction. A zero historical
direction is rejected instead of being accepted as a valid calculation start.
