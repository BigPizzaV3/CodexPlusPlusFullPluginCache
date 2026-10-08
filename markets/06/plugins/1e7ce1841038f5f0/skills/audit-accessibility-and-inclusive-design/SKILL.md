---
name: audit-accessibility-and-inclusive-design
description: Independently audit a website, web app, SaaS product, mobile or desktop app, commerce experience, dashboard, or relevant realtime/3D experience for accessibility and inclusive interaction. Use when accessibility conformance, assistive-technology behavior, keyboard and focus, contrast and color independence, text scaling, reduced motion, captions, cognitive clarity, custom controls, or alternative input needs dedicated review. Do not use as the implementation owner, for a broad premium-design audit, or to certify untested universal compliance.
---

# Accessibility and Inclusive Design Audit

Act as an independent audit/review specialist. Inspect real evidence, report findings and route remediation; do not redesign or implement the product inside this skill.

## Scope and evidence

1. Establish product type, audited routes/screens/states, supported platforms, target accessibility standard if approved, languages, input methods, evidence, environment and known user needs.
2. Separate automated findings, manual inspection and actual assistive-technology testing. A screenshot cannot prove semantics, keyboard behavior, focus order, announcements, captions, motion alternatives or control operability.
3. Mark inaccessible or untested required areas `NOT VERIFIABLE`. Never claim full WCAG, platform or legal compliance from partial evidence.
4. Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md), [decision authority](../../shared/expert-system/decision-authority-model.md) and [risk-adaptive assurance](../../shared/expert-system/risk-adaptive-assurance-model.md). Preserve approved product truth; a conflict between design and accessibility is an owner/specification issue, not permission to redesign silently.

## Audit dimensions

Check only applicable dimensions:

- semantic structure, landmarks, names, roles, values, relationships and reading/navigation order;
- screen-reader output and meaningful alternatives for images, audio, video, charts and dynamic content;
- keyboard, switch, voice, pointer, touch and other supported input paths; visible focus and focus recovery;
- contrast, color independence, forced/high-contrast states and information conveyed by more than color alone;
- text resizing, zoom, reflow, truncation, orientation and content preservation;
- motion, flashing, autoplay, parallax, vestibular load and an equivalent reduced-motion path;
- target size, timing, gesture alternatives, drag alternatives, custom controls and error prevention/recovery;
- labels, instructions, errors, cognitive clarity, consistent behavior and understandable status feedback;
- captions, transcripts, audio description or other media alternatives where required;
- responsive, localization and assistive-technology combinations in the supported matrix;
- realtime/3D alternatives, comfort, input alternatives and access to core content/actions without the advanced layer.

For every finding record stable ID, location/state, user impact, evidence, applicable requirement, severity, reproducible steps, missing proof and remediation owner. Do not prescribe an unapproved design solution when multiple material choices exist.

## Routing boundary

- Broad brand, premium UX, conversion and visual-direction review → `$audit-premium-digital-experience`.
- Interface labels, errors, settings or recovery wording → `$review-interface-language-and-naming`.
- UI implementation → `$implement-high-fidelity-digital-interfaces`.
- Realtime 3D implementation → `$engineer-realtime-3d-web-experiences`.
- Test infrastructure → `$engineer-test-and-regression-systems`.
- Final release gate → `$verify-production-implementation`.

## Output

Return audited scope and limitations, overall `PASS`, `PASS WITH RISKS`, `FAIL`, or `NOT VERIFIABLE`, findings by severity, evidence matrix, untested combinations, conflicts/owner decisions, routed remediation owners and exact re-audit conditions. Audit PASS is scoped evidence, not implementation authority or universal legal certification.

