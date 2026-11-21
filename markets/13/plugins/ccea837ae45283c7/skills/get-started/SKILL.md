---
name: get-started
description: Set up OpenPrefs for a user who has just connected it, and explain how ChatGPT keeps and uses their preferences there.
---

# Getting started with OpenPrefs

OpenPrefs keeps the user's preferences, such as diet, usual orders, travel seats, budgets and house rules, as exact settings grouped into spaces. The user chose, when connecting, which spaces ChatGPT may read or change.

When the user has just connected OpenPrefs or asks how to use it:

1. Tell them in a sentence or two what OpenPrefs does: it remembers their preferences in one place they control, and any assistant they connect can use them.
2. Ask whether they would like ChatGPT to use OpenPrefs for their preferences from now on: looking a preference up with `search_preferences` before making a choice for them, and saving a preference they state with `define_preference` or `set_preferences`. If they agree, remember that choice for later conversations.
3. Offer to save two or three preferences now. Ask, for example, about dietary needs, a usual coffee order, or a preferred seat when flying. Save only what the user states; never guess a value.
4. Tell them they can see, edit and undo every change at https://openprefs.ai, and change what ChatGPT may access there on the Agents page.

Guidelines:

- Search before creating, so a preference that already exists is updated rather than duplicated.
- Give each new preference a key in a fitting space, such as `food.diet` or `travel.seat`, and a description that says how to act on it.
- If a tool answers that a change is pending, tell the user it waits for their approval in OpenPrefs.
- Delete a preference or remove list items only when the user asks for that specific change.
