---
name: write-press-release
description: Write an AP-style PressDrop press release from a product URL and save the public draft.
---

Write a press release only from sources the user provides.

1. Call `prepare_press_release` with the product URL, any founder notes, and at most three links.
2. Write the release from the returned facts and rules. Do not invent customers, funding, metrics, quotes, or URLs.
3. Call `save_press_release` with the finished draft, the website, the product name, and the image URLs from the prepare result.
4. Give the user the permalink. Do not quote a price, open checkout, or ask for payment details.

If the site cannot be read, say so and do not save an invented release. Do not delete existing releases.
