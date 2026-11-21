---
name: idea-ai-character-consistency
description: "Create or edit a series of images with the same character using idea.ai, preserving defining features across scenes, poses, expressions, and outfits."
---

# Character consistency

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `create_image` for an initial text-only reference and `edit_image` for reference-based scenes and corrections. Keep the approved original URL or ready upload ID in every scene request.

## Establish the identity

Use an approved character reference as the source of truth. If references disagree, ask which controls the disputed feature. If no reference exists, write a brief and create one reference image within the authorized budget; get the character approved before producing the series.

Record the original reference ID or URL, visible defining features, proportions, distinctive marks, outfit, and rendering style. Keep requested changes in expression, wardrobe, setting, and lighting separate from identity. Do not invent hidden features or claim the brief persists into another chat.

## Choose reference controls

Inspect suitable models with `get_model`. Discovery examples include Kling V3 Omni (`kling_v3_omni_image`), Seedream 5 Pro (`seedream_5_pro`), FLUX.2 Pro (`flux_2_pro`), and Nano Banana 2.1 (`nano_banana_2_1`). Their inspected schemas support multiple reference/source images. Recheck any `aspectFit` rules and quote each affected reference with measured dimensions and the actual target options; a standard base price may not include fitting charges. Kling's named reference inputs require aliases; do not copy those roles onto another model.

Use the same approved original reference in each scene. No persistent character ID, character-training tool, or guaranteed identity lock was exposed in the inspected tools. Do not invent one or present a fixed seed as an identity guarantee.

## Generate and assess the set

Build each request from the stable brief plus the scene-specific changes. Keep the selected model and style consistent unless the user requests a change or a demonstrated limitation requires one.

Compare outputs with the original reference for facial structure, hair, marks, proportions, outfit, and style. Account for perspective, lighting, and intentional expression changes. Identify specific mismatches and repair only the affected scene, using a targeted edit when supported. Repeatedly using the newest output as the sole reference can accumulate drift.

Deliver the scene-ordered images, reusable brief, original reference identifier, and unresolved differences. Stop when the requested set is assessed or the agreed budget/retry limit is reached.
