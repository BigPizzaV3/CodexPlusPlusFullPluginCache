---
name: marketing-adapt-video
description: "An original video ad for your product, built on the story and sales structure of a reference ad. Use for \"make an ad like this one\", \"recreate this ad for my product\", \"use this video as a reference\", \"same structure, my product\", \"adapt this ad\". Takes no footage, people, words or logos from the reference."
---

# Ad Recreator

Keep the reference's structure: the order of its shots, their length, framing and camera moves, and the job each one does. Take nothing else from it: no footage, people, places, words, logos or music.

## Ask first

- The reference video, as a file or a public link, 2 to 30 seconds.
- The product: a clean photo, and what it is.
- Where it should be set and who should be in it, if they care. Otherwise pick a new place and new people that suit the product.

## Break the reference down

Look at its frames and write each shot: the seconds, what is on screen and its job, such as the hook on the product, a hand reaching for it, the product in use, a close-up with a person or a closing shot. Then write the new version shot for shot, with the same jobs and timing.

## Make a first frame for each shot

Make one still per shot before any video, with the product exactly as in its photo. Each costs far less than video, so show them first.

| Still | Model | Notes |
| --- | --- | --- |
| Shots with people | `edit_seedream_5_pro_image` | Give it the product photo, and the earlier still of the same person so the face stays the same. Ask for a frame from a 35 mm film commercial, real people with natural skin, light film grain and no big smiles. Polished, smooth faces read as fake |
| The product alone | `edit_gpt_image_2_5_image` | Keeps the words on the label exact |

## Make the video

Use `generate_seedance_2_5_video` with the reference clip in `videos`, and in `images` the first frames in shot order followed by the product photo. With a reference clip, both the reference seconds and the output seconds are billed, so quote it first. Keep the prompt to about 180 words:

- Name the product image, and say the video is a reference for the shots, their order, length, framing and camera moves only, with no people, places, product, words or logos taken from it.
- Say which image opens which shot, and give each shot its length and one line of action.
- End with real people, real physics, the sound you want, no voiceover and no captions.

## Check it before you deliver

Look at frames from every shot: the product and its label unchanged, no extra hands or fingers, and nothing from the reference's brand. If one shot is wrong, remake only that shot, and tell the user the added price first.

## Steps

1. Show the shot-by-shot breakdown, the stills plan and the total price, and wait for a yes.
2. Make the stills and show them, then make the video.
3. Deliver the clip with the breakdown beside it, and offer to change the opening or the offer.

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
