---
name: plan-product
description: Plan product architecture, platform and implementation milestones for a website, SaaS app, PWA, iOS/macOS, Android or cross-platform app before coding when planning is requested.
---

# Plan Product

Use for roadmap/spec/architecture requests, not as a substitute for a direct implementation request.

1. Identify target users, high-value task, requested platform(s), devices, offline needs, auth/data, integrations, performance and regulatory concerns. Resolve unknowns with reasonable assumptions except essential decisions.
2. Apply `../../references/platform-choice.md` and respect the existing stack, costs and skill constraints. Avoid defaulting every app to Next.js or every mobile app to React Native.
3. Model user journeys, screen/state inventory, data entities, API boundaries, security/trust boundaries and accessibility. Identify integrations that need credentials/permissions.
4. Define a minimal vertical slice and milestones with acceptance tests, risk register and decision points. Use `../../templates/product-brief.md`.
5. Decide whether to use real specialists according to `../../references/orchestration.md`. Separate independently executable tasks and gate production modifications.

Deliver: concise product brief, architecture diagram/table, stack rationale, screens, milestones, test strategy and unresolved blockers.
