---
name: props-and-objects
description: Keep a recurring object the same in every scene — a car, a sword, a robot, a phone, a bottle, a piece of furniture, a logo on a product — whether it is held, carried, worn or standing in the set. Use when a story has a hero object, when the user says a prop changed shape or colour between scenes, or when an object must appear next to a character at a fixed size.
---

# Props and objects

## Why a prop drifts

- A prompt describes an object in words, and words leave the model free: "a red sports car" is a different car in every scene. A reference picture fixes the shape, the proportions, the markings and the colour, so the prompt only has to say where the object is and what it does.
- A prop is generated in a scene most often small, partly hidden or in a hand. The model copies what it can see in the reference, so the reference must show the whole object, large and unobstructed.

## Make the reference

1. One `create_document` with the reference template per object. Under **What is it?** say the class in one line ("a 1960s two-seat roadster", "a bronze short sword"). Under **Description** give exact shape, proportions, materials, colour with a plain name, markings, wear, anything printed or engraved. Under **Consistency** write the three or four things that identify it from any angle ("round twin headlights, chrome grille bar, cream body with a red stripe"). Under **Avoid**, what the model tends to add ("no spoiler, no roof, no text on the doors").
2. The canonical view: `generate_image` with `document_id` and `image_name` "front" — or "three-quarter" for a vehicle or a piece of furniture, because that view shows more of the shape. Prompt for a product shot: the whole object, centred, large in frame, plain evenly lit light-grey studio background, no hands, no people, no scene dressing, no text. A reference works best at 1:1 or 4:3.
3. Read the result. Fix a wrong detail with `refine_image` on that picture (`image_url`, `document_id`, `image_id` to replace in place) before you make more views. Every later view copies its mistakes.
4. Derive the other views FROM the canonical one, never from a new prompt: `refine_image` with `image_url` of the canonical picture, `document_id` and `image_name` "side", "back", "top", "detail of the handle". One call with `images[]` makes them together. Add a view only when a scene needs it: a chase seen from behind needs "back"; a close-up on the engraving needs "detail".
5. An object the user photographed goes in with `set_document_image`, and a clean canonical view derives from the photo with `refine_image` ("the same object, whole, centred, plain light-grey studio background, even lighting, keep every marking exactly").

## Held, worn, carried

- When a character holds or wears the object, keep BOTH documents on the item: the character first in `reference_document_ids`, the object second. Say in the prompt who holds it and how ("Rin holds the sword in her right hand, blade down").
- Scale is a prompt job. State it against the character or the set in plain words ("the sword is as long as her arm", "the bottle fits in one hand", "the car is a small two-seater, its roof at her shoulder"). A reference fixes shape, not size.
- A "held" view of the object alone is rarely worth a bank entry; the character document and the object document together carry the pose.

## Objects that are the set

- A vehicle interior, a workbench, a cockpit or a shop counter is a place as much as a prop. Give it a wide "interior" view in the bank as well as the exterior, and treat it with the place rules in `style-and-world`.
- A logo or a label is a picture, not a prompt. Put it in the bank with `set_document_image` and name it "logo"; the prompt then says where it sits ("the logo on the side panel").

## In the scene batch

- Every item whose scene shows the object carries the object's document in `reference_document_ids`, along with the character and style documents it needs; the budget is 14 pictures per generation across every source, so keep a prop bank at two to four views.
- Do not re-describe the object in scene prompts. Name it, place it, and say what it does; the pictures carry the rest. A prompt that repeats the description pulls away from the references.
- After the first batch, read the stills. A scene that changed the object gets `refine_image` with the object document referenced ("match the car in the reference: cream body, red stripe, round headlights") instead of a regeneration.

## When not to bother

- A one-off object, background clutter, or a thing named once and never shown again needs no document. Describe it in the prompt and move on.
- Crowds of similar objects (books on a shelf, cars in traffic) are set dressing; only the hero object gets a document.