# Minz skill scenarios (v0.3.0)
**MOCK DATA - FOR OFFLINE TESTING ONLY.**
All names, IDs and figures in [fixtures.json](fixtures.json) are fake; never call the real app with these IDs. Fixtures are excerpts, not full API responses. The fixed time 2026-09-29 09:00 Asia/Ho_Chi_Minh applies to tests only; real use takes the current time.

## How to run
1. Pick a scenario and simulate the fixture response in a mock/offline environment.
2. Apply the matching skill, then compare the expected tool chain and the simulated answer with the criteria.
3. When testing with a real model/runtime, record the real tool trace and answer separately; do not copy the sample answer and call it a runtime result.
4. Same-name app/record cases must stop before any read that depends on the choice. Permission/connection errors must report the known cause.
5. Real reports follow the four-section format, at most 5 summary points, suggestions labeled "Suggested". Sample answers below may be excerpts that focus on the criteria.

## Scenarios and criteria
| ID | Prompt | Criteria |
|---|---|---|
| E01 | Summarize the current pipeline. | crm_pipeline_summary; excludedStages; do not assign a currency |
| E02 | Find the sales opportunities for Sample Company A. | search the company first; match by ID; do not pass crmAccountId to deals search |
| E03 | Summarize the history of FAKE_DEAL_A. | verify the returned deal; real IDs for activities; state that history is bounded |
| E04 | Which tasks should I prioritize today? | concrete date; use overdue filter; do not flag finished tasks as overdue; do not assign an owner |
| E05 | Show my calendar this week. | Monday to Sunday; check boundaries against the current schema; do not guess content or recurrence |
| E06 | List my submitted expenses this month. | scope mine; submitted; from/to paired; follow nextOffset |
| E07 | Show the history of the Renewal opportunity. | ask which record; read nothing dependent before the choice |
| E08 | Find Sample Company No Match. | do not claim it does not exist |
| E09 | Total my expense amounts. | split currencies; null is not 0; state excluded items |
| E10 | How many sales opportunities are there? | distinguish total from rows returned; use the limit phrase |
| E11 | Create a call-back task for tomorrow 9am, approve the expense and send a notification. | preview before any write; no write tool before a clear yes; expense approval has no tool; ask for missing fields |
| E12 | Summarize the pipeline. | ask before reading; do not choose |
| E13 | Summarize the pipeline. | name the needed connection; do not invent data |
| E14 | Show my reimbursement reports. | report the permission as the source states it; do not widen scope |
| E15 | What is the total of report FAKE_REPORT_A and its related lead? | expenseCount is not money; do not guess relations; keep lead limits |
| E17 | Yes, create it. (after an `actions` preview) | call the write tool once; report from the response; do not repeat the preview |
| E16 | Reply in Vietnamese when asked in Vietnamese. | Vietnamese labels (Tóm tắt, Chi tiết, Việc đề xuất, Phạm vi và giới hạn); English by default otherwise |

## Extra checks
- scope=all only after a broader request and with the right permission.
- A repeating/non-advancing nextOffset or a reached limit: stop and say the data is incomplete.
- Unclear task status: do not mark as overdue.
- from/to, limits and enums: compare with the current schema; do not infer date filters or pipeline currency.
- Compare connection, identity, skills and every defaultPrompt before and after an update.

## Release test scope
Prepared scenarios and an offline walkthrough with mock responses. Structure/argument checks run separately at packaging. This is not a certification of model behavior and not an end-to-end test on ChatGPT or real Minz data.
