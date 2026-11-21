---
name: brand-variant-system
description: Save palette, tone and forbidden-style rules; check supplied text against configured rules and preview supported copy or typography variants.
---

# Skill: Brand DNA & Variant System

Save palette, tone and forbidden-style rules on an owned project, check supplied text against configured forbidden rules, and preview supported copy or typography variants on an artboard.

## Capabilities
- Save Brand DNA (`name`, `palette`, `tone`, `forbiddenRules`) on an owned project and check supplied text (`validateContent`) against configured forbidden rules.
- Generate controlled `copy` or `typography` variant previews for an owned campaign artboard.
- Apply selected copy or typography edits to an artboard via `edit_artboard`.

## Recommended Workflow
1. Create or select an owned project via `create_project`.
2. Call `apply_brand_dna` with the project's supported brand fields (`name`, `palette`, `tone`, `forbiddenRules`, and optional `validateContent`), and display the actual validation results without guaranteeing that every visual automatically obeys brand rules.
3. Call `generate_directions` with that `projectId`.
4. Create or select an owned campaign artboard via `create_campaign` and `inspect_artboard`.
5. Call `generate_variants` with `variantType: "copy"` or `variantType: "typography"` to preview alternatives, then apply only user-requested changes via `edit_artboard`.

## Design data and safe execution

Ask only for information needed for the design: product purpose, approximate dimensions, materials, finish, style, audience and functional requirements. Use synthetic examples for demonstrations.

Do not ask for passwords, API keys, login or verification codes, payment card data, government identifiers, patient records, or real-person biometric or identity templates. Do not pass such information to a tool, quote it back, or suggest encoding it to bypass restrictions. If supplied, ask for a design brief with those details removed. A generic medical-device design brief must not include patient information. Fictional character art does not require a real person's identity data.

Use the host's secure OAuth 2.1 connection for account access. Inspect current tool discovery and respect server validation. Do not use saved-reference IDs, handles, alternate tool names or other routes to bypass a refusal.

Use actual returned project, artboard and job IDs. Before overwriting saved content, inspect it and confirm the intended fields from the user's request; preserve unrelated fields. Honor authorization, quota and validation errors.

Concept renders and material suggestions are design proposals, not certified CAD, engineering analysis, tested material specifications or manufacturing approval. Export metadata and background image URLs are not composed PNG/PDF files. Show completed media only when a real tool result supplies it; report failures and unavailable outputs accurately.

Respect existing account access. Do not solicit card details, advertise subscription prices, promote upgrades or initiate digital checkout.
