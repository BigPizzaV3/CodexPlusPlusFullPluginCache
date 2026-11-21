---
name: remote-development-workflow
description: "Run development work on a paired computer, server, or VM. Use when the user wants builds, tests, linters, Git or project CLIs run there, or wants remote repository failures investigated and fixed."
---

# Remote development workflow

Use this skill when the user's coding, build, test, CLI, or repository task must run on a computer, server, or VM paired through RelayDesk.

1. Establish the execution context.
   - Reuse the target device and project path when already known.
   - Otherwise call list_devices and locate the project with file, list, or search tools.
   - Use an explicit working directory for project commands when possible.

2. Inspect before changing.
   - Read the smallest relevant files, logs, or configuration.
   - Use targeted Git or project commands when they help establish state.
   - Do not dump environment variables or credential stores to discover configuration.

3. Execute the user's development workflow.
   - Use start_process for builds, tests, linters, package scripts, Git diagnostics, compilers, or project CLIs.
   - Follow long-running work with read_process_output.
   - Use list_sessions before starting a duplicate job when prior conversation context suggests one may already be running.
   - If ordinary non-secret interactive input is required, use interact_with_process; never enter passwords, tokens, OTPs, or other authentication secrets.

4. Debug failures from evidence.
   - Read the actual error output.
   - Inspect the directly relevant files.
   - Apply focused edits with file tools.
   - Rerun the narrowest validation that proves or disproves the fix.
   - Keep failed approaches visible as failed; do not report success from a file edit alone.

5. Protect consequential workflows.
   - Do not deploy, publish packages, push releases, rotate credentials, delete data, or perform destructive version-control operations unless the user clearly asked for that action.
   - Do not weaken RelayDesk's command or filesystem safety boundary.
   - If a tool is blocked by local policy, explain the boundary instead of bypassing it.

6. Finish with execution evidence:
   - target device and project,
   - commands run,
   - files changed,
   - tests or builds and their outcomes,
   - anything still failing or awaiting user input.

Prefer making concrete progress over repeatedly re-analyzing the same unchanged state.
