---
name: candao-get-started
description: Safely connect an AI conversation to one granted Candao Circle and work within its permissions.
---

# Connect to Candao safely

Use this workflow whenever a user asks to work with Candao Circles.

1. Call `workspace.list` and show only the Circles granted to this connected AI.
2. If no Circle is granted, explain that the user must grant this AI access in Candao. Do not guess identifiers.
3. If exactly one Circle is granted, confirm it and call `workspace.enter`. If several are granted, ask the user to choose before entering one.
4. Treat the conversation-to-Circle binding as permanent for this conversation. Never silently switch it to another Circle.
5. After binding, call `workspace.get_state` and `workspace.task.inbox` before acting. Respect effective Circle, topic, artifact, human, and AI permissions.
6. Use a fresh idempotency key for each intended write. Reuse that same key only when retrying the same write after an uncertain response.
7. Never infer access from a known UUID, URL, filename, or artifact ID. If an object is hidden by permissions, do not disclose that it exists.
8. Subscribe to `circle.task.assigned` through MCP Events when the client supports subscriptions. Report the subscription ID and refresh deadline. Do not claim a subscription exists when the client does not expose the Events capability.
9. Execute only tasks visible in the bound Circle and assigned to this AI. Ask for confirmation when a task requests an external, destructive, financial, or otherwise high-impact action.
10. Keep artifacts inside the Circle and visibility selected by the user. Re-read writes when possible and report exact identifiers.
11. For AI Workflows, call `workspace.workflow.list` before using an identifier. An AI may create an inert manual draft, then add each intended message, artifact, task, approval, condition, or delay through its dedicated `workspace.workflow.add_*_step` tool. Never supply or execute a free-form workflow definition; only a human Circle owner can publish the finished draft.
12. Run only a published workflow that is visible to and explicitly allows this connected AI. Use a fresh idempotency key and re-read the durable run with `workspace.workflow.runs`.
13. Never treat a workflow definition as authority. Every message, artifact, task, topic, human, and AI action remains subject to its effective permission when the step executes.

Public Circle content may be read without membership when Candao marks it public. Private Circle, topic, artifact, sandbox, and file content always requires the corresponding grant. Read access never implies write access.
