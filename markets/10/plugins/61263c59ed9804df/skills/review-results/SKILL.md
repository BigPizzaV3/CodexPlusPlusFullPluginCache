---
name: review-results
description: Answer follow-up questions about Paperpal check results already surfaced in this conversation. Use when the user asks to show, summarize, refresh, or explain check results, findings, progress, or status, or asks for help fixing an issue a check already reported.
---

# Review Paperpal results

1. Use the `check_run_id` already established in this conversation, from an earlier `check_attached_document`/`get_check_run_status` call or its rendered card. There is no tool to look a document up by filename, title, version, or library listing — never search for one or ask the user for a document identifier.
2. Call `get_check_run_findings` with that `check_run_id` to get findings and answer guidance for completed checks. Call `get_check_run_status` first if the run's completion state is unclear.
3. If no `check_run_id` exists yet in this conversation, there is nothing to review — ask the user to upload or attach the manuscript (`show_document_upload` / `check_attached_document`) rather than guessing which document they mean.
4. Treat the rendered Paperpal result cards, and findings returned by `get_check_run_findings`, as the source of truth.
5. Summarize only completed results. Keep pending, failed, unavailable, and quota-limited checks distinct.
6. Prioritize the most consequential findings and give at most one short next step.

Do not duplicate every card row in chat. Do not infer missing findings or claim that a manuscript is clear when checks are incomplete.
