---
name: pixly-setup
description: Set up Pixly right after installing it — check the account, choose the default interior style and video shape, and show what Pixly can do. Use when the user runs setup for Pixly or asks how to get started with Pixly.
---

# Pixly setup

The user's own instructions always come first. Setup runs nothing paid.

## 1. The account

Call `get_credit_balance`. Say in one line which plan they're on and how many credits they have. With no active plan, add that the free tools work without one (straighten, watermark, blur faces and plates, before-and-after images, floor plans) and that plans are described at https://pixly.app/pricing. Never offer to buy anything.

## 2. Two defaults, asked once

Call `get_pixly_settings`, then ask both at once — through ChatGPT's `ask_user_input` tool when it offers it (fixed choices, recommended first), otherwise in one short message:
- Default interior style for staging: their current one, or Modern minimal, Scandinavian, Japandi, Coastal — or "show me all" (open Pixly Studio with `open_studio`; all 61 styles are pictures there).
- Default video shape: the photo's own shape (recommended), 9:16 for Reels and TikTok, or 16:9.

Save only what they change with `update_pixly_settings`. If they skip, keep the current settings.

## 3. Show what Pixly does

In three short lines, suggest:
- "Attach a photo of the house and ask for a slow drone video."
- "Attach an empty room and ask to furnish it in a style you like."
- "Attach any photo and ask to change one thing — the rest stays as it is."

Then offer Pixly Studio (`open_studio`): the make box, camera-move examples and their library. Nothing in setup is charged.
