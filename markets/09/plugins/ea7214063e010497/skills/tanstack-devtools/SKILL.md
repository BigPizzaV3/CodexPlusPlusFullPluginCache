---
name: tanstack-devtools
description: Introduce, add, debug, or migrate TanStack Devtools for a shared development panel for library inspectors and custom plugins.
---

# TanStack Devtools

A shared development panel for library inspectors and custom plugins.

Use it for: Inspect active TanStack state or add an app-specific debugging panel.

Usually unnecessary for: Production UI or an app that does not need runtime inspection.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-devtools
```

Minimal example, paste into an existing React app:

```tsx
import { TanStackDevtools } from '@tanstack/react-devtools'
export function DebugPanel() {
  return <TanStackDevtools plugins={[{ id: 'sample', name: 'Sample', render: <p>App inspector</p> }]} />
}
```

Render this in the development app shell. The panel does not automatically inspect every library, register the supported library plugin. Keep framework plugin and core package versions compatible. Exclude sensitive data from inspectors and verify production build behavior.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/devtools/latest/docs/framework/react/quick-start) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
