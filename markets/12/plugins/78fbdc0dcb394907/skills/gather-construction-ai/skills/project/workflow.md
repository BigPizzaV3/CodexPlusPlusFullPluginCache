---
name: project
description: Show project overview — team, status, recent activity, who's assigned.
  Not for financial or cost queries (API exposes no contract sums or rates).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Project Overview

Show a structured overview of a Gather project — status, team, and recent shift activity. This is the starting point for most workflows and the skill users invoke first when orienting themselves.

Follow the shared patterns: `../../shared/patterns/01-project-resolution.md` (project resolution); `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: List or Identify the Project

**If `the user’s request` is empty** (user just typed `$project` with no argument):

1. Call `getMyProjects` to retrieve the user's assigned projects.
2. Present the results as a formatted table:

| # | Project Name | Status | Tags | Your Role |
|---|---|---|---|---|
| 1 | Example Project Alpha | Active | rail, civils | Project Manager |
| 2 | Example Project Beta | Active | highways | Viewer |

3. If the user has **exactly one project**, skip the table and proceed directly to Step 2 with that project — no need to ask. State explicitly which project was auto-selected: "Using your only assigned project: [name]."
4. If the user has **multiple projects**, show the table and ask: "Which project would you like to see? You can reply with the name or number."
5. If the user has **zero projects**, call `getProjects` to list all workspace projects instead. If that also returns nothing, inform the user that no projects are available in the workspace.

**If `the user’s request` contains a project name:**

1. Resolve the project using **Pattern 1 (Project Resolution)** from `../../shared/patterns/01-project-resolution.md`.
2. Once resolved, proceed to Step 2.

---

## Step 2: Retrieve the Project Team

Call `getProjectAssignments` with the resolved project UUID.

Present the team as a formatted table:

| Name | Job Title | Role |
|---|---|---|
| Jane Smith | Senior Site Engineer | Project Manager |
| Tom Williams | Site Supervisor | Contributor |
| Sarah Brown | QS | Viewer |

If no assignments are returned, state: "No team members are currently assigned to [project name]." This may indicate the project is newly created or assignments have not been configured.

---

## Step 3: Retrieve Recent Shift Activity

Call `getCachedReport` with the following parameters:
- **Report name:** `dashboardShiftTable`
- **Project:** the resolved project UUID
- **Date range:** last 4 weeks (today minus 28 days to today)

From the returned data, extract and calculate:
- **Total shifts** recorded in the period
- **Active supervisors** — distinct supervisor names who recorded shifts
- **Date range of activity** — earliest and latest shift dates in the data
- **Shifts per week** — total shifts divided by the number of weeks between the first and last shift in the returned data (not the fixed 4-week window). If activity started mid-window, use the span of actual activity and state that the average reflects only the active period.

If the report returns no data, follow **Pattern 3 (Empty Data Handling)** from `../../shared/patterns/03-empty-data-handling.md` — state that no recent shift activity was found and suggest possible causes (wrong project, no shifts recorded recently, etc.).

---

## Step 4: Present the Project Overview

Combine all retrieved data into a structured overview with clear sections:

### Project Details

| Field | Value |
|---|---|
| **Name** | [project name] |
| **Status** | [status from getMyProjects/getProjects] |
| **Tags** | [comma-separated tags, or "None" if empty] |
| **Your Role** | [role from getMyProjects — omit this row if the project was resolved via the getProjects fallback, where the user is not assigned and no role is available] |

### Team

[Table from Step 2 — all assigned members with name, job title, and role]

### Recent Activity (Last 4 Weeks)

| Metric | Value |
|---|---|
| **Total Shifts** | [count] |
| **Active Supervisors** | [count] ([list of names]) |
| **Date Range** | [earliest date] to [latest date] |
| **Average Shifts/Week** | [calculated average] |

---

## Related Skills

After presenting the overview, suggest these related skills for deeper analysis:

- `$diary` — Search and review individual shift records for this project
- `$labour` — Analyse labour hours breakdown by person and period
- `$commercial-report` — Generate a full commercial period report for this project
