---
name: restore-and-upscale
description: Repair and enlarge an existing image, recovering real detail rather than smoothing it away. Trigger when the user asks to upscale, enhance, sharpen, restore, fix, de-blur, or increase the resolution of an image they supply, including old, scanned, damaged, or low resolution photographs. Do not trigger for generating new images, for changing the content of an image, for video, or for stylistic edits.
---

# Restore and Upscale

Make an existing image larger and better without turning it into a different image.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## Content Lock

Restoration repairs an image. It does not reinterpret it.

Preserve every element: faces and their identity, text and its exact characters, logos, colours, grain structure appropriate to the era, and composition. Do not add detail that was never photographed, do not invent a face behind a blur, do not complete a cropped edge, do not modernise clothing or setting, and do not colourise unless explicitly asked.

The most common failure is a restored photograph where the person is no longer the same person. Treat that as a hard failure, not a stylistic variation.

## Preconditions

An image file. Ask what the result is for, because the destination sets how far to push.

## Intake

Ask once, bundled: the image; what it is for, such as print, web, archive, or a larger creative piece; and whether it needs repair as well as enlargement. If the image shows visible damage such as creases, tears, stains, fading, or scan artefacts, name what you can see and confirm what they want removed.

## Diagnose before acting

Different defects need different treatment and the wrong order makes things worse.

- **Low resolution but clean**: upscale directly. Nothing to repair first.
- **Soft or out of focus**: upscaling will enlarge the softness. Say so. Sharpening a genuinely out-of-focus image invents detail and changes faces.
- **Compression artefacts**: blocking and ringing around edges. Address before enlarging, or the artefacts scale with the image.
- **Film grain or scan noise**: grain is often part of the photograph's character. Ask before removing it. Removing grain from a film photograph is a stylistic choice, not a repair.
- **Physical damage**: creases, tears, missing corners, stains. Repair is reconstruction of background, never of a face. If damage crosses a face, say explicitly which part will be reconstructed and let the user decide.
- **Fading and colour cast**: correct toward neutral, but preserve the era's palette. A nineteen seventies photograph should still look like one.

## Order of operations

Repair defects first, then enlarge. Enlarging first multiplies the defect.

For a heavily damaged photograph, do it in visible steps and show the intermediate result, so the user can stop at the point they prefer rather than receiving one over-processed final.

## Execute

Call upscale_image for enlargement and detail recovery. When repair requires reconstruction of damaged areas, call generate_image with the source as reference and an instruction limited strictly to the damaged region, naming what must remain untouched.

State the output size in the delivery line.

## Quality gate

Compare against the source at matching scale. Reject if a face reads as a different person, if text characters changed, if a logo altered, if skin became plastic, if edges show halo or oversharpening, or if invented detail appeared in an area that was simply out of focus.

Regenerate once with a lower degree of intervention. Less is the fix.

## Deliver

Return the image, the final dimensions, and one line naming what was repaired and what was deliberately left alone. If grain or character was preserved on purpose, say so, otherwise the user may read it as a failure.

## Stop conditions

| Condition | Response |
|---|---|
| No image supplied | Stop and ask for one |
| Damage crosses a face | Name what would be reconstructed, ask before proceeding |
| Image is out of focus rather than low resolution | Explain the difference, offer enlargement without invented detail |
| User asks to change content rather than repair it | Route to a generation skill |
| Face identity fails twice | Deliver the lower intervention result and say why |
