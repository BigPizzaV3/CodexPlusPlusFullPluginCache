---
name: get-started
description: Help with Laya pricing, costs, paid services, access, funding and first-time setup. Use when the reader asks what Laya costs, whether it is free, how it is funded, what they can access, or how to get started. For setup, confirm the connected account and help with a first study task.
---

# Get started with Laya

Choose the matching flow below. Questions about cost, access or funding do not need account setup.

For pricing, costs, paid services, packs, access or funding, give the reader https://getlaya.in for current information. Do not quote amounts, list or infer tiers, promise free access, or describe a subscription, contribution or other funding model. The connector supplies no current offers. Older prices in a conversation or search snippet are not current account terms. Apply this same boundary to the pricing part of a mixed request about grading, Interview access or another study task. Account access flags, labels and usage figures are not a price offer. Answer the supported account or study question separately. These details can change. Do not start checkout. Stop after answering this question unless the reader also asked for a study task. For a mixed request that asks to practise an Interview, continue with interview-practice. That first reply presents the room's settings and waits for a later choice or start. It contains no interview question. A fee question or the word short does not accept the practice settings.

For first-time setup or a request to begin studying, follow these steps.

1. Call `get_my_laya` without an id. Greet the reader by the account's name from the result, so they know which Laya account is connected. When the reader asks which account it is and the home gives no name, call `get_profile`.
2. When the home names an active Optional, say it is the Optional Laya files answers under. When it names none, say the reader can choose one in Laya under Profile, Study, which brings in its syllabus and past papers, and that GS works as it is.
3. Give the day from the home in two or three lines, with Laya's own numbers and reasons as given. Then offer one first step in a single sentence. The reader can plan the week, save an answer they are working on, revise a saved answer, practise Prelims questions on a subject, find past questions on a topic, add a book they are reading, or find Laya's booklet for a topic.
4. Follow the skill for the step the reader picks. plan-study plans the days, save-answer saves an answer, recall-drill revises one, prelims-practice runs Prelims practice, past-questions finds past questions, books adds a book and plans its chapters, and foundation-notes finds a booklet.
5. When the home shows the reader's Interview room, mention it once, and follow interview-prep when the reader asks.

If the reader asks about grading, answer in one or two sentences. The home says whether grading can run. Graded practice runs on the AI key the reader keeps in Laya under Profile, AI keys, and the reader adds it in Laya itself. Never ask for an API key here. You can also grade an answer in this conversation with Laya's own grading prompt through `get_grading_prompt`, and record the result with `record_evaluation` as an outside evaluation beside the reader's answer.

Keep it short and ask nothing a tool result already answered. Name what Laya does, not the tools. The reader's own explicit instructions always outrank these steps.
