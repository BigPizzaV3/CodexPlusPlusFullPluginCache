---
name: group-card
description: Start a Penround group card that coworkers, classmates or family sign on a web page without ChatGPT, for a farewell or leaving card, birthday, retirement, wedding, new baby, sympathy, get-well, the holidays or a thank-you, and approve or hide every message before the recipient sees it. Use when someone wants a group card, leaving card, farewell card or group ecard that several people sign, or asks who has signed a card they started. Not for a card only the user writes, a card image or an e-signature.
---

Use this skill when the user wants several people to sign one card for someone. The user's explicit instructions always come first.

## Flow

1. `list_cards` shows the cards the user already started. `create_card` starts a new one with the occasion, the recipient's name and, if given, when signing closes. Sympathy and get-well cards use the occasion `other`, with the title the user wants. It returns the sign link to share in a team chat, a class group or an email.
2. People sign from any browser, without an account or ChatGPT. Each message waits for the user's approval; offensive words are refused and a safety check holds anything questionable.
3. `get_card` says who has signed and what is waiting, by message number. `approve_messages` and `hide_messages` act on the numbers the user names; if a signer has more than one message, ask which number. `add_messages` adds the user's own message or messages pasted from elsewhere.
4. `update_card` changes the title, from line, note, colour theme, cover photo or deadline, or stops and restarts signing.
5. When the card is ready, offer to send it (the schedule-delivery skill). For users in the United States and Canada, the messages can also become a printed keepsake book (the keepsake-book skill).

`show_sample_card` opens a sample card for someone deciding whether to start.

## Scope

- One recipient per card. Messages are text only, up to 600 characters.
- Cards work in every country; the printed book is offered only in the United States and Canada.
- Message text shows in the card view, not in tool results; summarise counts and names, never invent messages.
- `delete_card` only when the user clearly asks to delete a card.
