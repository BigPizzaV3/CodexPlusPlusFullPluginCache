---
name: tanstack-config
description: Introduce, add, debug, or migrate TanStack Config for shared configuration for maintaining and publishing JavaScript packages.
---

# TanStack Config

Shared configuration for maintaining and publishing JavaScript packages.

Use it for: An existing package needs TanStack linting or publishing conventions.

Usually unnecessary for: Ordinary application features, or a new library build that current docs recommend handling with tsdown.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install  --save-dev @tanstack/vite-config vite
```

Minimal example, run in a TypeScript module:

```ts
import { defineConfig, mergeConfig } from 'vite'
import { tanstackViteConfig } from '@tanstack/vite-config'
export default mergeConfig(
  defineConfig({}),
  tanstackViteConfig({ entry: './src/index.ts', srcDir: './src' }),
)
```

This is the documented legacy Vite package setup, save as vite.config.ts in a library with src/index.ts. Current Config docs recommend tsdown for future projects. Do not apply this library build config to a Start app. Inspect package exports and run publint before distributing a package. Never publish without authorization.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/config/latest/docs/vite) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
