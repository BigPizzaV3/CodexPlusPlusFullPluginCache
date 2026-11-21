---
name: build-web-app
description: Implement complete browser-based apps, dashboards, editors and SaaS products with real state, navigation, API boundaries and design-quality verification.
---

# Build Web App

1. Read `../../references/web-and-pwa.md`, `../../references/design-quality.md`, `../../references/testing-and-evidence.md` and project conventions.
2. Preserve existing framework if extending; for new apps select React/Vite, Next.js or another framework based on routing, rendering, hosting and data needs. Confirm current package versions and APIs from source docs when possible.
3. Start with a runnable vertical slice: one real workflow, state persistence strategy, accessible controls and error/retry handling. Separate UI primitives, features, API/data modules and routing. Avoid a single huge component.
4. Use actual user-approved integrations or local fixtures clearly marked as demos. No fictitious authentication, backend, data metrics or paid subscriptions.
5. Render desktop and mobile layouts, interact with the main workflow and check loading, offline, empty, error, focus and reduced motion. Read `../review-visual-ux/SKILL.md`.
6. Run typecheck/lint/unit/integration/browser tests when supported, record commands and failures, and fix critical defects before handoff.
