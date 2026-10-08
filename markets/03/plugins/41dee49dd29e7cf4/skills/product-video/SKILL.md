---
name: product-video
description: Turn a supplied product photograph into a short video for an ad, a store page, or social. Trigger when the user has a product image and asks to animate it, make a product video, a video ad, a product clip, or motion for their product. Do not trigger for narrated creator-style videos where a person speaks, for editing existing footage, for still images, or when the user has not supplied a photograph of the real product.
---

# Product Video

Produce one short video of a real product supplied by the user.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## The failure mode this skill exists to prevent

Video models deform geometry and labels when motion is fast, when the camera crosses the face of the product, or when duration outruns the reference anchor. Every rule below exists because of that.

## Product Lock

The product in the supplied reference is immutable data for the entire shot.

Preserve shape, proportion, colour, material, finish, label geometry, typography, logo, and every printed character. The product stays rigid. Camera, light, and environment move; the product does not change.

If label text is unreadable in the reference, keep that face away from camera rather than reconstructing it.

## Preconditions

A photograph of the real product is required. The product should occupy at least a fifth of the frame in the reference; below that, ask for a tighter photo before spending credits.

## Intake

Ask once, bundled: the product photo; duration; where it will run; and whether the user wants sound. Offer five, eight, and ten seconds.

Above ten seconds, say plainly that product fidelity degrades and propose two short shots instead of one long one.

## Permitted camera moves

Only these, because they preserve product legibility.

| Move | Effect | Best duration |
|---|---|---|
| Slow push-in | focus and desire | 5 to 8s |
| Partial orbit, up to forty-five degrees | reveals form and material | 8 to 10s |
| Tilt reveal, low to high | scale and presence | 5 to 8s |
| Pull-back from macro to wide | texture then context | 8 to 10s |
| Locked camera with environmental motion | product still, light or background moves | any |

Forbidden: whip pan, full three-hundred-and-sixty degree orbit, morph or transformation of the product, hard cut inside the shot, abrupt zoom, and any move that passes behind the product. If the user requests one, explain in one sentence that it deforms the label and offer the permitted equivalent.

## Put the motion in the environment

When the product carries dense label text, the safest way to get a living shot is to keep the product locked and move everything else: airborne particles, smoke, liquid, a falling leaf, a shifting light, a travelling shadow. Recommend this by default for text-heavy packaging.

## Sound

If the user wants sound, generate ambience or music only, using generate_audio.

Do not write spoken narration in this skill. Voiceover with a scripted presenter is a different format and out of scope. If narration is requested, say so in one sentence and offer the ambience version.

## Write the prompt

Name the product, the exact camera move and its speed, what moves in the environment, the lighting, the duration, and the instruction that the product stays rigid with geometry and label unchanged throughout the shot.

## Execute

Call generate_video with the product photograph as reference. Use nine-by-sixteen for vertical social, square for feed, sixteen-by-nine for website and long-form platforms.

## Quality gate

Inspect the first frame, a middle frame, and the last frame. The product must be the same object in all three.

Reject if the shape changes, the label shifts position relative to the form, any text changes, colour drifts, or a second product appears. Regenerate once with a slower move or a shorter duration.

## Deliver

Return the video and one line describing the move and duration. Never expose model names, job identifiers, prompts, or internal steps.

## Stop conditions

| Condition | Response |
|---|---|
| No product photograph supplied | Stop and ask for one |
| Product occupies less than a fifth of the reference frame | Stop and ask for a tighter photo |
| User requests a forbidden move and refuses the alternative | Stop and explain the deformation risk |
| User requests spoken narration | State that this is a different format, offer the ambience version |
| Quality gate fails twice | Deliver the most stable result and state what drifted |
