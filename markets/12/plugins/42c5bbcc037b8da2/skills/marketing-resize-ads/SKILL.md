---
name: marketing-resize-ads
description: "One static ad rebuilt for other placements and shapes, such as 1:1 and 4:5 for the feed, 9:16 for Stories and Reels or 16:9 for a banner, with the layout rearranged instead of cropped. Use for \"resize this ad\", \"make this ad for Stories\", \"other aspect ratios\", \"adapt it for placements\", \"banner size\". Not for new headlines (marketing-headline-variants)."
---

# Ad Resizer

Rebuild the layout for each shape so the product, headline and call to action stay clear. Never just crop or stretch the original.

## Ask first

- The ad, and which placements. Default to 1:1 and 4:5 for the feed and 9:16 for Stories and Reels.

Show the sizes and the price, and wait for a yes.

## Make each size

Use `edit_gpt_image_2_5_image` with the ad as the only image and the aspect ratio set to the placement, one request per size:

> Recompose this ad as a vertical 9:16 story ad. Keep the product, the photograph's look and every word exactly as they are, in the same fonts and colours; rearrange the layout to suit the new shape instead of cropping, and keep all text and the product well inside the edges. No other text.

For 9:16, say where things go: the logo near the top, the product in the middle and the text in the lower third, clear of the bars Stories draw over the top and bottom.

## Check before you deliver

Read every word in each size against the original, and check nothing touches an edge. Remake any size that drops or changes a word, and say so.

## Deliver

Label each link by placement, and suggest checking each one in the platform's preview before launch.

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
