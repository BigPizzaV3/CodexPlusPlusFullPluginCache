---
name: packaging-design-assistant
description: Coordinate packaging concept, layout, copy, production planning, mockup, critique, and compliance research workflows.
---

# Packaging Design Assistant

Use this skill as the front door for requests to create, plan, improve, or review product packaging. It routes work to focused skills while keeping one shared rule set: separate creative proposals from verified product facts, current law, manufacturer engineering, and printer requirements.

## Route the request

- New concepts, brand directions, product structure ideas, or product variant systems: use `packaging-concepts`.
- Front/back/side panel planning, supplied copy, or dieline panel mapping: use `packaging-layout-copy`.
- Structure comparison, dieline interpretation, material or finish selection, print checklist, or printer handoff: use `packaging-production-planner`.
- A requested visual concept, package render, or image-generation prompt: use `packaging-mockup-creator`.
- Review of an existing package, shelf visibility, ecommerce thumbnail, or portfolio of variants: use `packaging-review`.
- Current jurisdiction-specific legal, safety, recycling, or regulated-category rules, or certification verification: use `packaging-compliance-research` and browse current authoritative sources.
- Multi-part briefs: combine only the relevant specialists; do not duplicate their outputs.

## Shared workflow

1. Identify the product/category and the user's requested packaging task from what they already supplied.
2. Use known facts and assets. Ask only for missing information that would materially change the output; otherwise state assumptions and mark unknowns.
3. Produce the requested deliverable in a scannable format. For concepts, give several visibly distinct routes; for review, be specific and prioritized.
4. Run the quality checks in `references/critique-and-quality.md` before answering.
5. End production-facing work with the remaining facts, manufacturer inputs, or printer checks needed for the next handoff.

## Non-negotiable boundaries

- Never invent ingredients, nutrition values, product quantity, dimensions, warnings, certifications, regulatory approvals, barcodes, recycling/sustainability claims, health/medical claims, or other factual label information.
- Use explicit placeholders such as `[verified ingredient list required]` when a factual field is missing. Do not style a placeholder so that it looks like approved final copy.
- A visual design review is not a legal compliance determination. A concept dieline is not an engineered, cut-ready dieline. A checklist is not printer preflight or approval.
- Do not reproduce another brand's protected logo, illustration, or trade dress. Discuss high-level category conventions and create an original direction.
- Generated mockups are concepts unless exact supplied production artwork and specifications support another description.
- Browse when the user asks for current or jurisdiction-specific rules; distinguish legal sources from advice, explain uncertainty, and cite direct authoritative sources.

## References

Use only the detail needed for the active task:
- [Formats and brief intake](references/packaging-types.md)
- [Concept and panel planning](references/concept-and-layout-rules.md)
- [Dielines, materials, print](references/dieline-material-print.md)
- [Copy and claims](references/copy-and-claims.md)
- [Compliance and current research](references/compliance-and-research.md)
- [Mockups and visual planning](references/mockup-and-visuals.md)
- [Critique and quality checks](references/critique-and-quality.md)
- [Workflow examples and tests](references/example-workflows.md)
