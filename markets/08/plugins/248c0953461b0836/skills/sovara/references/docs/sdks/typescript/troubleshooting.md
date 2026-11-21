---
title: "Troubleshooting"
description: "Diagnose missing TypeScript runs, steps, project assignment, and noisy logs."
---

<script src="/assets/sdk-nav.js"></script>

## Common checks

| Symptom | Check |
| --- | --- |
| No run appears | Confirm the entrypoint reaches and awaits `sovara_client.run(...)`. Check the terminal for a Sovara warning. |
| An evaluation sample is missing from Runs | Look in <strong><Icon icon="chart-no-axes-column" size={14} /> Evaluations</strong>; the main Runs view excludes evaluation-owned samples. |
| Lessons are missing | Check that the proposal was applied, automatic injection is enabled, required models are configured, and the lesson scope includes the right folders. |
| Run appears in the wrong project | Check the `projectName` passed to `new SovaraClient(...)`. |
| An LLM or supported framework tool call is missing | Confirm the call executes and completes before the `run(...)` callback returns. |
| A custom operation is missing | Wrap its shared execution boundary with `trace`. |
| Claude Agent SDK calls are missing | Import `query` or `startup` from `@sovara/runner/claude`. |
| Logs mix between concurrent runs | Set `captureLogs: false` on concurrent top-level runs. |

## Recording is unavailable

For local recording, [install the CLI](/cli/install). For a remote server, set
`url` and `agentToken` (or `SOVARA_AGENT_TOKEN`); see the
[API reference](/sdks/typescript/api-reference).

An unreachable server may let your agent continue without recording.
`getRunId()` returns `undefined` in that case, and logging helpers do nothing.
During recording, await logging calls and handle any errors.

Authentication and version mismatches raise; update the component named in the error.

## Missing custom steps

Import `@sovara/runner` before creating clients or capturing a reference to
`fetch`. Add `trace` only to operations that are not already recorded:

```ts
const retrieveContext = trace(async function retrieveContext(question: string) {
  return vectorSearch(question);
});
```

For Claude Agent SDK calls, use the
[Claude wrapper](/sdks/typescript/api-reference#claude-agent-sdk-wrapper).

## Inspect what was recorded

```bash
sovara probe <run-id>
sovara probe <run-id> --step <step-ref> --preview
sovara logs <run-id> --tail 40
```

Use step references shown by `probe`.

## Runs and turns

Keep agent work inside `run()` and await tasks and streams before the callback
returns. Declare conversation turns with `turn()`; they are not created automatically.
Do not nest turns in the same run or use a different client inside it.
See [the usage guide](/sdks/typescript/use-the-sdk#explicit-conversation-turns).
