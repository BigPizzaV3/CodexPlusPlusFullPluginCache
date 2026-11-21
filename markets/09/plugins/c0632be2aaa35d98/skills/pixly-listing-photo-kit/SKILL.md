---
name: pixly-listing-photo-kit
description: Get a whole set of listing photos ready to publish with Pixly — straighten, brighten, a blue sky on exteriors, a green lawn, empty rooms staged — as one plan with one total and one confirmation. Use when the user shares several listing photos and asks to fix, improve, enhance or prepare them all.
---

# Listing photo kit

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Check the account first

Call `get_credit_balance`. If `canUseCredits` is false, say in one sentence that this needs a Pixly plan with credits (plans are described at https://pixly.app/pricing) and stop.

## 2. The property folder

Ask once, in the same message as anything else you need: "Which property is this?" Call `create_listing` with their answer as `title` (leave it out if they skip). If they name a property that already has a folder (`list_listings`), use that one. Pass its `listingId` to `plan_photos`.

## 3. Look at every photo

For each attached photo, decide what it needs — only what it clearly needs:
- leaning walls or a tilted horizon → `straighten_photo` (free)
- dark, flat or amateur → `enhance_photo`
- exterior with a grey or blown-out sky → `replace_sky`
- exterior with a patchy lawn → `replace_lawn`
- an empty room → `virtual_staging` (their default style unless they named one)
- clutter in a furnished room → `declutter_photo`
At most two steps per photo. A photo that already looks good gets nothing.

## 4. One plan, one total, one yes

Call `plan_photos` with the `listingId`, all the photos once and every step:
`{"listingId": "...", "photos": [<every photo, in order>], "steps": [{"tool": "straighten_photo", "photo": 1}, {"tool": "enhance_photo", "after": 0}, {"tool": "replace_sky", "photo": 2}]}`
— `photo` is the photo's number (from 1); `after` is the index (from 0) of an earlier step whose result this step works on. Leave every option out unless the user asked for it (a style for staging, say). It starts nothing: it returns the plan with each step's cost and the total, and the Pixly card shows it with one button.

Tell the user the plan in a short list (photo → what it gets) and the total in one line. If they change something, call `plan_photos` again with the new steps. If they tap the card's button, the card runs the whole plan. If they say yes in the chat, call `plan_photos` again with the plan's `confirmationCode`.

## 5. Wait for the results

The answer lists a job per step. Call `get_job` with `jobIds` (all of them at once) until every one is completed — each call waits up to 40 seconds. A failed step is not charged; say which one and offer to run just that step again.

## 6. Finish

Results are in their Pixly library at https://pixly.app/app. One or two lines: how many photos are ready. Don't describe each photo. Never show job ids or model names.
