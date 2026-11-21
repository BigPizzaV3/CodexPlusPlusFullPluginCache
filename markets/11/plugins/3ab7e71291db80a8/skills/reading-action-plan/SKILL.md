---
name: reading-action-plan
description: Turn a completed Tarot app reading into one to three manageable actions and a check-in question. Use when the user asks what to do with a reading, how to apply its themes, or how to make a practical plan from their drawn cards. Do not use for opening a routine spread, predicting outcomes, creating reminders, or medical, legal, or financial recommendations.
---

# Reading Action Plan

## Inputs

Use the completed spread, any interpretation already in the conversation,
the user's priorities, and their available time or energy. Accept the current
model-visible spread or an earlier reading the user supplies. Ask only for
missing context that would materially change the plan.

## Workflow

1. Establish which reading the user wants to apply. Read the instruction,
   ordered roles, and selected card names from `modelContent`, the widget's
   follow-up message, or the user's supplied reading. Keep every role/card
   pairing intact and treat app cards as upright. Verify that every role has
   a card before deriving a plan from the spread.
2. If the spread is still being drawn, ask the user to finish and select
   **Interpret these cards**, then yield. If no reading is available, request
   it. Do not call `offer-cards` merely to replace missing context or produce
   an action plan from an existing reading.
3. Reuse the existing interpretation when available. If the user requests a
   plan from a completed spread without an interpretation, briefly address
   each position and synthesize it first. Treat widget status `submitted` as
   confirmation that the follow-up was sent, not evidence that a reading was
   generated or stored.
4. Identify the themes most relevant to the user's stated priorities. Use
   tentative language and distinguish symbolic suggestions from facts the
   user has reported. Invite the user to reject themes that do not fit.
5. Convert those themes into one to three small actions within the user's
   control. Make each action observable, feasible, and tied to a named card
   and role. Use the supplied time horizon; otherwise propose a modest plan
   for the coming week without implying the user has agreed to it.
6. End with one check-in question that helps the user assess usefulness or
   adjust the plan. Describe timing as a suggestion; do not claim to create a
   reminder, task, calendar event, or saved journal entry.

## Deliverable

Give a short statement of the relevant themes and a compact table with:

- Action
- Card/role and the possible connection
- Suggested timing or effort
- A clear completion signal

Finish with one check-in question. Keep the plan short enough to act on and
avoid repeating a full reading that is already present.

## Boundaries

- Use only the completed spread and information supplied in the conversation.
  Do not access the private shuffled remainder or invent cards, priorities,
  past actions, or outcomes.
- Keep the reading reflective and symbolic. Do not present an action as
  required by the cards or as a guarantee of success.
- For medical, legal, or financial topics, keep actions to reflection and
  gathering questions for an appropriate professional; do not derive advice
  or consequential decisions from tarot.
- Deliver the plan in chat. Do not imply the app persists the interpretation,
  tracks progress, or schedules the check-in.
