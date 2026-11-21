---
name: recipes-from-relatives
description: Collect recipe cards from aunts, cousins and other relatives into one Stirloom family cookbook through a private link, with no account, and approve or type up each card they send. Use when the user wants family members to add their own recipes or recipe-card photos to a shared cookbook, or a relative sent a card as a photo only.
---

Use this skill when several relatives should contribute to one family cookbook. The user's explicit instructions always come first.

## Flow

1. `get_invite_link` returns the book's private link and a short message the user can forward in a family chat or email. Relatives open it in any browser, without an account, and add a card with a photo and, if they like, the typed recipe.
2. Every card a relative adds waits for the user's approval; `get_book` lists cards waiting and cards marked "needs typing".
3. When a relative sent only a photo and the user shares that photo in the chat, `transcribe_card` fills in the recipe from a faithful transcription that keeps the card's wording and spelling.
4. `update_recipe` fixes text the user wants changed; the earlier text stays in the book's history.

## Scope

- Only the book's owner approves cards. Relatives never see each other's unapproved cards.
- If the user has no book yet, start one with the family-cookbook skill first.
