# Verification Procedure

Verification is layered. Report each layer independently and use repository-native commands when they exist.

## V1 — Contract and fixtures

- Validate this skill's structure with the host's skill validator when available.
- Run the bundled fixture-schema check from the skill directory:

  ```bash
  python3 scripts/validate_fixture_schema.py
  ```

  This checks fixture structure and required scenario coverage only. It does not parse LaTeX, execute an ingestion adapter or renderer, compare build artifacts, or prove product integrity. If no executable product adapter or renderer gate is available, V1 remains `PARTIAL`.
- Exercise normal math, currency, ambiguous dollar signs, malformed delimiters, bare TeX, structured-block omission, mixed prose/math, generated drift, artifact drift, and browser-count mismatch fixtures.

## V2 — Canonical source

- Confirm item IDs and fields against the approved source.
- Record the exact source version or hash and retain the unmodified value used for ingestion.
- Parse every explicit math segment with hard failure enabled.
- Report unresolved items separately; do not include them in a pass count.

## V3 — Generated data

- Run the owning generator in check mode, or regenerate into a temporary directory and diff. During audit-only work, do not run a generator that may modify tracked outputs.
- Compare item IDs, provenance, segment order and values, segment counts, structured-block counts, parser versions, and relevant hashes.
- Run regeneration a second time when deterministic output is required.

## V4 — Build artifact

- Use the repository's production build only when authorized. Inspect an existing artifact during audit-only work and otherwise mark V4 unrun.
- Confirm the artifact contains the intended shared renderer, typed or compatibility data, and version.
- Re-run source and math checks against the artifact. Compare exact hashes for copied files and normalized semantic projections for intentional transforms.
- Fail the release when math-bearing data, renderers, block counts, or math runtime assets change unexpectedly during packaging.

## V5 — Browser

- Verify the primary desktop viewport first, then mobile.
- Check representative valid cases, every corrected defect class, and known false positives.
- Compare expected math count with rendered math roots and inspect visible placement and surrounding prose.
- Inspect learner-visible text outside rendered roots for raw delimiters, bare TeX commands, placeholders, and unresolved markers. Source-supported literal currency is not a defect.
- Record console, loading, and access failures separately from content defects.

## V6 — Authenticated live surface

- Verify the real learner route with normal authentication and protected-asset behavior.
- Confirm deployed release identity and relevant artifact hash when available.
- A public file fetch, local preview, or staff-only rendering is not a substitute.

## Failure injection

Before trusting a new gate, use temporary fixture copies to prove failure for ambiguous or unmatched `$`, malformed LaTeX, bare TeX in prose, a missing structured block, generated drift, artifact drift, and a rendered-count mismatch. Restore the fixtures and show the clean gate passing. Never inject failures into canonical, tracked learner, or deployed content.

## Report

State exact scope and build identity; confirmed defects, false positives, unresolved items, and unverified surfaces; commands run and results; source, generated, artifact, browser, and live status separately; and whether deployment occurred. Use `PASS` only for the measured layer. Use `PARTIAL`, `UNVERIFIED`, or `BLOCKED` for observed gaps.
