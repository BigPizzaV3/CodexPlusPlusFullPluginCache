---
name: tmc-ui-master
description: Audit, plan, implement, repair, refactor, and verify all frontend UI and UX work for The Moving Chain. Use for TMC visual quality, page redesigns, interaction simplification, responsive layouts, accessibility, design-system consistency, scoped frontend code hygiene, asynchronous and session recovery, frontend privacy and runtime checks, motion, loading or error states, rendered-browser testing, visual regressions, UI handoffs, and determining what UI work remains. Supports read-only audits and explicitly authorised implementation while protecting pricing, Quote, Instruction, Case, authentication, tenancy, and other business logic.
---

# TMC UI master

Improve the interface that exists, using current TMC authority and rendered evidence. Handle the whole UI loop without turning visual work into an unauthorised product or business-logic rewrite.

## Choose the operating mode

Infer the narrowest mode from the request.

- **Status:** Determine what is complete, partial, missing, stale, duplicated, or conflicting across current UI branches, PRs, Drive authority, and the rendered product. Do not edit.
- **Audit:** Inspect real routes, states, data, and widths. Return evidence-backed P0, P1, and P2 findings. Do not edit.
- **Plan:** Convert accepted findings into bounded implementation lanes with ownership, dependencies, acceptance criteria, and verification. Do not edit.
- **Implement:** Make the authorised UI changes on the verified isolated branch, then test them. Do not merge or deploy unless the user separately authorises that action.
- **Verify:** Review completed UI work against its authority, rendered result, responsive matrix, accessibility checks, tests, and protected invariants. Fix only when the request also authorises fixes.

If the request mixes modes, preserve their order: establish status, audit, plan, implement, verify.

## Read current authority first

Read [authority-and-invariants.md](references/authority-and-invariants.md) for every task. Resolve the current Drive authority, live repository state, target branch or PR, and relevant API contracts before judging or changing the UI.

Do not rely on a remembered SHA, old screenshot, superseded handoff, or copied summary when the live source can be checked. Stop before edits if the required base branch or commit does not match the authorised start condition.

Use connected Drive, repository, and browser tools to discover available authority and runtime access before asking the user to supply links, documents, branches, or screenshots. Ask only for evidence that the available tools cannot locate or access and that would materially change the result.

## Work from rendered evidence

Use the real application at exact routes, roles, states, viewport sizes, and usable container widths. Exercise the user journey. Source code explains a symptom but does not prove the final visual result.

Read [audit-and-implementation.md](references/audit-and-implementation.md) for status, audit, plan, or implementation work. Read [verification-matrix.md](references/verification-matrix.md) whenever the task touches responsive behavior, dense data, accessibility, motion, asynchronous behavior, session recovery, privacy-sensitive presentation, cross-browser behavior, representative-user acceptance, or completion claims.

For implementation, repair, refactor, or completion verification, also read [code-hygiene.md](references/code-hygiene.md). Apply its hygiene gate to the changed code and the shared code it directly depends on. Do not use UI work as permission for an unrelated repository-wide rewrite.

When available and relevant:

- use cino-product-design-review for the formal evidence-backed audit;
- use cino-critical-review for consequential product decisions, authority conflicts, or risky redesigns;
- use vercel:nextjs while implementing Next.js work;
- use vercel:geist for typography-system changes;
- use vercel:react-best-practices after editing multiple TSX components;
- use vercel:agent-browser-verify after starting a development server;
- use vercel:verification before claiming the full affected journey is complete.

Do not install a new UI library, replace the design system, or add a dependency merely because it makes one screen easier to build.

Scale verification to the risk and the changed behavior. Do not force every minor visual repair through every browser, failure sequence, or broker acceptance check. Do not omit those checks when the lane changes a consequential workflow, asynchronous state, authentication recovery, client-data handling, a shared system, or claimed browser or accessibility support.

## Preserve the boundary between UI and product truth

UI work may change presentation, layout, hierarchy, copy clarity, interaction feedback, responsiveness, accessibility, and motion within the authorised scope.

It must not silently change:

- pricing, eligibility, referral-fee calculations, totals, or data freshness;
- Quote persistence, recovery, versioning, stale-state behavior, or Provider selection semantics;
- Instruction idempotency, submission, frozen money, or exactly-one Case creation;
- authentication, invitation, permissions, tenancy, or admin authority;
- session semantics, client-data storage, analytics, telemetry, or privacy policy;
- backend truth, API contracts, lifecycle states, compliance claims, or production data.

If a visual improvement appears to require one of these changes, pause that decision and identify the required product or technical authority.

## Implement in bounded lanes

Prefer the smallest shared-system change that fixes a repeated root cause, followed by page-specific repairs. Keep unrelated working behavior untouched.

For each lane:

1. Name the affected routes, components, states, widths, and user task.
2. Capture the before state.
3. Record the governing authority and protected behavior.
4. Define observable acceptance criteria, the person responsible for verification, any required acceptance owner, and the applicable quality gates.
5. Implement only the authorised surface.
6. Test realistic data and interaction states.
7. Capture and inspect the after state.
8. Run the scoped code-hygiene gate and remove proven superseded code.
9. Run focused tests, then the relevant resilience, runtime, privacy, browser, accessibility, and wider gates.
10. Return the exact diff scope, hygiene evidence, deletions, gates actually completed, regressions checked, untested claims, remaining issues, and next safe lane.

Do not declare a page complete because it looks good in one screenshot.

## Make UI state reproducible

Prefer existing fixtures, seeded accounts, Storybook stories, test routes, or safe local mocks that reproduce consequential states. If the frontend lacks a reliable way to reach required UI states, propose a non-production UI state harness. Build it only when implementation is authorised and keep it out of production behavior.

The harness should represent product-valid states rather than invented mock behavior. It must not become a second implementation of pricing or other business logic.

## Decide completion honestly

Use one result:

- **PASS:** Required coverage is complete and no material P0 or P1 remains.
- **PASS WITH CORRECTIONS:** No P0 remains, but material P1 work remains.
- **FAIL:** A supported P0 blocks the required task or release standard.
- **INCOMPLETE EVIDENCE:** A required route, role, state, width, authority, or environment could not be inspected.

Separate observed defects from direct inferences and unverified risks. Never turn unavailable evidence into a confident pass.

## Handoff

Return:

- mode and result;
- authority, repository, branch, and commit inspected;
- routes, states, roles, widths, and browsers covered;
- the browser, device, accessibility, privacy, and user-acceptance targets used, including unresolved targets;
- changes made or findings produced;
- tests, rendered checks, failure sequences, runtime inspection, and representative-user checks completed;
- protected invariants rechecked;
- unresolved conflicts, blocked evidence, and remaining P0, P1, or grouped P2 work;
- the next smallest safe UI lane.

For implementation, include the branch and commit created. Do not merge, deploy, mark a protected PR ready, or mutate production unless the user explicitly asked for that action.
