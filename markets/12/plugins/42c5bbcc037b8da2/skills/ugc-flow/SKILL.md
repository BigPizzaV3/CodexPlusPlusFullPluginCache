---
name: ugc-flow
description: "A creator-style product review, from concept and script to a finished clip. Use for \"UGC video\", \"product review video\", \"tutorial ad\", \"TikTok ad\", \"creator showing my app\". Not for opening a package (unboxing-ugc-skill), trying on clothes (try-on-ugc-skill), a polished video with no presenter or an avatar reading a script with no product in hand."
---

# Product review UGC

A review people stop for: one moment only this product can cause, filmed from a phone on the table, with the product in the middle of the frame and a room with a clear color idea. The speech stays plain and the physics stay real.

## Ask first

- The product: photos, and what it does for the buyer. If they give a product page and you can read it, take the facts and images from it and show what you took.
- The format, from the table below.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 12 seconds, 9:16 for social and 16:9 for a website. If they want several angles, keep the creator and the product the same and make one video per format or hook.

## Pick the format

| Format | What happens |
| --- | --- |
| Review | One moment with the product, the creator's real reaction, the product in use, one closing line |
| How-to | The result first, two or three steps with the product in hand, one closing line |
| App or website | A hook, the problem, the creator holding a phone or laptop showing the product, the outcome, one closing line |

For an app or website, pass a screenshot as a reference. Generated screens rarely stay readable, so keep them brief, or suggest adding a real screen recording in an editor.

## Find the moment

Pick one believable thing that happens to this product in the first four seconds: a soda that foams over when it is opened, a spray that catches the light, a lid that will not come off. Keep its size ordinary, and say how big it is in the prompt, or the model makes it huge.

## Write the script and show it

Three short spoken lines, about 20 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

| Image | Model | Notes |
| --- | --- | --- |
| Product, if the user has no good photo | `generate_gpt_image_2_5_image` | Keeps the words on the label. Ask for real materials, such as transparent glass and liquid you can see through. Flat saturated color and water drops look pasted on |
| Creator, if generated | `generate_seedream_5_pro_image` | Waist-up, plain background, sharp |
| Opening frame | `edit_seedream_5_pro_image` | Takes the product and the creator, with the framing below |

For the opening frame, describe a phone resting on the table: ultra-wide, level with the table, deep focus. The product stands in the center at about 40% of the frame's height, lit by the same light as the room, with a reflection and a contact shadow. The creator's whole head is in frame with space above it. Show this frame to the user before making video, since video costs far more.

## Make the video

Use `generate_seedance_2_5_video` with the opening frame, the product and the creator as `images`, in that order, and with sound on. Keep the prompt under 150 words:

- One line per shot, in order. Do not describe what the opening frame already shows.
- Put the spoken lines in quotes.
- Say that her whole face and her hand on the product stay in frame. Without it, close shots cut off the face and the product floats with no hand.
- Say how many hands she uses.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a face cut off, extra fingers, a blurred label, or something that changed between cuts, such as a cap back on an opened bottle. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the moment, the script and the total price together, and wait for a yes.
2. Make the images and show the opening frame, then make the video with the script's exact words.
3. Deliver the clip. RunComfy has no tool for joining clips or burning in captions: if you remade part of it, hand the clips over in order, or join them with ffmpeg if you can run commands.

## Rules for every RunComfy skill

- Reply in the user's language. Tool arguments stay in English.
- Ask at most three short questions before starting, with choices where you can. Skip what the request, an attached file or an earlier turn already answers, and use a sensible default for the rest. Do not turn a single generation into a long workflow.
- Each step names the RunComfy tool to use. Never guess its inputs: use the ones the tool lists.
- Price first. Each generation tool names its model: read that model's price with `get_model` and tell the user the model and the total for the whole plan, adding up every step. Wait for their yes. Anything beyond the plan they agreed to, or a dearer model, needs another yes.
- Files. Tool inputs take public https links. For a past result use `list_my_generations` and for a file in My Assets use `get_asset_download_url` when they are available. Otherwise ask the user for a public link.
- Run with `wait_for_completion: false` and keep the `request_id`. Check `get_model_request_status` no more than every 15 seconds for images and every 30 seconds for video, then `get_model_request_result`. A timeout or an unclear outcome is not a failure: check the request before submitting again.
- Prompts. Be concrete: subject, setting, camera, light, style. For an edit, say what stays the same and what changes, and do not describe the rest of the image. For image to video, describe the motion, not the frame. Say what you want rather than what you do not want. With two or more references, open the prompt by naming each one, such as "image 1 is the product, image 2 is the creator".
- Work you do not own. Use someone else's image or video for its mood, pacing and layout only. Do not copy its people, logos, words or exact composition.
- Truth. Use only facts the user gave you or that you can point to. Never invent claims, results, prices, discounts, statistics, testimonials, awards or certifications.
- Several results. When a plan has many parts, make one, check it, then make the rest. Each result should differ in a way you can name, not be the same picture reworded. Redo only what is wrong and say what was wrong. If a safety filter refuses a prompt, tell the user instead of working around it.
- Deliver the output links with a short label for each. No raw JSON, no internal ids and no running commentary on status checks unless the user asks.
