---
name: generate-deep-art-image
description: Generate a brand-new raster image from a text description with the Deep Art AI MCP server. Use when the user asks Deep Art AI to create, generate, render, or explore an illustration, concept, poster, background, portrait, product scene, or visual variant. Do not use for editing an existing image unless the connected Deep Art AI tool supports image-to-image editing and the user requests it.
---

# Generate a Deep Art AI Image

Create an image with Deep Art AI, preserve the user's intent, and display the result in the conversation.

## Workflow

1. Extract the subject, setting, composition, style, mood, lighting, palette, aspect ratio, and exclusions from the request.
2. Ask a question only when a missing detail would materially change the result. Otherwise choose tasteful defaults and proceed.
3. Connect to the Deep Art AI MCP server and inspect the current image-generation tool schema before constructing arguments. Never guess tool names, parameter names, or enum values.
4. If the server or generation tool is unavailable, explain that Deep Art AI must be connected. Do not silently substitute another image generator.
5. Build one concise visual prompt. Put the subject and composition first, followed by style, environment, lighting, palette, camera or rendering details, and constraints.
6. Preserve requested text exactly. Warn briefly that image models may render text imperfectly.
7. Map only options supported by the current tool schema. Honor requested dimensions, aspect ratio, seed, model, quality, and negative prompt when supported; otherwise use server defaults.
8. Generate once unless the user requests variants. If the server reports an actionable prompt or parameter error, revise once and retry.
9. Inspect the successful response for the image or image URL. Request network permission before downloading when required, then save and display the image.
10. Briefly describe the generated result and mention only meaningful differences from the request.

## Prompt Guidance

- Describe visible details instead of abstract praise.
- Keep negative constraints in a negative-prompt field when supported; otherwise append a short `Avoid:` clause.
- For variants, keep the core subject stable and change one dimension at a time.
- Do not claim that Deep Art AI generated an image until the tool returns successfully.

## Example Requests

- “Use Deep Art AI to generate a cinematic alpine lodge at blue hour.”
- “Create a square editorial illustration of a robot tending a rooftop garden.”
- “Generate three poster concepts with a limited red-and-cream palette.”
