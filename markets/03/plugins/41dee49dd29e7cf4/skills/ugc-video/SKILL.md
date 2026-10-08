---
name: ugc-video
description: Produce a creator-style video ad for a product, shot the way a real customer would film it rather than like a commercial. Trigger when the user asks for a UGC ad, a creator video, an influencer-style ad, a testimonial-style video, an unboxing, a review video, or a TikTok or Reels ad for their product. Do not trigger for polished product hero videos with no person, for animating a personal photograph, for written ad copy alone, or when the user has not supplied a product reference.
---

# UGC Video

Produce a short vertical video that reads as filmed by a customer on a phone, not produced by an agency.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## What makes this different from a product video

A product video sells through craft: controlled light, clean surfaces, deliberate camera. A UGC video sells through the absence of craft. Handheld frame, ordinary room, uneven light, a real hand, a slightly off centre composition. If it looks produced, it fails as UGC.

Never apply studio lighting, never centre the product perfectly, never use a locked tripod frame, never grade it cinematically.

## Product Lock

The product from the reference is immutable: shape, proportion, colour, material, label geometry, typography, logo, printed text. It may be held, tilted, partially occluded by a hand, or slightly out of focus, which is normal in UGC. It may never be redesigned.

If label text is unreadable in the reference, let the hand or the angle hide that face. Never reconstruct it.

## People

Any person is auxiliary. Hands, a partial body, a shoulder, an over-the-shoulder view, or a face are all acceptable, but the product is the subject.

Never depict a real, identifiable person unless the user supplies their own photo and says it is them. Never imply a specific real person endorses the product. Generated people are fictional and must not resemble a public figure.

Never state or imply that the video shows a real customer, a real review, or a real result. If the user asks for a testimonial, produce it as clearly fictional demonstration and say so in the delivery line.

## Claims

Write no claim the user has not given you. No statistics, no before and after results, no medical, financial, or performance outcomes, no superlatives about the product. If the user supplies approved claims, use only their exact wording.

## Intake

Ask once, bundled: the product reference; the duration; the format, meaning whether they want spoken voiceover, on-screen captions, or neither; and any approved claims. Offer eight, fifteen and thirty seconds.

## Structure

Write the beats before generating anything.

- **Hook**, first two seconds. A problem stated, an unexpected visual, or the product already in hand. Never a greeting, never a logo, never a title card.
- **Context**, the ordinary setting that makes it believable.
- **Demonstration**, the product being used, held, opened, applied, or worked with.
- **Close**, the result or the reason to act.

For durations above fifteen seconds, plan two or three short shots rather than one long take. Long single takes drift and break the product.

## Look

Vertical nine-by-sixteen. Handheld micro-shake. Mixed domestic light, such as a window plus a lamp, not a softbox. Real background clutter, kept mild. Shallow phone-style depth rather than cinema bokeh. Slight overexposure or a mild colour cast is an asset here, not a defect.

## Audio and captions

Check explore_models for a video model that generates native speech. If one exists, use it and write the spoken lines in the prompt.

If none is available, say so plainly, deliver the video without speech, and produce the voiceover separately with generate_audio, returning both plus the script. There is no tool to combine them, so tell the user they will need to lay the track over the clip in their editor. Never imply the delivered file contains narration it does not.

Captions are not generated into the video. Text baked by an image or video model garbles. Deliver the caption text alongside so the user adds it in their editor.

## Execute

Call generate_video with the product asset id as reference, nine-by-sixteen.

## Quality gate

Reject if the product changed shape, colour, or label; if the result looks studio-lit or tripod-shot; if a hand shows the wrong number of fingers; if a person dominates over the product; if generated text appears in frame; or if a second product appears.

Regenerate once, moving further toward ordinary and handheld.

## Deliver

Return the video, the script if one was written, and the caption text if requested. State plainly that any person shown is fictional and that the video is a concept demonstration, not a real customer testimonial.

## Stop conditions

| Condition | Response |
|---|---|
| No product reference | Call show_upload_widget and wait |
| User asks for a real testimonial or real results | Offer a clearly labelled fictional demonstration instead |
| User asks for a named real person or lookalike | Decline in one sentence |
| User supplies claims you cannot verify | Write around them, say what was left out |
| Quality gate fails twice | Deliver the most believable take and say what drifted |
