---
name: style-and-world
description: Hold one visual style and one world across a whole project — a look (illustration style, film stock, palette), recurring places and props — and combine style, place and character references without them fighting. Use when the user names an art style, wants scenes to look like one film, or asks why scenes look inconsistent in tone.
---

# Style and world

## Three kinds of reference, three jobs

- A character document fixes WHO: face, body, costume. Its pictures are portraits on plain backgrounds.
- A place document fixes WHERE: layout, materials, landmarks. Its pictures are wide, empty views.
- A style document fixes HOW IT LOOKS: medium, line, palette, grain, lighting mood. Its pictures are two to four frames in the target look that contain none of the story's characters or places, so the model borrows the treatment and not the content.
- All three ride `reference_document_ids` on the same item. Order them subject first, place second, style last; the labels follow that order and the model weights earlier pictures as content and later ones as treatment.

## Build a style document

1. `create_document` with the reference template. Title it for the look ("Look — 1970s film"). In Description name the medium, palette, contrast, grain, lens feel, era. In Consistency write the two or three properties that must hold in every frame ("warm halation, muted greens, soft 35mm grain"). In Avoid, what breaks the look ("no neon, no clean digital sharpness, no anime line work").
2. Make the style frames with `generate_image` and `document_id`, `image_name` "look 1", "look 2": generic subjects (an empty street, a table by a window, a hand on a railing) rendered in the target style. Never a character or a story location; the model would copy them.
3. A style the user uploaded (a frame from a film, a painting) goes in with `set_document_image`. A recognisable artwork or a living artist's signature style is a request to decline politely; describe the qualities instead ("loose watercolour, warm paper").
4. Write the style words in the prompt too, briefly. The pictures set the treatment; the words keep it from drifting when the reference budget is tight.

## Build a place document

- One wide view first (`generate_image`, `document_id`, `image_name` "wide"), then derive "entrance", "interior", "night" from it with `refine_image` so the layout stays the same. A place is a set: the camera moves, the walls do not.
- Put the layout in words in Consistency ("door on the left, window wall at the back, long table centre") so a prompt can place characters correctly.
- Recurring props (the car, the sword, the robot arm) are product-style documents: exact shape, named angles, no re-description in prompts.

## Combine without conflict

- Budget: 14 pictures per generation across every source. Character (2-3) + place (2) + style (2-3) fits; two characters + place + style needs lean banks.
- Conflicts show up as muddy results: a photoreal character document with a watercolour style document. Resolve it at the document level: regenerate the character's canonical view in the style ("the same character, rendered in the look of the reference frames", with the style document referenced) so the character bank already carries the treatment.
- Set the style once for the project and reuse the same style document on every item. Changing style mid-project is a new project's worth of references.
- A style document alone is enough for scenes without recurring subjects: montage shots, inserts, landscapes.

## Prompt shape that works

`<subject and action>, <where, in the place's own words>, <camera>, <light and time>, <two or three style words>` — the references carry the rest. Long prompts that re-describe what the pictures show pull away from the references.

- Frame treatment is part of the look and drifts on its own: one scene comes back with a painted border, a vignette or a letterbox and the sequence stops reading as one film. Keep every scene full-bleed unless the user asks for a device. Put `borders, frame, vignette, letterbox, split panel, inset, text, watermark` in the batch-level `negative_prompt` and in the style document's Avoid section, and use the same two or three medium words in every scene prompt.

## Checks

- After the first batch, read the stills. If one scene broke the look, `refine_image` on it with the style document referenced ("match the look of the reference frames") instead of regenerating everything.
- Render settings (resolution, motion on stills, captions) are separate from the look; set them with `update_project` when the user asks.