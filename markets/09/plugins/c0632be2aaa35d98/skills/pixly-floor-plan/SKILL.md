---
name: pixly-floor-plan
description: Make a clean 2D floor plan with Pixly from the user's description of the rooms or from a hand sketch or brochure plan (free), then optionally a furnished 3D render of it. Use when the user asks for a floor plan, layout drawing or plan of a property.
---

# Floor plan

The user's own instructions always come first. Everything below is a default.

## How to ask, and what to report

- Questions: when ChatGPT offers its `ask_user_input` tool, ask through it — every question of the round at once, each with fixed choices (and the recommended one first); otherwise one short chat message. Never more than one round.

## 1. Start

The 2D plan is free, so there is nothing to check first.

## 2. Get the layout

- A sketch, brochure page or blueprint attached → read it yourself: every room as a rectangle in metres (or feet, if the plan uses feet), with doors and windows.
- A description → turn it into rooms with sizes. If a size or how two rooms connect is missing, ask once for everything missing in one message, with your best guess filled in, so they can just say yes.
- Never invent rooms they didn't mention.

## 3. Draw it

Call `draw_floor_plan` with the layout. If it answers with problems (overlapping rooms, a door between rooms that don't touch), fix exactly those and call again. To change a plan later, call again with its `planId` and the whole updated layout.

## 4. Optional: a furnished 3D view

Offer it in one line. If they want it, call `render_floor_plan` with the plan image (`look`: furnished, or isometric if they ask for 3D/isometric). It uses credits and quotes first: before running it, call `get_credit_balance`; if there is no plan or no credits, say that plans are described at https://pixly.app/pricing and stop. Otherwise tell them the cost in one line; they tap the card's button or say yes (then call again with the `confirmationCode`).

## 5. Finish

The card shows the plan; it can be fine-tuned in Pixly's floor plan editor. Never show internal ids or model names.
