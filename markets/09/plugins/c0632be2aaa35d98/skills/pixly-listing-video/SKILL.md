---
name: pixly-listing-video
description: Make a short property video with Pixly — a camera move from one listing photo (drone orbit, push-in, flyover…), a walkthrough through 2 to 4 room photos, or a video that travels from one photo to another. Use when the user asks for a video, drone shot, camera move, walkthrough, tour or flythrough of a property photo.
---

# Listing video

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Check the account first

Call `get_credit_balance`, before asking anything.
If `canUseCredits` is false, or `creditsRemaining` is clearly too low (a 5-second video uses about 8 credits, a walkthrough about 5 per move between rooms), say in one sentence that this needs a Pixly plan with credits and that plans are described at https://pixly.app/pricing. Stop. Never offer to buy anything and never give a checkout link.

## 2. Pick the tool

- One photo and a video wish → `cinematic_motion`.
- Two to four photos of different rooms, or "walkthrough / tour / flythrough" → `flythrough_video`, photos in walking order.
- A start photo and an end photo → `photo_to_video`.
- Empty room becoming furnished, a renovation, day to dusk as a reveal → use the pixly-empty-room-reveal skill instead.

## 3. Ask once, only what is missing

- No photo attached → ask the user to attach it, in one sentence. Nothing else.
- A walkthrough with no order given → say the order you will use and continue; they can correct it.
- A walkthrough is a whole property: in the same message, ask which property it is, then `create_listing` (title = their answer, none if they skip) and pass its `listingId` to `flythrough_video`. If they name a property that has a folder (`list_listings`), use that one. A single photo needs no folder.
- Never ask about model, resolution, frame rate, prompt or length.

Defaults: 5 seconds; the photo's own shape (`format: "original"`); 9:16 only when they say Reels, TikTok, Shorts or vertical; 10 seconds only when they ask.

Camera move (`cameraMove`) when they didn't name one: an exterior or aerial photo → `drone-orbit`; an interior → `zoom` (a slow push-in). Named moves: push in → `zoom`, pull back → `pull-back`, orbit → `orbit` inside or `drone-orbit` outside, rise / crane → `crane-up`, pan → `pan`, fly over the roof → `flyover`, climb away from the house → `aerial`, walk → `handheld`.

## 4. Run it

Paid tools quote first: the first call starts nothing and returns the settings and cost, and the Pixly card shows them with a button. Tell the user the cost in one short line. If they tap the button, the card runs it — don't call again. If they say yes in the chat, call the same tool again with the quote's `confirmationCode`. One quote runs once.

Videos take 2 to 5 minutes. Call `get_job` with the job id until it is completed (each call waits up to 40 seconds). If you stop before that, say it is still rendering and will be in their Pixly library at https://pixly.app/app.

## 5. Finish

The Pixly card shows the video, what it cost and the next steps — don't describe the video or list those steps again. At most one line: offer another camera move or a vertical version. Never show job ids, model names or internal steps.
