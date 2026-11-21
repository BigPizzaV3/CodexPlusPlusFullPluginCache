---
name: ai-visibility
description: >-
  Find out whether AI assistants recommend an iOS app, why rivals get named
  instead, and which web sources shape those answers, then turn the gaps into
  listing and keyword work. Use for "does ChatGPT recommend my app", "why
  does AI suggest my competitor", "how do I get recommended by AI", "AI
  visibility".
---

# AI visibility: measure, diagnose, act

## Measure

`check_ai_visibility` works on any App Store app without an account. It asks a
search-grounded answer engine three questions a real person would ask, then
scores whether the app is named and recommended. Pass `niche` (for example
"habit tracker") when the store category is broader than the app really is;
a wrong category produces a misleading score. Say which engine was asked; it
is not ChatGPT itself.

With a linked account, `aeo_visibility_report` shows the person's tracked
questions over time.

## Diagnose

Read the result honestly:

- Named but not recommended: the engine knows the app but other pages argue
  better for rivals.
- Not named: the app is missing from the sources the engine reads.
- The sources list is the lever: those are the pages that decide the answer.

## Act (what MetaRun can and cannot do)

MetaRun measures and diagnoses. It never posts, publishes, sends messages, or
writes reviews anywhere, and neither should you on the person's behalf. What
it can change is the person's own listing:

- Make the App Store listing state the niche plainly (App Store listings are a
  major source for these answers): subtitle and description through the
  localize-listing flow.
- Check keyword ranks for the same phrases with `aso_check_rank` and find
  phrasing people search with `aso_suggest_keywords`.

Everything else (getting covered by the sites in the sources list) is work the
person does themselves; give them a short, concrete list.
