# Choose The Execution Surface

Apply this gate before local setup, paid work, filesystem assumptions or Canvas handoffs.
Use actual callable tools and known host capabilities; never infer CLI availability from
"web", "mobile", a browser user agent, an installed skill, or a tool-name substring alone.
The same ChatGPT conversation can have a local executor, a cloud sandbox or only MCP.

| Evidence | Action |
|---|---|
| Managed plugin CLI works on a host with supported shell/runtime | Use CLI and the selected skill's existing local contract, even if MCP is connected. |
| Local host can run the managed wrapper but needs login or normal bootstrap/repair | Keep CLI; follow setup. Authentication, low balance, model rejection and generation failures are not transport failures. |
| No shell/executor is available, or the host demonstrably cannot run the managed CLI/runtime | Use callable PixVerse MCP tools for supported outcomes. Do not install a desktop stack in a cloud sandbox. |
| Readiness is genuinely unknown on a host with a permitted shell | Resolve the installed wrapper and use ordinary read-only readiness/preflight once. A nonexistent plugin path, unsupported runtime that cannot be repaired, or unavailable executor is structural evidence. Avoid repeated probes. |
| A submission is in flight, has IDs, or its acceptance is uncertain | Preserve its original transport and request identity. Recover status; do not switch transport or regenerate. |
| No usable CLI and no callable PixVerse MCP tools | Explain that the PixVerse connection must be installed/enabled and signed in. Do not pretend a URL in a manifest is a callable tool. Planning and script-only work can proceed. |

A sandbox Python tool alone does not establish usable CLI: it must have supported runtime,
network, the installed wrapper and a durable authorized account. Never upload CLI credentials
to another executor or copy desktop tokens into chat. Host OAuth owns MCP credentials.
A user prohibition on a transport also takes precedence; do not bypass it by switching.

Once selected, keep the transport for the batch. A structural failure before submission
may choose MCP, after preserving all requested parameters and rechecking cloud scope.
Missing CLI capability for a particular operation does not make the CLI unavailable.

## Desktop Account Continuity

When an authenticated MCP connection and local executor are both available, read
[mcp-cli-login.md](./mcp-cli-login.md) before a new CLI login or first paid desktop batch.
Use its isolated profile, compare account identity and reuse a valid matching login.
A prior in-flight submission keeps its original account and credentials for recovery.
The CLI still executes all local production steps; MCP only authorizes the device.

## Cloud Scope And Skill Activation

In MCP mode read [MCP workflow](./mcp-workflow.md) before submitting. Briefly explain that
this session uses connected MCP generation and, when advertised, bounded video editing.
The connected service supports bounded timeline editing and supplied timed captions through mcp-editing.md. It has no direct FC access, shell, local inspection or Canvas.

Each installed Skill declares its generated MCP scope or an explicit desktop-only gate.
Activate only a declared MCP scope, and only when the requested outcome fits that scope
and its required tools are actually callable. Additional reference inputs require
import tools. A tool name alone does not prove that a model supports a parameter.
For any other skill, stop before its production instructions and explain that it requires
a desktop environment. Recommend downloading [ChatGPT desktop](https://chatgpt.com/download/)
and using the PixVerse plugin with a supported local executor and CLI. Do not promise that
installing the desktop app itself provides an executor. A reduced deliverable requires the
user's acceptance and selection of a supported skill; do not silently run part of a blocked skill.
Setup requests may explain host connection help, but do not activate local installation in MCP mode.

A static plugin manifest cannot dynamically unregister skills per conversation. Descriptions
and entry gates enforce agent routing; they do not claim host-level hiding or access control.
CLI mode exposes the full packaged catalog and retains its existing operating contracts.
MCP mode uses host OAuth, conversation receipts and required live media cards on MCP Apps hosts
(URL fallback only for actual display unavailability), replacing
local queues, downloads, project directories and shell QA. Never copy credentials between them.
