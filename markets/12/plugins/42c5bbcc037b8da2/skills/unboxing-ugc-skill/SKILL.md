---
name: unboxing-ugc-skill
description: "A creator-style unboxing video with a clear reveal and close-up details. Use for \"unboxing video\", \"opening the package\", \"first look at my product\". Not for a review of a product already out of its box (ugc-flow) or a polished reveal with no presenter."
---

# Unboxing UGC

A closed package, a reveal, one close look and an honest first reaction, filmed on a phone close to the table in a place with character. The speech stays plain and the physics stay real.

## Ask first

- The product and its packaging: photos of both if they have them, and what the presenter should point out.
- The creator: their photo, or a generated person. Only use a real person who agreed.

Default to 12 seconds, 9:16 for social and 16:9 for a website.

## Plan the shots

| Shot | What happens |
| --- | --- |
| High angle, looking down | Her hands rest on either side of the closed package, and she looks up and says one line |
| Table height | She opens it or slides the product out, and reacts |
| Chest-up | With one hand she holds the product beside her cheek and says one line |
| Closer | She uses it: a bite, a pour, a first try |
| Chest-up again | She looks into the lens and gives one closing line |

## Write the script and show it

Three short spoken lines, about 15 words in all, the way a person talks. Do not claim results the user cannot back up.

## Make the images first

| Image | Model | Notes |
| --- | --- | --- |
| Product and packaging, if the user has no good photo | `generate_gpt_image_2_5_image` | Keeps the words on the box. Ask for real materials, such as matte printed cardboard and a clear film window |
| Creator, if generated | `generate_seedream_5_pro_image` | Waist-up, plain background, sharp |
| Opening frame | `edit_seedream_5_pro_image` | Takes the package and the creator, framed as the first shot above |

Show the opening frame to the user before making video, since video costs far more.

## Make the video

Use `generate_seedance_2_5_video` with the opening frame, the package and the creator as `images`, in that order, and with sound on. Keep the prompt under 150 words:

- One line per shot, in order. Do not describe what the opening frame already shows.
- Put the spoken lines in quotes.
- Say that her whole face stays in frame and that she holds the product with one hand. With two hands, close shots hide her face behind her fingers.
- End with natural delivery, real physics, no music and no captions.

## Check it before you deliver

Look at frames from every shot for a face cut off, extra fingers, a blurred label, a bite or pour that looks wrong, or something that changed between cuts. If a shot is wrong, remake only those seconds instead of the whole clip, and tell the user the added price first.

## Steps

1. Show the shot plan, the script and the total price together, and wait for a yes.
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
