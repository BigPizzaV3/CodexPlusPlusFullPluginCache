# Representative workflows

## 1. Simple task
User: "В понедельник надо найти где пройти MOT."
Expected:
- Interpret as a personal action, not a Calendar event.
- Create a TickTick task for Monday in the user's timezone.
- Use a specific title such as "Find/book MOT inspection".
- Do not create a Notion page unless research is also performed and worth retaining.

## 2. Appointment plus preparation
User: "Запиши меня к врачу во вторник в 16:00 и напомни утром взять результаты анализов."
Expected:
- Calendar event for the appointment.
- Separate TickTick preparation task/reminder if appropriate.
- Do not duplicate the appointment as a task.

## 3. Conditional watch
User: "Скажи мне, когда этот MacBook станет дешевле €2000."
Expected:
- Create a condition-watch automation at a reasonable cadence.
- Do not create a static TickTick task as the primary solution.

## 4. Durable decision
User: "Мы решили оставить WebView для MVP. Сохрани почему."
Expected:
- Create/update a Notion decision record.
- Capture decision, rationale, alternatives, implications, and date/context when known.
- Do not create a task unless an action is also stated.

## 5. Research -> action
User: "Найди где пройти MOT рядом, выбери нормальные варианты и напомни мне в понедельник записаться."
Expected:
- Research current options now.
- Summarize/rank useful choices.
- Create Monday TickTick action.
- Save research to Notion only if it is likely to remain useful or the user asks to preserve it.

## 6. Personal work follow-up
User: "Завтра напомни спросить Мишу про PSP timeout."
Expected:
- TickTick personal task.
- Do not create a Linear issue merely because the subject is engineering work.

## 7. Shared engineering issue
User: "Создай баг: webhook processor retries 429 without backoff."
Expected:
- Linear issue, with concise reproduction/context if available.
- Do not make TickTick the team source of truth.

## 8. Retrieval without backend question
User: "Что мы решили по собственной Card Vault?"
Expected:
- Infer durable decision -> search Notion first.
- If project source is elsewhere and evidence points there, continue appropriately.
- Do not ask "Где мы это сохраняли?" unless retrieval genuinely cannot proceed.

## 9. Email -> follow-up task
User: "Посмотри ответ школы и если от меня что-то нужно — поставь задачу."
Expected:
- Read relevant Gmail message/thread.
- Determine whether action is required.
- Create TickTick task only if needed; title should describe the actual action.

## 10. Non-persistent brainstorming
User: "Может когда-нибудь надо начать учить иврит."
Expected:
- Discuss if useful.
- Do not create a task/habit automatically; commitment is too vague.

## Negative activation examples

- "Почему небо синее?" -> ordinary Q&A; do not invoke persistence workflow.
- "Какие плюсы и минусы Notion?" -> analysis only unless user asks to save/act.
- "Придумай десять названий проекта" -> brainstorming only unless user asks to record the choice.
