---
name: tanstack-charts
description: Introduce, add, debug, or migrate TanStack Charts for typed chart definitions and rendering for data visualization.
---

# TanStack Charts

Typed chart definitions and rendering for data visualization.

Use it for: Interactive charts or reusable visual definitions that need control over scales and marks.

Usually unnecessary for: A single decorative graphic or an existing chart package that already fits.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/charts
```

Minimal example, run in a browser module:

```ts
import { defineChart, lineY, mountChart } from '@tanstack/charts'
import { scaleLinear } from '@tanstack/charts/scales/linear'
const definition = defineChart({
  marks: [lineY([2, 5, 3])],
  scales: { x: { scale: scaleLinear }, y: { scale: scaleLinear } },
})
const container = document.createElement('div')
document.body.append(container)
const host = mountChart(container, { definition, width: 640, height: 320, ariaLabel: 'Three sample values' })
// When the owning page is removed, call host.destroy().
```

This uses current built-in scales. Earlier releases use configured D3 scales with x/y options, inspect installed guidance before adapting old examples. Add only the framework adapter and scale capabilities actually needed. Provide meaningful accessible chart text and destroy DOM hosts on removal. Charts is evolving, verify current release availability.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/charts/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
