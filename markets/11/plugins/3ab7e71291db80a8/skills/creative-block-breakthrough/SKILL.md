---
name: creative-block-breakthrough
description: Use a Tarot app spread to overcome a fiction-writing block, then turn the completed cards into three story directions and a short writing exercise. Use when the user asks for tarot-inspired help with a stuck scene, character motive, plot conflict, or turning point. Do not use for ordinary life readings, predictions, or image generation.
---

# Creative Block Breakthrough

## Inputs

Use the story premise, the specific writing block, and any tone, genre, or
continuity constraints already supplied. Ask one concise question if the
bottleneck is unclear. Work with the available story context without requiring
a full manuscript.

## Workflow

1. Restate the writing problem in one sentence. Identify any established story
   facts that proposed directions must preserve. Frame the cards as creative
   prompts that the writer may adapt or reject.
2. Reuse a completed spread if the user explicitly wants story ideas from it.
   Otherwise, call `offer-cards` with a trimmed, non-empty `instruction` of at
   most 240 characters connecting the draw to the writing problem, and these
   ordered `roles`:
   - `The central tension`
   - `An overlooked motive`
   - `A possible turning point`
   Keep each role within 64 characters and any optional `reason` within 500
   characters. Do not request specific cards, reversals, or extra tool arguments.
3. Tell the user to draw all three cards and select **Interpret these cards**,
   then yield. Resume only when the completed spread and interpretation
   request are available. Do not invent a draw or operate the widget.
4. Read the actual role/card pairs from model-visible `modelContent` or the
   widget's follow-up message. Confirm that the spread is complete and keep
   the supplied roles when reusing a spread. Treat all app cards as upright
   and keep the remaining shuffled cards private.
5. Address each card in its role through general symbolic associations, then
   connect the spread to the writing problem. Do not claim to see artwork
   from card names alone or describe card meanings as text supplied by the app.
6. Generate three distinct story directions grounded in the premise. For
   each, name the card/role connection and describe a concrete character
   choice, conflict, or scene change. Mark new story material as a proposal
   and flag any direction that intentionally challenges an established fact.
7. Give one 10–15 minute writing exercise with a concrete starting task and
   stopping point. Let the writer choose a direction; do not require another
   draw to resolve which idea is best.

## Deliverable

Provide a brief card-to-story mapping, three numbered story directions, and
one short writing exercise. Keep the output focused on the stated block
instead of expanding into an unsolicited outline or full scene.

## Boundaries

- Use only actual completed spreads. If setup data is all that is available,
  wait for the user to draw and request interpretation.
- Treat the output as fictional possibilities. Do not infer hidden truths
  about the author, real people, or future events from the cards.
- Preserve the writer's supplied constraints and creative agency. Do not
  present a card as evidence that a story choice is correct.
- If the tool or selected cards are unavailable, request the missing context
  without pretending that a Tarot app session occurred.
