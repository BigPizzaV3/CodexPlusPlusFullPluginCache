---
name: print-the-book
description: Order the printed hardcover of a Stirloom family cookbook in the United States and Canada, where it ships, through a secure checkout on stirloom.ambientapp.ai, and track it until it arrives. Use when a user in the United States or Canada wants printed copies, for example as gifts, or asks whether their book has shipped. Elsewhere the online cookbook and its page preview are the whole product.
---

Use this skill when the user wants to order the printed hardcover (United States and Canada only). The user's explicit instructions always come first.

## Flow

1. `preview_book` lays out the book page by page and lists anything to fix first, such as blurry photos or cards that still need typing. Walk the user through those fixes before ordering.
2. `start_order` saves the current version of the book for printing and returns a secure checkout link on stirloom.ambientapp.ai. The user enters the delivery address and pays on that page. One order has up to 10 copies to one address. Never ask for an address or card details in the chat.
3. `get_order_status` answers whether the book is paid, printed, shipped or delivered, with the tracking link and expected dates.

## Scope

- The printed book is offered only to users in the United States and Canada, where it ships. Elsewhere `preview_book` still lays out every page, and `start_order` and `get_order_status` reply that printed cookbooks aren't available in the user's country.
- Nothing is charged in ChatGPT; in the United States and Canada the cost appears in the preview and on the checkout page.
- `delete_book` only when the user clearly asks; orders already paid are still printed.
