---
name: tanstack-db
description: Introduce, add, debug, or migrate TanStack DB for reactive collections, live queries, and optimistic local updates.
---

# TanStack DB

Reactive collections, live queries, and optimistic local updates.

Use it for: Views that join or filter shared collections, optimistic writes, or synced local data.

Usually unnecessary for: A simple remote read that Query already handles. DB is not a hosted database.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/db
```

Minimal example, run in a TypeScript module:

```ts
import { createCollection, localOnlyCollectionOptions } from '@tanstack/db'
type Todo = { id: string; text: string }
const todos = createCollection(localOnlyCollectionOptions<Todo>({
  id: 'todos', getKey: todo => todo.id,
}))
todos.insert({ id: '1', text: 'Ship the app' })
todos.update('1', draft => { draft.text = 'Shipped' })
console.log(todos.get('1')?.text)
```

This example is memory-only. Persistence requires a collection adapter. New SSR work uses stable collectionOptions descriptors and a request-scoped DbClient. Match the installed DB version before adopting that newer API. For remote writes, supply real handlers and test failure rollback.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/db/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
