---
name: study-plan
description: Generate a listening or reading revision calendar with the existing TCFCAN scheduling algorithm, or build and save a short text study plan. Use for revision schedules and study plans; do not save without explicit confirmation of the exact content.
---

For a listening or reading revision calendar, use the algorithm workflow below. For a short text plan or writing/speaking plan, retain the existing text workflow.

## Listening and reading revision calendar

Ask only for supported calendar inputs. Confirm missing weekly rest preferences: “休息安排选无固定周休、周日休息，还是周末双休？” Map them to `NONE`, `SUNDAY`, `WEEKEND`; reuse a stated or previously confirmed preference. Do not assume an unspecified “single day off” means Sunday: clarify. Never ask for daily question limits, available hours or arbitrary unavailable weekdays. Estimated time is a server output derived from the schedule, not a scheduling constraint. Explain `data.workload` as a study-day average estimate, using the project's 35 attempts/hour convention, never as an official standard or an exact daily duration. Wrong-book review requires additional time. If the user volunteers an unsupported constraint, explain that it cannot drive this algorithm and offer supported parameter changes without pretending the constraint was applied. For changes, ask only which supported parameters changed; preserve the others.

Include the confirmed `restDayMode` when generating or saving a calendar. Changes to this value require a new preview and confirmation, just like duration or strategy. Old saved calendars without the field default to `NONE`. The exact-save workflow below now uses seven parameters, including `restDayMode`; do not copy `workload` into a save request.

Collect a concrete exam date or revision-day count, not a choice of input method. Ask dates and durations as free-text questions, without options such as “我有确定考试日期 / 我想按准备天数安排” (“I have an exam date / I want to plan by days”). Use the user's language:
- If the user explicitly wants to plan by days: “你准备复习多少天？支持 15–180 天。” / “How many days will you prepare? The supported range is 15–180 days.”
- If the user mentions an exam but gives no date: “你的考试日期是哪一天？请给出年月日。” / “What is your exam date? Please include the year, month and day.”
- If neither a date nor duration is available: “你计划哪天考试？如果还没定日期，直接告诉我准备复习多少天即可。” / “When do you plan to take the exam? If you have not set a date, tell me how many days you want to prepare.”
- Reuse a concrete date or day count already supplied; do not ask for it again. If a future account goal date is already in the conversation, confirm that specific date once instead of asking how the user wants to provide it.
Do not impose a separate input-method selection followed by another question for the actual value. Strategy and weekly rest preferences may use choices; dates and durations must collect the actual value.

1. Establish one subject and a valid client IANA timezone; ask only for missing information. Generating a new calendar must NOT call `get_learning_context`, including its planning branch, to read goals, statistics or calculate days. Reuse a revision duration or exam date already supplied by the user. If a future account exam date is already available in this conversation, confirm it once: “你之前设置的是 11 月 26 日考试，仍按这个日期安排吗？” Otherwise ask the exam date or revision duration directly. If a known date is empty or on/before the user's local today, ask how many days they want to prepare. Do not offer arbitrary durations with invented personalized benefits.
2. For 60 days or fewer choose `REVERSE_HIGH_SCORE` directly: do not ask for strategy or mention a system limitation. Only for more than 60 days ask “优先冲高分，还是从基础逐级巩固？” Map the choices to `REVERSE_HIGH_SCORE` and `SEQUENTIAL_STEADY`. Preserve an already stated supported choice. The supported duration is 15–180 days; if an exam date falls outside it, ask the user to choose an in-range revision duration, never silently truncate. Use the supplied duration or the date difference from a known local today only to choose the strategy branch; if local today is unavailable, ask the revision duration rather than making a context call or guessing. Pass the confirmed exam date directly to `render_study_plan_card`; the server computes the exact duration and validates it without modifying the account goal.
3. Call `render_study_plan_card` with `mode: calendar`, `scope`, `strategy`, `timeZone`, `locale`, `restDayMode`, and either `totalDays` or `examDate` (YYYY-MM-DD). The server starts on local today and ends the day before the exam when a date is supplied. Never construct daily tasks, choose repetition counts, or transcribe a schedule into card fields. Briefly explain the returned dates and workload. Do not infer score fluctuations, mastery, or personal weaknesses from a fixed algorithm.
4. Ask whether to save this calendar. If the user changes the duration, exam date, rest arrangement or strategy, regenerate using the modified parameters and show the updated calendar; save only after confirmation of the final version. Call existing `save_study_plan` with `mode: calendar` and only the returned final `scope`, `locale`, `timeZone`, `startsOn`, `totalDays`, `strategy`, and `restDayMode`. Do not pass daily tasks, rounds, workload, a hash or an encrypted reference. The server stores parameters and reuses the same algorithm. A cross-day preview must be regenerated and confirmed before saving.
5. After successful saving, give a short text receipt using actual `recordRef`, `savedAt` and dates; do not render a second card just to announce success. To find a saved calendar use `get_learning_context` with `mode: planning`; to reopen it call `render_study_plan_card` with `mode: saved_calendar` and its `recordRef`. For a failed or uncertain save, do not claim success or retry automatically; first check the latest saved calendar. The calendar never tracks completion and is not evidence of completed work.

### Exact calendar save arguments

Make calendar access actionable in the save receipt. Put the saved subject/date summary first, then “日历订阅地址” / “Calendar subscription address” with the exact returned subscription.httpsUrl in a fenced text block, and a “下载日历（ICS）” / “Download calendar (ICS)” Markdown link targeting the exact returned subscription.downloadUrl. Put record IDs after the instructions. HTTPS is the primary subscription address; do not display Webcal. Use neutral instructions, not warnings such as “勿下载导入” or claims about calendar pollution.

Always include brief subscription instructions with a returned HTTPS address. If the user's device is known, show only its applicable steps; otherwise give both Apple paths without requiring an extra device-selection turn:
- Mac: “打开系统日历 → 文件 → 新建日历订阅 → 粘贴上面的地址 → 订阅。命名为‘TCFCAN 听力计划’或‘TCFCAN 阅读计划’，选择颜色；如需跨苹果设备显示，位置选 iCloud。” / “Open Calendar → File → New Calendar Subscription → paste the address → Subscribe. Name it ‘TCFCAN Listening Plan’ or ‘TCFCAN Reading Plan’ and choose a color; select iCloud as the location for access across Apple devices.”
- iPhone/iPad: “打开日历 → 日历列表 → 添加日历 → 添加订阅日历 → 粘贴地址 → 查找／订阅，再确认完成添加。” / “Open Calendar → Calendars → Add Calendar → Add Subscription Calendar → paste the address → Find/Subscribe, then finish adding it.” Button wording varies by OS version; iOS/iPadOS 26 uses Find, older versions use Subscribe.
Explain that a subscription is a separate calendar and the client refreshes later confirmed plan changes. For another client, ask which calendar app they use if needed and give verified subscription steps. Reference for Apple instructions: https://support.apple.com/102301.

ICS download instructions: “下载当前计划后，先新建‘TCFCAN 听力计划／阅读计划’专用日历，导入时选择它。之后选中这个专用日历即可整体删除。下载文件不随计划更新。” / “After downloading the current plan, create a dedicated TCFCAN Listening/Reading Plan calendar and select it when importing. You can later delete that calendar as a whole. The downloaded file does not update with the plan.” On Mac give File → New Calendar, then File → Import and select that dedicated calendar; to remove it select its name in the sidebar → Edit → Delete. Do not promise that the file automatically creates a dedicated calendar. For a replacement export, delete the old dedicated plan calendar and import into a new one. Do not instruct users to delete their Work/Personal calendar.

Use only the returned subscription.httpsUrl and subscription.downloadUrl, verbatim. Never build, modify or shorten them, claim the calendar was already added or promise instant refresh. If a field is absent, report that this address was not returned; do not invent it or repeat a save. Do not expose another account's links, offer public sharing or send email. If the user confirmed via the card button, use that actual save receipt without repeating a save.

Use the **last successful calendar result** whose final version the user confirmed. It must have `cardType: calendar` and a valid `data` object. Set `mode` to `calendar` and copy only these seven fields from that result's `data`, without translating, recalculating or changing their types:

| Argument | Exact source | Format / allowed values |
| --- | --- | --- |
| `scope` | `data.scope` | `listening` or `reading` |
| `startsOn` | `data.startsOn` | `YYYY-MM-DD` string; use the returned local start date |
| `totalDays` | `data.totalDays` | Integer 15–180; never a string such as `60天` |
| `strategy` | `data.strategy` | `REVERSE_HIGH_SCORE` or `SEQUENTIAL_STEADY`, preserving case |
| `timeZone` | `data.timeZone` | Returned IANA timezone, e.g. `America/Vancouver` |
| `locale` | `data.locale` | `zh` or `en` |
| `restDayMode` | `data.restDayMode` | `NONE`, `SUNDAY` or `WEEKEND` |

Format example only — never copy these sample values unless they are the actual confirmed result:

```json
{
  "mode": "calendar",
  "scope": "listening",
  "startsOn": "2026-09-28",
  "totalDays": 60,
  "strategy": "REVERSE_HIGH_SCORE",
  "timeZone": "America/Vancouver",
  "locale": "zh",
  "restDayMode": "SUNDAY"
}
```

Before calling `save_study_plan`, compare each of the seven outgoing values with the corresponding field of that one result. Do not combine fields from different previews, use remembered conversation values, substitute an exam date for `startsOn`, or recompute `totalDays` from dates. User modifications invalidate the previous preview: regenerate first, then use the new confirmed result. If the final successful result is missing or the local date has changed, regenerate and confirm instead of guessing. Do not add `examDate`, `endsOn`, `days`, `rounds`, `workload`, `userId`, `horizon`, `plan`, or card text to the calendar save arguments. Only a successful save response containing `saved: true`, `recordRef`, and `savedAt` permits a success receipt.

### Two confirmation paths

Calendar cards have a “确认并保存 / Confirm and save” button. Clicking it is the user's confirmation of that card's seven parameters; the component calls the same `save_study_plan` directly, without model transcription. Briefly mention the button when presenting an unsaved calendar. Keep conversation saving available: if the user says to save the confirmed preview, use the exact-argument workflow above. Do not save automatically just because a card was generated.

Both paths reuse an existing saved record for the same account and exact seven parameters. A successful component result is authoritative; do not issue another model save merely to acknowledge it. If a model save definitively fails before writing (`INVALID_INPUT`, `FORBIDDEN`, `AUTH_REQUIRED`, `RATE_LIMITED`), explain the applicable correction and offer the existing card button after it is resolved. Regenerate a card only if it is unavailable or its parameters/date need changing. For a timeout or `SAVE_UNCONFIRMED`, first use the lightweight planning read to compare the saved record's seven parameters; if it matches, report the actual saved receipt. Otherwise state that saving is unconfirmed, without automatic retry. Do not tell the user to click again before checking. The card performs this same bounded check after an uncertain button save and never automatically repeats a write.

## Existing short text plans

Create one realistic plan and render one plan card.

1. Establish scope, horizon, available time, and a valid IANA timezone. Ask for missing time or timezone when it affects the plan; never silently use UTC for a user schedule.
2. Call `get_learning_context` with `showDiagnosisCard: false` for planning facts and reuse a current evidence-bounded diagnosis when available. Use `list_available_practice` for real training entries and timing guidance. Use `get_topic_catalog` only for writing/speaking topic inventory, and `get_practice_question` only when the user explicitly needs one concrete exercise.
3. Do not invent durations, unseen questions, remaining topic counts, or mastery. Keep `today`, `next7Days`, and `next30Days` inclusive of the user's local current date rather than calendar-week or calendar-month boundaries.
4. Before saving, call `render_study_plan_card` with `awaiting_confirmation` and show the exact title, steps, dates, time budget, and links. Ask the user to confirm that exact content.
5. Call `save_study_plan` only after explicit confirmation. If any saved content changes, return to `awaiting_confirmation` and ask again.
6. After a successful save, call `render_study_plan_card` with `saved` and copy `savedAt` from the actual save result. For refusal use `declined`; for an uncertain failure use `save_failed`. Never invent success or retry an uncertain write automatically.

Only the calendar confirmation button can initiate a write, after the user's click; other cards remain display-only. Saved plans are historical advice, not evidence that work was completed. Do not create task-tracking state, reminders, or WhatsApp messages in this skill.
