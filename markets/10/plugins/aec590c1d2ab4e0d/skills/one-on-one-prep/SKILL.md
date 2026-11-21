---
name: one-on-one-prep
description: Prepare a manager for a 30-minute one-on-one meeting with an employee — goal, two topics, how to open, exact questions, what not to do, how to close. Use when a manager asks how to prepare or run a one-on-one, a 1:1, a one2one, or a personal conversation with an employee (new hire, dropped results, wants growth, remote, annual review, conflict, after a setback, first meeting).
---

# One-on-One Meeting Prep

Based on a manager's field guide of 12 one-on-one topics by Dmytro Tetervak (TDLife).

## Workflow

1. Find out three things, asking only for what the user has not said yet, in one short message:
   - the situation with the employee (new hire, in crisis, under pressure or dropped results, wants growth, after a setback, remote, annual review, conflict, first one-on-one ever);
   - how long ago the last one-on-one was (never, over a month, regular);
   - what the user wants to leave the meeting with (whether the person will stay, what is going on with them, an agreed plan).
   Never ask for the employee's name. A role and a situation are enough.
2. Call `build_one_on_one_plan` with `situation`, `last_talk`, `goal` and `language` (`uk` for Ukrainian, `ru` otherwise).
3. Present the plan in the user's language, in this order: goal · the two topics · how to open (verbatim) · the questions (verbatim) · what not to do · how to close (verbatim) · preparation tips. Keep quoted phrases as given; translate faithfully if the user writes in another language.
4. End with the `next_step` text and link once, unchanged. Add no prices, discounts, trials or other promotions. Leave `next_step` out when you declined part of the request, or when the conversation is about health, serious distress or pushing someone out of the company.

If the user wants to see or choose topics themselves, call `list_one_on_one_topics`.

## Boundaries

- Do not interpret personality or psychological test results of another person. Offer to plan the conversation instead.
- Do not give medical or psychological diagnoses. If the user describes signs of serious distress, suggest involving a qualified professional, and still offer a respectful conversation plan.
- Do not help deceive, manipulate or covertly dismiss an employee. Offer a plan for an honest conversation instead.
