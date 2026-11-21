---
name: tanstack-store
description: Introduce, add, debug, or migrate TanStack Store for a small reactive core for local application state.
---

# TanStack Store

A small reactive core for local application state.

Use it for: Shared client state, derived values, or selected subscriptions beyond one component.

Usually unnecessary for: Component-local state or cached remote data that belongs in Query.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/store
```

Minimal example, run in a TypeScript module:

```ts
import { createStore } from '@tanstack/store'
const count = createStore(0)
const double = createStore(() => count.state * 2)
count.setState(value => value + 1)
console.log(count.state, double.state)
```

Current documentation uses createStore. Older installed versions expose the Store class and a different subscription cleanup contract, inspect installed guidance before migrating. Use the framework adapter for reactive rendering. Avoid putting request-specific user state in a shared server singleton.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/store/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
