---
name: optisigns-setup
description: First-run setup for OptiSigns. Use right after the plugin is installed, or when the user says get started, set up, connect my OptiSigns account, or how do I begin with OptiSigns. Connects the account, takes a quick look at their screens, and drafts three starter prompts tailored to them.
---

# OptiSigns setup: first result fast

Goal: within a minute the user sends a real request, such as a sign for one of their own screens.
Keep everything before the starter prompts under about 120 words.

## 1. Connect (optional, one line)

Say: "Sign in to OptiSigns so I can publish to your screens. I can also design without it."

- If the account tools work, go to step 2.
- If a call fails because the user isn't signed in, the connector is turned off, or access is denied,
  explain the fix in one or two lines from [references/connect.md](references/connect.md), then carry on
  in design-only mode. Don't block on it.

## 2. Snapshot (signed in only)

Call each once:
1. `optisigns_me`: their name and teams. Greet them by first name. If they have several teams, ask
   which one to work in before going further.
2. `optisigns_screen_list`: how many screens, their names, which are online, what each is playing.

Read the screen names: they reveal the use case without a question ("Drive-Thru", "Lobby TV",
"Break Room", "Waiting Room"). Map them with [references/starter-prompts.md](references/starter-prompts.md).

No screens yet? Say they can try it on a laptop first (a Mac or Windows player app works as a test
screen; see the Help Center), and that once a screen shows its pairing code you can pair it here.
Continue with design.

## 3. Draft three starter prompts

Use what you already know about this user (role, company, industry, tone, tools they use) plus the
snapshot. Write three one-line prompts they could send right now to design a sign and publish it.

Each prompt names: **the screen** (a real one if signed in), **the audience**, **the content**, **the
look**. Prefer facts from their account over guesses. Mix: one quick static slide, one with a schedule,
one recurring or interactive idea.

If you know nothing about them, ask one question first: "What are your screens for?" Then draft.

Example (signed-in restaurant owner, screens "Front Counter" and "Drive-Thru"):
1. "Design a lunch-special slide for Front Counter: four items with prices, warm colors, and show it
   11:00–14:00 daily."
2. "Make a Drive-Thru sign announcing our new iced lavender latte, big photo, price, readable from the car."
3. "Every Monday, turn our specials sheet into a fresh menu slide for Front Counter."

## 4. Wait for their pick

Run nothing until the user picks or edits a prompt. Then go: `signage-design` (make it, show it, get
OK) → `optisigns-operate` (publish, schedule, assign with their confirmation). Tell them once: "Any
time, ask me what you should put up next and I'll look at your screens and the calendar."

## Rules

- No changes to the account during setup: reads only.
- Don't save anything to memory and don't infer sensitive traits; use only what the user has shared.
- House rules: [references/house-rules.md](references/house-rules.md).
