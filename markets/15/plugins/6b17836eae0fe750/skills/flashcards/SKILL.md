---
name: flashcards
description: Create flashcards from study material (photos, worksheets, notes, vocabulary lists, PDFs) or a topic and save them to the user's Memro account. Use when the user asks for flashcards, vocabulary cards, "Karteikarten" or "Vokabelkarten", or wants to add cards to one of their Memro sets.
---

# Flashcards with Memro

Use this skill when the user wants flashcards from their material or about a topic, or wants to add cards to an existing Memro set. Reply in the user's language.

## Workflow

1. Make sure you have the material. If the user only says "make flashcards" without any material or topic, ask for it in one short message.
2. Read Memro's current card guidelines with the `get_flashcard_guidelines` tool and follow them.
3. Only ask about options (number of cards, language or vocabulary direction, length, hints) when they are unclear. Ask at most three short questions in a single message, each with a suggested default. If the request already makes everything clear, start right away.
4. Save the cards with `create_flashcard_set`. Send at most 60 cards per call; for more, save the first 60 and append the rest to the same set with `add_flashcards` using the returned `set_id`.
5. To add cards to an existing set, find it with `list_flashcard_sets`. If several sets could match, ask which one. Then use `add_flashcards`.
6. Answer briefly with the set title, the number of saved cards and the link from the tool result. Do not repeat all cards in the chat.

## Card quality

- One fact, term or question per card. No duplicates. Do not invent content that is not in the material; leave out anything unreadable.
- Vocabulary: foreign language on the front, the user's language on the back unless they ask otherwise. Set fitting side labels, such as "Spanish" and "German".
- Keep facts and terms short; use two or three sentences only for connections and processes.

## Limits

The Memro tools can only create sets, append cards to the user's own sets and list set titles. They cannot delete or edit cards, read learning progress or account data, or access other people's sets. If the user asks for that, explain it briefly and point them to the Memro app at https://memro.link.
