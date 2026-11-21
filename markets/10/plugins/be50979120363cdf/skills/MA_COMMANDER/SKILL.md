---
name: MA Commander
description: Safely inspect and manage an authorized remote Windows computer through MA Commander, including files, processes, development commands, WSL workspaces, transfers, screenshots, guarded GUI actions, and typed privileged operations.
---

# MA Commander Skill

Use MA Commander as a capability-oriented computer agent, not as an unrestricted shell.

## Operating rules

Before modifying a repository, inspect its current state and relevant files. Prefer narrow, reversible edits. Run the smallest meaningful validation first, then the full project test suite before committing.

Do not bypass MA Commander safety policy. Never attempt raw-disk, format, partition, EFI/BCD, recovery destruction, or protected-root deletion. Do not turn GUI control on implicitly; GUI input requires explicit local policy enablement.

For Windows-specific elevated work, use the privileged broker only through exposed typed operations. Do not try to obtain or simulate an unrestricted Administrator shell.

For AI/development work in Linux, prefer an MA Commander isolated WSL workspace. Do not access `/mnt/c`, `/mnt/d`, or other Windows mounts from an isolated workspace unless the user explicitly requests a Windows-integrated workflow.

For large file writes or uploads, prefer resumable transfer operations with SHA-256 verification. For remote access, prefer the direct relay/MCP route; GitHub is a repository and optional fallback, not an execution dependency.

When a tool changes state, verify the resulting state before reporting success. Commit or push only after validation passes, unless the user explicitly asks for a different workflow.
