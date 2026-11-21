---
title: "API reference"
description: "The public client, run, tracing, subrun, logging, and lesson APIs in @sovara/runner."
---

<script src="/assets/sdk-nav.js"></script>

The main package exports `SovaraClient`, `trace`, and `CompatibilityError`, plus
the TypeScript types `SovaraClientOptions`, `SovaraRunOptions`,
`SovaraSubrunOptions`, `SovaraTurnOptions`, and `TraceOptions`.

## `new SovaraClient(options)`

Creates a project-bound client. Project identity and connection configuration
belong to the client, not to individual runs.

```ts
import { SovaraClient, trace } from "@sovara/runner";

const sovara_client = new SovaraClient({ projectName: "support-agent" });
```

| Option | Required | Purpose |
| --- | --- | --- |
| `projectName` | Yes | Project name selected by SDK code. Project admins can rename a project; update this value when they do. |
| `url` | No | Execution server URL. Defaults to `SOVARA_EXEC_SERVER_URL`, otherwise `http://127.0.0.1:5960` (port configurable with `SOVARA_EXEC_SERVER_PORT`). Set environment variables before importing the runner. |
| `agentToken` | No | Project-scoped token for an agent host without a signed-in Sovara user. Defaults to `SOVARA_AGENT_TOKEN`. |
| `fetch` | No | Caller-owned `fetch` implementation used for lifecycle and runtime requests. |

## `sovara_client.run(name, fn, options?)`

Opens and finalizes a recording session around a synchronous or asynchronous
callback. No turn is created implicitly; work outside `turn()` remains recorded
without a turn.

```ts
await sovara_client.run("agent-task", async () => runAgent());
```

| Option | Purpose |
| --- | --- |
| `runId` | Your own stable identifier or the ID from `getRunId()` in a previous SDK run. Reuse it to add steps to the same run in this project. |
| `evalRunId` | Existing evaluation run in this project that owns the sample run. Set on creation; inherited by subruns and cannot be reassigned. |
| `captureLogs` | Captures stdout/stderr unless set to `false`. |
| `lessonScope` | Folder path, path list, `null` for root/all, or `[]` to disable retrieval. |

Returns the callback result as `Promise<T>`. Use `getRunId()` inside the callback
to read the run ID. A supplied `sovara-` ID must already exist in the project.

If the server is unreachable, the callback may run without recording and
`getRunId()` returns `undefined`. Authentication, compatibility, and callback
errors propagate.

For a remote server:

```ts
const sovara_client = new SovaraClient({
  projectName: "support-agent",
  url: "https://exec.example.com",
  agentToken: process.env.SOVARA_AGENT_TOKEN,
});
```

## `sovara_client.subrun(name, fn, options?)`

Creates a child run under the active run. The optional `lessonScope` replaces
the inherited lesson scope for that child.

```ts
await sovara_client.subrun("research", () => research(question));
```

Returns `Promise<T>` for the callback result. Requires an enclosing run
opened by the same client; the callback still executes if that enclosing run
is in no-capture mode.

## `sovara_client.turn(options, fn)`

Groups one interaction in the active run or subrun. Accepts optional
`turnInput?: string` and returns the callback result as `Promise<T>`.

```ts
await sovara_client.run("conversation", async () => {
  return await sovara_client.turn({ turnInput: "Hi." }, () => respond());
}, { runId: "chat-123" });
```

Use the same client and do not nest turns within a run. Finish tasks and streams
before the outer run returns. See the
[usage guide](/sdks/typescript/use-the-sdk#explicit-conversation-turns) for examples.

## `trace(fn, options?)`

Wraps a synchronous or asynchronous function as a step, recording arguments,
return values, latency, status, and exceptions.

```ts
const lookupCustomer = trace(
  async function lookupCustomer(customerId: string) {
    return crm.get(customerId);
  },
  { name: "lookup_customer", meta: { system: "crm" } },
);
```

`name` defaults to the function or method name. `meta` adds step metadata.
The curried form `trace(options)(fn)` and Stage 3 method decorators are also
supported. Use standard decorators rather than TypeScript's legacy
`experimentalDecorators` mode. Wrapping a synchronous function preserves its
synchronous return value; wrapping an async function preserves its promise.

## `sovara_client.lessonScope(scope, fn)`

Temporarily replaces the active lesson scope. Paths include descendants;
`null` or a root marker selects all lessons, and `[]` disables retrieval.
Restores the previous scope when the callback completes and returns the callback
result as `Promise<T>`. It can wrap an existing run's work or establish a scope
for runs opened inside the callback. Inside an active run, use the same client.

```ts
await sovara_client.lessonScope(["conventions/", "markets/"], runOneSample);
```

## `sovara_client.logInput(value)`

Stores the latest user-visible input on the active run. This value appears in
the Input column of the Runs table and replaces the previously logged input.
Objects and arrays are serialized as JSON.

```ts
await sovara_client.logInput({ question, customerId });
```

Returns `Promise<void>`. Outside an active run, it warns once and does nothing.

## `sovara_client.logOutput(value)`

Stores the latest user-visible output on the active run. This value appears in
the Output column of the Runs table and replaces the previously logged output.
Objects and arrays are serialized as JSON.

```ts
await sovara_client.logOutput({ answer, sources });
```

Returns `Promise<void>`. Outside an active run, it warns once and does nothing.

## `sovara_client.logMetrics(metrics)`

Adds filterable custom metrics to the active run. Values must be booleans or
finite numbers. Supply at least one metric. Keys must start with a lowercase
letter, contain only lowercase letters, digits, and underscores, and be at most
32 characters. Strings, objects, arrays, and `null` are not metric values.

```ts
await sovara_client.logMetrics({ answered: true, latency_ms: 842 });
```

Returns `Promise<void>`. Logging the same key again updates its latest value.
Outside an active run, it warns once and does nothing.

Await logging calls inside the run opened by this client. Validation and
transport errors reject the promise. These helpers do not log evaluation-level results.

## `sovara_client.getRunId()`

Returns the current run or subrun ID as a string, or `undefined` when called
outside an active run.

```ts
const runId = sovara_client.getRunId();
```

## Claude Agent SDK wrapper

Install `@anthropic-ai/claude-agent-sdk` separately and import its instrumented
entrypoints from `@sovara/runner/claude`:

```ts
import { SovaraClient } from "@sovara/runner";
import { query } from "@sovara/runner/claude";

const client = new SovaraClient({ projectName: "coding-agent" });
await client.run("inspect-project", async () => {
  for await (const message of query({ prompt: "Describe this project's structure." })) {
    // Handle each message in your application.
  }
});
```

The subpath exports `query` and `startup`. Create the query or connection inside
the intended run and turn, and consume it before leaving the recording. A
long-lived connection retains the context in which it was created. Custom
Claude Agent SDK transports are not supported by this wrapper.
