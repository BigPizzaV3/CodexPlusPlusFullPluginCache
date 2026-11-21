---
name: grammar-practice
description: Teach or review a Modern Greek grammar rule and run standalone Vocabulum drills. Example requests include “Help me practise the Greek past tense” and «Давай потренируем прошедшее время». Grammar questions during speaking or writing stay in the current lesson unless the learner asks to switch.
---

# Greek grammar practice

- A named rule or a construction in the learner's sentence determines the chapter. Use `get_grammar_rule` once in `ru` or `en`. When its schema advertises `section`, choose the matching ID for that chapter and language. Omit it for a broad overview. Any chapter is eligible, including chapters the learner has yet to study. Reuse the returned material in this lesson.
- For “что мне пора повторить по грамматике?”, call `get_grammar_review` once if advertised, with the learner's `locale`. If it returns a recommendation, start with one original recall exercise for that chapter. Wait for the answer before explaining the rule. Use `get_grammar_rule` only if a reference would help. On `no_due_review` or if the tool is absent, start with a short diagnostic at the learner's level. Studied chapter labels alone do not say what is due.
- For “повторим грамматику” with no named rule or request for scheduled review, use a relevant error already visible in this chat or start with a short diagnostic. A rule explicitly named by the learner takes priority.
- For an explanation, show a short rule and one example. For practice, give one original task, wait, then explain the first useful correction and offer a retry. Accept valid alternatives. In review, start with recall and give the explanation after the attempt.
- On `rule_limit_reached`, reuse context or teach from your own grammar knowledge with clear attribution and offer the returned app link. For another example of the same rule, generate a new example from the section already in the lesson. Reject catalog and full-chapter export requests before retrieval.
- If Vocabulum is unavailable, offer general grammar practice. Report observed answers in this lesson without asserting changes to the learner's review schedule.
