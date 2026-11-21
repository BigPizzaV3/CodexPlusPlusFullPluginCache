---
name: idea-ai-3d-assets
description: "Develop a 3D asset from a description or reference images with idea.ai, selecting supported mesh, material, and export options for its intended use."
---

# 3D asset development

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_3d_model` with the selected model and its supported format options. Omit files for text-to-3D; for image-to-3D, supply ready upload IDs or existing result URLs without inventing file roles.

## Define the asset

Establish the object's shape, distinguishing features, materials, intended use, and desired file format. Separate appearance from requirements such as scale, rigging, topology, game-engine readiness, or printing. Ask about those requirements when they determine whether generation alone can satisfy the request.

For reference-based work, choose complementary views of the same object. Do not treat conflicting designs as a consistent multiview reference. Create additional concept views only when requested or included in the approved budget.

## Inspect generation and export options

Hyper3D Gen2 (`hyper3d_gen2`) exposes `textTo3D` and `imageTo3D`; its inspected image mode accepts up to five images. It exposes `file_format` choices GLB, OBJ, USDZ, FBX, and STL, plus `material`, `mesh_mode`, `hd_texture`, and `seed` settings. Recheck current values before use.

Meshy 7.1 (`meshy_7_1`) and Meshy 7.1 Print (`meshy_7_1_print`) expose single-image generation with fewer options. A model name containing Print is not a printability certificate. Do not invent absent polygon-count, skeleton, retopology, or manufacturing controls.

## Inspect what can be verified

Review available previews for silhouette, proportions, missing parts, materials, and reference fidelity. Verify that an actual returned artifact matches the requested supported format before describing it as delivered. If geometry cannot be inspected, identify that limitation.

For completed GLB or glTF outputs, use the free `preview_3d` once with the existing generation ID when available; deliver the model URL alongside it. Other formats use their returned download URL. Do not generate another asset solely to obtain a preview. Call `quote_cost` for the actual request before generation even when get_model shows a standard base price.

Deliver the model and preview with the selected settings. Do not claim that the result is watertight, correctly scaled, rigged, production-ready, or printable without appropriate checks. Explain any remaining validation or editing step and the additional tooling it needs.
