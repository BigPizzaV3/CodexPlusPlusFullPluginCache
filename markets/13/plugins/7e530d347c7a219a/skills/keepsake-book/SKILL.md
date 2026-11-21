---
name: keepsake-book
description: Turn the approved messages of a Penround group card into a printed hardcover keepsake book, one message per page with the recipient's name on the cover, and track the order until it arrives. Use when the user wants to print or keep the messages from a group card, asks what the keepsake book looks like, wants to order it as a gift, or asks whether their book has shipped. The printed book is offered only to users in the United States and Canada, where it ships.
---

Use this skill when the user wants the messages from a group card as a printed book. The user's explicit instructions always come first.

## Flow

1. The book is made from a card's approved messages. If the user has no card yet, start one first with the group-card skill.
2. `preview_keepsake_book` lays out the square hardcover page by page and lists anything to fix first, such as too few approved messages or a script the book cannot print yet. Show the user what it reports before ordering.
3. `order_keepsake_book` saves the approved messages as they are now and returns a secure checkout link on penround.ambientapp.ai. The user enters the delivery address (it can be the recipient's) and pays on that page. Never ask for an address or card details in the chat.
4. `get_order_status` answers whether the book is paid, printed, shipped or delivered, with the tracking link.

## Scope

- A book needs at least 3 approved messages and holds up to 150, one per page, plus a page of everyone who signed.
- The printed book is offered only to users in the United States and Canada, where it ships. Elsewhere the book tools reply that printed keepsake books aren't available in the user's country; cards themselves work in every country and can be signed and sent anywhere.
- The book cannot yet print Chinese, Japanese, Korean, Arabic, Hebrew or Devanagari script; the preview names any message that needs it.
- Nothing is charged in ChatGPT. The cost is shown in the preview and on the checkout page.
