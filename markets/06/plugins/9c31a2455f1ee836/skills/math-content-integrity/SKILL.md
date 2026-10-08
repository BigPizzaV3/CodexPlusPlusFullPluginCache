---
name: math-content-integrity
description: Find and fix KaTeX and LaTeX rendering errors in math content. Distinguish currency such as $5 from math such as $x+2$, repair broken delimiters and malformed formulas, and verify source data, builds, and learner pages so the error does not return after deployment. Use when math renders incorrectly or raw TeX appears.
---

# KaTeX Error Fixer

Use this skill when KaTeX or LaTeX renders incorrectly in math content. Give it the approved source plus the data, build, or learner page that shows the problem. It finds raw TeX, broken delimiters, malformed formulas, missing math, and dollar signs misread as math; fixes the owning layer; and verifies that rebuilding or deploying does not bring the error back.

Protect the complete path from an approved source to the learner screen. The recurring risk is not the math renderer alone: it is untyped notation in flat prose being reinterpreted by ingestion, generation, build, or browser stages. Treat visible agreement with the approved source as the outcome. A successful build or syntactically valid data file is supporting evidence only.

## Route the task

Respect the requested scope.

- For an audit, inspect and report without editing. Preserve unrelated worktree changes and use temporary or isolated outputs for safe reproduction.
- For an authorized correction, edit the owning source, parser, generator, renderer, or packaging layer; regenerate owned outputs; and verify the affected surfaces.
- For release verification, use the repository's real build and release gates and verify the deployed authenticated route when access is available.
- A skill run does not itself authorize deployment, dependency installation, destructive cleanup, or external publication.

Choose the smallest intervention that closes the demonstrated risk:

- Correct a confirmed learner-visible defect at the layer that owns it.
- When current content passes and the request is recurrence prevention, preserve it and strengthen regression, artifact, and browser gates.
- When a structured-data migration is in scope, preserve the approved source unchanged and generate a reproducible typed projection. Do not rewrite canonical strings merely to remove ambiguity from derived data.

Read [source-authority.md](references/source-authority.md) when identifying the original, comparing a PDF, or changing generated content. Read [math-content-contract.md](references/math-content-contract.md) for ingestion, delimiter, typed-block, or renderer work. Read [migration-architecture.md](references/migration-architecture.md) for a durable structured-ingestion design. Read [verification-procedure.md](references/verification-procedure.md) before declaring a correction, build, or release verified.

## Required workflow

1. Enumerate the program, level, route, item IDs, fields, canonical sources, generators, generated artifacts, renderers, build target, and learner surfaces in scope. Mark an inapplicable field `N/A` with a reason.
2. Establish source authority. Record the approved source path and, when practical, its page, item ID, version, and hash. Do not silently promote generated data or the current screen to the original.
3. Capture the current state before editing. Separate confirmed defects, candidates, false positives, and unverified surfaces.
4. At ingestion, retain the canonical source value and create a separate typed projection for prose, currency, inline math, display math, and structured visual blocks. Use source context and metadata; never decide whether `$` means currency or math from regex shape alone. Emit `unresolved` when evidence is insufficient.
5. Correct the owning layer and regenerate outputs through their declared owner. If an artifact has no reproducible owner, report that pipeline defect before treating an output edit as durable.
6. Render only typed math segments with the shared renderer. Keep currency and prose as text. Preserve structured-block content, order, count, display mode, association, and placement.
7. Validate canonical source, typed projection, generated data, production artifact, browser output, and deployed authenticated learner screen as separate layers. Make the relevant gate fail on malformed math, missing blocks, raw delimiters or TeX, generated drift, and packaging drift.
8. Report what changed, what passed, what failed, what was not run, and whether the verified path still depends on legacy classification. Never turn partial, historical, local, or unauthenticated evidence into current production proof.

## Invariants

- The latest approved PDF or explicitly designated authored source outranks derived files.
- Preserve canonical source bytes and provenance. Structured data is a reproducible projection, not replacement authority.
- Change generated files through their generator and check reproducibility.
- Balanced `$...$` is not proof of mathematical intent. Currency remains literal learner text and is never rescanned as math.
- Migrated screens use one typed contract and shared renderer; page-specific dollar heuristics are prohibited.
- Structured blocks preserve semantic content, order, count, display mode, association, and placement unless the approved source changes them.
- Validation uses throwing math parsing or an equivalent hard failure. Learner-facing error containment is not proof of valid math.
- Expected math-expression counts match rendered math-root counts on representative and defect fixtures.
- Renderer trust is disabled by default. Any exception uses a command and protocol allowlist shared by validation and learner rendering.
- Confirmed defects and false positives become regression fixtures with source references.
- Production packaging proves that math-bearing data and renderers were not omitted, replaced, or unexpectedly transformed.
- Build success, static preview, and an unauthenticated route do not prove the authenticated learner experience.

## Stop and report

Do not guess when the approved source is missing, versions conflict, notation is semantically ambiguous, a generator would overwrite the proposed change, or the authenticated surface cannot be reached. Preserve evidence, label the exact gap, and complete only the independent checks that remain valid.
