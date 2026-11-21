# PlatformIO v6 Toolchain and Recovery Boundary

`pio pkg exec` resolves tools from PlatformIO packages. It does not provide a
security sandbox, a PIO Agent approval grant, project policy enforcement, or a
hardware port claim. Do not use it as a fallback for unavailable or denied PIO
Agent operations, and do not install substitute toolchains to bypass a refusal.

**Reference Documentation:** [PlatformIO pkg exec Guide](https://docs.platformio.org/en/latest/core/userguide/pkg/cmd_exec.html)

## Guarded diagnostics

Use the guarded CLI or existing MCP session for device discovery, target
resolution, bounded monitoring, backtrace decoding, firmware size analysis, and
debugging. Keep project, environment, artifact identity, and resolved physical
target explicit; observe each operation's policy and approval requirements.

## Unsupported hardware recovery

Flash erasure, eFuse changes, direct microcontroller utilities, and a manually
launched debug server are not authorized fallback paths. If the guarded interface
does not support the requested recovery, stop and explain the missing capability
to a local operator. Do not execute a raw erase, upload, identity-probing, or eFuse
command, infer a port, terminate an unrelated process, or create an untracked
hardware session.

eFuse writes are irreversible and can permanently disable a device. An operator
must assess the exact board, wiring, command, backups, and effects before a manual
recovery outside PIO Agent. A user's request or consent does not authorize the
agent to bypass an existing project policy or host denial.
