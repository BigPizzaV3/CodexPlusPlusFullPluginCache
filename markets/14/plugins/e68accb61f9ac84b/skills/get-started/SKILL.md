---
name: get-started
description: Help learners set up Vocabulum after installation or check their connection. Example requests include “Is my Vocabulum account connected?” and «Мой аккаунт Vocabulum подключён?». Practice and general questions about available modes go to the relevant practice skill.
---

# Getting started with Vocabulum

Before onboarding or checking the connection, check the request's scope. For an unsupported bulk/full-dictionary export, SRS/review-date or learned-status change, or another learner's data, explain the limitation without calling Vocabulum tools. Do not fetch private words to probe support, assemble a partial export as a substitute, or replace a progress change with `add_words`. For an unrelated request such as translating an email into Spanish, answer normally without Vocabulum onboarding or tools.

1. Briefly explain in the learner's language: Vocabulum handles memorization and scheduled reviews; ChatGPT helps them speak and write with their words. Chat practice does not change SRS or learning status.
2. If they already chose a practice, continue directly with its skill: [speaking, writing and personal vocabulary](../greek-practice/SKILL.md), [listening and reading](../greek-comprehension/SKILL.md), [grammar](../grammar-practice/SKILL.md) or [Cyprus culture](../cyprus-culture-practice/SKILL.md). Do not insert a menu or a separate connection check.
3. Otherwise call `get_my_words` with `filter: all`, `limit: 5` and `locale: ru` or `en` to check the connection. Explain any notice or error honestly and include `appLink` when supplied. If no personal words are available, explain why and offer general practice labelled as non-personalized; never invent a dictionary or insist on returning to the app. On limits, reuse available words rather than fetching more.
   On `no_studied_words`, use the first-practice guidance in [greek-practice](../greek-practice/SKILL.md). Offer the short session and a ready-to-send dialogue request before showing the practice menu.
4. On success, briefly summarize the returned `learner` counts if helpful. Vocabulary levels describe the words, not a measured proficiency level. Do not list target words or their translations before a recall task.
5. When personal words are available, offer the four core choices: translation, own sentences, role-play or writing feedback. Mention rephrasing, similar words, A2/B1 speaking exam practice and retelling when relevant. Offer listening and reading comprehension as separate A2/B1 practice that does not need personal words. When they choose, follow the corresponding skill.
6. Mention briefly that an explicit request can add existing dictionary words to their study list through `add_words`. That action does not mark them learned; do not add words automatically.
