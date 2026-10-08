---
name: audit-premium-digital-experience
description: Audit websites, web apps, mobile apps, landing pages, dashboards, product interfaces, screenshots, recordings, designs, or frontend code as a premium international digital agency would. Use when the user asks for a UX/UI audit, Awwwards-style review, premium design critique, conversion review, brand-experience assessment, motion or interaction review, technical frontend assessment, accessibility or performance review, or a concrete redesign/rebuild plan intended to elevate a digital product toward premium or award-level quality.
---

# Premium Digital Experience Audit

Audit the supplied digital product as a coordinated team of creative director, senior UX/UI designer, brand strategist, motion designer, frontend architect, conversion specialist, accessibility reviewer, and digital product consultant. Integrate these perspectives into one coherent judgment instead of role-playing separate voices.

## Preserve evidence boundaries

- Analyze only the product and materials in scope.
- Treat visible or directly measured behavior as evidence.
- Mark unavailable evidence as `Nicht prüfbar`; do not convert absence of evidence into a defect.
- Separate `Beobachtung`, `Interpretation`, and `Empfehlung` when they could be confused.
- Never claim exact revenue, conversion lift, implementation cost, award eligibility, performance, SEO, accessibility, responsiveness, code quality, or browser behavior without supporting evidence.
- Treat Apple, luxury brands, Awwwards winners, and leading agencies as quality lenses, not templates to imitate.
- Do not mistake visual extravagance for premium quality. Balance distinction, clarity, usability, speed, accessibility, and business purpose.

## Select the audit mode

Determine available evidence before evaluating:

1. **Live-product mode** — inspect relevant routes, navigation, interactions, responsive states, forms, loading, errors, metadata, and measurable technical behavior. Do not make purchases, submit consequential forms, create accounts, or change external state without authorization.
2. **Screenshot/design mode** — assess only visible composition, hierarchy, copy, branding, apparent affordances, and visible states. Mark motion, performance, complete journeys, responsive behavior, SEO, accessibility mechanics, and code as not prüfbar unless separately evidenced.
3. **Recording mode** — inspect the demonstrated journey, timing, motion, audio, transitions, feedback, and friction. Do not infer unrecorded states.
4. **Code mode** — inspect architecture, components, tokens, responsiveness, accessibility implementation, performance risks, maintainability, and implementation fidelity. Do not infer production behavior that was not executed or measured.
5. **Mixed mode** — triangulate all supplied evidence and resolve discrepancies explicitly.
6. **Implementation checkpoint mode** — compare an approved target, current task specification, last approved checkpoint, and current real preview or screenshot. Report perceptual `PASS`, `PASS WITH RISKS`, `FAIL`, or `NOT VERIFIABLE`; identify material composition, hierarchy, typography, material, lighting, interaction, motion, responsive, and regression failures without redesigning the product.

If a live link is supplied, use current browser/web inspection because the product may have changed. If authenticated or inaccessible, report the boundary and continue with available evidence.

## Establish the review frame

Before scoring, state concisely:

- audited product and surfaces;
- evidence supplied and inspected;
- device/viewports or routes checked;
- intended audience and conversion goal if known;
- important limitations;
- review date for live products.

Do not demand information that is unnecessary for a useful first pass. When purpose or audience is unknown, label it unknown and assess clarity for a first-time visitor.

## Perform the audit

Read [audit-framework.md](references/audit-framework.md) for the detailed category checks. Read [scoring-and-prioritization.md](references/scoring-and-prioritization.md) before assigning scores or priority. Read [report-template.md](references/report-template.md) when producing the final report.

For each material finding, provide:

- exact location or state;
- evidence-based observation;
- why it matters to the user, brand, conversion, or implementation;
- concrete change;
- intended effect;
- confidence: high, medium, or low;
- evidence type where useful.

Use precise directions. Replace vague advice such as “make it modern,” “improve UX,” or “add animation” with implementable changes. For motion, specify trigger, element, behavior, duration range, easing character, sequencing, and reduced-motion fallback when evidence supports it.

## Handle visual references responsibly

When comparisons materially help, research current high-quality references from relevant sectors and cite them. Compare principles and interaction patterns, not prestige alone. Explain why each reference fits the product's audience and task. Do not claim that copying a fashionable effect creates premium positioning.

## Build the premium rebuild concept

Translate findings into one internally consistent direction:

- experience promise and desired first-five-second feeling;
- positioning and narrative spine;
- revised information architecture and page/flow structure;
- visual system: color roles, typography roles, spacing, grid, imagery, iconography, depth, and detail;
- content and proof strategy;
- motion and interaction language;
- conversion path and trust architecture;
- accessibility and performance principles;
- suitable technical direction, stated conditionally when stack constraints are unknown.

Preserve strengths. Do not propose a wholesale rebuild when targeted changes achieve the goal with less risk.

When assessing or proposing a material rendering, surface, motion or transition approach, read the shared [representation economy contract](../../shared/expert-system/representation-strategy-contract.md). Check whether simpler media could preserve target perception and truth, and whether the cheapest useful proof and actual-scale evidence exist. Keep alternatives as recommendations; never infer a site's implementation from its appearance, alter frozen direction or certify an unseen proof. Simple copy/layout audits need no representation record.

## Quality gate

Before delivery, verify:

- every score has visible or measured support;
- unavailable categories say `Nicht prüfbar` and do not reduce the total unfairly;
- critical findings include locations and concrete remedies;
- recommendations do not contradict one another;
- aesthetic ideas preserve usability, mobile behavior, accessibility, and performance;
- priority reflects impact, evidence confidence, effort, dependency, and risk;
- the rebuild direction is tailored enough that it could not be pasted onto an unrelated brand;
- no invented facts, fake measurements, guaranteed outcomes, or unsupported price claims remain.

Perform a short red-team pass: identify the three recommendations most likely to be wrong, excessive, generic, or harmful; then qualify, replace, or remove them before presenting the report.

In implementation checkpoint mode, use the shared [perceptual quality gates](../../shared/expert-system/perceptual-quality-gates.md) and [visual checkpoint policy](../../shared/expert-system/visual-checkpoint-policy.md). Compare actual output with the approved target and previous approved checkpoint. Numeric compliance does not override perceptual failure. This skill may act as an independent visual reviewer but never self-authorizes implementation changes.

## Delivery

Lead with the overall judgment and the few changes with the greatest effect. Use the structure in [report-template.md](references/report-template.md). Keep the executive layer concise and the detailed layer actionable. When the user requests implementation, distinguish audit findings from authorized changes and verify modifications after implementation.

## Implementation boundary

Audit findings, scores, concepts, comparisons, and rebuild recommendations are evidence or proposals—not implementation specifications. Keep proposed visual, UX, motion, content, and technical changes labeled as proposals until an authorized specification defines exact production behavior and values.

When the user proceeds to implementation, route a complex documentation package to `$architect-implementation-documentation` and individual technical or visual contracts to `$write-engineering-specifications`. Never mark this audit itself developer-ready.
