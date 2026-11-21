---
name: search
description: Find and select presentation decks or individual slide references in Deck.gallery by topic, audience, slide purpose or visual style. Use when the user asks for examples, inspiration, layouts or more search results; it does not create or edit a presentation.
---

# Find useful references

Apply [best-practices](../best-practices/SKILL.md) if it is not already loaded. Use the user's request, attachments and previous results as context. Ask for missing context only if it would materially change the search; a clear request such as SaaS product introductions is enough to start.

## Choose the search

| User needs | Starting point |
| --- | --- |
| Comparable presentations, opening sequences or deck structure | `deckgallery_search_decks` |
| A particular slide purpose or layout, such as pricing or a team grid | `deckgallery_search_slides`, if available to this account |
| A deck already returned in the chat | Reuse its `deck_id` with `deckgallery_get_deck` |
| Today's deck | `deckgallery_get_deck` with `deck_id: "today"` |

For a named deck or supplied Deck.gallery link that has not been resolved, search by its title and verify the matching result. Use returned identifiers and links; do not guess a deck or slide ID from a title or URL. If the user asks to inspect only an attachment, inspect that attachment without an unrelated library search.

Write a focused query combining the subject with the most useful constraint. Use an available `deck_type` or `structure_type` filter when it reflects the request. Take enum values from the current tool schema rather than inventing them. Do not force every adjective from the brief into the first query.

Examples of intent, not mandatory query strings:

- SaaS startup pitch references: search decks for SaaS software startups, with the pitch filter if supported.
- Three pricing layouts: search slides for pricing tables, keeping the presentation type open unless the user specified it.
- Report opening sequences: search report decks, then inspect the opening slides of the best matches.

## Select and refine

Start with a small result page, usually four to six candidates. Match the substance of each result to the request. A deck labeled pitch can still be an earnings update; check its summary and relevant slides before recommending it as a startup fundraising example. Covers alone do not establish how a product is introduced.

Choose a few distinct, relevant references, usually about three for an open-ended comparison. Respect an explicit requested count. Prefer useful differences in approach to a longer list of near-identical examples.

If matches are weak, broaden one constraint or try a more useful term. For an exact-title or exact-topic search, report that the exact match is missing before offering alternatives, and keep any alternatives clearly separate. Do not broaden when the user asked only for exact matches. Stop when there is enough evidence to answer; do not exhaust the catalog by default.

Read the selected decks' outlines once, then retrieve only slide ranges needed for the question. `include_previews: false` is useful when locating positions first, but it does not remove content or call limits. Reuse previews already returned. Request previews for selected slides before making visual or exact-text claims; if none is available, label the evidence as outline-based.

If slide search is unavailable on the connected plan, use permitted deck search and accessible outlines to locate examples, explaining that the search is narrower. If the response instead reports an account, authentication or usage refusal, follow best-practices and do not treat it as a no-match result.

## More results

When the user asks for more, carry forward the same search state and avoid repeating previously shown references. Use `next_cursor` only when returned, preserving the exact query, filters and limit that produced it. Do not decode or construct a cursor. A changed query is a new search with no old cursor.

For a longer outline, use its returned `next_outline_from`; this is separate from the `slide_from` position used to request preview images. Continue only as far as the task requires. Slide-search `total_matches` can count only openly accessible slides, so it is not a complete inventory of all matches; use the returned cursor to determine whether another page is available.

## Deliver

Link the selected decks or slides and explain why each fits. For a simple discovery request, a short list is enough. For a comparison, explain the relevant differences using inspected evidence. Apply [analyze-deck](../analyze-deck/SKILL.md) when the user asks how the references tell their story or introduce an idea, reusing this search's results.
