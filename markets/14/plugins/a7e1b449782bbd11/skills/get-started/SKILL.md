---
name: get-started
description: Set up Groceriva after it is installed. Confirms which Groceriva account is connected, explains what Groceriva can do with shopping lists, recipes, meal plans and the pantry, and helps the user make or fill a first shopping list.
---

# Get started with Groceriva

Use this when the user has just added Groceriva, or asks how to start using it.

## 1. Check the connection

Call `get_account_profile` (it takes no arguments).

- If it returns a profile, tell the user which account is connected, using the name and email it returned.
- If it fails because the user is not signed in, tell them to connect their Groceriva account when ChatGPT asks, signing in with the
  account they use in the Groceriva app (or creating a new one). Do not ask for their password in the chat.

## 2. Show what is already there

Call `list_shopping_lists`. Then summarise in one or two sentences: how many lists they have and what is left to buy on each.
If they have no lists yet, say so.

## 3. Explain what they can ask

Keep it short. Groceriva can:

- add groceries to a shopping list (several at once), tick them off, change amounts or remove them;
- save a recipe from the conversation, and find saved recipes by name or ingredient;
- add the missing ingredients of a saved recipe to a list, scaled to the number of servings;
- plan saved recipes on days of the week, and turn the plan into one combined shopping list;
- show the pantry and find saved recipes that can be cooked with it (only on plans that include the pantry).

Everything happens in the user's own Groceriva account. Shopping lists sync live; open or refresh the app's recipe,
meal-plan and pantry screens to see changes there.

## 4. Offer a first step

Ask one question, for example: "Shall I start a shopping list for this week? Tell me a few things you need."

- If they name items and have no list, call `create_shopping_list` with the name they choose (suggest "Shopping" if they have no
  preference), then `add_items_to_list` with all the items in a single call.
- If they already have a list, ask which one to use before adding.

Do not create, change or delete anything the user did not ask for.
