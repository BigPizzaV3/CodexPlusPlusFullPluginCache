---
name: conduct-optional-live
description: "Провести отдельную добровольную разговорную Live-сессию по английскому, не изменяя основной урок и его счётчик."
---

Этот плагин обучает только английскому. Сервер закрепляет язык за подключением; не передавай параметр смены языка. Для другого языка укажи Language Trainer SRB, сохранив текущий курс. Следуй языку объяснений, письменности, уровню и специальным правилам выбранной программы.

Read [content-use rules](../../references/content-use.md) and [protocol 2](../../references/protocol.md), [persistence](../../references/compact-persistence.md) and [learner experience](../../references/learner-experience.md).

For a voluntary conversation outside the main lesson, call open_lesson(kind=practice,request_id,objective if agreed,requested_minutes if requested). To resume an identified practice, include its actual lesson_id. Use returned familiar targets, methodology and memories; do not open or move the main lesson. Optional Live stays independent of the main cursor/count.

Set a finite familiar topic, level-appropriate target-language conversation and STOP boundaries in the chat. Follow the chosen program's language/script and feedback policy. No forced new grammar, vocabulary quota, debt or homework. The learner controls voice. If tools are unavailable in voice, return to text in the same chat; do not ask for a copied handoff/report.

Use selective correction, one useful cue and at most one retry. Respect requests for explanations in Russian. Do not invent audio observations or elapsed time. Save actual requested/unknown words with the full vocabulary workflow and IPA. No preparation record or voice report is required.

STOP ends conversation immediately. For an intentionally ended actual optional session, complete_lesson may close that separate practice without affecting main progress. Send actual_minutes and minutes_source=user_reported or timer only when genuinely known. Otherwise omit actual_minutes or use minutes_source=not_observed; never substitute the requested budget for observed duration. The server decides whether the actual standalone Live qualifies for the activity streak. If the learner wants to resume the unfinished conversation later, use pause_lesson instead.

Update bounded memory only for future-useful facts. Confirm completion only from the successful receipt; a failed vocabulary save is not a reason to invent extra speaking or repeat the optional session.
