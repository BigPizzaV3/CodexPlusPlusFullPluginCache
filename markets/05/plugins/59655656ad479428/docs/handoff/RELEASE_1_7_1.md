# Empire LLM for Codex 1.7.1 release process

Status: locally tested submission candidate; not yet declared shippable or submitted.
Authority: user request to finish relevant tasks, test, package a deployment ZIP,
and open the completed release process in Canvas. This does not authorize a
publication, paid provider dispatch, release attestation, or unrelated roadmap work.

## Release packets — package integrity and fresh-install behavior

F1 is metadata plus builder/install tests; F2 is benchmark tier handling plus
live diagnostics; F3 is final evidence-bound export. These are separate bounded
packets, each below eight implementation files.

Reuse the existing explicit-allowlist deterministic builder, its install smoke
checks, the standard regression suites, and the original hardening gauntlet.
Reuse the bundled Plugin Creator validator; do not add a new plugin format,
service, dependency, or marketplace installation.

- [x] Correct benchmark skill icon metadata rejected by the bundled validator.
- [x] Keep at most three manifest starter prompts, consistent with the bundled
  manifest specification, and advance the patch version to 1.7.1.
- [x] Keep the manifest display and short descriptions within the stricter
  30-character final-directory limits documented by OpenAI.
- [x] Test skill asset references against real packaged files.
- [x] Exercise review/recovery, handoff preview and benchmark rank/render using
  the extracted ZIP, synthetic fixtures, isolated local state, and no network.
- [x] Re-run regression, adversarial, fuzz, static, manifest and archive checks.
- [x] Build matching independent archives, retain checksum and inventory, and
  verify the final ZIP against the tested source hashes.
- [x] Record release-specific readiness without reusing old approval as proof.
- [x] Explain Free-tier identity limitations and test unverified research charts
  plus fail-closed route qualification. Do not invent mappings or buy access.
- [x] Require CI to fail when the existing readiness gate fails.

Local result: 305 regression tests, 11 original adversarial probes, 311 endpoint
fuzz cases, source/archive security 8/8 each, deterministic build tests 2/2,
Ruff, mypy, architecture/onboarding checks and plugin/skill validation pass.
These results do not establish the external gates below.

Export using `scripts/export_release_candidate.py --validator PATH`, where PATH
is the bundled Plugin Creator `scripts/validate_plugin.py`. It refuses stale
gauntlet/live evidence, independently rebuilds and audits the archive, validates
the extracted plugin, refuses overwriting an existing release, and writes the
ZIP, SHA-256, inventory and verification receipt. Its candidate-only export is
deliberately not a mechanism for asserting that external release gates passed.

## External evidence boundaries

The July publisher approval and comparative record are historical evidence.
Current architecture/handoff documents still require comparative evaluation;
release-specific comparative and web live validation remain pending. Resolve these explicitly,
not by increasing a score or changing the human attestation file.

Native Linux/Windows execution and fresh-conversation skill activation have not
been established for this revision. The locally available platform is macOS.
Paid web/model operations require separate specific authority where applicable.

The read-only catalog check retrieved 643 Artificial Analysis records across
four pages and 428 OpenRouter models. The account's `free` tier provides zero
`openrouter_api_id` fields. Research ranking and rendering pass with zero
qualified routes; strict qualification is blocked with an explicit diagnostic.
The provider documents those identity fields as Pro-only:
[Artificial Analysis API contract](https://artificialanalysis.ai/data-api/docs).
Redacted source-bound evidence: `readiness/release-1.7.1-live-catalog.json`.

Remaining release actions:

- [ ] Supply Pro/Commercial identity evidence and validate exact live joins, or
  explicitly approve a reduced release scope retaining the documented limitation.
- [ ] Authorize bounded paid web-provider smoke tests and record their results.
- [ ] Validate native Linux/Windows execution and fresh-conversation activation.
- [ ] Reconcile release-specific comparative/acceptance evidence with the active
  handoff; do not replace historical human attestations with agent assumptions.
- [ ] Confirm current publisher submission fields and approve the final release.

The requested Canvas completion view is conditional on a shippable result.
Do not open it as a completion signal while required release gates are pending.

## Submission guidance verified 2026-09-04

The official documentation describes a root `.codex-plugin/plugin.json`, local
installation and complete-workflow testing, and submission as a skills-only
plugin. Prepare five positive and three negative reviewer cases, verified
publisher identity, public policy URLs, and release notes. Uploading an artifact
does not imply review approval or publication.

- [Package format](https://developers.openai.com/plugins/build/plugins)
- [Complete-plugin testing](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Submission process](https://developers.openai.com/plugins/deploy/submission)
