---
name: cache-stats
description: Set up, verify, use, update, or uninstall the bundled local Cache Stats runtime on ChatGPT for Windows; show verified prompt-cache usage; or diagnose Responses API cache misses. Use when the user invokes Cache Stats, asks about cached, fresh, or cache-write tokens, requests local setup or removal, or asks about prompt_cache_diagnostics.
---

# Cache Stats

Use the bundled Windows scripts for installation lifecycle operations. Use only the registered MCP tool for cache statistics.

## Route the request

- For the immediately preceding ChatGPT/Codex response, use **Show cache usage** below.
- For Responses API `prompt_cache_diagnostics`, read [the diagnostics reference](references/prompt-cache-diagnostics.md) and follow it. This mode can explain a supplied diagnostic result or help the user update their API request.
- Do not imply that the local runtime can request or reconstruct Responses API diagnostics. It reports host-recorded usage only.

## Show cache usage

1. Find the available MCP tool named `show_cache_stats`. Its qualified tool name may include a server prefix.
2. Call it exactly once with no arguments.
3. Present its card and concise fallback text without recomputing or relabeling any value.
4. Describe cached tokens as reused input-prefix tokens and cache-write tokens as eligible input stored for later reuse. Never describe the response itself as cached; output tokens are newly generated.
5. Non-cached input includes cache-write input; do not add those counts together. The runtime retains the field name `freshInputTokens` for compatibility. Cache reuse percentage measures input tokens, not cost savings.

Never read task transcripts, session telemetry, or shell output as a fallback. If the MCP tool is unavailable or returns an error, report the exact error and offer setup or repair.

## Diagnose a Responses API cache miss

Read [references/prompt-cache-diagnostics.md](references/prompt-cache-diagnostics.md) completely before advising on or interpreting diagnostics.

- Preserve the user's chosen model and application structure.
- If the user supplies `prompt_cache_diagnostics`, explain the reported type, reason, token estimates, and suggested fix. Do not infer additional reasons.
- If no diagnostic result exists yet, show how to compare a new request with a recent completed baseline. Do not claim a comparison was run.
- Use the current response's `usage.input_tokens_details` for actual cache reuse and billing, not the diagnostic estimates.
- Link to the [official Prompt cache diagnostics guide](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics).

## Set up or repair

1. Confirm the environment is ChatGPT for Windows and that local command execution is available.
2. Explain that setup will:
   - copy the reviewed runtime to the current user's local application-data folder;
   - add one `cache-stats-local` MCP registration to the user's ChatGPT/Codex configuration;
   - use Windows PowerShell without administrator privileges or network access.
3. Ask for explicit confirmation before changing the machine.
4. After confirmation, run:

   `powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File <skill-directory>\scripts\install-cache-stats.ps1 -ConfirmInstall`

5. Report the script's exact result. If successful, tell the user to restart ChatGPT for Windows and open a new task before invoking Cache Stats.

Do not pass `-ConfirmInstall` until the user has confirmed the disclosed changes. Do not download code or substitute files from the internet.

## Check status

Run:

`powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File <skill-directory>\scripts\status-cache-stats.ps1`

Use status only to diagnose installation. Do not derive cache statistics from it.

## Uninstall local runtime

1. Explain that removal deletes the locally copied runtime and removes its single MCP registration. It does not uninstall the directory skill itself.
2. Ask for explicit confirmation.
3. After confirmation, run:

   `powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File <skill-directory>\scripts\uninstall-cache-stats.ps1 -ConfirmUninstall`

4. Report the exact result and tell the user they can separately remove the Cache Stats directory plugin from ChatGPT if desired.

Never pass `-ConfirmUninstall` without confirmation. Never remove an unowned MCP registration or an unverified directory.

## Boundaries

- Support ChatGPT for Windows only in this release.
- Keep all runtime processing local and read-only.
- Refuse to guess task identity or token values.
- Refuse to guess a cache-miss reason when the Responses API did not return diagnostics.
- Do not require administrator access.
- Do not modify `AGENTS.md`.
