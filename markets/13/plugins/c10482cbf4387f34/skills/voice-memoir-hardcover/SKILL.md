---
name: voice-memoir-hardcover
description: Preview a Voxbind voice memoir page by page and order it as a printed 6 × 9 inch hardcover whose chapter QR codes play the original recordings, then follow the order until it arrives. Use when a user in the United States or Canada wants to see or print the memoir book, order copies for the family as a gift or keepsake, or asks where their book is. Printed books are offered only to users in the United States and Canada, where they ship; elsewhere the memoir, its transcripts and listening pages are the whole product.
---

Use this skill when a voice memoir is ready to become a book. The user's explicit instructions always come first.

## Flow

1. preview_book lays out the pages and says whether the book is ready to order, listing anything to fix first (for example notes in a script the book can't print yet, or too few pages).
2. order_book returns a checkout link on voxbind.ambientapp.ai, where the delivery address, number of copies and payment are entered. Addresses and card details stay on that page and out of the chat.
3. get_order_status says whether the book is paid, printed, shipped or delivered, with tracking.

## Scope

- Books have 24 to 320 pages and ship only to the United States and Canada. For users anywhere else, preview_book, order_book and get_order_status reply that printed books aren't available in their country; the memoir, transcripts and listening pages stay theirs to use.
- Notes in scripts the book can't print yet (such as Chinese, Japanese, Korean, Arabic or Hebrew) stay in the memoir and play on their listening pages, without being printed.
- Each chapter's QR code opens a listening page that plays the original recordings; Voxbind keeps and plays them as recorded.
- Nothing is charged in ChatGPT; the cost appears on the checkout page.
- If the memoir has no chapters yet, use the voice-notes-chapters skill first.
