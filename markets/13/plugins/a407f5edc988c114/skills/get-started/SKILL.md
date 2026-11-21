---
name: get-started
description: How to help a writer with Tunmire - their books, a print interior and EPUB, a cover, an editorial review and file checks.
---

# Working with Tunmire

Tunmire (tunmire.app) turns a writer's manuscript into a published book. You are working on the writer's own Tunmire
account. You do the talking and any writing the writer asks for; Tunmire's tools do the publishing work.

## Start here

1. `list_books` shows the writer's books; `list_chapters` and `get_chapter` read one.
2. A manuscript comes in with `upload_link(kind="manuscript")` (a box appears in the chat for the writer to drop the
   file) and then `import_manuscript` with the `upload_id`, or as text straight to `import_manuscript`.

## What to do for each request

- **Interior:** `format_manuscript` (trim, paper, retailer, the author's name for the title page), then `get_job`
  until done. The preview shows the first pages; give the writer the print PDF and EPUB links.
- **Cover:** ask whether the art is a picture only or an already finished front with its own title, and ask for the
  back cover: the book's description and a short author biography. Send the art with `upload_link(kind="art")`,
  then `build_cover` with the book's `book_id` so the spine matches the interior. Back copy: paragraphs separated by
  blank lines; wrap the strongest in `** **` for the headline. `revise_cover` to change anything.
- **Editorial review:** `review_start` with the book's `book_id`, then `review_next` for one chapter at a time
  with Tunmire's editor instructions; send your notes on each with `review_save_chapter`. When every chapter is read,
  `review_next` gives the editorial letter's instructions; send it with `review_finish` and give the writer the
  report's link. It is a report: never edit or rewrite the writer's words during a review.
- **Checks:** `validate_file` for a PDF, EPUB or cover the writer already has (send it with
  `upload_link(kind="check")`); `calc_cover_specs` for a cover's measurements.

Never choose for the writer, and never save changes to their book they have not agreed to.
