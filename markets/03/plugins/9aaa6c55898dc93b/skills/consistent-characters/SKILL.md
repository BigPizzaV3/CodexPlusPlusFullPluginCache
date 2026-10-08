---
name: consistent-characters
description: Keep a character, creature, mascot or product looking the same in every scene. Use when a story has a recurring subject, when the user says a character drifted between scenes, when several characters share a scene, or when a subject needs more views (side, back, another outfit).
---

# Consistent characters

## How references reach the picture model

- A reference document is a document with a picture bank. `reference_document_ids` on `generate_image` and `refine_image` attaches EVERY picture in each named document's bank to the generation, in bank order, after any `reference_image_urls` or attached files.
- The picture model receives them as numbered inputs labelled with their bank names ("Ref 1 (front)", "Ref 2 (three-quarter)"). The labels are appended to your prompt, so name bank pictures for what they show, never "image1".
- One generation takes at most 14 reference pictures across every source. Two documents of four pictures each plus a previous still is nine; keep banks lean so a group shot still fits.
- Nothing attaches on its own. A batch item without `reference_document_ids` inherits the call's top-level list, and an item that names its own list replaces it for that item only.

## Build a character reference

1. `list_documents` first. A document for this character usually exists; extend it instead of creating a second one.
2. `create_document` with the reference template: `# Name`, `## What is it?`, `## Description`, `## Reference Images / Media`, `## Consistency`, `## Avoid`. Put the invariant facts in Consistency: species, silhouette, colours, materials, signature items, proportions, age. Put what the pictures must never show in Avoid: other outfits, hats, text, extra limbs, a different palette.
3. Make the canonical view: `generate_image` with `document_id` and `image_name` "front". Prompt for a full-body or three-quarter studio portrait, plain evenly lit neutral background, no props that are not part of the design, no text, no other characters. Match the project's aspect ratio only for scenes; a reference works best at 1:1 or 3:4.
4. Read the result. If it is wrong, fix it with `refine_image` on that picture (`image_url` from the job result, `document_id`, `image_id` to replace in place) before you derive anything from it. Everything downstream copies its mistakes.
5. Derive the other views FROM the canonical one, never from a new prompt: `refine_image` with `image_url` of the canonical picture, `document_id` and `image_name` "side", "back", "face close-up". One call with `images[]` makes them together. Add a view only when the story needs it: a chase seen from behind needs "back"; a talking scene needs "face close-up".
6. Say which documents you created and what they hold. The user sees the bank in the editor.

## Generate scenes against it

- Every scene item that shows the character carries its document in `reference_document_ids`. A scene without it is a scene that drifts.
- In the prompt, call the character by the document's name and describe the action, camera and setting. Do not re-describe the design that the pictures already fix; a long re-description fights the reference. Repeat only what the scene changes on purpose ("Rin, soaked from the rain").
- Prompt the scene, not the reference: "Rin sprints across the rooftop at night, low angle, rain, neon reflections" — not "a character with red hair and a green jacket".
- Keep the same `reference_document_ids` on the `refine_image` calls that touch those scenes. An edit without the reference loses the face.

## Several characters in one scene

- Pass every governing document on that item: `reference_document_ids: [rin, tomas]`. Name both in the prompt and say who is where and what each does, so the model maps the labelled pictures to the right person.
- Two characters fit comfortably; with three or more, trim each bank to its canonical view plus one so the total stays under 14.
- Two very similar designs (two humans of the same age) blur into each other. Give each a distinguishing anchor in the prompt ("Rin, the taller one in green") and keep that anchor in their Consistency sections.

## Variants of one character

- A new outfit, an age change or a damaged state is a new bank picture in the same document, not a new document: `refine_image` on the canonical view ("same character, now in a torn winter coat") with `document_id` and `image_name` "winter coat". Mention the variant in the scene prompt so the model knows which pictures apply.
- A transformation (human to wolf) is a second document, since the two forms share no silhouette.

## When it goes wrong

- The face changed: the scene was generated without the document, or the bank holds pictures that disagree. Re-run that item with `reference_document_ids`; remove any bank picture that contradicts the canonical one (`edit_document` and the editor both can).
- A prop keeps appearing: put it in Avoid and regenerate the canonical view without it.
- Every scene looks like the studio portrait: the prompt is too close to the reference prompt. Prompt the scene's setting, light and action first; the reference supplies the subject.
- Never substitute your own image tool for a scene or a reference view: its output never reaches the project and carries no document behind it.