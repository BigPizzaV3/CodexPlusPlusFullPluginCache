---
name: poster-campaign
description: Turn a single concept or product brief into an editable multi-format visual campaign with scoped artboard editing.
---

# Skill: Poster & Multi-Format Campaign Creation

Use SketchMonkey to turn a single concept or product brief into an editable multi-format visual campaign.

## Capabilities
- Generate 5 distinct art directions (Ren, Maya, Zola, Kai, Nova) with palettes, typography, and rationales.
- Create multi-format campaigns across supported formats (`poster_a4`, `square_1x1`, `story_9x16`, `banner_16x9`, and `cmf_sheet`).
- Edit specified saved fields (headline, subheadline, body copy, tagline, font family, alignment, accent color) while preserving unrelated layers and background artwork.

## Recommended Workflow
1. Call `get_account_status` when accessing saved work.
2. Call `create_project` with project `name` and `brief`.
3. Call `generate_directions` to inspect the 5 creative lenses.
4. Call `select_direction` to save the chosen direction for the project.
5. Call `create_campaign` to produce artboards in the requested supported formats (`poster_a4`, `square_1x1`, `story_9x16`, `banner_16x9`, `cmf_sheet`).
6. Call `inspect_artboard` before and after calling `edit_artboard` to edit only the requested saved fields while preserving unrelated layers and background artwork.
7. Call `get_artboard_export_metadata` to inspect saved artboard dimensions and available background image URLs (`composedFileAvailable: false`).

## Design data and safe execution

Ask only for information needed for the design: product purpose, approximate dimensions, materials, finish, style, audience and functional requirements. Use synthetic examples for demonstrations.

Do not ask for passwords, API keys, login or verification codes, payment card data, government identifiers, patient records, or real-person biometric or identity templates. Do not pass such information to a tool, quote it back, or suggest encoding it to bypass restrictions. If supplied, ask for a design brief with those details removed. A generic medical-device design brief must not include patient information. Fictional character art does not require a real person's identity data.

Use the host's secure OAuth 2.1 connection for account access. Inspect current tool discovery and respect server validation. Do not use saved-reference IDs, handles, alternate tool names or other routes to bypass a refusal.

Use actual returned project, artboard and job IDs. Before overwriting saved content, inspect it and confirm the intended fields from the user's request; preserve unrelated fields. Honor authorization, quota and validation errors.

Concept renders and material suggestions are design proposals, not certified CAD, engineering analysis, tested material specifications or manufacturing approval. Export metadata and background image URLs are not composed PNG/PDF files. Show completed media only when a real tool result supplies it; report failures and unavailable outputs accurately.

Respect existing account access. Do not solicit card details, advertise subscription prices, promote upgrades or initiate digital checkout.
