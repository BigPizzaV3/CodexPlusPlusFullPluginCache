---
name: family-cookbook
description: Turn handwritten family recipe cards, a recipe box or a scanned binder into a family cookbook with Stirloom, each card's handwriting facing its typed recipe, printed as a hardcover in the United States and Canada. Use when someone wants to make a family cookbook or family recipe book, digitize or scan handwritten recipe cards into a book, or is looking for a cookbook gift or keepsake of a relative's cooking. Not for recipe ideas or meal plans.
---

Use this skill when the user wants a cookbook made from their family's recipe cards, for themselves or as a gift. The user's explicit instructions always come first.

## Flow

1. `list_books` shows whether the user already has a book; `create_book` starts one with a title and, if given, a subtitle and dedication.
2. The user shares photos or a scanned PDF of the cards. `add_recipe_cards` takes the files in `photos` and a faithful transcription of each card in `recipes`, keeping the cook's wording, spelling, amounts and units, with [?] for a word that cannot be read and only the ingredients and steps the card shows.
3. `get_book` says what is in the book, what still needs typing and what waits for approval. `update_recipe` corrects text already in the book; `remove_recipe` only when the user clearly asks.
4. For cards from relatives, use the recipes-from-relatives skill. `preview_book` lays out every page; in the United States and Canada the print-the-book skill orders the hardcover.

`show_sample_book` opens a finished sample cookbook for someone deciding whether to start.

## Scope

Stirloom makes one product, a family cookbook from recipe cards that can be previewed page by page in every country, up to 120 recipes. In the United States and Canada, where it ships, it can also be printed as an 8.5 × 11 inch hardcover once it has 6 recipes. It does not invent, improve or rewrite recipes.
