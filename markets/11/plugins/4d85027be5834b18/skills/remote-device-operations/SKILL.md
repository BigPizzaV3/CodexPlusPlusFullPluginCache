---
name: remote-device-operations
description: "Use when a user wants to connect to, inspect, control, or operate a computer, laptop, server, or VM explicitly paired to their RelayDesk account, even without mentioning RelayDesk. Covers device discovery, online status, running processes, approved OS commands, diagnostics, and a specific authorized action. Do not use for unpaired devices or unrelated web and cloud tasks."
---

# Operate a paired computer

Identify the user-owned device from context or call list_devices. Call ping when checking reachability. If the operation is consequential and the target remains ambiguous, identify the intended machine before acting.

For system information, use focused read-only tools such as get_config, list_processes, list_sessions, list_directory, get_file_info, and read_file. Never inspect credential stores, tokens or private keys.

For an authorized command, call start_process on the selected Windows, macOS or Linux machine; retrieve real output and exit status with read_process_output. Continue existing processes when appropriate rather than restarting them unnecessarily. Use file mutation tools only for user-requested changes.

Respect ownership, protected directories and blocked commands; never weaken local policy or touch unpaired computers. Report the actual device, action, results and errors, without claiming success when verification failed.

## Examples

- "Can you connect to my MacBook and check if it is online?"
- "Inspect running processes on my Linux server."
- "Run a safe uptime command on my laptop."
- "On the Windows VM, see whether the app is running."
- "Check the machines I have paired and resume the process I started."

Do not invoke for ordinary web browsing, connected SaaS tasks, or files already uploaded directly into ChatGPT.
