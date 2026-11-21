---
name: remote-execution
description: Use when a task needs filesystem, command, or process work on a computer connected through RemoteCommander, including cross-conversation continuation.
---

# Remote execution

Use RemoteCommander's existing MCP tools to operate on the user's connected computers. This Skill is instructions, not an additional execution mechanism.

## Workflow

1. Begin a new conversation with `memory` `op=recall`, using the user's actual request as the hint. Then call `fs` `op=roots` to see the effective base, allowed roots, and read-only mode.
2. If there is more than one connected computer, use `list_devices` and select the computer identified by the user's request or by explicit project context. Pass `deviceId` consistently; do not silently switch devices.
3. Prefer `fs` operations to inspect or edit files. Use `exec` for bounded commands and `process` for long-running or interactive commands. No shell is implicit in `exec`: pass argv directly or invoke an explicit shell.
4. For long-running work, `process op=start` returns a handle; obtain output and completion with `process op=status` and `process op=read`. Do not treat process start as task completion.
5. Observe approval and permission responses. If a tool returns a pending approval, wait for the human's decision; never forge a confirmation value.
6. Verify important effects with a fresh read, status check, or tool result. State what was observed, and distinguish attempted actions from confirmed outcomes.
7. At the end of the reply, use `history op=checkpoint` to record what ran and inspect open or unresolved work.

## Device-local Skills

`memory op=recall` may include the catalog of Skills available on the selected computer. If a Skill matches the task, first read its exact listed `SKILL.md` using `fs`, then follow its applicable instructions. Do not guess locations or assume that a Skill included in the ChatGPT plugin exists on the computer.

## Recovery

If the conversation has lost context, recall the relevant project or thread from `memory`, inspect current repository/environment state, and continue only from evidence that can be established. Keep checkpoints minimal: persist goals, decisions, unresolved blockers and resume pointers; recover reproducible facts from the device later.
