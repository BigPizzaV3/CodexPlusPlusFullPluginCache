---
name: thumbnail
description: Design a thumbnail or cover image that stays readable at small size, for YouTube, podcasts, courses, blogs, or playlists. Trigger when the user asks for a thumbnail, a video cover, a podcast cover, a channel art piece, or an image to sit next to a title in a feed. Do not trigger for general poster or social graphic design, for product photography, for video, or for images where small-size legibility is not the point.
---

# Thumbnail

Design one image whose entire job is to win a click at roughly two hundred pixels wide.

## Morphix tool contract

These are the tools available and the order they run in. Follow it exactly.

**Getting the user's image in.** Chat attachments cannot be passed to generation. When a reference is needed, call show_upload_widget, which shows a drop box and returns an asset id once the user uploads. Never call upload_asset directly. If the user uploaded something earlier in the conversation, call get_assets and reuse that asset id rather than asking again.

**Before spending credits.** Call explore_models to choose a model for this job, and get_account to confirm the user has credits. Both are read-only and free. Choosing a model blind, or starting a generation the user cannot pay for, are the two most common wasted turns.

**Choosing a model.** Never hardcode a model name. Read the capabilities returned by explore_models and pick for the job at hand: reference fidelity when the result is anchored to a supplied image, text handling when legible type matters, motion quality for video, voice range for audio.

**Generating.** generate_image and generate_video accept asset ids to edit or reference existing images, including image-to-video. generate_audio takes the script plus a voice chosen through explore_models. Each spends credits and renders a live view that polls itself, so never poll manually and never tell the user you will check back.

**Retry spends again.** A regeneration costs credits a second time. The quality gate in this skill allows one automatic retry. Beyond that, say what is wrong and let the user decide.

**Finishing.** upscale_image and upscale_video raise an existing asset. Offer these instead of regenerating at a larger size.

**Recovering work.** get_assets lists the library newest first. get_generations fetches a generation by id. Use them to pick up earlier work instead of remaking it.

## The constraint that defines this skill

A thumbnail is not a small poster. It is viewed at a fraction of its size, next to competing thumbnails, often on a phone, frequently in dark mode. Every decision follows from that.

Three elements maximum. One focal point. Readable in one glance at thumbnail scale.

## Preconditions

Ask for the video or episode title and the topic. Without the title you cannot decide what the image must not repeat.

A source photo is optional. If the user supplies a face shot, use it and preserve the likeness.

## Intake

Ask once, bundled: the title; the platform; whether they have a face or product shot to include; and the channel's existing look if there is one. Never ask about resolution.

## Composition rules

**Subject scale.** The focal element occupies at least a third of the frame. A subject that reads at full size disappears at thumbnail size. When in doubt, go bigger.

**Face rules.** If a face is included: crop at chest or tighter, eyes in the upper third, one clear expression, lit so the face separates from the background. A face reading a single strong emotion outperforms a neutral one. Never manufacture an expression on a supplied photo of a real person; recompose and relight instead.

**Contrast and separation.** The subject must separate from the background by luminance, not only by colour. Test the idea in greyscale mentally: if subject and background merge, add a rim light, a dark vignette, or a flat colour field behind the subject.

**Colour.** Two dominant colours plus one accent. High saturation reads at small size. Avoid muddy mid-tones and avoid palettes that vanish against both light and dark interface backgrounds.

**Negative space.** Leave a deliberate clear zone where platform elements land: the lower right corner carries a duration badge on video platforms, and the lower edge can be overlaid by progress bars.

## Text in the thumbnail

Prefer no text. The title already sits next to the image, and repeating it wastes the frame.

If the user insists on text: three to four words maximum, one line if possible, heavy weight, very large, placed in the clear zone, never crossing the face. Text must add something the title does not say.

Because generated text is unreliable, deliver the image with the text zone left clear whenever the user can add type themselves, and say that is what you did and why.

## Write the prompt

Name the subject and its scale in frame, the expression if a face is present, the background treatment, the lighting that creates separation, the two-colour palette and accent, and the clear zone. State explicitly that the composition must read at small size.

## Execute

Call generate_image, sixteen-by-nine for video platforms, square for podcast and playlist covers.

## Quality gate

Judge the result as if it were two hundred pixels wide. Reject if the subject does not read instantly, if subject and background merge in luminance, if more than three elements compete, if any generated text is misspelled or garbled, or if a supplied face has been altered.

Regenerate once with a tighter crop and a larger subject.

## Deliver

Return the image and one line naming the focal point and the clear zone. Offer upscale_image if the user needs a larger master.

## Stop conditions

| Condition | Response |
|---|---|
| No title or topic given | Stop and ask for the title |
| User wants a long text block in the image | Explain the small-size constraint, offer three to four words |
| Supplied face is too low resolution to hold at crop | Ask for a better photo or offer a non-face composition |
| Generated text garbles twice | Deliver with the text zone clear and say why |
