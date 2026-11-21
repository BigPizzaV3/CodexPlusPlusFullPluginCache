---
name: try-on-ugc-skill
description: "A creator-style try-on video that shows how an outfit looks and fits. Use for \"try-on video\", \"outfit video\", \"get ready with me\", \"how this fits\", \"fashion UGC\". Not for a review of a product that is not worn (ugc-flow) or for changing clothes in a photo."
---

# Try-on UGC

The change is the point: the creator shows the clothes, the viewer sees them up close, then she is wearing them and they move. The speech stays plain and the physics stay real.

## Ask first

- The outfit: a photo laid flat or on a hanger, plus anything worn with it, and what should stand out, such as the fit, the fabric or one detail.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 15 seconds: about 4 for the selfie, 5 for the bed and 6 for the whole body. Use 9:16 for social and 16:9 for a website.

## Plan the shots

| Shot | What happens |
| --- | --- |
| Selfie at arm's length | In a plain T-shirt, she holds the top on a hanger beside her face and says one line |
| Looking down at the bed | The whole outfit is laid out with the shoes and accessories. One hand lifts a hem or touches a detail, and she says one line |
| Whole body, phone on the floor | She now wears everything. She turns so the fabric moves, then looks at the lens and gives one closing line |

## Write the script and show it

Three short spoken lines, about 15 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

Make one still for each shot, so the clothes and the room stay the same. Each one costs far less than video, so show them to the user first.

Give every piece its length, such as a cardigan that ends at the waist and a skirt one and a half times as long, with its hem just below the knee. "Long" or "midi" alone comes out too long or too short.

| Image | Model | Notes |
| --- | --- | --- |
| Outfit, if the user has no good photo | `generate_gpt_image_2_5_image` | A flat lay from above, with the fabric texture visible |
| Creator, if generated | `generate_seedream_5_pro_image` | Head and shoulders in a plain T-shirt, sharp |
| Selfie and bed | `edit_seedream_5_pro_image` | Give it the outfit and the creator. Make the selfie first, with her phone hand out of frame |
| Whole body | `edit_gpt_image_2_5_image` | Give it the outfit, the creator and the selfie, so the room matches. Say she is an adult whose head is about a seventh of her height, and keep the camera nearly level. From a head-and-shoulders photo, Seedream draws the head too large |

Before the video, check her proportions in the whole-body still: an adult stands about seven heads tall.

## Make the video

Use `generate_seedance_2_5_video` with the three stills, the outfit and the creator as `images`, in that order, and with sound on. Keep the prompt to about 150 words:

- Say which image opens which shot, and give each shot its length.
- Say what moves in one line per shot. Do not describe what the stills already show.
- Put the spoken lines in quotes.
- Keep the camera still in the second and third shots.
- In the bed shot, say only her hand comes in, or her head may enter the frame.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a head cut off, extra fingers, a detail that changed, such as buttons or a hem, or clothes that are different between shots. A mirror in the room may not show her, so keep it out of frame if that matters to the user. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the shot plan, the script and the total price together, and wait for a yes.
2. Make the images and show them, then make the video with the script's exact words.
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
