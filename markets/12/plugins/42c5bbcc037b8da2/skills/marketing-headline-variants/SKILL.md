---
name: marketing-headline-variants
description: "New versions of one static ad where only the headline changes, ready to test against each other. Use for \"headline variations\", \"test different headlines\", \"A/B test this ad\", \"10 versions of this ad\", \"new copy for this ad\". Not for new ad ideas from scratch (marketing-research-to-ads) or new sizes (marketing-resize-ads)."
---

# Headline Multiplier

Change only the headline, so a test shows which message works. Keep the picture, layout, fonts, colours, brand and offer exactly as they are.

## Write the headlines

- Default to 10 unless the user asks for a number.
- Spread them across angles: a benefit, a moment of use, curiosity, a problem, the flavour or feel, sharing.
- Keep each one as long as the original and in the same rhythm, so it fits the same space. If the original is two short lines, write two short lines.
- Add no claims, prices or offers the original ad does not make.

Show the list and the price, and wait for a yes.

## Make the versions

Use `edit_gpt_image_2_5_image` with the ad as the only image, one request per headline, at the ad's own shape:

> Change only the headline. It now reads exactly "line one" on the first line and "line two" on the second, in the same font, size, colour and position. Keep everything else in the image exactly the same. No other text.

Read every result: the words must match exactly, and nothing else may change. Remake any that do not, and say so.

## Deliver

Label each link with its headline and angle, and suggest testing them with the same audience, budget and placement, so only the headline differs.

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
