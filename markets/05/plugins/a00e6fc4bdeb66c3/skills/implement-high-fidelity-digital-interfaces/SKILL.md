---
name: implement-high-fidelity-digital-interfaces
description: Implement an approved website, web app, SaaS interface, dashboard, or mobile-facing digital experience to high visual and interaction fidelity with real preview checkpoints, responsive behavior, accessibility, performance, and perceptual QA. Use when the primary task is building or refining an interface, not merely auditing it. Do not use to invent brand direction, write the initial specification, build a realtime 3D scene as the main task, or conduct read-only review.
---

# Implement High-Fidelity Digital Interfaces

Own the real interface implementation and its perceptual quality while preserving approved product, brand, architecture, content, and behavior.

## Establish the contract

1. Inspect the repository, existing interface, design source, tokens, components, assets, content, supported viewports, and implementation specification.
2. Identify visual and behavioral invariants, targets, bounds, calibrated values, responsive rules, accessibility requirements, and protected areas.
3. Use the shared [false-precision policy](../../shared/expert-system/false-precision-policy.md) and [observable ownership model](../../shared/expert-system/observable-ownership.md). Do not freeze unsupported microvalues.
4. Route a lean team. Typical lead is `PRINCIPAL_FRONTEND_ENGINEER` or `DIGITAL_ART_DIRECTOR` according to task ownership; support may include UX, design systems, typography, motion, accessibility, and responsive expertise; review must include independent visual quality when material.
5. Issue the shared [task execution contract](../../shared/expert-system/task-execution-contract.md), select proportionate assurance under the [risk-adaptive assurance model](../../shared/expert-system/risk-adaptive-assurance-model.md), and classify decisions under the [decision-authority model](../../shared/expert-system/decision-authority-model.md).

## Prove the direction

When the approved experience depends on an unproven layout, medium, animation system, asset treatment, or rendering technique, use the [representation strategy contract](../../shared/expert-system/representation-strategy-contract.md) and build a focused proof before full production.

Keep browser-native content and interaction in the DOM when it provides superior semantics, accessibility, selection, linking, forms, responsiveness or dynamic information. Use canvas/WebGL layers only for observables that materially need them. When source assets differ from delivery assets, preserve the Source Master and document responsive image, optimized texture, video, vector or other publishing targets without forcing a heavy asset pipeline on an ordinary website.

## Implement in visual checkpoints

Use the applicable sequence from the shared [visual checkpoint policy](../../shared/expert-system/visual-checkpoint-policy.md): composition shell, tonal structure, hero, primary components or materials, secondary elements, full experience, motion, responsive behavior, and final polish.

At each expensive transition:

- run the real local preview;
- inspect target routes and states at representative viewports;
- capture comparable evidence;
- check composition, hierarchy, typography, spacing rhythm, color roles, depth, imagery, motion, interaction feedback, and brand relationships;
- stop for required owner or independent review before downstream work.

For a material visual gate, keep the approved target/calibration authority separate from the candidate. When abstract direction is insufficient, use a small project-specific PASS/FAIL calibration set under the shared perceptual gate instead of expanding generic design rules. The builder may self-review, but required fresh perceptual or owner ratification remains separate.

Classify an early visual proof as throwaway exploration or a production-candidate proof. An authorized real-output PASS may establish a scoped calibration checkpoint whose accepted typography, crop, surface, depth, composition, motion, parameters or assets cannot drift silently. Predetermined cinematic motion may be authored or baked; user-controlled motion must remain responsive to current user state.

Do not pause after every microchange. Pause where a wrong decision would multiply rework.

For premium, brand-led or differentiation-critical work, apply the shared genericity/authorship gate before the full-experience checkpoint advances and again before final handoff. Assess layout, hierarchy, navigation, component language, typography, imagery/product representation, motion, interaction, copy presentation and visual storytelling. If the experience could be reused almost unchanged for unrelated brands by swapping logo, copy and colors, record GENERICITY_RISK or GENERIC_DESIGN_FAILURE. A generic design failure blocks production PASS and routes to the evidenced experience-thesis, product-truth, composition, representation, typography, brand-relationship or content-structure owner—not superficial decoration.

Require each nontrivial visual effect to improve an approved perceptual, interaction, orientation, storytelling, brand, material or product-understanding outcome. For a complex interface, a bounded subtraction pass may be selected before final review when accumulated effects, layers, decoration, duplicated interaction or runtime machinery create a material clarity, performance or authorship risk. If selected, remove only elements that contribute no approved value. Do not impose minimalism or remove approved identity.

## Technical and perceptual verification

Verify functionality, loading and error states, keyboard and screen-reader behavior, reduced motion, responsive layout, localization stress where required, supported browsers, build, performance budgets, and regressions. Apply the shared [perceptual quality gates](../../shared/expert-system/perceptual-quality-gates.md) separately.

Technical pass plus perceptual fail is overall fail. Beautiful output with functional, accessibility, performance, or build failure is also overall fail. Correct compliance with a defective specification is not success.

## Boundaries and output

Do not redefine brand identity, product behavior, copy, architecture, or scope. Route unknown defects to `$diagnose-and-fix-software-defects`, deep 3D work to `$engineer-realtime-3d-web-experiences`, performance bottlenecks to `$optimize-runtime-performance`, and final release acceptance to `$verify-production-implementation`.

Return the working interface, changed-file manifest, checkpoints and evidence, Class-2 decisions, technical, perceptual and applicable genericity/authorship results, accessibility and responsive evidence, regressions, rollback, and unresolved owner decisions.
