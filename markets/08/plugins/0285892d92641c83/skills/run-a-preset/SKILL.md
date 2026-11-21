---
name: run-a-preset
description: Use this when someone asks what NOLGIA can make, names one of the guided routes such as a commercial, a social media ad, a product demo, product photos, listing images, an unboxing, a music video, a logo reveal, a poster, a cover, animated titles or a color grade, or wants help choosing where to start. Do not use it when the person has already given a complete brief for a single piece and just wants it made.
---

# Run a preset

Presets are NOLGIA's guided routes. Each one knows what it needs, so the person answers a few short questions instead of writing a brief.

## When to trigger

Trigger on "what can you make", "show me the options", "do you have something for", or on any named route: commercial, social media ad, creator review ad, app ad, product demo, product commercial, outfit try-on, unboxing reaction, narrated channel video, fashion film, music video, film scene, animated cartoon, motion graphics, animated titles, logo reveal, logo, poster, billboard, cover art, YouTube thumbnail, interior design, concept art, color grade footage, product photos, listing images, A+ content, infographic.

Do not trigger when the person has handed you a finished brief for one piece. Make that instead.

## Steps

1. Call `nolgia_list_presets` ONCE. It takes no arguments and returns the whole catalog, so if it has
   already been called in this conversation, reuse that result: calling again draws a second, identical
   gallery on top of the first.
2. Narrow to at most three that fit what the person said, using each preset's own name, description and best-for line. Prefer the ones whose output type matches what they asked for, a still or a moving picture.
3. The catalog is ALREADY ON THEIR SCREEN as a gallery of cards they can scroll, filter and open. Do not
   list it back to them. Name at most three that fit, one line each on what it makes and who it suits,
   and ask which one. If they already named one, skip straight to it.
4. If the preset card shows a FORM, the person is already looking at a field, chips or a library picker
   for every question. Point at it and let them fill it in rather than asking the same things in chat.
   Only when the card says a step needs answering in the conversation do you ask it yourself.
   Otherwise, ask the preset's questions in one bundled message. Every preset needs the subject, where it runs, and the feeling. Add the ones the chosen route obviously needs: a tagline for a commercial, a hook line for a social ad, the product and its photos for a demo, the mark for a logo reveal, the track for a music video, the source clip for a color grade.
5. Write all the prompting yourself from their answers and the preset's description. Their words are inputs, never the prompt.
6. Generate. Stills go through `nolgia_text_to_image`, or `nolgia_image_to_image` when they supplied a reference. Moving pictures go through `nolgia_text_to_video`, or `nolgia_image_to_video` when there is a starting frame. Check `nolgia_list_models` first so the model you choose accepts the length, the shape and the references you plan to send.
7. Video is a background job: poll `nolgia_list_jobs`, then `nolgia_get_asset` for the link. Stills come straight back.
8. If the person supplied a photo, a product, a garment or a mark, repeat it word for word in the prompt and say it must match the reference exactly. Compare the result against what they gave you before you deliver, and re-run anything that drifted.

## What to return

The finished file, the preset you used by its plain name, and what you decided on their behalf so they can correct it. Offer one variation.

Never repeat a preset's internal guidance field back to the person, never name a model, and never discuss what anything cost.

## When to stop or decline

- Nothing in the catalogue fits: say so and offer to make it without a preset.
- A preset needs source material the person does not have: say exactly what is missing before you spend anything.
- The person wants a real, named public figure in the result: decline.
