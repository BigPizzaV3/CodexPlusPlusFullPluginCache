---
name: printed-tarot-deck
description: Order a Kinarcana tarot deck printed as 23 cards (22 Major Arcana and a title card) in a tarot box, through checkout on kinarcana.ambientapp.ai, and follow the order until it arrives; printed decks ship only to the United States. Use when a user in the United States wants their custom tarot deck printed, as a keepsake or a gift, or asks where their printed deck is.
---

Use this skill when a Kinarcana deck is ready to print. The user's explicit instructions always come first.

## Flow

1. `show_deck` shows which cards still carry the gold emblem; the deck prints as it is, so offer to finish any card the user cares about first.
2. `order_printed_deck` returns the checkout link on kinarcana.ambientapp.ai, where the user enters the delivery address and pays. Addresses and card details stay on that page and out of the chat.
3. `get_order_status` says whether the deck is paid, printed or shipped, with tracking.

## Scope

- Printed decks are offered and ship only in the United States. For a user anywhere else, `order_printed_deck` and `get_order_status` say printed decks aren't available in their country, and the deck and the daily card work the same.
- Nothing is charged in ChatGPT; the cost appears on the checkout page.
- If the user has no deck yet, start one with the custom-tarot-deck skill.
