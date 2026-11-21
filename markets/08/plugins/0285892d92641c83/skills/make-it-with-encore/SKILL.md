---
name: make-it-with-encore
description: Use this when someone wants a finished, styled edit made from their own files and words in one of the Encore styles, such as a product drop, a travel film, a lyric or music video edit, a fit check lookbook, a car reveal, an anime hero opening, a talking clip cut like a trailer, captions for a talking clip, or an edit they love remade with them in it. Trigger on Encore, make it in this style, paste the edit, remake this edit with me, turn my footage into a travel film, launch edit for my product. Do not use it for a single new shot from a brief, for changing the look of one clip, or for other camera angles of one take.
---

# Make it with Encore

Encore makes a finished edit in one of its styles from the person's own photos, clips, song and words, on NOLGIA's servers. It keeps going after the chat moves on, and the result lands in their library and in Studio.

## When to trigger

Trigger on "make an Encore", "make me a product drop", "turn my trip footage into a travel film", "a lyric video from my song", "remake this edit with me in it", "caption my talking clip", or any Encore style by name.

Do not trigger for one new shot from a brief (use make-a-video), a new look on one clip (use grade-my-footage), a remake of one clip with a new subject or place (use remake-a-clip), or other camera angles of one take (use every-angle-from-one-take).

## Steps

1. Call `nolgia_encore_catalog` to show the styles. It takes no arguments. Where the host shows this server's cards, the styles appear on a card with posters and previews; say in one sentence what Encore does and let the person pick.
2. Call `nolgia_encore_style` with the chosen `preset` (and a `mode`, if the person picked one) for its form. Each mode says what it needs: photos, clips, a song, a saved character, words.
3. Gather what the form needs.
   - Files must be in the person's NOLGIA library. Use `nolgia_list_assets` to find them. Save files attached in this chat with `nolgia_add_chat_files`.
   - For the flagship's edit given as a direct link, use `nolgia_encore_link_clip`, only after the person says they made the clip or hold its rights.
   - Never invent the person's words. Ask for them, within the limits the form shows.
4. Price the form with `nolgia_encore_quote`. It prices a new run of one style and is free. Pass on every problem it names in its own words, fix them, and price again.
5. Ask the person to confirm the consent statement the form shows. It says that everyone in their files agreed to appear and that they hold the rights to the files. Also ask them to agree to the price. A style cut from their own footage often costs nothing; a generated one says its price and the retake reserve.
6. Only then call `nolgia_encore_start` with the same form, `consent` true and `agreed_credits` set to the quoted price. Nothing starts if the price moved, the balance is short or the form has a problem.
7. Check the run with `nolgia_encore_status` about every half minute while it runs, not in a tight loop. Where the host shows cards, the card refreshes itself.
8. When it finishes, the edit plays on the card with its compare file. Offer `nolgia_encore_download` for every file in one ZIP, and give the link exactly as returned.
9. If they ask to stop, confirm first, then call `nolgia_encore_cancel` and say what the result says about charges.

## Making shots of a finished run again

When a finished run's result lists a residual with a `redo` list (for example a sign or a logo in one shot of an Encore Travel film that reads wrong), those shots can be made again without making the whole run again.

1. Price it with `nolgia_encore_redo_quote`: the finished run's `run_id`, the shot ids from the residual's `redo` list as `items`, and, if the person has them, up to 3 library images of the logo or text as `vibe_marks`. It is free. Pass on any problem in its own words.
2. Only once the person has agreed to the price, call `nolgia_encore_redo_start` with the same `run_id`, `items` and `vibe_marks`, `consent` true and `agreed_credits` set to the quoted price. Every other shot of the finished run is kept as it is.

## For the flagship, "Paste the edit"

The flagship (preset `encore`) remakes an edit the person made or holds the rights to, with them in it.

1. Scan the edit first with `nolgia_encore_scan_edit`: the clip's library id as `reference`, and `consent` true only once the person has confirmed the consent statement. The scan is free and makes no edit. Check it with `nolgia_encore_status` until it finishes; the finished scan lists the edit's word slots.
2. Then price the remake with `nolgia_encore_quote`: preset `encore`, mode `remix` (or `exact` to keep the edit's own moves shot for shot), the finished scan's run id as `inputs.scan_id`, one subject (`subject_photos`, `character_id`, `product_photos` or `footage`), and the person's own words keyed by the scan's word ids. Start it with `nolgia_encore_start` as in the steps above.

## When to stop or decline

- A link to TikTok, Instagram, YouTube, X, Facebook, Vimeo or a similar platform: do not fetch it. Ask for a clip they made, attached here or uploaded to nolgia.ai.
- Files that show people who did not agree to appear, or a song or edit they do not hold the rights to: stop and say why.
- A real, named public figure as the subject: decline and offer their own photos or a saved character instead.
- The balance does not cover the run: say so and stop. Nothing starts.

Never name a model, and never promise a price the tool result does not show.
