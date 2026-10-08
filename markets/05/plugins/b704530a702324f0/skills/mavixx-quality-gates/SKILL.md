---
name: mavixx-quality-gates
description: Verify a software project or material project phase with evidence-based functional, visual, accessibility, performance, security, and release checks. Use before handoff or deployment and after broad upgrades; scale checks down for small changes.
---

# Mavixx Quality Gates

Test the changed behavior and the risks introduced by the task. Read [references/quality-matrix.md](references/quality-matrix.md) and select applicable gates rather than running irrelevant tooling. When invoked during an authorized implementation, fix in-scope failures and rerun the affected gates instead of only listing defects.

## Verification order

1. Preserve the baseline: distinguish new failures from pre-existing failures.
2. Run repository-defined format, lint, type, unit, integration, and build checks.
3. Exercise critical user journeys and negative/error states.
4. For interfaces, start the app and inspect rendered desktop and mobile states, interactions, overflow, loading, empty, success, and error states. Compare against the pre-change baseline when available and capture evidence when tools allow it. Source inspection alone cannot pass the visual gate.
5. Check keyboard use, focus visibility, semantic structure, labels, contrast, and reduced-motion behavior where applicable.
6. Assess exposed secrets, authorization boundaries, input validation, unsafe data handling, and dependency risk proportionate to the change.
7. Evaluate performance where the change affects load, rendering, media, animation, queries, or bundles.
8. Fix issues within scope and repeat affected checks until they pass or a concrete blocker remains.

## Exit report

Report commands/checks run, results, visual states inspected, fixes made, remaining risks, skipped gates with reasons, and deployment or rollback notes. Never claim a gate passed without observable evidence. A project is not release-ready while a critical journey fails, the build is broken, a high-impact security issue remains, required user input is unresolved, or a claimed UI upgrade has not been rendered and inspected.
