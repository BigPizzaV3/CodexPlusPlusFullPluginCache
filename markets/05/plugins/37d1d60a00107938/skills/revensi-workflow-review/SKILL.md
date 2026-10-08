---
name: revensi-workflow-review
description: Review an existing Revensi workflow map for unanswered questions, decision gaps, handoffs, and readiness for human review. Use when the user asks what is missing or wants a map checked; do not edit or publish it.
---

# Revensi Workflow Review

Use `list_workflows` to identify the intended workflow, `get_workflow` to inspect its map, and `list_workflow_questions` to fetch the server's open blockers and questions. If the user only asks for questions, call `list_workflow_questions` directly with the available workflow, department, priority, or state filters; paginate until the requested set is covered. Ask the user to choose if several workflows match. Do not treat a workflow title alone as enough evidence to select one.

Summarize the purpose, trigger, inputs, ordered steps, decisions, handoffs, review, and output. Separate:

- structural gaps that prevent a useful end-to-end map;
- open blockers and unanswered questions returned by Revensi;
- optional refinements that should not hold up review.

For each material gap, ask the smallest concrete follow-up question. Do not invent criteria, outcomes, system names, role ownership, effort, or expected savings. Connector catalog records and workflow mentions do not indicate a live connection or permission grant.

This skill is read-only. It may suggest changes but must not create, update, score, publish, or run a workflow.
