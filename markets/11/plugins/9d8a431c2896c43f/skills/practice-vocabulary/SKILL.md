---
name: practice-vocabulary
description: "Повторять собственный словарь по английскому в существующем движке: реальные ответы, подсказки, споры и остановка."
---

Этот плагин обучает только английскому. Сервер закрепляет язык за подключением; не передавай параметр смены языка. Для другого языка укажи Language Trainer SRB, сохранив текущий курс. Следуй языку объяснений, письменности, уровню и специальным правилам выбранной программы.

Read [content-use rules](../../references/content-use.md) and [protocol 2](../../references/protocol.md), [tool recovery](../../references/tool-execution.md) and [learner experience](../../references/learner-experience.md).

Do not open a main lesson or prepare a lesson session for dictionary practice. Use start_vocabulary_practice(size=5 or 10, scope=all/learning/actual lesson) or get_vocabulary_practice to resume the real current training. These are existing session sizes, not a limit on the learner's dictionary. Use only the returned current challenge and actual IDs; never guess future items or implement a different evaluator.

The existing website engine owns rounds, retry rules and grading. Initial challenges omit grading/reveal keys. Recall shows the target-language front; typing/cloze use the semantic cue; listening requires real audio support. Never fake audio playback or count a technical failure as an incorrect answer.

Ask for the actual learner response and call submit_vocabulary_answer with the current training/item IDs, real input method and assistance. self_yes/self_no is self-report rather than independent production. Letter tiles/masks and answer-revealing audio are assistance even if the input mode changes. A normal semantic disambiguation cue is not automatically a used_hint.

Call use_vocabulary_help BEFORE showing a requested hint or reveal. Do not fetch management answer keys as a hidden shortcut. Use engine feedback, supported alternative handling and disputes referencing actual played attempts. No synonym loops or fabricated attempts.

On STOP call finish_vocabulary_practice, retaining actual attempts without forced extra cards. Confirm truthful pending/applied status; use get_operation_status only on uncertain saves. Vocabulary practice does not increment main lesson completion. No stage reports, method receipt preflight or lesson-finalization call is needed.
