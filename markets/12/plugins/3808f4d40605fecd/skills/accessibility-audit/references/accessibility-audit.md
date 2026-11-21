# Accessibility Audit

## Purpose

Audit an implemented website, app, page, workflow, or component for barriers that prevent people from perceiving, understanding, navigating, completing, or recovering from a task.

Accessibility Audit owns audit scope, sampling, evidence, user impact, classification, and verification limits. It receives intended semantics and behavior from [User Experience](user-experience.md), text treatment from [Typography and Readability](ui-design/typography-readability.md), color roles from [Color Discipline](ui-design/color-discipline.md), motion behavior from [Motion and Transition](ui-design/motion-transition.md), and transformations from [Responsive Adaptation](responsive-adaptation.md).

It verifies those decisions in the rendered result. It does not redesign them, mutate the target, certify compliance, establish legal applicability, or replace testing by people with disabilities. Unless another target is confirmed, use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) Levels A and AA as the practical reference, not as a conformance claim.

## Canonical Component Boundary

Treat [canonical components](canonical/components.md) as indivisible units. Test their rendered names, roles, states, content, keyboard and focus behavior, and supported alternatives without rebuilding anatomy or adding local overrides.

Report a confirmed canonical barrier to the affected [component](canonical/components.md) or [component-token](canonical/component-tokens.md) owner. Mark unsupported requirements as gaps; never approximate missing coverage.

## Core Rules

1. **Keep the audit read-only.** Do not change repository, generated, external, account, or user state.
2. **Bound every conclusion.** Define the target, journeys, sample, environments, conditions, exclusions, and limitations.
3. **Verify rendered behavior.** Code, screenshots, intent, component names, and automated results are leads, not proof.
4. **Test real use.** Cover important journeys, relevant states, failure, cancellation, and recovery.
5. **Combine methods.** Use automation for detection and manual testing for interaction, meaning, applicability, and impact.
6. **Classify honestly.** Separate confirmed issues, verified passes, human judgment, untested conditions, and out-of-scope items.
7. **Prioritize and route.** Rank findings by user impact and send design corrections to their owning skills.

## How to Apply

### Accessibility Audit Pass

1. Confirm the target, important journeys, representative sample, environment, modes, viewports, input methods, and available assistive technology. Use [WCAG-EM](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) when sampling a larger experience.
2. Choose methods proportional to the risk: automated checks, rendered DOM and accessibility-tree inspection, keyboard testing, zoom and reflow, state testing, and representative assistive technology.
3. Follow each journey through normal use, interruption, failure, cancellation, and recovery. Record evidence while testing and mark unavailable conditions untested.
4. Group repeated failures by root cause, then report only material findings, useful verified passes, untested risks, and canonical gaps.

### Perceive and Understand

- Verify landmarks, headings, reading order, labels, instructions, page language, relationships, and alternatives for meaningful images, icons, media, charts, and embedded content.
- Test text and images of text at `4.5:1`, large text at `3:1`, and required controls, focus indicators, boundaries, and meaningful graphics at the applicable `3:1`. Check every relevant mode and state; route corrections to [Color Discipline](ui-design/color-discipline.md).
- Verify `200%` text enlargement, reflow at `320 CSS px`, and user spacing overrides without clipping or loss: `1.5` line height, `2` paragraph spacing, `0.12` letter spacing, and `0.16` word spacing relative to font size. Route type roles, measure, and wrapping to [Typography and Readability](ui-design/typography-readability.md).
- Check captions, transcripts, descriptions, controls, autoplay, and non-color alternatives when the content requires them. Use [WAI Media Accessibility](https://www.w3.org/WAI/media/av/) for media requirements.

### Navigate and Interact

- Test keyboard access, logical and visible focus, focus entry and return, bypass paths, current location, dynamic focus, and freedom from traps or obscured focus.
- Verify names, roles, states, properties, visible-name matching, and programmatic relationships. Prefer native semantics; validate ARIA with [ARIA in HTML](https://www.w3.org/TR/html-aria/) and custom widgets with the [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/).
- Test pointer cancellation, gestures, dragging alternatives, orientation, and concurrent input methods when applicable. Apply the WCAG 2.2 AA `24 × 24 CSS px` target rule with its documented exceptions.

### Complete and Recover

- Run forms, authentication, search, checkout, settings, and other important tasks with real content. Check instructions, errors, retained input, status messages, time limits, interruptions, session expiry, and recovery.
- Verify that loading, progress, empty, success, warning, and error updates are communicated without unexpected focus movement.
- Test flashing, auto-advancing content, animation, and reduced-motion results; route intended alternatives and timing to [Motion and Transition](ui-design/motion-transition.md).
- Repeat critical journeys in the supported contexts that could change the outcome, including modes, narrow containers, zoom, text enlargement, orientation, localization, writing direction, dynamic content, and delayed loading. Route transformations to [Responsive Adaptation](responsive-adaptation.md).

### Evidence and Report

Classify each result as **confirmed issue**, **verified pass**, **human judgment required**, **not tested**, or **out of scope**. An automated warning is not confirmed until its applicability is verified; silence from a tool is not a pass.

For each confirmed issue, report the representative location, actual and expected behavior, affected users, task impact, evidence and method, applicable requirement, severity rationale, owning correction direction, confidence, and retest need. Recommend an exact canonical replacement only when active mappings prove it.

## Focused Audit

- Are the target, journeys, sample, conditions, exclusions, and limitations explicit?
- Were automated signals manually validated and rendered behavior tested with proportional methods?
- Are findings evidence-based, impact-prioritized, owner-routed, and free of unsupported legal, accessibility, or conformance claims?
- Did the audit leave repository, generated, external, account, and user state unchanged?
