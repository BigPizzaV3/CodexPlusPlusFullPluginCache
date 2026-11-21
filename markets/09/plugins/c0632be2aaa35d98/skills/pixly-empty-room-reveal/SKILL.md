---
name: pixly-empty-room-reveal
description: Furnish an empty room with Pixly's virtual staging in any of 61 interior styles, then make a before-and-after video of it — the free one in the result card, or an AI reveal video. Use when the user wants an empty room furnished and shown as a reveal, transformation or before-and-after video.
---

# Empty room to furnished reveal

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Check the account first

Call `get_credit_balance`. Staging uses 1 credit; the AI reveal video about 5 more. If `canUseCredits` is false or there are no credits, say in one sentence that this needs a Pixly plan with credits (plans are described at https://pixly.app/pricing) and stop. Never offer to buy anything.

## 2. Ask once, only what is missing

One short round: the photo and the style together. Don't ask about the video — the card has a free Before & after video button (step 4).

- No photo → ask them to attach the empty room.
- No style named → ask once, as buttons (the form shows at most four, and its own "describe something else" line takes any of Pixly's 61 styles): Modern Minimal (recommended), Scandinavian, Coastal, "Show all 61 styles in Pixly Studio". Pass the style id (`modern-minimal`, `scandinavian`, `coastal`, or the one they type); if they skip, leave `style` out and their default style from Pixly settings applies. If they choose to see all styles, call `open_studio` — all 61 are pictures there.
- Leave `customInstructions` empty unless they asked for something specific (a reading chair, no rug). Pixly writes its own prompts.

## 3. Stage the room

Call `virtual_staging` with the photo. It quotes first: tell them the cost in one line; they tap the card's button or say yes (then call again with the `confirmationCode`).

## 4. The before-and-after video

When the staged room is ready:
- The Pixly card has a free before-and-after video right on it (transitions, shape, length, made on their device). Mention it in one line — that's usually all they need.
- If they want the AI reveal (furniture appearing in the room), call `before_after_reel` with `beforeR2Path` = the original photo and `afterR2Path` = the staged result's `resultPaths` entry. It quotes first too. Then `get_job` until completed (2 to 5 minutes).

## 5. Finish

Don't describe the room or the video — the card shows them. Never show job ids or model names.
