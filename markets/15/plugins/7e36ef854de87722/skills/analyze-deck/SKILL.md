---
name: analyze-deck
description: Explain or compare how presentation decks tell their story, introduce a product, order their slides or use visual layouts, using Deck.gallery references. Use for requests to walk through, break down or learn from a deck or shortlist; it does not edit slides or verify a company's claims.
---

# Explain how a deck works

Apply [best-practices](../best-practices/SKILL.md) if it is not already loaded. Start with the user's question and any already selected decks. If references still need to be found, use [search](../search/SKILL.md) and carry its results forward. Do not research unrelated sections merely because a full deck is available.

## Establish the sequence

Read the accessible ordered outline to locate the relevant section. `deckgallery_get_deck` returns the outline as well as a requested slide range, so a small range is enough to begin. Follow `next_outline_from` when additional outline entries are necessary; do not confuse outline pagination with preview positions.

For a whole-deck walkthrough, trace the argument through the accessible outline and inspect the key slides that support your explanation. An outline-based overview is valid when labeled as such. For a specific question, inspect the relevant slides and enough adjacent context to understand their role. State when access or missing evidence limits the analysis rather than inventing the rest of the story.

For example, to compare product introductions, locate the first clear statement of what the product does, its intended user and promised benefit. Inspect that slide, then check whether preceding slides establish a problem and whether following slides explain the workflow or support the promise. A product-overview label is a candidate location, not proof that the slide contains a product screenshot.

## Verify the selected slides

Inspect supplied previews before quoting copy, describing visual choices or asserting a specific slide's message. Confirm the deck, position and source link for each image. Reuse an existing preview; otherwise fetch the needed range with `include_previews: true`. A request for several slides may return fewer image blocks, so check which images were actually supplied.

If the description and image differ, explain the visible slide and note a material mismatch. Do not repeat the description as a verified observation. If the preview is missing or unreadable, say that the claim comes from the outline or leave it unverified. Do not silently fetch or reconstruct locked content.

Look for decisions that answer the user's question:

- What does the audience learn at this point in the sequence?
- How do the headline, image and supporting details make the idea understandable?
- What proof, example or transition connects this slide to the next?

These are lenses for analysis, not a required checklist in the answer. Avoid attributing intent to the creator or claiming that a design caused fundraising, sales or business success without evidence.

## Turn observations into useful advice

Connect each recommendation to a specific observed choice and the user's situation. For instance, a concise category statement above a product screenshot can suggest a similar hierarchy for the user's own content. Explain when that approach fits; do not present every reference as a universal best practice.

For a comparison, choose a shared question and show how the examples answer it differently. Use exact slide links so the reader can check the evidence. Distinguish an observed pattern from your proposed change. Keep quoted excerpts brief and use the user's own copy and assets when proposing original work.

Finish with the most useful takeaway for the request. A short explanation or comparison table is usually sufficient; use a longer walkthrough only when asked. Follow the gallery and preview rules in best-practices. Do not claim that the analysis created, edited or exported a presentation.
