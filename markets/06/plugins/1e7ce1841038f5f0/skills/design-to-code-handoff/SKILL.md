---
name: design-to-code-handoff
description: Compile a frozen, approved visual design into an evidence-linked implementation handoff for Claude Code or another developer, including visual tokens, surface recipes, asset and copy mapping, build and acceptance specifications. Use when the design is already decided and must be translated without material design choices left to the builder. Not for inventing art direction, redesign, writing a whole product specification, coding the interface, or an audit-only request.
---

# Design-to-Code Handoff

Own only the translation between approved visual truth and its implementation layer. Produce documents and data, not implementation code, new art direction, assets or copy. Preserve the existing repository and documentation structure. A frozen design is an input claim to verify, not permission to fill its gaps.

## Authority and narrow routing

Read the shared [decision authority](../../shared/expert-system/decision-authority-model.md), [false precision](../../shared/expert-system/false-precision-policy.md) and [minimum sufficient context](../../shared/expert-system/context-package.md) contracts. They retain their canonical ownership; do not reproduce them as a new governance system.

- Whole-suite architecture belongs to `$architect-implementation-documentation`; contribute the visual implementation slice to its approved blueprint when present.
- General engineering requirements belong to `$write-engineering-specifications`. Reference their approved interfaces, behavior and architecture; do not re-author them.
- Audit-only requests belong to `$project-specification-auditor`; building belongs to `$implement-high-fidelity-digital-interfaces`. Ordinary session transfer belongs to `$handoff-work-between-chats`.
- Missing art direction goes back to the authorized design owner. Do not automatically invoke a redesign skill or execute a proposed solution.

This handoff has a deliberately stricter readiness boundary than a general visual specification: **if any material design decision remains with the builder, emit `BUILD READY = NO` and `DESIGN SPEC CONFLICT`.** This includes missing decisions as well as contradictory ones. Delegated Class-2 discretion is not sufficient to pass a still-material design choice here. Nonmaterial calibration may remain only with an approved target, bounds, evidence, reviewer and stop condition. Class-3 engineering mechanics remain permitted within the existing contract; do not freeze variable names or invent pixel values to eliminate harmless engineering judgment.

For any material representation choice—not only asset lineage—read the shared [representation economy contract](../../shared/expert-system/representation-strategy-contract.md). Carry the approved decision and its applicable truth, degrees of freedom, material signals, motion/state, fallback and proof into the existing eight sections by reference. Do not reopen frozen direction or silently simplify an approved medium. Missing material decisions or unapproved visible trade-offs retain the NO/conflict rule; unproven technical feasibility gets a bounded proof prerequisite, not invented production readiness. No new ninth document is required.

## Intake

Identify the exact requested screens, components, states, viewports, repository baseline, write destination, source access and design approval. Inspect only relevant current design frames, specifications, tokens, assets and copy. Record missing or inaccessible required evidence as a blocker, never as inspected. Screenshots do not prove hidden states, exact font metrics, layer semantics or responsive rules. Do not assume tool connections or infer authority from a newer timestamp.

Use [handoff fields](references/handoff-fields.md) when compiling the package. The eight phases below are required logical sections, not eight compulsory folders. A small component can use one document. For larger work, reuse approved document IDs and canonical assets instead of duplicating their truth. Before writing, state the output manifest; do not overwrite an approved package without authorization.

## Required sequence

1. **DESIGN FREEZE** — identify approved source revisions, scope, owner and approval evidence. Separate CURRENT from SUPERSEDED per scope using explicit precedence; preserve historical pointers but exclude superseded instructions from build inputs. An unapproved newer export does not replace an approved frame.
2. **DESIGN GAP AUDIT** — inspect every applicable observable and state using the field reference. For each gap/conflict record exact source, affected element/state, missing decision, impact, decision owner and blocked task. Ask only questions not answered in available authority. Do not advance a blocked dependent section as ready; safe transcription of decided portions may continue as DRAFT.
3. **VISUAL SYSTEM** — extract approved geometry, typography, color roles, grid, spacing, radii, responsive relations and interaction rules with source evidence and units. Distinguish measured values from approved requirements. Preserve explicit tolerances or controlled calibration; do not derive false precision from a compressed image.
4. **SURFACE RECIPES** — bind each visible surface to its approved material/layer recipe and state variants. Preserve composition, layer/occlusion order, clipping and anti-generic identity constraints. Unsupported rendering or art choices remain gaps, not suggested defaults.
5. **ASSET MAP** — verify exact assets and copy against approved sources and recipient access. Where production lineage is material, read and reference the shared [representation contract](../../shared/expert-system/representation-strategy-contract.md); distinguish source masters, delivery exports and runtime representation. Missing rights, files, exports, fonts or copy block dependent build work. Never substitute stock images, icons, generated copy or CSS approximations silently.
6. **BUILD SPEC** — map decided observables to existing components, approved paths/interfaces, data states and implementation order. Separate Create, Modify, Preserve and Prohibited. Unknown repository paths or architecture choices must be resolved by the existing engineering owner; do not create a parallel architecture. Record representation feasibility evidence where material; unproven fidelity gets a bounded proof task, not production readiness.
7. **ACCEPTANCE SPEC** — use the shared [perceptual gates](../../shared/expert-system/perceptual-quality-gates.md) and [risk-adaptive assurance](../../shared/expert-system/risk-adaptive-assurance-model.md). Define technical tests separately from real-output visual review against frozen authority. Trace each material observable to an acceptance oracle, environment, criterion, evidence and authorized evaluator. A passing build, screenshot diff or numeric test cannot certify perceptual quality. Do not claim runtime tests were executed during documentation work.
8. **CLAUDE TASK CONTRACT** — instantiate the existing [task contract](../../shared/expert-system/task-execution-contract.md) with the smallest accessible current source slice for the next authorized task. Do not copy all project history or use hidden chat memory. Include protected areas, forbidden substitutions/redesign, declared engineering discretion, exact next action, tests, stop conditions and rollback. No hooks, provider-specific setup, installation, tool activation or code execution is authorized by this documentation skill.

## Readiness and delivery

Perform a receiver simulation using only the delivered package: can the receiver locate every required source/asset, distinguish active truth, reconstruct all in-scope states and identify tests without inventing a material visual choice? Record actual questions or unresolved dependencies, not a ceremonial PASS. For material handoffs, use an independent read-only reviewer under the existing assurance rules; the author cannot ratify their own material gate. If required independent review is unavailable, readiness stays NO.

Deliver the eight sections, traceability and a compact gap/decision register. Conclude with scope, source revision, `BUILD READY = YES` or `BUILD READY = NO`, and blocker IDs. YES is scoped document readiness, not implemented quality, whole-project readiness or permission to deploy. It requires approved design freeze, no unresolved material choices/conflicts, accessible required assets/copy, consistent build mapping, sufficient acceptance criteria, receiver check and applicable independent approval. For material design gaps add `DESIGN SPEC CONFLICT`; for other blockers state their actual type, such as missing access or unverified technical prerequisite.

After relevant design, copy, asset, repository contract or approval changes, invalidate the affected derived slice and dependent readiness; recompile and recheck it. Preserve unaffected source truth and never silently overwrite the freeze.
