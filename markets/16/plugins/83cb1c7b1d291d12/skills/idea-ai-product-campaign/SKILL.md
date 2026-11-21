---
name: idea-ai-product-campaign
description: "Create coordinated product campaign images with idea.ai from product references, including hero images, lifestyle scenes, detail shots, and social variants."
---

# Product campaign kit

Read [the shared MCP workflow](../../references/mcp-workflow.md) before calling tools. It defines discovery, file handling, cost authorization, waiting, and delivery for this skill.

## MCP operation

Use `edit_image` for product-reference scenes, focused corrections, resizing, and outpainting; use `create_image` only for requested text-only concepts. Quote every supplied reference input, not just the output resolution.

## Define the campaign

Establish the product, audience, campaign message, intended placements, and requested deliverables. Reuse supplied brand choices. Ask only for missing facts that affect the assets, such as packaging details that must be legible or a claim that needs the user's exact wording.

Treat product geometry, label text, colors, and essential accessories as invariants. Distinguish the product reference from style or setting references. Propose a small scene plan with the purpose and format of each asset before pricing the batch.

## Select a reference-based image workflow

Inspect available image models. Discovery examples include Seedream 5 Pro (`seedream_5_pro`), Nano Banana 2.1 (`nano_banana_2_1`), and Kling V3 Omni (`kling_v3_omni_image`) for multi-image work. Ideogram 4.5 Precise Edit (`ideogram_v4_5_precise_edit`) exposes a rectangular edit region for a focused correction.

Create one representative campaign image first when the visual direction is unsettled. Use an existing approved direction directly. Keep product and style references stable across scenes, changing only scene-specific composition, props, action, or framing.

## Review and deliver

Check each result for product shape, proportions, packaging, readable text, brand colors, misleading additions, and placement requirements. Reference inputs do not guarantee exact logo or packaging reproduction. If exact artwork cannot be preserved, identify the affected asset and propose a supported correction or later layout step.

Resize or outpaint approved images when that meets the format requirement without another redesign. Do not add video, new claims, or extra variants outside the requested campaign and budget.

Deliver a labeled asset set with its intended placement and dimensions, approved creative direction, references, and any corrections still needed.
