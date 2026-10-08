---
name: readdy-mcp
description: Create, monitor, modify, and inspect Readdy websites through the Readdy MCP server. Use when the user asks to create a website, refine an existing Readdy project, check generation status, answer non-secret generation questions, or inspect projects.
---

# Readdy MCP Website Builder

Use the connected Readdy MCP server to create or modify a Readdy website and keep the user informed until the project is ready or needs their input.

Use only `create_website`, `update_website`, `get_website_status`, `continue_website`, `list_projects`, and `get_project`. Do not invoke tools outside this supported first-release set.

## Authorization and connection

- Installing the Readdy plugin also registers its bundled MCP connection. Do not tell the user to install Readdy MCP separately.
- On first use, call the requested Readdy tool normally. Treat an unavailable MCP tool, an authentication-required response, or HTTP 401 as a connection issue rather than a website failure.
- If the client shows a Readdy **Connect** or **Authenticate** action, pause the workflow and direct the user to use that action. Prefer this direct authorization entry over manual settings navigation.
- In Codex, direct the user to open **Plugins → Readdy → Connect/Authenticate**. If that action is not shown there, use **Settings → MCP servers → Readdy → Authenticate**.
- After browser login and consent complete, tell the user to return to the conversation, then retry the same requested operation once. Suggest starting a new task or restarting the client only when the Readdy tools still do not appear.
- In other MCP clients, direct the user to the Readdy connection in that client's MCP settings and use its authentication action.
- Do not ask ordinary users to run terminal commands for authorization. CLI login is only a development or diagnostic fallback.
- Do not retry a mutating tool while authorization is unresolved.

## Before creating a project

- Use the requirements already present in the conversation. Do not make the user repeat information that is clear.
- Ask only for information whose absence would materially change the result.
- Never include passwords, API keys, access tokens, or other secrets in the website prompt.

## Plan once, then generate one page or task at a time

- Every `create_website` or `update_website` call must cover exactly one page or one independently verifiable task. Do not send a multi-page site specification or several unrelated changes in one generation request; oversized requests can time out.
- A page may include the sections needed to make that page complete. A task may affect multiple pages only when it is one cohesive change, such as replacing the shared navigation or applying one global visual theme.
- Before the first mutating call, turn a multi-page or multi-task request into one concise ordered plan. Ask for approval once when the plan introduces meaningful sequencing, scope, or design choices. Do not ask for approval again after every completed item.
- After the plan is approved, execute its items serially on the same project. Wait for the current job to complete before starting the next `update_website` call. Never start generation jobs for the same project in parallel.
- For a new multi-page website, create the project with the homepage as the first page unless the user explicitly prioritizes another page. Add the remaining pages one at a time with later `update_website` calls.
- Split one page into multiple tasks when it contains several independently complex functional areas, integrations, data flows, or interactive states that would make one generation request unreliable. Start with the page structure and core content, then add each complex function as a focused update. Do not split ordinary content sections merely to create more steps.
- Keep the remaining requirements in the conversation as a backlog, but do not include them in the current tool prompt until their turn. Preserve the user's original intent when moving to the next item.
- Continue through the approved backlog automatically. Pause only for a material missing choice, `waiting_input` that cannot be answered from context, `waiting_secrets`, or a failed job. If the plan must change materially, explain the change and ask for approval once.
- For every `create_website` or `update_website` call, set `scopeType` to `page` or `task` and set `scopeName` to a short name for that one page or task. These fields are required by the MCP server.

## Create and monitor

1. Call `create_website` once with `scopeType`, `scopeName`, and a complete prompt for the selected single page or task. Preserve relevant user requirements and constraints without including the remaining backlog.
2. Pass `projectName`, `framework`, `device`, or `useSelfHostDB` only when the user explicitly chose them or the conversation makes the choice unambiguous.
3. Retain the returned `jobId`. Treat project creation as non-idempotent: after a timeout or uncertain response, do not call `create_website` again unless the user explicitly wants another project.
4. Retain the same `jobId` as the only source of truth for this request. When an MCP App card is visible, let the card monitor the job and do not repeatedly call or narrate `get_website_status`. Without a live card, check the same job sparingly.
5. Handle the returned status:
   - Use only the explicit `status`; the API does not expose percentage progress.
   - For queued, generating, building, or finalizing states, the job is still active. An unchanged state can legitimately last a long time and must never be treated as a timeout, interruption, or failure.
   - For `waiting_input`, follow the Ask handling rules below, call `continue_website` with the original `jobId`, then resume status checks.
   - For `waiting_secrets`, direct the user to the returned Readdy project URL to enter secrets securely. Never request secrets in chat or pass them to `continue_website`.
   - For a failed state, report the returned error and keep the project URL and `jobId` available for diagnosis. Do not create a replacement project automatically.
   - For `completed`, present the preview URL when available and the Readdy project URL for further editing.

## Modify and monitor

1. When the user wants to change an existing website, identify the target project. Use `list_projects` and `get_project` if the project ID is not already known.
2. Call `update_website` once with the project ID, `scopeType`, `scopeName`, and a complete prompt for the selected single page or task while preserving requirements that must remain unchanged.
3. Retain the returned `jobId`. Treat each update as non-idempotent: after a timeout or uncertain response, check known job state before starting another update, and never create a duplicate update automatically.
4. Let the live card monitor the update, or check it sparingly when no card is available. Handle `waiting_input`, `waiting_secrets`, failure, and completion exactly as in the creation workflow, always using the same `jobId` for status checks and `continue_website`.
5. A completed project may be modified repeatedly. Start a new `update_website` job only for a new user-requested change; the server resolves the project's latest editable version for each update.

## Handle generation questions

- Treat the MCP card as status-only. Never instruct the user to answer inside the card.
- First answer from explicit requirements and preferences already present in the conversation.
- When the missing detail is non-sensitive and does not materially change the user's intent, choose a reasonable default that fits the project context and continue automatically.
- Ask the user in the main conversation only when the answer is not available and the choice would materially change the result. Preserve the question and its suggested options.
- For multiple questions, collect or infer every answer, then call `continue_website` once with a numbered answer matching the original question order.
- Never infer passwords, API keys, access tokens, or other secrets. For `waiting_secrets`, direct the user to Readdy as described above.

## Find and inspect projects

- Use `list_projects` when the user refers to an existing project without supplying its ID. Keep pagination bounded and ask the user to choose only when multiple plausible projects remain.
- Use `get_project` to confirm the project identity, access, and URLs before acting on an existing project.
- Prefer the project URL when the user needs to open or edit an existing project in Readdy.

## User communication

- Tell the user when creating a project will consume Readdy resources or credits if that is surfaced by the client or tool.
- Distinguish a queued job from a completed website.
- Never invent progress, project IDs, URLs, or completion states.
- If the user says “continue”, “check again”, or otherwise returns while a known job is active, call `get_website_status` with that original `jobId` before taking any other action. Never call `create_website` or `update_website` again for the same request unless the user explicitly asks for a different project or a new change.
- Do not end an active generation with language that implies completion or interruption. State that the existing job is still running and that the card will resume the conversation when its status changes.
- Prefer the preview URL for viewing the result and the project URL for editing it in Readdy. When an update completes, state clearly that it produced a new project version rather than a new project.
