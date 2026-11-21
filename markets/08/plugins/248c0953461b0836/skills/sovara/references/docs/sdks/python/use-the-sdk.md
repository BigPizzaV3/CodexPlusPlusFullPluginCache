---
title: "Use the SDK"
description: "Understand project clients, runs, steps, subruns, metadata, and lessons."
---

<script src="/assets/sdk-nav.js"></script>

## The ownership model

The Python SDK exposes two top-level building blocks:

- `SovaraClient` owns project identity and run-scoped helpers.
- `trace` wraps application functions that should appear as steps.

```python
from sovara import SovaraClient, trace

sovara_client = SovaraClient(project_name="support-agent")
```

All run, subrun, logging, lesson, and control operations go through that client.
The project is not inferred from the working directory.

## Top-level runs

Use a top-level run for a workflow, evaluation sample, batch job, or durable
conversation. A recording session opens that run for appending work; a
[turn](#explicit-conversation-turns) groups one interaction within it.

```python
with sovara_client.run("research-and-answer"):
    answer = run_agent()
```

The SDK registers the run with the exec server when the context opens and
finalizes it when the context exits. The same context works with `with` and
`async with`.

For a durable conversation or workflow, pass your own stable identifier as
`run_id`, or reuse the run ID yielded by a previous SDK run. Reuse either value
to add new steps to the same run in that project.

```python
with sovara_client.run("support chat", run_id=chat_id) as run_id:
    reply = agent.reply(message)
    if run_id is not None:
        sovara_client.log(run_id=run_id, run_input=message, run_output=reply)
```

Keep prompts, messages, and secrets out of `run_id`; use a stable ID such
as a chat, ticket, or job ID.

The context yields the run ID. Omit `run_id` to create a new run. Pass
that ID to the CLI, here as `RUN_ID`:

```bash
sovara probe "$RUN_ID"
```

## Steps and explicit tracing

Inside a run, supported provider and MCP calls become ordered steps with input,
output, latency, status, and error data. `trace` adds the same visibility to
important application work that automatic instrumentation does not capture.

```python
@trace
def lookup_customer(customer_id: str) -> dict:
    return crm.lookup(customer_id)
```

Place explicit tracing at shared tool or dispatch chokepoints. A trace filled
with miscellaneous helper calls is harder to understand than one that exposes
the agent's decisions and meaningful actions.

## Subruns

Subruns organize child agents, delegated branches, parallel work, and coherent
multi-step phases under the active run.

```python
with sovara_client.run("finance-eval"):
    with sovara_client.subrun("sample-42"):
        run_one_sample("sample-42")
```

Use `subrun()` for child work. Nesting `run()` does not create a child run.

## Run metadata

Use `log()` to attach input, output, and custom fields to a run.

```python
with sovara_client.run("answer-question") as run_id:
    answer = agent(question)
    if run_id is not None:
        sovara_client.log(run_id=run_id, run_input=question, run_output=answer,
                          answered=True, latency_budget_ms=2500)
```

Input and output must be strings; serialize structured values with `json.dumps()`.
Custom fields accept booleans, integers, finite floats, or strings. Omit absent
values instead of passing `None`. If recording is unavailable, `run_id` is
`None`; skip logging for that run. See the [API reference](/sdks/python/api-reference)
for details.

To group sample runs and record verdicts, follow the
[Evaluations guide](/evals/evals-in-sovara).

## Lessons

When automatic injection is enabled and the required models are configured,
supported model calls retrieve from the project's production lessons.
Unapplied proposals are not used. Narrow retrieval with `lesson_scope` on a run or subrun:

```python
with sovara_client.run("answer-question", lesson_scope="financebench/"):
    answer = call_model(question)
```

Temporarily replace the active scope inside a smaller block:

```python
with sovara_client.lesson_scope(["conventions/", "markets/"]):
    answer = call_model(question)
```

See [runtime retrieval](/sovaradb/auto-injection) for project settings.

## Controls and concurrency

```python
with sovara_client.disable_tracing():
    warm_cache_without_recording()

with sovara_client.disable_lesson_injection():
    answer_without_lessons()
```

Async tasks inherit context. Create the `with_context(...)` wrapper inside the
active run before submitting it to a thread pool:

```python
from concurrent.futures import ThreadPoolExecutor

with sovara_client.run("parallel-research", capture_logs=False):
    with ThreadPoolExecutor() as pool:
        result = pool.submit(sovara_client.with_context(research), question).result()
```

Await tasks and consume provider streams before leaving the recording context.

For concurrent top-level runs, set `capture_logs=False` to avoid mixing process
stdout/stderr between runs.

## Run the application

Run the application normally. The SDK records the run:

```bash
uv run python agent.py
```

Open Sovara to inspect the recorded run.

Use the [API reference](/sdks/python/api-reference) for exact signatures.

## Explicit conversation turns

`run()` opens a recording session; it does not create an implicit turn. Declare
interactions with scoped `turn()` blocks. Setup, cleanup, and other work outside
those blocks are still captured, with no turn membership.

```python
with sovara_client.run("conversation", run_id="chat-123"):
    setup()
    with sovara_client.turn(turn_input="Hi."):
        respond()
    with sovara_client.turn(turn_input="Another question."):
        respond()
    cleanup()
```

For one recording per interaction, reuse the same `run_id` and declare
the interaction explicitly:

```python
for message in messages:
    with sovara_client.run("conversation", run_id="chat-123"):
        with sovara_client.turn(turn_input=message):
            respond()
```

Both `run()` and `turn()` support `async with`. `turn_input` is an optional
string for the interaction; logged input and output describe the whole run.
Do not nest turns in the same run. Await tasks and consume streams before
leaving the recording context.
