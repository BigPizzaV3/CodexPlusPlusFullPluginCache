---
name: daily-tarot-card
description: Draw a tarot card of the day face down from the user's own Kinarcana deck, or from the emblem deck if they have none yet, and turn it over with its keywords and a question for reflection. Use when the user asks for a daily tarot card, a card of the day or a single card draw.
---

Use this skill when the user wants one tarot card for today. The user's explicit instructions always come first.

## Flow

1. `draw_daily_card` shows today's card face down, from the user's deck or the emblem deck. The same day returns the same card.
2. The card's name is in the result once the user turns it over or asks which card they drew.
3. Share its keywords and question as prompts for reflection. They are not predictions, and Kinarcana gives no advice on health, money, law or relationships.
4. If the user has no deck yet, offer to start one with the custom-tarot-deck skill so tomorrow's card shows them.

## Scope

- One card a day, from the Major Arcana only.
