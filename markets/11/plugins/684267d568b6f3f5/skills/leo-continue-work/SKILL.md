---
name: leo-continue-work
description: Use when the person asks you to continue, pick up, finish or hand over a Leo task, or to bring an existing client or project into Leo from what they tell you.
---

# Continuing and handing over work in Leo

> Work in Leo only through its tools, or the Leo CLI when the tools are not loaded. Never operate Leo's web app in a browser on the person's behalf: that records your work as theirs, and no record can say otherwise afterwards. If the tools are missing after the person connected Leo, ask them to start a new chat so the tools load.

Leo is the continuity between agents. Another agent (possibly a different model) may have worked on this before you, and another will continue after you. Neither of you needs the other's conversation: everything durable is in Leo.

## Continue a task

1. `get_context_package` with scope `task` and the task id. Read the latest handoff, the decisions, the open questions and the prior runs.
2. If another agent's run is still live, tell the person and ask before passing `takeover`.
3. `start_task_run` with a one-line objective. Do the work.
4. `report_run_progress` for real progress, discoveries, blockers and decisions that need a person. Not a heartbeat.
5. `publish_artifact` for what you produce, linked to the task.
6. `finish_task_run` with an honest outcome and summary. If you stop before the end, `hand_off_work` instead, with the next steps and open questions. Your run ends with the handoff.

## Bring a project into Leo

Work only from what the person tells or shares with you in this conversation. Never bulk-import, and never invent.

1. Check the project is not already in Leo (`search`, `list_projects`).
2. Ask what should survive: purpose and outcome, decisions already taken (when and by whom), facts and constraints that still hold, risks, open questions, and the work that is genuinely still open. Leave out what is finished and no longer matters.
3. Propose the structure in plain words and wait for confirmation.
4. Write it: `create_project` with a `source`, `record_project_decision`, `record_context`, `add_project_reference`, and `create_task` only for open work.
5. Finish with `get_context_package` for the project, and tell the person what Leo now knows and what it still does not.
