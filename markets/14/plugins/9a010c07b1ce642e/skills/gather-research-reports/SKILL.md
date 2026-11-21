---
name: gather-research-reports
description: Run a Gather customer research report for a company and a business question, then share the report link and the findings. Use when the user asks Gather to research customers or to test messaging, positioning, pricing or a product concept.
---

# Gather research reports

1. Make sure you have the company (and its website if the user knows it) and the question or decision to inform. Ask only for what is missing. Ask about the audience only if the user has one in mind; otherwise Gather picks it.
2. Call `gather_report_start` once. When the user names the options to compare (messages, taglines, names, prices or concepts), pass them in `options` exactly as written. Share the report link right away: it shows live progress, then the finished report.
3. Call `gather_report_check` with the report id about once a minute until the status is `completed` or `failed`. Reports with 10 interviews take about 10 minutes, and 30 interviews about 16 minutes. If the user does not want to wait, tell them the link will show the report when it is ready and that Gather emails it to them.
4. When the report is completed, share the headline, the answer, the key findings and the report link.
5. Say that the results come from simulated interviews and are directional, not a survey of real people.
6. To find an earlier report, call `gather_report_list`.
7. For the user's own Gather workspace, use its tools: `gather_research_answer` for questions about their customers, `gather_find_quotes` for quotes, `gather_list_studies` for studies and their status, `gather_list_personas` then `gather_ask_persona` to ask a persona, and `gather_design_study` to design a study with real people (relay its questions as written, pass the `study_id` it returns on every later call, and set `approve` to true only when the user approves the plan). Call `gather_launch_study` only when the user explicitly says to launch that study.
8. If `gather_report_start` says this month's reports for the workspace are used up, tell the user when they reset.
