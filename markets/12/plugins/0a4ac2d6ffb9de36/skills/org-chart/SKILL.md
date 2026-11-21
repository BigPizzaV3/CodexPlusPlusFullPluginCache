---
name: org-chart
description: Turn a list of people and who they report to (typed, pasted, or a CSV/XLSX file) into a laid-out org chart with downloadable SVG and PDF files using the make_org_chart tool.
---

# Zovo Org Chart Maker

Use `make_org_chart` whenever the user asks for an org chart, an organizational chart, a company hierarchy chart or a team structure chart.

1. Turn the request into people records with `name`, optional `title`, `department`, and `manager`. A record with no `manager` is a top person.
2. Match each `manager` to a person by exact `id` or by case-insensitive `name`. Leave `manager` blank for the person at the top.
3. If the user's list already has the people and who reports to whom, call the tool right away. Ask one short question only when the people are missing.
4. Options: `orientation` (`top_down` default or `left_right`), `color_by` (`department` default, `level`, or `none`), and `paper` (`letter` default, `a4`, `a3`, `tabloid`) for the landscape PDF.
5. If the user attaches a CSV or XLSX file, pass it as `file`; the header row is matched case-insensitively for id/name/title/manager/department. Do not retype the file's rows yourself.
6. After the tool returns, share the counts (people, levels, departments), every warning verbatim, and the SVG and PDF download links. Mention that the links expire in about one hour.

Do not use this skill for family trees, flowcharts, seating charts, or to read a photo or PDF of an existing chart.
