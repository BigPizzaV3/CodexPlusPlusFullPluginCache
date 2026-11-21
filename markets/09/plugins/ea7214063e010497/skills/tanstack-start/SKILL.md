---
name: tanstack-start
description: Introduce TanStack Start or build, extend, debug, migrate, preview, and deploy a Start application. Use for full stack React or Solid apps and existing Start projects.
---

# TanStack Start

Start combines TanStack Router with server rendering, server functions, streaming, and deployment integration. Use it when an app needs typed routing plus server behavior. A static page or an existing framework that already meets the need does not require a migration. Router alone can suit a client-only app. Query is optional, add it when shared server-state caching needs it.

## Check the environment

Inspect the current project, framework, package manager, installed versions, and available tools before changing it. Preserve the user's chosen framework. The example below uses React, use the Solid docs for Solid.

With shell and workspace access, scaffold, install, edit, run, and validate the app. With read-only docs tools or a shell-less ChatGPT session, explain and produce specific code/files that the user can run, or use an available app-building tool. This plugin's public docs MCP cannot write files, run a preview, or deploy. Do not claim these actions happened without tool evidence.

## Install and try it

For a new local React app in an empty target directory:

```sh
npx @tanstack/cli@latest create my-app --framework React --blank --package-manager npm -y
cd my-app
npm run dev
```

Use the existing package manager when working in a repository. Do not run a new initializer over an existing app. The blank preset intentionally avoids extra starter UI and unrelated dependencies. Discover available add-ons with `npx @tanstack/cli@latest create --list-add-ons --framework React --json`, add only what the requested product needs.

Replace `src/routes/index.tsx` with this small route, which reads a value from a server function:

```tsx
import { createFileRoute } from '@tanstack/react-router'
import { createServerFn } from '@tanstack/react-start'

const getGreeting = createServerFn({ method: 'GET' }).handler(() => ({
  message: 'Hello from TanStack Start',
}))

export const Route = createFileRoute('/')({
  loader: () => getGreeting(),
  component: Home,
})

function Home() {
  const { message } = Route.useLoaderData()
  return <main><h1>{message}</h1></main>
}
```

The CLI supplies the root document, router factory, build integration, and generated route tree. Never edit `routeTree.gen.ts` by hand. The loader can run during server rendering and browser navigation, the server function keeps its handler on the server. Do not put credentials in route components or browser environment variables. Validate inputs and authorize mutations inside server code.

## Build the requested app

Read [App workflow](references/app-workflow.md) for project creation, preview, validation, and hosting. For existing features, follow the current route and data patterns and change the smallest useful slice. When debugging, reproduce the error first and check routing, server/client imports, hydration, runtime logs, and installed dependency versions. When migrating, map routes, data loading, mutations, authentication, redirects, errors, metadata, and deployment behavior before moving one route at a time.

For deeper APIs, use version-matched Intent guidance. Run `npx @tanstack/intent@latest list` in the installed project, select a returned skill ID that fits the change, then run `npx @tanstack/intent@latest load <returned-skill-id>`. Do not invent IDs or treat the latest web docs as proof of an older version's behavior. Consumer `install` updates agent guidance and hooks are optional, neither is required just to load a skill.

Sources: [Getting started](https://tanstack.com/start/latest/docs/framework/react/getting-started), [Build from scratch](https://tanstack.com/start/latest/docs/framework/react/build-from-scratch), [Hosting](https://tanstack.com/start/latest/docs/framework/react/guide/hosting), [Intent](https://tanstack.com/intent/latest/docs/overview).
