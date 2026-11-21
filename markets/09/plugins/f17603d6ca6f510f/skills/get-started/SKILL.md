---
name: get-started
description: Connect MasterKi and save flashcards from a ChatGPT conversation for spaced-repetition review.
---

# Get started with MasterKi

MasterKi saves flashcards from this chat into the user's MasterKi inbox. Cards stay as drafts until they open the MasterKi app, review them, and pick a deck.

## Connect

1. Ask the user to connect MasterKi if it is not already connected.
2. They sign in with their MasterKi email and password, or enter a pairing code from MasterKi → Settings → Connect MasterKi to AI apps.
3. After connect succeeds, use `add_flashcards` to save cards.

## Saving cards

- Prefer clear front/back pairs (vocabulary, facts, Q&A).
- At most 50 cards per tool call; split larger sets across multiple calls.
- Optional `deck_name` is a hint only; the user confirms the deck in the app.
- Never claim you can read, edit, or delete existing MasterKi decks — this connector only adds new inbox cards.
- Do not mention MasterKi subscription plans or upsells.
