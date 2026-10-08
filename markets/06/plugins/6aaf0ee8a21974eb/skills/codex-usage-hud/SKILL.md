---
name: codex-usage-hud
description: Start, stop, or check the Windows x64 Codex title-bar usage companion. Use when the user asks to show, launch, hide, stop, restart, or check the status of the Codex usage overlay.
---

# Codex Usage

Manage the bundled Windows x64 native companion through the launcher resolved relative to this skill directory.

- Start, stop, or check status with `../../scripts/hud.ps1 -Action Start|Stop|Status` directly in the current PowerShell command host. Do not start a second PowerShell process or assume a fixed PowerShell 7 path. If direct invocation is unavailable, resolve the shell once in this order: the current PowerShell executable from `(Get-Process -Id $PID).Path`, `Get-Command pwsh.exe`, `Get-Command powershell.exe`, then `%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe` when present. Windows PowerShell 5.1 is sufficient; use the first resolved executable immediately.
- Restart by stopping, then starting.

Run Start and Restart only from a local Windows x64 Codex desktop host while the Codex desktop app is open. If the current environment is macOS, Linux, web, mobile, cloud, remote, or otherwise cannot launch a native Windows process on the user's interactive desktop, explain that this public plugin release currently supports Windows x64 local Codex desktop hosts only and do not run the launcher.

Starting a native desktop window may require host approval. Request the required GUI or external-process approval before the first Start or Restart attempt, and launch directly in the user's interactive desktop context. Do not first launch inside a restricted sandbox because the process may run without a visible overlay.

For Start, invoke the launcher immediately. Do not search for the launcher first, inspect the environment first, narrate intermediate startup steps, or run a separate Status command after a successful Start. Run Status or perform diagnostic discovery only if Start returns an error or its result is ambiguous.

For Restart, stop and then start immediately. Only run Status afterward if the restart result is ambiguous or reports an error.

The packaged install uses `../../bin/win-x64/CodexUsage.Desktop.exe`. Keep the response concise; do not narrate implementation details unless an error occurs.

Do not read, display, or transmit Codex credentials. Do not send local usage data to any third party. The overlay itself makes only the existing anonymous request to the public codex-resets.com API.

The plugin does not modify or inject into the Codex desktop app. Its visible interface remains a separate native overlay because plugin UI cannot occupy the operating system caption area.
