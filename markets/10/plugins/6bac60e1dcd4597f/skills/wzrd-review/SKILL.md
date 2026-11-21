---
name: wzrd-review
description: Review, create, or refine WZRD rooms, product flows, visual design, and interface copy using the WZRD brand system and product-trust principles. Use for WZRD brand checks, UX writing, room critiques, launch-readiness audits, guest-sharing flows, AI behavior, and implementation decisions. Do not use for unrelated products or generic wizard-themed work.
---

# WZRD Review

Help make WZRD feel like one calm, attentive intelligence across every surface. Ground conclusions in the artifact the user supplied or the behavior you can inspect; treat the references as decision criteria, not as evidence that a current defect still exists.

## Route the work

- Read [references/brand-system.md](references/brand-system.md) for visual design, interaction, naming, or copy work.
- Read [references/product-trust.md](references/product-trust.md) for room reviews, guest journeys, sharing, permissions, AI behavior, launch readiness, mobile, accessibility, analytics, or reliability.
- Read both when reviewing an end-to-end experience or creating a product surface.

## Review method

1. Identify the artifact, audience, user goal, and stage of the journey. Ask only when a missing choice would materially change the result.
2. Inspect the actual artifact or behavior. Separate observed evidence from inference and from recommendations.
3. Check the relevant brand and product-trust criteria. Preserve the user's explicit product direction unless it creates a concrete trust, safety, accessibility, or brand conflict.
4. Prioritize findings:
   - **P0:** misleading success, broken primary actions, unsafe sharing or permissions, lost work, false AI claims, or blockers to the core journey.
   - **P1:** material beta risk in comprehension, mobile use, accessibility, grounding, recovery, or measurement.
   - **P2:** polish, consistency, and optimization.
5. Lead with the verdict and the smallest set of changes that materially improves the experience. For each issue, state the evidence, why it matters, and the recommended change.

## Creating or editing

- Apply WZRD's visual and language system without turning every surface into a brand showcase. Calmness and clarity come before decoration.
- Use normal product language. Prefer short, spoken phrases and one idea at a time.
- Keep AI claims exact. Do not imply that content was changed, a person was notified, an action completed, or data was retained unless that outcome is verified.
- For implementation requests, make the requested change, then verify the rendered result and the relevant primary journey. Do not expand a review request into a live mutation.

## Output defaults

For a review, use a compact structure:

- Verdict
- Findings grouped by P0, P1, and P2; omit empty groups
- Recommended next move

For copy work, provide the finished copy first, followed by only the rationale needed to explain important choices.
