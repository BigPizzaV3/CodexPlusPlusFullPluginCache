---
name: decision-reflection
description: Guide a reflective comparison of two options through a Tarot app spread, then turn the completed cards into a comparison and a reversible next step. Use when the user asks to think through a choice or compare paths using tarot. Do not use for a routine reading alone, certain predictions, or medical, legal, or financial recommendations.
---

# Decision Reflection

## Inputs

Use the situation, two options, relevant values, and practical constraints
already supplied in the conversation. Ask one concise question when essential
context is missing. If there are more than two options, ask which pair to
compare before opening a spread.

## Workflow

1. Summarize the choice and identify what the user wants to understand. Keep
   reported facts and uncertainties separate. Frame the cards as prompts for
   reflection and keep the decision with the user.
2. Reuse a completed spread if the user explicitly wants to apply it to this
   choice. Otherwise, call `offer-cards` with a trimmed, non-empty `instruction`
   of at most 240 characters that briefly describes the choice, and these
   ordered `roles`:
   - `What matters most`
   - `Option A lens`
   - `Option B lens`
   - `An overlooked concern`
   - `A useful next step`
   Identify Option A and Option B in the conversation. Keep each role within
   64 characters and any optional `reason` within 500 characters. Do not add
   arguments for card identities, orientation, or randomness.
3. After opening the table, tell the user to draw every card and select
   **Interpret these cards**, then yield. The tool response contains setup
   data, not drawn cards. Resume when the completed spread and the user's
   interpretation request arrive; do not choose cards or operate the widget.
4. Read the actual instruction, roles, and selected cards from model-visible
   `modelContent` or the widget's follow-up message. Verify that every role has
   a selected card before interpreting. Preserve each role/card pairing and
   treat every card as upright. Do not access or infer the private deck order.
5. Address each position briefly, then compare the two options using the
   user's stated values and constraints. Label symbolic themes as possible
   perspectives. Do not turn a favorable card into evidence that an option
   will succeed, or invent facts about either option.
6. Suggest one small, reversible step that gathers information or tests an
   assumption. Tie it to an unresolved question and give the user a simple
   way to reflect afterward.

## Deliverable

Produce a concise position-by-position reading, followed by a two-row table
with the option, known practical considerations, symbolic reflection, and
one question to investigate. End with the proposed next step and one
reflection question. Retain the original roles when reusing an earlier spread.

## Boundaries

- Interpret only actual, completed spreads; never fill missing positions or
  replace an existing spread without the user's request.
- Use neutral symbolic guidance. Do not claim certainty, predict outcomes, or
  infer another person's private thoughts.
- Keep medical, legal, and financial topics to values clarification and
  questions to discuss with an appropriate professional. Do not recommend a
  consequential action on the basis of cards.
- If the tool or completed spread is unavailable, explain what is missing and
  request the needed context without fabricating a draw.
