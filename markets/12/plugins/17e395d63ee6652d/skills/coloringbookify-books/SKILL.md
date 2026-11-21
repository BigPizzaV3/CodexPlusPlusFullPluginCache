---
name: coloringbookify-books
description: Create, download, and refine printable coloring books and pages using the connected ColoringBookify account. Use for ColoringBookify planning, generation, exports, and page edits; not for requests limited to native ChatGPT image generation, marketplace publishing, or print ordering.
---

Keep the work in the conversation. Custom cards are optional, for users who
want a visual gallery or comparison. Explicit user choices take precedence
over these defaults. Use the connected account's tools for authoritative
quotes, generation, progress, and files.

## Plan and confirm

- For a book idea, call `plan_book` with the user's requested scope. Infer
  reasonable defaults for unspecified choices and summarize them; ask only
  questions that materially affect the result. Preserve privacy unless the
  user asks to make content public. Language values are `en`, `es`, `fr`, `pt`.
- Present the returned scenes, style, difficulty, shape, privacy, print size,
  and exact `quoted_credits`. Distinguish coloring scenes from total PDF
  pages, which include covers and the ownership page. Do not invent costs.
- Ask for explicit consent to that scope and credit cost. Planning is free;
  silence, a request to explore, or approval of a different quote is not
  generation consent. Native host tool permissions still apply.
- If the user revises a book plan, call `revise_book_plan`, summarize the
  replacement quote, and obtain consent for it. The previous quote is invalid.
- After consent, call `execute_confirmation` with the quote's `id`,
  `request_digest`, `quoted_credits` as `expected_credits`, and
  `user_confirmed: true`. Do not also call `prepare_book_quote`: the quote already
  contains the generation request. Reuse the same quote on retry.
- For one page, an additional book page, or a reusable character, the
  corresponding creation tool prepares the quote; use the same consent and
  execution sequence. Convert an attached photo using `prepare_page_quote` with
  `source_image`; do not create a character unless the user wants one.

## Complete and deliver

- After execution, call `wait_for_operation` with its operation ID. Continue
  checking that same operation while work is pending. Report useful progress
  between waits. For books, download and attach ALL `newly_ready_pages` immediately
  from their `file.download_url`, including ready covers and other book pages.
  These are intermediate deliveries: keep working until the final PDF is ready.
  Pass cumulative `delivery_key` values in `delivered_page_versions` only after
  successful transfers to avoid duplicate images. Do not acknowledge failures.
  If transfer fails, provide the authorized links and explain the limitation;
  set `include_page_images: false` if image transfer is unavailable or the user
  wants only the PDF, and keep polling for completion. A succeeded generation
  can still be assembling its PDF:
  wait for `ready_for_delivery`, not just `status: succeeded`.
- A timeout or interrupted conversation does not authorize another generation.
  Resume with `get_confirmation`, `get_operation`, or `list_operations` and
  reuse the existing operation. On failure or partial success, explain the
  actual state and reported refunds; obtain new consent before any paid retry.
- For a completed book call `get_book_files`, passing cumulative
  `delivered_page_versions` from successful transfers. It returns the PDF and
  ALL remaining page images by default. Download and attach every `pages[].file`;
  verify the number against `image_file_count`. Include covers, ownership and
  ending pages; never filter to `kind=coloring` or select only a main scene.
  Set `include_images: false` only for an explicit PDF-only request. Keep the
  page IDs, labels, PDF positions, and source revisions for edits. Use the user's
  print size or the book's compatible default. Do not call `show_book` to finish
  delivery; it creates an embedded widget and does not attach these files.
- For a standalone page or character call `get_page_image` or
  `get_character_image`. These return existing files without creating widgets.
- Treat export tools and `resource_link` results as remote file references.
  They have not downloaded a file or created a conversation attachment.
- Before your final reply, use the host's file/download tools to retrieve the
  original bytes from `download_url` into its workspace. Verify download success
  and file type, then attach the saved file using the host's supported file
  reference. Complete this step without another user request for delivery.
  Calling `get_book_pdf` or `get_book_files` again only refreshes the links.
- Show only the exact returned ColoringBookify files. Never use web image search,
  stock images, or a new drawing as a substitute preview, especially for an
  original/proposed edit comparison. If an exact preview cannot render, omit it
  and provide the labeled attachment or authorized link.
- Reuse any real attachment the host already materialized. Otherwise attempt
  the transfer once, then use the linked fallback if it fails. Do not repeatedly
  call retrieval tools to force a preview; refresh only expired or changed files.
- Only claim "attached" after downloading the bytes and including a real host
  file reference in the reply. Do not encode bytes in the conversation or
  fabricate local file paths, file IDs, previews, or Outputs placement.
- If the host has no file-transfer capability or the transfer fails, include
  a labeled authorized download link in your reply and briefly explain why.
  Refresh expired URLs through the same read tool. Retrieval and export
  consume no generation credits; never regenerate a book to deliver its files.
- After delivery, briefly offer relevant refinements or additional pages.
  Do not leave the result solely inside a widget or generate an unsolicited edit.

## Refine in chat

- Use `get_book` and its `workspace.pages` to resolve a requested scene. Coloring
  scene numbers differ from PDF page positions. Ask when the intended page is
  ambiguous; use its real ID and never redraw a whole book to edit one page.
- Call `request_page_edit`, show its one-credit quote, obtain consent, and
  execute it. The original remains unchanged while the proposal generates.
- Once ready, call `get_page_edit` and `get_page_edit_image` for both
  `variant: original` and `variant: proposed`. Present the images or accessible
  links, explain any effect on shared books, then ask whether to keep the
  original or accept the proposal.
- After the user's decision call `review_page_edit` with `decision: accept` or
  `discard` and the returned `review_revision`. Review adds no charge;
  discarding a successful preview does not refund its generation credit.
  If the source changed, retrieve current state rather than forcing acceptance.
- After acceptance, retrieve the updated page and a fresh book PDF when
  relevant. For more pages use `prepare_book_page_quote`, with a new exact quote and
  consent, then deliver the updated book.

An existing Business account is required. Explain entitlement or credit
limitations factually. Do not initiate credit purchases, upgrades, KDP/Lulu
publishing, or physical ordering. Use `show_books`, `show_book`,
`show_characters`, `show_confirmation`, or `show_page_edit` only when an
interactive visual view is explicitly requested by the user. For `show_book`,
set `user_requested_gallery: true` only for that explicit request. Creating a
book, downloading files, or announcing completion does not request a gallery.
