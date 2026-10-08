# Finding and severity standard

Use this standard for every Cino Product Design Review.

## Severity

### P0 — critical

Use P0 only when the observed design or interaction:

- blocks a required user task;
- conceals or materially misrepresents important information, especially financial, health, legal, identity, or safety information;
- creates a credible risk that the user takes the wrong consequential action; or
- presents a serious accessibility barrier on a required journey.

Aesthetic weakness, trend mismatch, minor responsive awkwardness, or an unproven code concern is never P0.

### P1 — material

Use P1 when the issue makes an important task confusing, unreliable, error-prone, or meaningfully difficult at a required width or state, without meeting the P0 threshold.

Examples include unclear hierarchy around a primary decision, clipped controls with a workaround, inconsistent terminology that changes interpretation, weak focus treatment on an important flow, or a responsive layout that becomes laborious but remains usable.

### P2 — polish

Use P2 for visual refinement or local consistency that does not materially impede the task: minor spacing drift, small typographic inconsistencies, nonessential animation refinement, or decorative alignment.

## Finding schema

Give every finding a stable identifier such as `DESIGN-001` and include:

- **Title:** a concise statement of the problem, not the proposed solution.
- **Severity:** P0, P1, or P2.
- **Scope:** system-wide or page-specific.
- **Route/page:** exact URL, route, screen, modal, or step.
- **Viewport/container:** viewport dimensions and, when relevant, the usable application or component width.
- **State/data:** loading, error, empty, populated, focused, expanded, long content, role, permissions, or other reproduction state.
- **Component/area:** the precise control, panel, table, heading, or region.
- **Basis:** observed, directly inferred, or unverified.
- **Evidence:** screenshot reference, browser observation, DOM/accessibility evidence, or relevant code location. Describe what the evidence shows.
- **User impact:** the affected user, task, and consequence.
- **Likely cause:** only when supported; otherwise say unknown.
- **Recommended repair:** a bounded direction that preserves product rules and tells an implementer what must change.
- **Verification:** a reproducible check with expected outcome.

For P2 findings, related instances may be grouped, but they must still be locatable. P0 and P1 findings must use the complete schema.

## Evidence rules

- One finding should express one root problem.
- Consolidate repeated symptoms under a system finding and cite representative instances.
- Do not duplicate one issue at every width or route.
- Use a screenshot as evidence of appearance, not as proof of invisible behavior or business logic.
- Use source code as evidence of implementation, not as proof of final rendering.
- A directly inferred claim must name the observation it follows from.
- An unverified risk belongs under gaps or follow-up unless evidence supports a present defect.
- Never assign P0 when the required route, state, or user impact cannot be reproduced or otherwise established.

## Result rules

- **PASS:** required coverage completed; no material P0 or P1.
- **PASS WITH CORRECTIONS:** no P0; at least one material P1.
- **FAIL:** at least one supported P0.
- **INCOMPLETE EVIDENCE:** a required part of the journey could not be inspected, making a reliable result impossible.

An incomplete audit may still list verified findings. Do not convert missing access into a failure of the product.
