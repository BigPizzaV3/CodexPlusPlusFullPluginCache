---
title: "API reference"
description: "The public Sovara Python SDK surface and exact client methods."
---

<script src="/assets/sdk-nav.js"></script>

The package exports `SovaraClient` and `trace`. Run-scoped helpers are methods
on `SovaraClient`; module-level `run`, `subrun`, and logging helpers are not
supported.

## `SovaraClient(*, project_name, base_url=None, agent_token=None, http_client=None)`

Creates a client bound to one project name. Project admins can rename a project
from the Sovara app; update this value when they do.

```python
from sovara import SovaraClient

client = SovaraClient(project_name="finance-agent")
```

| Parameter | Required | Purpose |
| --- | --- | --- |
| `project_name` | Yes | Stable project name for every top-level run created by this client. |
| `base_url` | No | Execution server URL. Defaults to `SOVARA_EXEC_SERVER_URL`, otherwise `http://127.0.0.1:5960` (port configurable with `SOVARA_EXEC_SERVER_PORT`). Set environment variables before importing Sovara. |
| `agent_token` | No | Project-scoped token for an agent host without a signed-in Sovara user. Pass it explicitly; the Python client does not read `SOVARA_AGENT_TOKEN` automatically. |
| `http_client` | No | Caller-owned synchronous `httpx.Client`. Sovara uses it for lifecycle and runtime requests and does not close it. |

For a remote server, pass `base_url` and `agent_token` explicitly:

```python
import os
from sovara import SovaraClient

client = SovaraClient(
    project_name="finance-agent",
    base_url="https://exec.example.com",
    agent_token=os.environ["SOVARA_AGENT_TOKEN"],
)
```

## `client.run(name=None, *, run_id=None, eval_run_id=None, capture_logs=True, lesson_scope=<inherit>)`

Opens a recording session on a durable run, usable with `with` or `async with`.
No turn is created implicitly; work outside `turn()` remains recorded without a turn.

```python
with client.run("sync-agent"):
    ...

async with client.run("async-agent", run_id=chat_id):
    ...
```

| Argument | Purpose |
| --- | --- |
| `name` | Optional display name. Sovara generates one when omitted. |
| `run_id` | Optional. Pass your own stable identifier or the ID yielded by a previous SDK run. Reuse it to add steps to the same run in this project. |
| `eval_run_id` | Optional eval run that owns this run. Set it when the run starts; subruns inherit it and it cannot change later. |
| `capture_logs` | Captures `stdout` and `stderr` by default. Disable for concurrent top-level runs. |
| `lesson_scope` | Folder path or list for this run. Omit to inherit; `None` selects root/all; `[]` disables retrieval. |

Entering the context yields the run ID, or `None` if recording is unavailable.
Use a stable `run_id` to append to the same run. A `sovara-` ID must already exist
in the project.

## `client.subrun(name, *, lesson_scope=<inherit>)`

Creates a child run under the active run.

```python
with client.run("batch"):
    with client.subrun("sample-1"):
        run_one_sample()
```

`name` is required. Returns `SovaraRunContext`, supporting `with` and
`async with`; entering it yields
the subrun's run ID, or `None` in no-capture mode. Requires an enclosing run
opened by the same client.

## `client.turn(*, turn_input=None)`

Groups one interaction in the active run or subrun. Supports `with` and
`async with`, yielding the turn ID or `None` if recording is unavailable.
`turn_input` accepts a string or `None`. Use the same client and do not nest
turns within a run.

```python
with client.run("conversation", run_id="chat-123"):
    with client.turn(turn_input="Hi.") as turn_id:
        reply = respond()
```

Finish tasks and streams before leaving the run. See the
[usage guide](/sdks/python/use-the-sdk#explicit-conversation-turns) for turn examples.

## `trace(fn=None, *, name=None, meta=None)`

Wraps a sync or async function as a tool-like step. It is the only top-level
instrumentation helper.

```python
from sovara import trace

@trace(name="lookup_customer", meta={"system": "crm"})
def lookup_customer(customer_id: str):
    return crm.get(customer_id)
```

| Argument | Purpose |
| --- | --- |
| `fn` | Function to wrap. Omit when using decorator options. |
| `name` | Optional step name; defaults to the function name. |
| `meta` | Optional step metadata. |

The wrapper preserves the call signature, records arguments and return values,
records raised exceptions, and re-raises them.

## Lesson methods

### `client.lesson_scope(scope)`

Temporarily replaces the active lesson scope. Paths include descendants;
`None` means root/all and `[]` disables retrieval.

```python
with client.lesson_scope(["conventions/", "markets/"]):
    call_model()
```

### `client.disable_lesson_injection()`

Temporarily prevents automatic lesson retrieval while leaving tracing active.

## `client.create_eval_run()`

Creates an evaluation in the client's project and returns its `eval_run_id`.
Record samples with `client.run(eval_run_id=...)`, then log results with `client.log()`.

## `client.log(*, run_id=..., eval_run_id=..., **fields)`

Logs to an explicit target, including after the recording context closes.
No identifier is inherited from a context. Agent runs and eval runs must already exist.

| Supplied targets | Meaning |
| --- | --- |
| `run_id` | Update that run or subrun using its Sovara ID or your own identifier. |
| `eval_run_id` | Update custom fields on that eval run. |
| Both | Check that the eval run owns the run, then update the run's fields. |
| Neither | Validation error. |

Reserved fields `run_input`, `run_output`, `groundtruth`, and `llm_judge_output`
accept strings; `llm_judge_is_correct` accepts a boolean. These require `run_id`.
Custom fields accept booleans, strings, finite floats, and integers between
-2**53 and 2**53. Explicit `None` is invalid.

Writes replace supplied fields and leave others unchanged. Logging never changes
a run's evaluation owner. `groundtruth` updates the run annotation;
`llm_judge_is_correct` records a separate evaluation verdict.
See [Evaluations](/evals/evals-in-sovara) for aggregate metrics and accuracy.

```python
eval_run_id = client.create_eval_run()
with client.run(eval_run_id=eval_run_id) as run_id:
    if run_id is None:
        raise RuntimeError("This evaluation requires a recorded sample.")
    client.log(run_id=run_id, run_input=question, groundtruth=expected_answer)
    answer = agent(question)

client.log(
    run_id=run_id,
    eval_run_id=eval_run_id,
    run_output=answer,
    llm_judge_output="The answer matches the expected value.",
    llm_judge_is_correct=True,
    latency_ms=842,
)
client.log(eval_run_id=eval_run_id, accuracy=1.0, sample_count=1)
```

`log()` and `create_eval_run()` are synchronous and raise on errors. Skip run
logging when recording yields `None`. After a timeout, check the saved result
before retrying; the write may have succeeded.

## `client.get_run_id()`

Returns the current run or subrun ID as a string, or `None` when called outside
an active run.

```python
run_id = client.get_run_id()
```

## Context and tracing controls

### `client.with_context(fn)`

Captures the current context and returns a wrapper for another thread.

```python
executor.submit(client.with_context(eval_sample), sample)
```

### `client.disable_tracing()`

Temporarily disables supported provider, MCP, and explicit `trace` recording.

```python
with client.disable_tracing():
    noisy_or_sensitive_work()
```
