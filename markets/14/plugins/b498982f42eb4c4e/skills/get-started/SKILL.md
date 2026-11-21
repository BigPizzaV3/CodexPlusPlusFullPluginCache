---
name: papergarden-get-started
description: Make a printed hardcover picture book with papergarden. Use when the user wants a picture book, children's book or storybook made or printed.
---

# Making a book with papergarden

1. Call `get_guide` (topic "all") once. It has the page geometry, the workflow and the taste rules.
2. Plan the story with the user: who it is for, what happens, names, the look.
3. `create_book`, then put the text on its pages with `add_layers` (all pages in one call) and `show_book` so the user can read it.
4. When the user is happy with the text, draw each picture with your image tool and add it with `add_image`.
5. Place full-page pictures with `add_scenes` and other pictures with `add_layers` (a few spreads per call). Change what's there with `update_layers`. Every edit sends `baseVersion`.
6. Fix every print error from the results. `render` shows how pages will print.
7. When `printReady` is true, the user can order: `create_order`, then `update_order`
   with email, address and shipping. Give the user the payment link; they pay on papergarden.ai.

Rules that always hold:
- No sexual content and no graphic gore. Dark or scary stories are fine. Asked for either: say so and offer a version without it.
- papergarden can't delete a book. Asked to delete one: say so. Never empty a book with `delete_pages` or `delete_layers` to imitate deleting it. Removing a page or picture the user wants gone while editing is fine. Every version is kept; `restore_version` brings one back.
- Payment happens only on papergarden.ai's checkout page: never take card details in the chat or pass them anywhere; give the order's `checkoutUrl`.
- A view link (papergarden.ai/b/...) is read-only; nothing edits a book through it. Offer a new book (or `list_books` for the user's own).
- One picture per page; no pictures across a spread.
