---
name: idea-ai-vector-artwork
description: "Develop related icons or illustration concepts with idea.ai\u2019s SVG-oriented generation model, verifying actual output formats before claiming editable vectors."
---

# Vector artwork kit

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_image` for text-to-image artwork concepts. Do not route raster-to-vector requests to `edit_image` without a model whose inspected capabilities actually support that operation.

## Establish the visual system

Define the required icons or illustrations, their meanings, intended sizes, palette, stroke treatment, fill style, level of detail, and background treatment. Identify which details must remain recognizable at small sizes.

Use an approved sample or create one representative design first when the direction is unsettled. Translate the chosen direction into a concise art-direction brief for the remaining items. Do not assume that a model can ingest a style reference unless its current modality explicitly accepts one.

## Inspect the SVG-oriented model

The discovered catalogue includes Recraft V4 SVG (`recraft_v4_svg`) with `textToImage` and an `aspect_ratio` option. Its inspected schema labels the output type as `image` and does not expose an SVG path editor or a reference-image input. Verify the actual returned artifact before claiming SVG export or editability.

If the user needs vectorization of an existing raster image, search the live catalogue for that specific capability. Do not relabel fresh text-to-image generation as faithful raster-to-vector conversion.

## Review the set

Compare silhouette, visual weight, spacing, stroke treatment, palette, and semantic clarity across assets. Inspect small-size legibility where the host can display the results. Preserve approved items and revise the inconsistent ones within budget.

Deliver the returned artwork, its verified file type, and the reusable style brief. If an output is a raster preview or its vector structure cannot be checked, state that limitation. Do not promise editable layers, outlined fonts, production-ready paths, or a complete design-system component library without corresponding verified artifacts.
