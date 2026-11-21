---
name: "client-rollup-sheet"
description: "Build a monthly spreadsheet report for an agency: one row for each project or client with all, branded, and non-branded visibility, top rival, and recommendations."
---

# Client rollup sheet

Use this guidance to build one sheet with a row for each project. It is for an agency or a team that reports on many businesses and prepares the same summary each month.

## Build the sheet

1. Call `list_projects`. Use every project that has a `latest_scan`. List the projects with no finished scan below the table.
2. Make one row for each project. The row key is the project `id`. Put it in the last column and never change it.
3. Fill the Frontmost AI columns from `metric_breakdown`, `top_rivals`, and the recommendation fields:

| Column | Value |
|---|---|
| Project | `name` |
| Scan Date | `latest_scan.delivered_at` as a date |
| AI Visibility, All Questions | `total.visibility`: the rate, then `named` of `answers` |
| AI Visibility, Branded | `branded.visibility`, the same way |
| AI Visibility, Non-Branded | `unbranded.visibility`, the same way |
| Change, Non-Branded | `unbranded.visibility.change` |
| Top Rival | the first entry of `top_rivals`: its `name` and `answers` |
| Open Recommendations | `open_recommendations` |
| Top Recommendation | the title of `top_recommendation` |
| Link | `url` |

4. Write each rate with its counts in one cell, such as "22% · 8 of 36".
5. Add the columns that the person fills in: Client Contact, Sent On, Note. Leave them empty.
6. Sort by Change, Non-Branded. Put the largest fall first, because that client needs a call first.
7. Above the table, write the day of the report and the number of projects.

## Refresh the sheet

1. Call `list_projects` again.
2. Match each project to a sheet row by the project `id`. Rewrite only the Frontmost AI columns.
3. Keep Client Contact, Sent On, Note, and each column that the person added.
4. Add a row for a new project. Keep the row of a project that the data no longer returns, and write "Not in this workspace now" in Scan Date.
5. For a monthly report, keep last month's sheet as it is and build the new month as a new tab.

## Rules

- Never show one visibility number alone. Always show all questions, branded, and non-branded side by side.
- Non-branded is the number that shows if new buyers find the business. Say this once below the table.
- Do not add or average rates across projects. Each project has its own questions.
- Compare a project only with its own previous scan. Scan dates differ between projects.
- A rate from few answers moves a lot between scans. The counts show this, so never drop them.
- Do not put one client's data in a file for a different client. Ask which projects the report covers when the person sends it outside their team.
- Ask before you change anything in Frontmost AI. This sheet reads only.

## Output

A spreadsheet file that opens in Excel, with one table and the report day above it. Then three lines: the largest rise, the largest fall, and the project with the most open recommendations. If the AI app cannot make a file, return the table as CSV.
