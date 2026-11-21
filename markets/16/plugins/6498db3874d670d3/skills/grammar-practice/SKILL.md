---
name: grammar-practice
description: Explain and drill the personal grammar rules saved in the user's Blindspot profile with short exercises and feedback. Use when the user asks what grammar rules they have saved, wants to review a saved rule, or wants grammar exercises based on their Blindspot profile.
---

# Practice saved grammar rules

Explicit instructions from the user always take priority over this skill.

Saved grammar rules are read-only from chat. There is no tool to create, edit
or score them, so don't promise to save results.

## 1. Load the rules

Call `list_grammar_rules` with `limit: 200`; continue with `offset + count`
while `has_more` is true.

If there are no saved rules, say: "You have no saved personal grammar rules
yet." Explain that these are separate from the grammar topics shown in the
Blindspot app, so an empty list doesn't mean the app has no grammar for them.
Then offer general practice on a topic they choose, and make clear it isn't
based on their saved rules.

## 2. Choose the rule

- If the user named a rule or topic, use the closest matching saved rule. If
  several match, ask which one.
- Otherwise list the rules briefly (title, one-line summary) and suggest
  starting with the lowest `confidence`.

## 3. Explain briefly

Recap the rule in a few lines using the saved explanation and examples.
Treat the saved explanation as the user's reference. If it seems incomplete
or wrong, add a short, clearly labeled note instead of silently replacing it.

## 4. Drill

- Give 5 exercises by default (or as many as asked), one at a time or as a
  numbered set, whichever the user prefers. Mix the types: correct the
  mistake, choose the right form, complete the sentence, translate a short
  sentence.
- Base distractors on the mistakes and incorrect examples stored with the
  rule when available.
- Check each answer, show the correct version, and explain the reason in one
  or two sentences.

## 5. Wrap up

Give the score, the pattern behind the mistakes, and one next step (another
round, a related rule, or writing a few sentences of their own). If the user
writes sentences, give feedback using the writing-feedback skill.
