---
name: save-your-card
description: "Save the hands from the user's own American mahjong card so Jokerly checks against them. Use when the user types or photographs the lines on the card their table plays this year, wants to see the hands Jokerly uses, or wants to remove saved hands."
---

Use this skill when the user wants Jokerly to check against the card their table plays. The user's explicit instructions always come first.

## Flow

1. `save_card_hands` adds hands to this user's private card, exactly as the user's card or message shows them, in Jokerly notation: the line's groups separated by spaces, 14 tiles, with a suit tag a, b or c after each group of numbers or D (for example FF 2222a 4444b 6666c). Lines that don't parse come back with the problem, and the rest are saved.
2. `show_card_hands` lists the saved hands with a # each (`hand_source: mine`), or Jokerly's practice hands (`hand_source: practice`).
3. `remove_card_hands` removes hands by #, or the whole saved card.
4. Until the user saves hands, `check_rack` and `suggest_charleston_pass` use Jokerly's practice hands and say so.

## Scope

- Jokerly ships no league's card; the hands come from the user's own card.
- Saved hands are kept under ChatGPT's anonymous ID for this user, shared with nobody, and deleted on request or after 12 months without use.
