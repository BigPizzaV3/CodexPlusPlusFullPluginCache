---
name: tanstack-query
description: Introduce, add, debug, or migrate TanStack Query for cache and coordinate asynchronous server state.
---

# TanStack Query

Cache and coordinate asynchronous server state.

Use it for: Repeated API reads, shared request state, retries, mutations, and background refresh.

Usually unnecessary for: A one-off fetch with no shared cache or a component-local UI toggle.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-query
```

Minimal example, paste into an existing React app:

```tsx
import { QueryClient, QueryClientProvider, useQuery } from '@tanstack/react-query'
const client = new QueryClient()
function Greeting() {
  const query = useQuery({ queryKey: ['greeting'], queryFn: async () => 'Hello' })
  if (query.isPending) return <p>Loading</p>
  if (query.isError) return <p>{query.error.message}</p>
  return <p>{query.data}</p>
}
export function App() {
  return <QueryClientProvider client={client}><Greeting /></QueryClientProvider>
}
```

Use stable query keys that include every query input. Throw on failed HTTP status, because fetch does not. Keep one browser client and request-scoped clients for SSR. For writes, define invalidation and rollback. Query v5 uses object options. Do not replace local UI state with Query.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/query/latest/docs/framework/react/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
