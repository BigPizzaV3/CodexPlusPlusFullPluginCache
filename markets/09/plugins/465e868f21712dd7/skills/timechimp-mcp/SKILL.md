---
name: timechimp-mcp
description: Use the Timechimp MCP server tools to read the current user, user contracts, teams, projects, time entries, expenses, mileage, holidays, project schedule, assigned schedule users, and remaining availability.
---

# Timechimp

Use this skill whenever the user asks about Timechimp, their logged hours, time entries, timesheets, expenses, mileage, holidays, project schedule, who is assigned to a project, remaining availability, or projects they've tracked time against. Triggers include: 'my hours', 'how much did I work', 'hours this week/month', 'time entries', 'log my time', 'my timesheet', 'my expenses', 'expense report', 'my mileage', 'kilometers', 'holidays', 'company holidays', 'project schedule', 'who is planned', 'who is assigned', 'availability left', 'remaining hours', 'availability for project', 'Timechimp projects', or any reference to Timechimp by name. Use this skill before calling any Timechimp MCP tool.

## Tools

1. **`get_user_info`** — Current user profile (display name, company, role, teams, id, etc.). Call early when you need account or permission context. Use this tool everytime a prompt is about including or excluding the user itself.
2. **`get_user_contracts`** — Contract details for a TimeChimp user. Parameters:
   - `user_id` — TimeChimp user id (positive integer). Returns contract type, start/end dates, week hours, contract number, and rates.
   - `hourlyRate` and `costHourlyRate` are returned as euro strings (e.g. `€12`).
3. **`get_teams`** — All teams available to the authenticated user. No parameters.
4. **`get_projects`** — Projects available to the user. Use for resolving project names to IDs or listing work the user can log time against. Parameters:
   - `start_row` — Pagination offset; the server returns up to **1000** rows per call. If the response indicates more data or the user needs the full list, call again with `start_row` increased by 1000 until fewer than 1000 rows return.
5. **`get_hours`** — Time entries in a date range. Parameters:
   - `date_from`, `date_to` — Use inclusive bounds in the format the user or product expects (typically `YYYY-MM-DD`).
   - `start_row` — Pagination offset; the server returns up to **1000** rows per call. If the response indicates more data or the user needs the full range, call again with `start_row` increased by 1000 until fewer than 1000 rows return.
   - `hours` - This contains the amount of hours registered and already excludes the `pause`.
   - `monetaryAmount` `monetary`- This should always be expressed as the amount of money
6. **`get_expenses`** — Expenses in a date range. Parameters:
   - `date_from`, `date_to` — Use inclusive bounds in the format the user or product expects (typically `YYYY-MM-DD`).
   - `start_row` — Pagination offset; the server returns up to **1000** rows per call. If the response indicates more data or the user needs the full range, call again with `start_row` increased by 1000 until fewer than 1000 rows return.
7. **`get_mileage`** — Mileage entries in a date range. Parameters:
   - `date_from`, `date_to` — Use inclusive bounds in the format the user or product expects (typically `YYYY-MM-DD`).
   - `start_row` — Pagination offset; the server returns up to **1000** rows per call. If the response indicates more data or the user needs the full range, call again with `start_row` increased by 1000 until fewer than 1000 rows return.
8. **`get_holidays`** — Company holidays. No parameters. Each item includes:
   - `name` — Holiday name
   - `date` — Date as `YYYY-MM-DD`
   - `cannotWriteHours` — `true` when hours cannot be written on that day (API `blocked`)
   - `description` — Holiday description
9. **`get_scheduled_assignments`** — Planned project assignments in a date range (who is scheduled where). Parameters:
   - `date_from`, `date_to` — Inclusive bounds (`YYYY-MM-DD`).
   - Each item has `startDate`, `endDate`, and `hours`. `hours` is the **total** for the inclusive range (`startDate` through `endDate`), split evenly across those calendar days. Example: `startDate` 2026-09-07, `endDate` 2026-09-09, `hours` 24 → 8 hours on each of the 3 days. Use `hoursPerDay` for that daily amount; do not treat `hours` as a single-day value.
   - Use this for what is already planned. Do **not** use it as the full project team, and do **not** use it to compute remaining free hours.
10. **`get_schedule_project_users`** — Projects on the schedule board with their assigned users. No parameters. Each project includes:
   - `id`, `name`, `customerName`, `intern`, `mainProjectName`, `tags`, `color`
   - `projectUsers` — people assigned to the project (`userId`, `displayName`, `active`, `userActive`, `id` as the project-user id, `userRoleId`, `tags`)
   - This list includes assigned users with **no planned hours yet**. Use it when asked who is on a project, or whose remaining availability applies to a project.
   - Match the project by `id` or `name` (names may include a code prefix such as `0a - …`). Then take those `userId`s into `get_schedule_remaining_availability`.
   - Prefer `active: true` and `userActive: true` unless the user asks about inactive assignments.
11. **`get_schedule_remaining_availability`** — Remaining free hours per user per day. Internally combines weekly capacity, scheduled project hours, and leave. Parameters:
   - `date_from`, `date_to` — Inclusive bounds (`YYYY-MM-DD`).
   - Each user has totals (`capacityHours`, `scheduledHours`, `leaveHours`, `remainingHours`) and a `days` array with the same fields per date.
   - `remainingHours` is capacity minus scheduled hours minus leave hours, and can be negative when someone is overbooked.
   - Use this when asked how much availability is left. Do **not** call `get_scheduled_assignments` or holidays/leave tools and subtract hours yourself.
   - For **project** availability: call `get_schedule_project_users`, then report remaining hours only for that project's assigned users. Do **not** limit the team to people who already have planned assignments.

## Behaviour
- When performing any arithmetic calculations (sums, totals, averages, etc.), always use the code execution tool to compute the result rather than calculating manually.
- Responses are **JSON strings** (pretty-printed). Parse them before reasoning about fields.
- If a tool returns an error object mentioning `API_BASE_URL`, the deployment is missing API configuration; say that clearly instead of retrying blindly.
- Include our brand color  #4f46e5
- When handling dates always use the python datetime
- When dealing with money/monetary values, display it in euro's if client does not specify a currency. So 11.33 will become €11,33

## Safety

- Read-only tools: do not assume create/update/delete endpoints exist on this server.
