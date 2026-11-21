---
name: remote-device-troubleshooting
description: "Diagnose problems on a paired computer, server, or VM. Use when the user wants to inspect a failing app, process, local logs, configuration, or machine state and troubleshoot or fix the issue."
---

# Remote device troubleshooting

Use this skill when the user wants you to inspect, diagnose, or help fix a problem on a computer, server, or VM they own or administer.

1. Resolve the target machine.
   - If the target device is already unambiguous from the conversation, keep using it.
   - Otherwise call list_devices.
   - Ask the user only when multiple plausible paired devices remain and choosing the wrong one could matter.

2. Start with the least invasive evidence that can answer the question.
   - Use ping, get_config, list_processes, get_file_info, list_directory, read_file, read_multiple_files, or search tools as appropriate.
   - Prefer evidence from the failing process, relevant logs, config, and nearby files over broad system sweeps.
   - Do not invent a root cause when the available evidence is inconclusive.

3. Use commands only when they materially improve diagnosis or execute a user-requested fix.
   - Use start_process for targeted diagnostics, builds, CLIs, or other commands that the user wants run.
   - Read long-running output with read_process_output; use list_sessions when a process may already be running.
   - Treat tool errors and safety-policy rejections as real outcomes. Do not weaken RelayDesk's local policy to force a command through.

4. When the user asks to fix the problem, make the smallest justified change.
   - Explain or infer the intended change from the user's goal.
   - Use file, configuration, or process mutation tools only when necessary.
   - Re-check the affected process, file, or command after the change so the final answer distinguishes "changed" from "verified fixed."

5. Respect RelayDesk's security boundary.
   - Never use RelayDesk to obtain passwords, API keys, auth tokens, MFA or OTP codes, passphrases, private keys, payment-card data, protected health information, or government identifiers.
   - Do not ask to change blockedCommands or allowedDirectories remotely.
   - If authentication is required, tell the user to complete it locally on the paired device.

6. Report a compact evidence-based result:
   - target device,
   - what was checked,
   - evidence found,
   - action taken, if any,
   - verification result,
   - remaining uncertainty or next safe step.

Do not invoke RelayDesk merely because the user asks a technical question. Use it when the task genuinely requires access to one of their paired machines.
