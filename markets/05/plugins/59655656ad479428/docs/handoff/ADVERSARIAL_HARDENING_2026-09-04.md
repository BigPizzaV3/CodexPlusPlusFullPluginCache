# Adversarial hardening implementation checklist

Status: complete for the defined offline scope. Authority: user request on 2026-09-04 to implement the
adversarial findings and continue until confidence and feedback exceed 4/5.
Scope: seven findings in `readiness/reviews/2026-09-04-adversarial/REVIEW.md`,
plus the user-authorized continuation packet E below.
Architecture: `PYTHON_MARKETPLACE_PLUGIN_V1`.

## Acceptance and scoring, fixed before implementation

Completion requires every finding closed, all original eleven acceptance probes
passing without weakening their assertions, new adjacent-case regression tests,
and a green complete offline gauntlet. A numerical score cannot override an
unresolved P1/P2 finding in this scope.

- Feedback score: `5 * passing original probes / 11`. Baseline: 3/11 = 1.36/5.
  This is deterministic test feedback, not user feedback or an external review.
- Confidence score: an engineering evidence rubric, not a statistical probability.
  One point each for original regression closure, adjacent-boundary coverage,
  full regression/static validation, and reproducible package validation.
  The fifth point is split equally between verified local CLI/fixture integration
  and live-provider/native cross-platform execution. Only the first half of that
  final point is in this offline scope, so the maximum supported score is 4.5/5.
- Target: feedback 5/5 and confidence 4.5/5, both strictly above 4/5.

## Packet A — outbound confidentiality and paid output (web runner + tests)

- [x] H1 / P1: inspect the actual upload bytes before credentials or transport;
  refuse formats whose content cannot be validated safely with the bundled runtime.
- [x] Add clean-upload, secret-bearing upload, encoded/split secret, size-limit,
  malformed input, and unsupported opaque-format tests.
- [x] H3 / P2: preflight output destinations and screenshot requirements before
  paid Unlocker/result/browser work, with atomic no-clobber writes at delivery.
- [x] Check browser action arguments before opening the paid browser connection.
- [x] Run focused web regressions and the original web probes.

## Packet B — durable response capture (review runtime + router tests)

- [x] H2 / P1: capture successful provider content before health/reference writes.
- [x] Preserve reconciliation and recovery metadata on later failures.
- [x] Test health-write and budget-reference failures with a successful response;
  assert recoverability and exactly one transport call.
- [x] Run the router/recovery regression suite. Also repaired and tested the
  identical pre-capture reference-write ordering in the Handoff path.

## Packet C — benchmark identity, modality and cost (shared runtime + benchmark tests)

- [x] H4 / P2: share an exact-ID collision-rejecting join for AA and OpenRouter.
- [x] H7 / P2: preserve `:free` and exact case; require explicit matching IDs.
- [x] H5 / P2: missing provider modalities remain unverified and ineligible.
- [x] Update synthetic fixtures to contain explicit positive capability evidence.
- [x] H6 / P2: use one cost unit for scoring; preserve missing values and metric provenance.
- [x] Test duplicates, variant/case mismatches, missing/malformed modalities,
  mixed units, equal costs, negative/nonfinite costs and the valid paths.
- [x] Run focused benchmark and affected routing regressions.
- [x] Invalidate prior normalized catalogs with schema 1.9.0 so pre-hardening
  identity/capability assumptions cannot survive through the old cache.

## Packet D — integration, evidence and feedback

- [x] Re-run the unchanged eleven adversarial acceptance probes: require 11/11.
- [x] Run all standard offline suites, 311-case endpoint fuzzing, Ruff, mypy,
  architecture validation, onboarding lint and whitespace checks.
- [x] Validate two deterministic temporary builds and audit a fresh temporary
  archive containing these fixes. Keep the previous release ZIP as historical.
- [x] Record exact results, remaining limits and scores here and in a completion record.
- [x] Document unreleased behavior changes, including any narrowed upload support.
- [x] Final self-review: inspect the delta for adjacent failure modes and verify
  no source changes or release/package claims are omitted.

## Final evidence and scores

- Feedback: **5.0/5**, calculated from 11/11 unchanged original probes (baseline
  was 3/11). No original assertion was removed or relaxed.
- Engineering confidence: **4.5/5** under the rubric above. This is a local
  evidence score, not external adjudication or a probability of being bug-free.
- Regression: **305 tests across 12 suites**, up from 281 (298 at the original
  seven-finding closure, three packet E tests, four release metadata/tier tests);
  all pass. The separate release process is `RELEASE_1_7_1.md`.
- Endpoint fuzz: **311/311**. Source and fresh-archive security: **8/8 each**.
- Deterministic release tests: **2/2**. Ruff, eight-module mypy, architecture,
  onboarding lint, whitespace and fixture-based rank/render CLI checks pass.
- No unresolved finding from the seven-item review or continuation packet E
  remains in this scope.
- Machine-readable evidence, production package hashes, the exact probe results
  and the reproducible gauntlet are under
  `readiness/reviews/2026-09-04-adversarial/`.
- The historical 1.7.0 ZIP remains unchanged. The repaired source is unreleased;
  temporary archives were built and audited, then removed by their test lifecycle.

Reproduce: `PYTHONDONTWRITEBYTECODE=1 python3 readiness/reviews/2026-09-04-adversarial/gauntlet.py --write-results`.

## Continuation packet E — recovery availability and bounded reads

User authority: "continue then test". Scope stays offline and unreleased.
Reuse scan: harden the existing recovery descriptor opener, streamed hash reader,
and append-only repair log; do not add another storage layer or provider route.

- [x] Reproduce named-pipe blocking in receipt/content reads, repair hashing and
  event-log append using disposable files and bounded subprocesses.
- [x] Open potential special files without blocking, then validate the descriptor
  as regular before reading/writing; preserve existing ownership and symlink checks.
- [x] Reproduce content growing beyond the safety ceiling after initial metadata
  validation, and enforce the byte ceiling throughout ordinary recovery reads.
- [x] Test exact-limit, Unicode and ordinary repair/read success paths.
- [x] Rerun the full offline gauntlet and refresh source-bound evidence; retain
  the original scoring rubric and all eleven independent probes unchanged.

Observed before repair: all four named-pipe operations exceeded the three-second
subprocess deadline; the growing-content reader exceeded the byte ceiling.
The exact-limit positive test already passed. After repair: all three new tests
(including the four special-file subcases), ordinary repair, and symlink
rejection pass. These are two additional availability/resource-bound findings;
the seven original assertions and the scoring rubric remain unchanged.

Final continuation validation: 301 regression tests, 11 original probes, 311
endpoint fuzz cases, source/archive security 8/8 each, deterministic builds 2/2,
static/architecture/onboarding checks and rank/render fixture CLI checks pass.
The review skill contract now matches endpoint schema 1.9.0 and documents these
recovery safeguards; its skill validator also passes. Confidence stays 4.5/5 and
automated feedback stays 5/5 rather than inflating scores for additional tests.

The Empire Readiness loop separately reports 10.0/10 and
`codex_app_store_approved` from existing historical attestations, with no
unchecked publishing items and a recommendation to track directory availability
and release evidence. That record is not new approval or live validation of this
unreleased source. The next remaining validation boundary is release-specific
live-provider and native cross-platform execution; no such result is inferred.

## Reuse scan and packet boundaries

Existing implementation selected after inspection:

- `empire_secret_policy.secret_findings` is the shared classifier; reuse it for
  upload content instead of adding another secret engine. The stdlib HTML parser
  can expose entity-decoded and tag-split text. Opaque PDF/Office/RTF files cannot
  be completely inspected by the current dependency-free runtime; fail closed
  with a local conversion instruction until format-aware validation is supported.
- The web runner already owns multipart, transport, output and browser actions;
  keep bounded preflight and atomic delivery helpers in that module.
- The review runtime already owns `capture_provider_response` and the durable
  receipt; move its placement rather than adding a second recovery store.
- `aa_index` is the existing AA join and collision policy; generalize its small
  index helper for both catalogs instead of maintaining a second join engine.
- Benchmark normalization, metric projection and `_scale` are existing scoring
  seams; retain measured per-task cost as the single scoring unit.
- Existing tests and the independent eleven-probe script are reusable evidence.
  Each implementation packet stays below eight source files. No new service,
  dependency, external model reviewer, or architecture authority is required.

## Boundaries and follow-up

No paid completions, live provider refresh, external publication, commit, tag or
push are part of this plan. Scores apply to this hardening scope. The older
marketplace readiness 10/10 and July publisher attestations remain separate.
The active comparative-evaluation documents conflict with the historical passing
record; preserve both until release-specific evidence is reconciled. Broader
invocation-time preflight and streaming remain separate roadmap work.
