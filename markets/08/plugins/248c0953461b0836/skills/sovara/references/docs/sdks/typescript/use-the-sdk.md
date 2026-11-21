---
title: "Use the SDK"
description: "Understand TypeScript project identity, runs, steps, subruns, metadata, and lessons."
---

<script src="/assets/sdk-nav.js"></script>

## Project-owned top-level runs

Create one `SovaraClient` for a stable project name. Use one top-level run for
a workflow, evaluation sample, batch job, or durable conversation. A recording
session appends work to that run; a [turn](#explicit-conversation-turns) groups
one interaction within it.

```ts
import { SovaraClient, trace } from "@sovara/runner";

const sovara_client = new SovaraClient({ projectName: "support-agent" });

await sovara_client.run("research-and-answer", () => runAgent());
```

For a durable conversation or job, pass your own stable identifier as `runId`,
or reuse the ID from `getRunId()` in a previous SDK run. Reuse either value to add steps
to the same run in that project.

```ts
await sovara_client.run(
  "support chat",
  () => agent.reply(message),
  { runId: chatId },
);
```

Keep prompts and secrets out of `runId`. `run()` returns the callback result. To
read the run ID, call `sovara_client.getRunId()` inside the callback
while the run is active. Pass that ID to the CLI, here as `RUN_ID`:

```bash
sovara probe "$RUN_ID"
```

## Steps and explicit tracing

Supported provider, framework tool, and MCP calls inside a run become ordered
steps. Wrap an important uncaptured application boundary with `trace`:

```ts
const lookupCustomer = trace(async function lookupCustomer(customerId: string) {
  return crm.lookup(customerId);
});
```

Prefer shared tool or dispatch chokepoints. A trace filled with miscellaneous
helper calls is harder to understand than one that exposes agent decisions and
actions.

## Subruns

Use `sovara_client.subrun(...)` for child agents, delegated branches, parallel
work, and coherent multi-step phases:

```ts
await sovara_client.run("finance-eval", () =>
  sovara_client.subrun("sample-42", () => runOneSample("sample-42")),
);
```

Use `subrun()` for child work. Nesting `run()` does not create a child run.

## Run metadata

```ts
await sovara_client.run("answer-question", async () => {
  await sovara_client.logInput(question);
  const answer = await agent(question);
  await sovara_client.logOutput(answer);
  await sovara_client.logMetrics({ answered: true, latency_budget_ms: 2500 });
});
```

Await logging calls inside the active run. Input and output accept strings or
JSON-serializable values; metrics accept booleans and finite numbers with
lowercase names such as `latency_ms`. See the
[API reference](/sdks/typescript/api-reference) for validation rules.

## Evaluation samples

Pass an existing evaluation run ID with `evalRunId` to record a sample under it:

```ts
await sovara_client.run("sample-42", () => runOneSample("sample-42"), {
  evalRunId,
});
```

The evaluation must exist in the same project. To create evaluations and log
aggregate results, use the [Python evaluation workflow](/evals/evals-in-sovara).

## Lessons

When automatic injection is enabled and the required models are configured,
supported model calls retrieve from the project's production lessons.
Unapplied proposals are not used. Narrow retrieval with the run's `lessonScope` option:

```ts
await sovara_client.run(
  "answer-question",
  () => callModel(question),
  { lessonScope: "support/refunds/" },
);
```

Temporarily replace the active scope with `sovara_client.lessonScope(...)`
inside the run. Use `null` for all folders or `[]` for no lessons:

```ts
await sovara_client.run("answer-question", async () => {
  return await sovara_client.lessonScope([], () => callModel(question));
});
```

See [runtime retrieval](/sovaradb/auto-injection) for project settings.

## Logs and concurrency

Log capture is enabled by default. Pass `{ captureLogs: false }` as the third
argument to `run()` for concurrent top-level runs to avoid mixing process output.

## Run the application

Run the application normally. The SDK records the run:

```bash
npm run start
```

Open Sovara to inspect the recorded run.

Use the [API reference](/sdks/typescript/api-reference) for exact signatures.

## Explicit conversation turns

`run()` opens a recording session without an implicit turn. `turn(options, fn)`
declares a scoped interaction and returns the callback result. Work outside turn
callbacks is still captured, with no turn membership.

```ts
await sovara_client.run("conversation", async () => {
  await setup();
  await sovara_client.turn({ turnInput: "Hi." }, async () => respond());
  await sovara_client.turn({ turnInput: "Another question." }, async () => respond());
  await cleanup();
}, { runId: "chat-123" });
```

For one recording per interaction, reuse the same `runId` and declare
each interaction explicitly:

```ts
for (const message of messages) {
  await sovara_client.run("conversation", async () => {
    return await sovara_client.turn({ turnInput: message }, () => respond());
  }, { runId: "chat-123" });
}
```

`turnInput` is an optional string for the interaction; logged input and output
describe the whole run. Do not nest turns in the same run. Await tasks and
consume streams before the outer callback returns.
