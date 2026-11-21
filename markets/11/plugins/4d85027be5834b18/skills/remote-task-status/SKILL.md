---
name: remote-task-status
description: "Read the status and output of a task already running on a computer paired through RelayDesk, without starting, resuming, repeating, or modifying the task."
---

# Inspect remote task status

Use this skill only to answer a user's request for the status or output of a task that was already started on their paired device.

- Identify the specific paired device and existing task session the user referenced.
- Read only the existing session status and already-produced output needed to answer.
- Summarize what finished, what is still running, and any observed errors.
- Do not start, resume, repeat, restart, terminate, or otherwise modify any task or process.
- Do not send input to an interactive process.
- Do not change files, configuration, permissions, safety controls, or device state.
- If the user asks to continue or change the task, hand off to the relevant dedicated workflow and require that separate user-requested operation.
- Report only observed results and clearly state uncertainty.
