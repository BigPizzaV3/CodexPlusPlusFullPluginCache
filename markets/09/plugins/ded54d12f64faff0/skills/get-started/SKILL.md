---
name: get-started
description: Introduce MeltFlex and run a first interior redesign. Use when someone has just connected MeltFlex, asks what it can do, or wants to try it without a specific plan.
---

# Get started with MeltFlex

MeltFlex redesigns real rooms from a photo. The walls, windows and doors stay where they are; the style, furniture, materials and colours change.

## What to offer

- **Redesign a room**: a photo plus a style ("warm Japandi", "dark moody library").
- **Furnish an empty room**: virtual staging for listings and new builds.
- **Place an exact product**: a photo of a real sofa, rug or tile placed into the room.
- **Walkthrough video**: a 4 or 8 second cinematic clip from any render.
- **3D model**: a photo of one furniture piece turned into a GLB.

## First run

1. Ask for a room photo if none was shared. Never invent a room.
2. If the user has no look in mind, call `browse_presets` for the matching tool (interior, kitchen, bathroom, exterior, garden…) so they can pick a style from pictures instead of answering questions.
3. Call `generate_interior` with the photo, the `tool` and `style` they picked, and `prompt` for any extra wishes. Without a preset, write `prompt` as one sentence.
4. After the render, offer the natural next step: another style, a walkthrough video, or placing a specific product.

## Credits

Every generation spends credits on the user's MeltFlex account. Call `get_credits` when the user asks what something costs or before a walkthrough or 3D model, and tell them the cost before spending it. Failed jobs are refunded automatically. Do not link to pricing or checkout pages in the chat.

## Design tools and presets

MeltFlex has a dedicated tool with its own style presets for each kind of space. Call `browse_presets` with no arguments to show them all as a picture gallery, or jump straight in with a slash command: /kitchen, /bathroom, /exterior, /garden, /walls, /floors, /stairs, /doors, /windows, /home-office, /closet, /coffee-shop, /restaurant. Browsing is free; only generating spends credits.
