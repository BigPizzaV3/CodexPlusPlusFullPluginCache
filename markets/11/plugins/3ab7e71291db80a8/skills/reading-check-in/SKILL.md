---
name: reading-check-in
description: Revisit an earlier Tarot app reading and intended actions using the user's reported experience, then identify lessons and a next step. Use when the user asks to check in on, review, or follow up on a previous reading supplied in the conversation. Open a fresh spread only when requested. Do not claim access to a reading archive, automatic reminders, or proof of predictions.
---

# Reading Check-In

## Inputs

Use the earlier reading or journal entry available in the conversation or
supplied by the user: its question, any role/card pairs, interpretation, and
intended actions. Use the user's account of what they tried and what changed.
Ask one concise question to obtain essential missing context.

## Workflow

1. Identify the earlier reading being revisited. Ask which one when several
   are plausible. Do not treat the current widget state as a history archive
   or silently substitute it for the earlier session. If no earlier reading
   is available, request the reading or a summary before comparing sessions.
2. Reconstruct a short account of the original intention and proposed action
   from the available material. Preserve any supplied role/card pairs. If
   only a summary is available, label it as such and do not invent missing
   cards, positions, dates, or interpretations.
3. Ask what the user tried, what they noticed, and what still matters unless
   they have already explained it. Treat not taking an action as useful
   context. Separate reported events from the earlier symbolic interpretation;
   do not rewrite the reading to fit events or score its predictive accuracy.
4. Identify one useful lesson and a modest next step based on the user's
   experience and current priorities. Keep the action within the user's
   control and describe uncertainty plainly.
5. If the user explicitly requests a fresh spread, first summarize the
   check-in so far, then call `offer-cards` with a trimmed, non-empty
   `instruction` of at most 240 characters and these ordered `roles`:
   - `What has changed`
   - `What still needs attention`
   - `A useful next step`
   Keep roles within 64 characters and any optional `reason` within 500
   characters. Do not add arguments for card selection or reversals. Tell
   the user to draw every card and select **Interpret these cards**, then
   yield until the completed spread and interpretation request arrive.
6. If a fresh spread was requested and completed, read its actual instruction,
   roles, and selected cards from model-visible `modelContent` or the widget's
   follow-up message. Verify that all roles have cards, treat app cards as
   upright, and interpret each position before synthesizing. Keep the earlier
   and fresh spreads distinct; compare only what their questions and roles
   support. Do not interpret a change of cards as evidence that fate changed.

## Deliverable

Produce a compact comparison of the original intention, the action tried,
the user-reported result, and the lesson learned. End with one practical next
step and one reflection question. Include a fresh reading only after the user
requests and completes it. Deliver the check-in in chat without implying that
it has been saved or scheduled.

## Boundaries

- Use conversation context and the user's supplied history; do not claim to
  retrieve prior sessions, track progress automatically, or inspect the
  private shuffled remainder.
- Treat `submitted` as a sent follow-up status, not proof of a stored
  interpretation or a completed action.
- Keep tarot as neutral symbolic reflection. Do not claim certainty, validate
  predictions, or infer another person's private thoughts.
- Keep medical, legal, and financial matters to reflection and questions for
  an appropriate professional; do not recommend consequential actions based
  on cards.
