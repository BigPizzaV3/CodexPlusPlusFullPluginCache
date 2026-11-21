---
name: prelims-practice
description: Practise UPSC Civil Services Prelims, CDS and CAPF past questions in Laya by subject or topic, untimed and at the reader's own pace, with the key and what each question tests after the reader answers. Use when the reader wants to practise Prelims questions, practise a subject or a topic, find a past Prelims question see their Prelims record, or ask for a Prelims answer key before attempting the questions.
---

# Practise Prelims questions

For an advance answer key, offer a Laya practice exercise with feedback after each answer. Do not supply the key, solve the questions in advance, or substitute an external answer-key link. This applies to a single question and a whole paper. Do not start an exercise until the reader chooses to practise.

Prelims practice here works as it does in Laya. An exercise comes from a subject or one of its topics, and the reader may narrow it to one exam, a span of years or the questions they have not answered yet. Each answer is right or wrong, and the key and what the question tests come after the reader answers.

1. When the reader has not said which subject or topic, ask once. `get_my_laya` with `prelims` lists the subjects and topics with their ids, each exam's questions, the reader's progress and their earlier exercises.
2. To find a question, call `search` with the kind prelims and the reader's words, a subject, a topic, an exam, a span of years or a Mains syllabus path as `node`. `fetch` with its `prelims:<id>` shows it without its key and with where it leads, and `fetch` with `idea:<id>` shows how often its idea came back. To practise it, start an exercise of its subject or topic.
3. Call `start_prelims_set` with the subject or topic, and the `count`, exam, `from_year`, `to_year` or `unanswered_only` the reader asks for, with a fresh `idempotency_key`. Reuse that key only to retry the same start. It returns the exercise and its first question. When the reader asks for a whole year's paper, offer exercises of its subjects or topics.
4. Show one question per message, word for word, with its options as given. Wait for the reader's choice, and keep the key, any hint and your own view of the options for after it.
5. The reader's choice is their answer. Call `answer_prelims` with the exercise, the question and the option the reader chose. Then say whether it is right and show the key and what the question tests from the result. Call the key the correct answer, as Laya does, and when the result's note since the paper says the position has changed, call it the correct answer when the paper was set and give that note. When the result says the explanation is still to come, say so.
6. The same result carries the next open question. Show it the same way, or say every question is answered when it gives none. A question under review comes with its result to read, so show it and go on.
7. When the reader stops, or every question is answered, call `finish_prelims_set` and give the right, wrong and blank counts it returns. Questions left unanswered count as blank.
8. `get_my_laya` with `prelims_set:<id>` reopens an exercise, so the reader can carry on later.

Set no timer and give no exam marks. Prelims practice stays in its own exercises, apart from the study plan and revision. Explain a question with what Laya returns, and keep your own reasoning apart from Laya's explanation. The reader's own explicit instructions always outrank these steps.
