---
title: "Troubleshooting"
description: "Diagnose missing Python runs, steps, project assignment, and context."
---

<script src="/assets/sdk-nav.js"></script>

## Common checks

| Symptom | Check |
| --- | --- |
| No run appears | Confirm the entrypoint enters `sovara_client.run(...)`. Check the terminal for a Sovara warning. |
| An evaluation sample is missing from Runs | Look in <strong><Icon icon="chart-no-axes-column" size={14} /> Evaluations</strong>; the main Runs view excludes evaluation-owned samples. |
| Lessons are missing | Check that the proposal was applied, automatic injection is enabled, required models are configured, and the lesson scope includes the right folders. |
| Run appears in the wrong project | Check the `project_name` passed to `SovaraClient(...)`. |
| An LLM or supported framework tool call is missing | Confirm the call executes before the `run(...)` context exits. |
| A custom operation is missing | Wrap its shared execution boundary with `trace`. |
| Threaded work attaches to the wrong run | Submit `sovara_client.with_context(fn)` to the executor. |
| Logs mix between concurrent runs | Set `capture_logs=False` on concurrent top-level runs. |

## Recording is unavailable

For local recording, [install the CLI](/cli/install). For a remote server, set
`base_url` and pass `agent_token` explicitly; see the
[API reference](/sdks/python/api-reference).

An unreachable server may let your agent continue without recording. Check the
run ID before logging:

```python
with sovara_client.run("answer-question") as run_id:
    answer = run_agent(question)
    if run_id is not None:
        sovara_client.log(run_id=run_id, run_output=answer)
```

`log()` and `create_eval_run()` raise on errors. Authentication and version
mismatches also raise; update the component named in the error.

## Missing custom steps

Import Sovara before creating provider clients and tools. Use
`openai-agents>=0.13,<1` for OpenAI Agents function-tool capture.
Add `@trace` only to operations that are not already recorded:

```python
from sovara import trace

@trace
def retrieve_context(question: str) -> list[str]:
    return vector_search(question)
```

## Inspect what was recorded

```bash
sovara probe <run-id>
sovara probe <run-id> --step <step-ref> --preview
sovara logs <run-id> --tail 40
```

Use step references shown by `probe`.

## Runs and turns

Keep agent work inside `run()` and await tasks and streams before leaving it.
Use `with_context()` when passing work to another thread.

Declare conversation turns with `turn()`; they are not created automatically.
Do not nest turns in the same run or use a different client inside it.
See [the usage guide](/sdks/python/use-the-sdk#explicit-conversation-turns).
