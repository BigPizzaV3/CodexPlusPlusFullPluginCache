---
name: wonderwhy
description: Analyze supplied POD product images and personalization previews, propose 3 visually grounded marketing hypotheses with confidence scores, and generate 3 portrait ad creatives. Use when the user invokes WonderWhy or requests product-image analysis leading to advertising concepts.
---

# WonderWhy

Turn supplied product images into commercial hypotheses and visual ads. Images reveal design choices and possible uses; they do not establish customer motives or market demand.

## Input and default contract

Use one or more user-supplied images as the primary input: product photos, mockups, personalization previews, or artwork. Optional context includes product name, material, personalization options, audience, market, offer, and brand constraints. A SKU is only an optional label, not a lookup trigger.

If no usable image is supplied, ask for a product image. If several unrelated products are supplied and the target is unclear, ask which one to analyze. Otherwise proceed using visible evidence and clearly marked assumptions; do not require a completed product brief.

Inspect the images → propose 3 distinct scored marketing hypotheses → render one creative per hypothesis. Briefly present the hypotheses before rendering without waiting for approval. Default to Vietnamese analysis and English ad copy for the US market unless the user specifies otherwise.

Honor narrower requests: “chưa render”, “insights only”, or “3 đề xuất trước” means stop after hypotheses. A later render request uses the inspected references. This workflow has no store connection, order retrieval, or sales-data requirement. It does not launch ads, create videos, or modify products.

## 1. Inspect the source images

Read [references/image-workflow.md](references/image-workflow.md) for image intake and evidence handling.

Assign each image a stable reference such as IMG-01. Inspect every supplied image relevant to the target and distinguish product photos, mockups, personalization previews, artwork, and styling references. Record visible product shape, design, readable text, personalization, colors, apparent material, and scene context. Treat exact material, dimensions, printing technique, and included accessories as unknown unless established by the image or user context.

Separate directly visible observations, user-provided facts, and interpretations. Flag unreadable names and ambiguous details rather than guessing. Repeated images or designs are not independent customers or purchases. Do not infer sensitive traits or family relationships from names or faces.

Summarize the inspected references, product invariants, and limitations that affect the concepts. Do not claim visual inspection for inaccessible inputs. When only some images are accessible, proceed provisionally if they are sufficient; otherwise request a usable image.

## 2. Propose three marketing hypotheses

Explore plausible emotional meaning, use occasion, gifting context, personalization appeal, or purchase friction. Choose three commercially useful angles with distinct motivations or occasions rather than three phrasings of one emotion.

For each hypothesis provide:
- A proposed customer tension or desire in one sentence, explicitly framed as a hypothesis.
- Supporting visual observations with image references, plus any relevant user-provided facts.
- The interpretation and at least one alternative explanation or limitation.
- Confidence from 0–100 with a brief rationale: subjective confidence in the visual interpretation, not purchase intent, market demand, or expected ad performance. A single image can establish a visible feature but cannot validate a buyer motive. Mark weakly supported angles exploratory.
- An ad/video concept with an opening moment, product reveal, and short English hook; the deliverable remains a still image.
- A concrete product or offer extension, labeled as a proposed concept if not confirmed available, and one small test to validate the hypothesis.

Do not invent customer quotes, reviews, order counts, sales patterns, popularity, discounts, or performance claims. Avoid calling the hypotheses validated customer insights. Summarize the best first test and the assumption it would test.

## 3. Render three concepts

Read [references/creative-direction.md](references/creative-direction.md) before generation. Use the image-generation/editing tool configured in the current runtime and supply inspected product images as actual reference inputs, not just filenames in the prompt. Inspect local references before using them. Do not assume tool names or integrations from a different environment.

Produce three separate portrait 3:4 creatives, each tied to one hypothesis. Preserve the visible product shape, artwork, personalization logic, and confirmed material. Use realistic photography, a large recognizable product, and one bold mobile-readable English headline. Use the supplied product by default; label any new-product rendering as a concept.

Inspect each result for product fidelity, readable correct personalization, plausible anatomy and perspective, prominent accurate headline text, and 3:4 composition. Correct concrete defects using supported editing or generation tools. If exact 3:4 output needs recomposition, preserve the product and text and never stretch the image. Disclose any unresolved output limitation.

Return the three hypotheses, the three generated images through the runtime's supported output mechanism, and a concise creative-to-hypothesis mapping with the first recommended test. In API environments return actual file identifiers or URLs supplied by the runtime, never invented links. If image generation is unavailable, return usable creative briefs and clearly identify the unrendered outputs. No additional report file or deck is required unless requested.
