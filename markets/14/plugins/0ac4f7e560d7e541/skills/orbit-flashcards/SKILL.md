---
name: orbit-flashcards
description: Create and maintain private flashcards in the signed-in user's Orbit account.
---

# Orbit flashcards

Use the Orbit MCP tools for the signed-in user's hosted library. A deck is a named collection of cards. Each card holds exactly one flashcard: one question and its answer. If the user asks for several flashcards, create a separate card for each question and answer; never put multiple flashcards inside one card. Keep questions concise and answers complete. When the user provides study notes or textbook pages, preserve their wording and topic order, and avoid adding unsupported facts. For a long answer, use a short numbered list.

Before saving any card, call `list_decks` and inspect the user's current deck names. Reuse an existing deck when its subject clearly fits the new cards, even if the user did not mention the deck. For example, biology cards belong in an existing Biology deck. Create a deck when the user explicitly asks for a new one or no current deck fits. Name a new deck for its subject in a short, simple form such as `Anatomy`, with initial capitals; do not use verbose labels such as `Anatomy Flashcards for My Exam` unless the user requested that name.

If more than one deck could fit, or the intended destination is unclear, ask the user to choose during this conversation and wait before saving. Show the current deck names and an option to create a new deck. If `choose_deck` is available, you may use its picker; otherwise ask in chat. Do not call an unavailable tool. Do not wait until after creating cards to resolve the destination. After the choice, continue the same flashcard task.

Deck and card IDs are for internal tool calls only. Never print IDs in the user-facing reply. Say the deck name, how many cards were saved, and show the flashcard content when useful. Read existing cards before editing or deleting so you use the correct internal card ID.

After creating or editing cards, read them back to verify the saved content. Use `get_card_status` and `get_due_cards` to answer study status questions. Record a review only when the user has supplied an actual recall grade. Delete a card only when the user explicitly requests it.

Do not claim that local desktop cards or review progress are synced unless the app shows that a sync has completed.
