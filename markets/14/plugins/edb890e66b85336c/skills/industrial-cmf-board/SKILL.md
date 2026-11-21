---
name: industrial-cmf-board
description: Explore conceptual Color, Material and Finish directions and organize them into editable design artboards.
---

# Skill: Industrial Design & CMF Direction Board

Use SketchMonkey to explore conceptual Color, Material and Finish (CMF) directions and organize them into editable design artboards.

## Capabilities
- Enrich informal hardware prompts with conceptual CMF terminology, parting lines, and studio lighting cues.
- Explore five creative lenses (`ren`, `maya`, `zola`, `kai`, `nova`) for product and material concepts.
- Organize conceptual material callouts into editable `cmf_sheet` campaign artboards.

## Recommended Workflow
1. Call `get_account_status` when accessing saved work.
2. Create or select an owned project via `create_project`.
3. Enhance the concept brief via `enhance_prompt`.
4. Call `generate_directions` and present the five directions so the user can choose one.
5. Call `select_direction` with the user's chosen direction and actual `projectId`.
6. Call `create_campaign` with `formats: ["cmf_sheet"]` using the owned `projectId`.
7. Call `inspect_artboard` and `edit_artboard` to refine supported text fields, then call `get_artboard_export_metadata` if export metadata is requested.

## Design data and safe execution

Ask only for information needed for the design: product purpose, approximate dimensions, materials, finish, style, audience and functional requirements. Use synthetic examples for demonstrations.

Do not ask for passwords, API keys, login or verification codes, payment card data, government identifiers, patient records, or real-person biometric or identity templates. Do not pass such information to a tool, quote it back, or suggest encoding it to bypass restrictions. If supplied, ask for a design brief with those details removed. A generic medical-device design brief must not include patient information. Fictional character art does not require a real person's identity data.

Use the host's secure OAuth 2.1 connection for account access. Inspect current tool discovery and respect server validation. Do not use saved-reference IDs, handles, alternate tool names or other routes to bypass a refusal.

Use actual returned project, artboard and job IDs. Before overwriting saved content, inspect it and confirm the intended fields from the user's request; preserve unrelated fields. Honor authorization, quota and validation errors.

Concept renders and material suggestions are design proposals, not certified CAD, engineering analysis, tested material specifications or manufacturing approval. Export metadata and background image URLs are not composed PNG/PDF files. Show completed media only when a real tool result supplies it; report failures and unavailable outputs accurately.

Respect existing account access. Do not solicit card details, advertise subscription prices, promote upgrades or initiate digital checkout.
