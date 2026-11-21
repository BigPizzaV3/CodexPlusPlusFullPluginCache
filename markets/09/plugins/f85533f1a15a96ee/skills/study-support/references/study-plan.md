# Study Plan

Use this skill when a student asks for a study plan, wants to revise their active plan, asks what to study today, or reports progress on a plan task.

## Create a plan

1. Run the normal account preflight. Continue only when onboarding is complete and `prepare_study_plan` is enabled and operational.
2. Use seven days when the student does not request a duration. Ask how many minutes they can reliably study each day if they have not said; do not invent availability.
3. Call `get_study_plan_insights` with the agreed duration and daily minutes. Treat its primary exam, guidance, recent mocks, vital memories, and active plan as authoritative. Do not claim a weakness without mock evidence or a clearly labelled self-report.
4. Only one study plan can be active. If one exists, offer to update it or replace it. Before replacement, name the current plan and explain: "Saving this new plan will archive [current plan title]. Its tasks and progress will remain in your history. Do you want to replace it?" A request to draft or create a new plan alone is not confirmation to archive the existing plan. Wait for explicit agreement.
5. Draft a practical plan in the conversation. Give every day one primary, independently completable task that the student can do with MockMentor in chat and that fits the daily limit. A task may contain a short sequence, such as an explanation followed by practice questions, but do not split the day's focus across unrelated goals. Prioritize observed improvement areas while retaining revision, practice, and review of strengths across the plan.
6. After the student agrees to the draft and any replacement, call `save_study_plan` once with the complete plan and a stable request ID. For replacement, pass `replaceActivePlan: true` and `expectedActivePlanId` from the confirmed `activePlan.id`. Otherwise omit both fields. Reuse the request ID and identical inputs on retries. If the tool reports that the active plan changed, reload insights and get fresh confirmation for the current plan; never automatically substitute its ID. Use the requested number of sequential days. Confirm the returned plan summary and dashboard link, and mention archival when replacing; the full schedule is already in the agreed draft.

## Revise or follow a plan

- Before revising, call `get_study_plan_insights` so task and day IDs come from the active plan. The default response includes seven days; follow `daysPage.nextCursor` using `dayCursor` to retrieve later task IDs before editing them. `update_study_plan` overwrites the supplied saved content without revision history, while preserving task completion state. Apply clearly specified edits the student requested; for an ambiguous request, show the proposed changes and obtain agreement before saving.
- For "what should I study today?", call `get_todays_study_tasks` with the student's current local date when known, then summarize the returned tasks in order.
- When the student says they started, completed, skipped, or reopened a task, identify the task from the latest tool result and call `set_study_task_status`. Never mark progress from an assumption.

Apply the guardrails skill's educational tone and accuracy guidance to plan copy and follow-up. The database stores the plan and task state; the conversation may summarize it, but must not invent saved progress.
