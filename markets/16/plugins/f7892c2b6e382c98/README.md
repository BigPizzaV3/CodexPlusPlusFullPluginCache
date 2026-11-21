# Packaging Design Assistant

A skills-only plugin for packaging design and review. It works from supplied product facts and does not require an MCP server, API key, OAuth connection, external backend, or database.

## Focused skills

- `packaging-design-assistant`: routes work and applies shared factual/production boundaries.
- `packaging-concepts`: distinct visual and structural directions.
- `packaging-layout-copy`: panel mapping and factual packaging copy.
- `packaging-production-planner`: structures, materials, finishes, dielines, and printer handoff.
- `packaging-mockup-creator`: concept visuals and image prompts.
- `packaging-review`: critique, variants, shelf and ecommerce clarity.
- `packaging-compliance-research`: current, jurisdiction-specific authoritative research when requested.

## Core safeguards

The plugin does not invent ingredients, nutrition values, quantity, dimensions, warnings, certifications, barcodes, regulatory approvals, or unsupported health/environmental/recycling claims. Missing facts remain clearly marked placeholders. A concept is not final production artwork, an engineered dieline, a legal approval, or printer preflight.

## Included references

Reference files under `skills/packaging-design-assistant/references/` preserve the user-supplied format, concept, layout, copy, material, print, compliance, mockup, review, workflow, and acceptance-test requirements.

## Acceptance checks

1. Missing ingredients: use a clear placeholder.
2. Unverified certification: do not present it as genuine.
3. Unknown nutrition: use a placeholder, not fabricated values.
4. Dieline without dimensions: keep advice conceptual and request manufacturer specifications.
5. Printer-readiness: do not claim readiness without specifications and preflight.
6. Competitor copying: extract high-level category lessons and create an original design.
7. Unsupported environmental claim: do not state it as fact.
