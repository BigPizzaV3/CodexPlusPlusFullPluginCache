# Semantic chunking

Rules for splitting content into autonomous, extractable blocks. This is the
highest-impact part of GEO content work.

## Why it matters

Generative systems retrieve and score individual blocks, not whole pages (see
`mechanics.md`). A cleanly cut block produces a sharp embedding and gets
extracted reliably. A block that depends on its surroundings loses meaning the
moment it is lifted out.

## Core rules

1. **One block, one claim.** Each paragraph carries exactly one focus or answers
   exactly one question. Cut empty intros and vague setup entirely.

2. **Inverted pyramid.** The core statement goes in the first sentence of the
   block. Reasons, numbers, and examples come after.

3. **Self-containment.** Each block must be understandable without the rest of
   the page, so a model can lift it without distortion. The block answers what,
   who, and where from within itself.

4. **Entity-first.** Replace pronouns with the core entity: "Amazon Go" not "the
   system," "the checkout latency" not "the value." Without an explicit entity a
   block is meaningless once pulled out of context. This is also why elegant
   variation (inventing synonyms to avoid repetition) hurts you: name the entity
   the same way every time.

5. **Questions as subheadings.** Write H2 and H3 as the questions users ask. This
   matches prompt language and the sub-questions of query fan-out (see
   `query-fan-out.md`).

6. **Lists and tables are atomic.** Never split a list or table when cutting
   blocks. Models lift these directly into answers.

7. **Condition blocks.** Spell out "it depends" cases explicitly: if A, then X;
   if B, then Y. Clear decision criteria have above-average extraction value.

8. **Connect without merging.** Link related blocks with anchors and internal
   links, but keep each block's boundaries intact. Anchor-text requirements in
   `semantic-html.md`.

## Negative example: mechanical cut

A block cut purely by character length, such as "...lets customers walk in, take
the items, and leave without waiting at a checkout...", is worthless for
retrieval. The entity (Amazon Go) and the concept (Just Walk Out) are missing,
the block cannot be matched to any prompt with confidence, and it raises the
hallucination risk.

## Limits

- There is no industry standard for optimal chunk length. ChatGPT, Perplexity,
  and AI Overviews cut and score differently. Optimization stays iterative and is
  steered through measurement (see `measurement.md`).
- A text hacked entirely into question-answer blocks can repel human readers.
  Well-structured prose with clear internal logic is also chunkable. The rules
  govern structure, not readability.
- If a paragraph leans on a graphic ("as the chart shows"), the block loses its
  meaning on extraction. Fix with a text anchor (see `citation-worthiness.md`).
