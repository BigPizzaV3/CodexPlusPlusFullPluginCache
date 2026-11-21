---
name: custom-tarot-deck
description: Make a personal 22-card Major Arcana tarot deck with Kinarcana, with the user, a partner, friends or pets as the figures, each card restaged from the 1909 composition by ChatGPT's image generation and framed with its numeral and name. Use when the user wants custom or personalized tarot cards, a tarot card of themselves or from a photo, or a tarot deck as a gift.
---

Use this skill when the user wants their own tarot deck. The user's explicit instructions always come first.

Kinarcana keeps the user's tarot decks (up to 5) under their ChatGPT account. A deck holds the 22 Major Arcana in the 1909 order (VIII Strength, XI Justice); each card shows a gold emblem until the user replaces it with a picture.

## Flow

1. `start_deck` creates or returns the deck; `set_deck_title` changes the title on the title card. `show_deck` shows all 22 cards and which ones still show emblems.
2. For each card the user wants, `get_card_brief` returns the card's 1909 composition restaged with every figure fully clothed, plus the picture rules: portrait 2:3, no words or numbers in the picture, one style for the whole deck, and a face reference only for the user or someone who agreed to be on the card.
3. ChatGPT's image generation makes the picture from that brief, the look the user asked for and any photo they attached. `add_card_art` then frames it with the numeral and the name. `replace_card_art` swaps a picture; `remove_card_art` puts the emblem back.
4. For a card of the day use the daily-tarot-card skill.

## Scope

- Major Arcana only: 22 cards plus a title card, no Minor Arcana.
- Pictures that aren't fully clothed, or are suggestive or graphic, are refused and not kept.
- `delete_my_data` deletes the user's decks and pictures when they ask.
