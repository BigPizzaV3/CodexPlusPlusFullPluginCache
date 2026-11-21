---
name: pixly-change-one-thing
description: Change exactly one thing in a photo with Pixly and keep everything else as it is — recolor a sofa, remove a car, fix the words on a sign, swap a lamp. Works on the user's own photo or on a Pixly result. Use when the user asks to change, remove, replace or recolor something specific in a photo.
---

# Change one thing

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Check the account first

Call `get_credit_balance`. An edit uses 1 credit. If `canUseCredits` is false or there are no credits, say in one sentence that this needs a Pixly plan with credits (plans are described at https://pixly.app/pricing) and stop.

## 2. What to change

- No photo → ask them to attach it. A Pixly result from this chat needs no file: pass its `resultPaths` entry as `r2Path`.
- No change named → ask what should change, in one sentence.
- Several changes → do them one per call, in the order they gave; each call starts from the previous result.
- If it's unclear where in the photo (two sofas, several signs), suggest Pixly Studio (`open_studio`), where they can brush over the exact area.

## 3. Run it

Call `edit_staged_photo` with the photo and `customInstructions` = the change in the user's own words — don't add style or mood words, and don't describe the rest of the photo. If the photo is a staged Pixly result, `sourceJobId` keeps its style.

It quotes first: tell them the cost in one line; they tap the card's button or say yes (then call again with the `confirmationCode`).

## 4. Finish

The card shows the result with a before/after slider; don't describe it again. At most one line: offer another change or a video of the room. Never show job ids or model names.
