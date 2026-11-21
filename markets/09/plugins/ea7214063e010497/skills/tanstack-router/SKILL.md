---
name: tanstack-router
description: Introduce, add, debug, or migrate TanStack Router for type-safe navigation, route loading, and URL state.
---

# TanStack Router

Type-safe navigation, route loading, and URL state.

Use it for: An app with multiple screens, validated search parameters, or route-level loading.

Usually unnecessary for: A single static page or a project whose existing router already meets the need.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-router
```

Minimal example, paste into an existing React app:

```tsx
import { createRootRoute, createRoute, createRouter, Outlet, RouterProvider } from '@tanstack/react-router'
const root = createRootRoute({ component: () => <Outlet /> })
const home = createRoute({ getParentRoute: () => root, path: '/', component: () => <h1>Hello</h1> })
const router = createRouter({ routeTree: root.addChildren([home]) })
declare module '@tanstack/react-router' { interface Register { router: typeof router } }
export function App() { return <RouterProvider router={router} /> }
```

This code-based route example needs no generator. For file routes, configure the framework build plugin and generate the route tree, never hand-edit generated output. Start already includes Router. Validate URL search state and test direct links plus browser back navigation.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/router/latest/docs/framework/react/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
