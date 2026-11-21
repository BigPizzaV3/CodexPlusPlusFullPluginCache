---
name: review-visual-ux
description: Audit an implemented app or compare a rendered web/mobile interface with reference screenshots or a design specification; produce evidence-linked fixes.
---

# Review Visual Ux

1. Read `../../references/design-quality.md`, `../../references/reference-usage.md` and `../../references/testing-and-evidence.md`.
2. Determine review target: user screenshot/Figma, existing app, or documented design spec. Capture actual render with available browser/simulator tools; if absent, perform a clearly labeled static code review only.
3. Inspect information architecture, visual hierarchy, spacing, type, color roles, content density, image treatment, component consistency, input states, responsive/adaptive behavior, accessibility and reduced motion.
4. Check at least: primary screen, one critical workflow state, small screen, large screen and one error/empty state where available. Record findings with severity, evidence, specific remedy and status.
5. Never report objective pixel fidelity without a source image and comparable render. Do not substitute a synthetic design-quality score for screenshot comparison.
6. If implementation changes are requested and authorized, apply bounded fixes, rerender and report before/after evidence. Preserve brand and existing structure unless redesign explicitly requested.
