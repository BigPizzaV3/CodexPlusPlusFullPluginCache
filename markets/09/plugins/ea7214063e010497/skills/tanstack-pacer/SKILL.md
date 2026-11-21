---
name: tanstack-pacer
description: Introduce, add, debug, or migrate TanStack Pacer for debouncing, throttling, rate limiting, batching, and queues.
---

# TanStack Pacer

Debouncing, throttling, rate limiting, batching, and queues.

Use it for: Control how often work runs or how pending work is scheduled.

Usually unnecessary for: Infrequent actions with no timing or concurrency requirement.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/pacer
```

Minimal example, run in a TypeScript module:

```ts
import { Debouncer } from '@tanstack/pacer'
const search = new Debouncer((value: string) => console.log(value), { wait: 250 })
search.maybeExecute('t')
search.maybeExecute('tanstack')
search.flush()
search.cancel()
```

Debounce waits for quiet time, throttle caps frequency, rate limiting enforces a budget, queues control pending execution, and batching groups work. Choose deliberately. Use framework hooks to preserve identity and clean up timers. Cancellation and rejected asynchronous work need explicit behavior.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/pacer/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
