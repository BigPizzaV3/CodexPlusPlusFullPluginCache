---
name: product-photography
description: Photograph a product the user supplies, in a studio or lifestyle setting, for a store listing, website, catalog, or paid ad. Trigger when the user provides a product image and asks for a product photo, product shot, hero shot, studio shot, lifestyle shot, packshot, catalog image, or listing image. Do not trigger for applying flat label artwork onto a container, which belongs to packaging-mockup. Do not trigger for video, for multi-version test sets, or when the user has not supplied a photograph of the real product.
---

# Product Photography

Produce one photograph of a real product supplied by the user.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## Product Lock

The product in the supplied reference is immutable data.

Preserve its shape, proportion, colour, material, finish, label geometry, typography, logo, and every printed character exactly as they appear. Angle, lighting, surface, background, relative scale, and framing are free. Never redesign, restyle, correct, translate, beautify, or recreate any part of the product. If the request requires changing the product itself, stop and ask whether the user wants a different product or a different scene.

If label text in the reference is blurred, cropped, or unreadable, do not reconstruct it. Frame so that face falls out of focus, turns to profile, or sits partially out of frame. Invented packaging text is the most expensive defect in this category.

## Preconditions

A photograph of the real product is required. Never generate a product from a description, never substitute stock, never complete a poor reference with invention. Without a photo, stop and ask for one.

Every generation spends the user's credits. Resolve ambiguity before the first call.

## Intake

Ask once, bundled, only for what is missing: the product photo; where the image will be used (marketplace listing, website, paid ad, catalog, social); clean studio or lifestyle scene; and output shape. If the destination is a marketplace listing, assume a neutral background with the product centred, and say that you assumed it.

Never ask about models, resolution, providers, or internal mechanics.

## Classify the product before writing the prompt

Category determines treatment. This step is not optional.

- Transparent or liquid (bottle, flask, glass): reflection control is the core problem. Use a gradient backdrop, raking side light, and a vertical edge highlight. Never pure white, which erases the silhouette.
- Cosmetic and skincare: clean surface, soft short shadow, tonal background, no competing props.
- Electronics: edge definition sells. Controlled hard light, specular edge reflection, neutral cool or dark background.
- Textile and apparel: texture and drape. Wide diffuse light, flat lay or on a form, never hard light.
- Food and beverage: freshness cues. Condensation, a crumb, steam, window light. Never perfect symmetry.
- Rigid objects and tools: scale. Include a size cue or use a three-quarter angle.

## Choose the angle by function

Three-quarter at roughly thirty degrees is the hero default. Straight-on front for marketplace listings. Overhead for flat lay and food. Macro for texture and finish. Avoid dramatic low angles unless requested, as they distort product proportion.

## Write the prompt

One continuous description containing: the product named for what it is, the surface, the background, the lighting scheme, the angle and camera distance, the implied lens, the expected shadow and reflection, and the product preservation instruction. No keyword lists. No generic style words such as premium, high quality, or professional.

Always constrain against: added text, watermarks, third-party logos, duplicate products, hands unless requested, plastic skin if a person appears, exaggerated bokeh, and teal-and-orange grading.

## Execute

Call generate_image once, passing the product photograph as the reference image and the validated prompt.

Derive aspect ratio from destination: square for marketplace listings, four-by-five for social feed, sixteen-by-nine for banners and website heroes, nine-by-sixteen for stories.

## Quality gate

Before delivering, reject and regenerate once if the product diverges from the reference in shape, colour, or label; if any text is unreadable or invented; if a duplicate product appears in frame; if a hand shows the wrong number of fingers; or if a third-party brand mark is visible.

## Deliver

Return the image and one line describing what was made. Offer upscale_image to 4K when the destination is print, catalog, or a website hero. Never expose model names, job identifiers, prompts, or internal steps.

## Stop conditions

| Condition | Response |
|---|---|
| No product photograph supplied | Stop and ask for one |
| Product obstructed, cropped, or unrecognisable in reference | Stop and ask for a clearer photo |
| User asks to change the product design | Stop and ask: different product, or different scene |
| Quality gate fails twice | Deliver the closest passing result and state what could not be preserved |
