---
name: product-ad-variations
description: Produce an ordered set of creative variations of the same product, each changing one controlled variable, so the user can test, compare, or run them across placements. Trigger when the user supplies a product image and asks for multiple versions, variations, angles, options, A/B test creatives, or a set of ads for the same product. Do not trigger for a single image, for video variations, for applying label artwork to a container, or when the user has not supplied a photograph of the real product.
---

# Product Ad Variations

Produce N ordered variations of one product creative, built so the result of a test can actually be read.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## The governing principle

A variation set is only useful if the user can attribute a difference in outcome to a specific change. That requires each version to change one axis while everything else is held constant. A set where several things change at once is an assortment, not a test. Never produce an assortment.

## Product Lock

The product in the supplied reference is immutable data across every version.

Preserve its shape, proportion, colour, material, finish, label geometry, typography, logo, and every printed character exactly as they appear. Never redesign, restyle, correct, translate, or recreate any part of the product. If label text is unreadable in the reference, frame it out of focus or out of frame rather than reconstructing it.

## Preconditions

A photograph of the real product is required. Every version spends credits, so resolve the axis and the constants before the first generation.

## Intake

Ask once, bundled: the product photo; how many versions, N; which axis to test; and where the creatives will run. If the user does not know which axis, recommend scene for top of funnel and angle for listings and retargeting, then proceed.

## Permitted axes

Choose exactly one as the axis of the set.

| Axis | What changes between versions | Use when testing |
|---|---|---|
| Scene | the environment around the product | positioning and audience |
| Angle | camera position | product legibility in feed |
| Light and mood | lighting scheme and palette | brand tone |
| Human presence | no person, hands only, partial use | social proof |
| Format | aspect ratio and crop | placement adaptation |

## Fix the constants first

Before generating, write down everything that does not change: the product, camera distance, base palette, aspect ratio, and the lighting treatment unless light is the axis. Every version inherits these verbatim. Writing the constants before writing the variations is mandatory, otherwise the set drifts and the test becomes unreadable.

## Write N prompts in order

Each prompt repeats the constants word for word and alters only the value of the chosen axis.

Order is stable from planning through delivery. Version 1 is always the most conservative and closest to conventional use of the product. Later versions move progressively further from it. This gives the user a readable baseline.

Cap N at six in one round. Beyond six the user cannot compare and the credit cost stops being justified. If more are requested, deliver six and offer a second round after the first is read.

## Execute

Call generate_image once per version, in order, each with the same product reference.

## Quality gate

Reject and regenerate a single version once if the product diverges from the reference, if text is invented, if a duplicate product appears, or if the version accidentally changed an axis other than the chosen one. Frozen constants are the point of the set.

## Deliver

Return the images labelled Version 1, Version 2, and so on, each with one line naming the axis value it carries. Close with one sentence naming the axis tested and what a win for each version would indicate.

Never promise performance, never estimate click-through or conversion, never declare a winner before the test runs.

## Stop conditions

| Condition | Response |
|---|---|
| No product photograph supplied | Stop and ask for one |
| User wants several things to change at once with no axis | Explain in one sentence that the set would be unreadable, then ask for the axis |
| User asks to change the product design | Stop and ask: different product, or different scene |
| More than six versions requested | Deliver six, offer a second round |
