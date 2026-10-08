---
name: references-from-uploads
description: Turn pictures the user uploads or makes in chat into reference documents Screel can generate from — a real person, a pet, a product, a logo, a brand look, a place. Use when the user attaches a photo and wants it in a video, or asks for their product, brand or self to appear.
---

# References from uploads

## The rule

A picture that lives only in this chat does nothing for the project. It becomes usable in exactly two ways: `set_document_image` puts it into a reference document's bank, or `set_scene_image` makes it a scene's still. Do the handoff in the same turn the picture arrives; the file link expires within minutes.

## A person or a pet

1. `list_documents`, then `create_document` with the reference template. In Description write what the photos show (hair, build, clothing in the photo, distinguishing marks); in Consistency what must hold (face, hair colour, glasses, the dog's coat pattern); in Avoid what the story must not change.
2. `set_document_image` with the uploaded file as `image` and a `name` for what the photo is: "photo front", "photo profile". Attach up to three or four photos that show different angles; skip near-duplicates and group shots.
3. Photos are noisy references: backgrounds, other people, phone lighting. Derive a clean canonical view before generating scenes: `refine_image` with `image_url` of the best photo, `document_id`, `image_name` "front": "the same person, full body, plain light-grey studio background, even soft lighting, neutral expression, keep the face and hair exactly". Read the result. If the likeness slipped, retry from another photo or adjust the instruction; do not build on a bad likeness.
4. Scenes then use `reference_document_ids` with that document. The clean view plus one or two photos is enough; more photos dilute the likeness.
5. Ask before putting a real person into anything they would not expect: an ad, a scene that implies something about them, a different body. Keep them as they are unless the user says otherwise.

## A product, a package or a device

- Products need exact shape, label, colour and proportions. Attach the clearest photos from front, side and three-quarter as separate bank pictures, named by angle.
- A clean packshot as canonical view: `refine_image` "the same product on a plain white surface, studio lighting, no reflections, label readable". Write the exact label text into Consistency; picture models misspell, so say in every scene prompt that the label must read exactly as in the reference.
- In scene prompts, describe how the product is held, placed or lit; never re-describe the product. The pictures carry the design.
- A product with a screen: describe what the screen shows in each prompt, or put a fixed screen state in Consistency.

## A logo or a brand mark

- Attach the logo on a plain background as its own document ("Acme logo"), Consistency: exact letterforms, colours, no restyling; Avoid: no gradients, no 3D, no extra text.
- Logos degrade in generation. Use them as a reference where the mark is small (a badge, a sign in the distance) and keep close-ups of the mark for the editor, where the user can place the original file.
- Never invent a brand's mark. If the user did not upload one, ask for it or leave the mark out.

## A place, a set or a vehicle

- Same shape as a character: a document per place, two to four photos or generated views named by angle ("wide", "entrance", "interior"), a Consistency section with the fixed layout (where the door is, what the walls are made of).
- A place reference conditions the environment strongly. Pair it with the character document on the same item, and put the place second in `reference_document_ids` so the character labels come first.

## A picture the user made in chat

- The same handoff: `set_document_image` with the file. Generating a reference picture in chat is allowed only when the user asks for it; scene visuals always come from `generate_image`.

## Keep it honest

- If the user's photo is low resolution or heavily filtered, say so; the derived views inherit it.
- Do not remove watermarks or reproduce a photo the user says belongs to someone else.
- Report what the document now holds after the upload so the user can open it in Screel and swap a picture if they want.