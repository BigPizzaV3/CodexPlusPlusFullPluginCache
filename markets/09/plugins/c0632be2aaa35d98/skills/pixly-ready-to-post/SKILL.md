---
name: pixly-ready-to-post
description: Get a set of property photos ready to post for free with Pixly — straighten leaning walls, blur people's faces and car licence plates, and add the agent's watermark (text and/or logo). Use when the user wants photos ready to post or publish, watermarked, privacy-safe, or cleaned up for free.
---

# Ready to post, free

The user's own instructions always come first. Everything below is a default.

All three tools are free (no credits), so nothing needs a confirmation and no plan is needed.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. The photos

Up to 10. Attached in the chat, or from their Pixly library (`list_library`, or a property folder via `list_listings`). None yet → ask them to attach the photos. Nothing else.

## 2. Ask once, only what is missing

- The watermark: their name, agency or phone as text, and/or the logo saved on their Pixly account (`useLogo`). If they have said nothing, ask once; offer "logo only" when one is saved. Default position bottom-right, size small.
- Skip any step they don't want (e.g. no blur for interior shots with nobody in them).

## 3. Run, in this order

1. `straighten_photo` on each photo, one call per photo. If it says a photo is already straight, keep the original.
2. `blur_faces_plates` on the straightened photos that show a street, cars or people (up to 5 per call, `photos` with each result's `r2Path`). Skip interiors with nobody in them. It says so when it finds nothing — keep those as they are.
3. `watermark_photos` on the whole set (up to 10 per call), using the latest version of each photo.

Pass results on by `r2Path` — the user never has to attach anything twice.

## 4. Finish

One or two lines: how many photos are ready and that they're saved in their Pixly library (https://pixly.app/app). Offer, in one line, a listing description or a staged version of an empty room. Never show job ids or model names.
