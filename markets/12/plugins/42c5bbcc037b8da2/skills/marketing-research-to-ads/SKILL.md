---
name: marketing-research-to-ads
description: "Static ads built on research into a product and its competitors, each with its own angle. Use for \"make ads for my product\", \"ad ideas\", \"ad angles\", \"research my competitors and make ads\", \"Meta ads\", \"static ads\", \"ads from these reviews\". Not for new headlines on an existing ad (marketing-headline-variants)."
---

# Ad Strategist

An ad works when it says a true reason to buy that the buyer already cares about. Research first, then design.

## Gather

- The product: a photo, a page or an ad the user already runs. If they give a page and you can read it, take the facts from it and show what you took. Otherwise ask them to paste the facts.
- The competitors: the ones the user names, or the closest products you can find. Note how they sell: their headlines, claims, colours and what they all leave out.
- Anything else they have, such as reviews or survey answers.
- Where the ads run. Default to 9:16 for Stories and Reels; use 4:5 or 1:1 for the feed.

## Find the angles

Write five angles that do not overlap, such as the main benefit or flavour, a moment of use, a pairing, a treat and a plain call to action. For each one:

- Who it is for, and what they want.
- The headline, under eight words, and one short line under it.
- The proof: the fact it rests on. Say when an angle rests on thin evidence.

Compare only on facts the user can stand behind, and do not name a competitor unless the user asks.

## Make them

| Job | Model |
| --- | --- |
| With a product photo, the default | `edit_gpt_image_2_5_image` |
| No photo | `generate_gpt_image_2_5_image` |

Keep one system across the set: a big bold headline at the top, the short line under it, and a real photograph below. Give each ad its own background colour. Tell the model to keep the product exactly as in the photo, and quote every word that appears on the ad.

## Steps

1. Show the five angles, the exact words and the total price, and wait for a yes.
2. Make the ads. Read the words in each result, since image models sometimes misspell, and check that the product matches the photo. Redo only what is wrong.
3. Deliver the links labelled by angle, and suggest testing them against the same audience and offer. For more headlines on a winner, use the `marketing-headline-variants` skill.

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
