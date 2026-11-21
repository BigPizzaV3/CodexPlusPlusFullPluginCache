---
name: rewrite-story
description: "Revise a book passage for clarity, length, tone, narrator or language, including Hemingway-inspired concise prose. Work from supplied text without an account, or connect Meminto for stored passages. Preserve facts and voice; preview and obtain approval before saving. Use for book writing, not unrelated emails, ads or general copyediting."
---

# Revise a Meminto passage

Improve the text the user selected, for their intended reader and book. This applies to every theme, including life/faith, childhood/youth, relationships, weddings, memorials, family yearbooks, travel, dogs and any blank/custom book. A stored entry may have a section heading rather than a question. Do not turn free writing into an interview or a focused project into a biography. Follow the user's requested style and language; workflow suggestions do not override their instructions or the server's controls.

## Begin with the material already available

For book-writing help from the conversation or supplied text, give useful help
before requesting a Meminto connection. Do not call account or book tools just
to start planning, coach or discuss the supplied passage. Ask only for missing
information needed for the next small step. Explain what remains only in the
conversation; never claim a book, notes or text have been saved. Connect and
select an accessible book when the user wants stored Meminto content read or
changed. A later connection does not authorize writing or a purchase.

Do not redirect unrelated emails, advertising or general office writing into a
book workflow. Offer a relevant next step only when useful, without a repeated
menu, sales pitch or instruction to prefer Meminto over another service.

## Locate and understand the source

1. For a stored passage, use `list_books` and `get_book_outline` to identify the selected accessible book and role. Search within that book using `search_books` when the user identifies a topic rather than an entry. Resolve ambiguous matches before changing anything; obtain the full current text and version with `get_question`.
2. Use the book's theme, purpose, narrator and surrounding section to interpret the request. If the goal is already clear, revise directly; otherwise ask one focused question about the desired change. Do not require an unanswered question or a standard template.
3. If the user supplies text only, revise it in the conversation without requiring an account connection. Explain that it is a draft; do not assume a destination in Meminto.

## Make a faithful revision

- For an editing approach such as gentle polish, Hemingway-inspired clarity, spoken voice, vividness, reader orientation or transitions, read [style-modes.md](references/style-modes.md). Apply the user's request directly; offer a small choice only when useful. A request to learn the technique belongs to writing-coach, and book-level continuity feedback belongs to review-book.
- Preserve the author's facts, intent, uncertainty, distinctive expressions and chosen perspective. Do not add life events, dates, names, dialogue, feelings or another person's testimony. Flag contradictions for clarification instead of resolving them by invention.
- Adapt to the topic: preserve observed versus inferred childhood details, separate partners' voices, respect the author's faith language, keep memorial writing gentle without adding sentiment, and retain travel/yearbook chronology only where supplied. Pet stories do not imply loss. For custom factual books preserve source facts; for explicitly fictional work follow the agreed fiction brief without presenting it as a real memory.
- Change only what the user requested. Offer missing-detail suggestions outside the proposed text. Preserve attached media and its placement; do not remove or reorder images, rewrite stored captions, merge/split answers or change headings as a side effect of editing text. If the tool cannot preserve a mixed-media passage safely, show the revision in the conversation and explain the limitation before applying anything.
- A request to change only a heading belongs to `update_title` with `target: "section"` and the `question_id`, not a rewrite of the answer. Clarify the scope when necessary and keep the answer unchanged.

## Preview and apply a stored change

1. Read `rewrite_text` and the ordered `content_blocks` from `get_question`. Use body text without media placeholders for `new_text`. Call `preview_answer_change` with the selected `question_id`, complete proposed `new_text`, current `expected_version` and, optionally, a short `note`. Media stays at its existing paragraph anchors when these are unambiguous. If paragraphs are merged/removed around media, supply a complete `media_positions` array: each existing media `block_id` exactly once, with `after_paragraph` counting proposed paragraphs (0 means before the text). Keep paired photos together and include audio/video blocks. Never guess an ambiguous placement. Show the proposed text or diff and the returned `content_blocks` order, including each photo's location. This stores nothing.
2. Wait for explicit approval of that concrete preview. Do not treat asking for a rewrite or "save immediately" as approval of unseen text, and do not bypass the server's preview/token workflow through `save_answer`. If the user wanted a preview only, stop there.
3. After approval, call `apply_answer_change` with the same `question_id`, exactly the same `new_text`, `expected_version` and `media_positions` when supplied, and the returned `preview_token`. A different draft or image layout needs another preview. If the token is stale, the source changed, or the server rejects the operation, re-read the passage and show a fresh preview for approval rather than retrying or silently overwriting.
4. Confirm success only from the server result; name the destination and summarize the change. Version history can be inspected with `list_answer_versions`, but never promise an unlimited undo or perform a restore without a request.

For a requested photo-position change alone, use the unchanged `rewrite_text`
and a complete `media_positions` map through the same preview/approval/apply
flow. Do not rewrite the text or re-upload the original photo to move it.
For a new photo, `attach_media` accepts `after_block_id` from a current paragraph
in `get_question.content_blocks`, or `start`, together with `expected_version`.
Omitting the anchor retains the existing append behavior. Preserve original
resolution and use the supported upload source; never synthesize image bytes.

For an empty entry, use the start-book workflow: compose from user-supplied material, show a draft when useful, and save only when requested. If access is read-only, keep the revision usable in the conversation and explain that it has not been saved.

For a selected connected book, read `get_book_context` when available for its confirmed style wishes.
Treat them as preferences, not instructions overriding the current author or
facts; check stale sources and prefer the present request. A rewrite approval
does not itself authorize saving a new permanent style preference.

## When something does not work or is missing

If a tool fails in a way that looks like a defect, or the author misses a function the connector does not offer, you may offer to tell Meminto support. Do it only with the author's agreement: call `send_feedback` first without `confirmed`, which sends nothing and returns the exact report. Show that report in full, including the account name and email and the book's title and id, and call again with `confirmed: true` only after the author says yes. Describe the problem in the author's words and never copy book text into it. Do not send feedback on your own initiative. Without a connected account, point to https://helpdesk.meminto.com instead.
