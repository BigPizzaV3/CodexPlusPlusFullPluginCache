---
name: tanstack-virtual
description: Introduce, add, debug, or migrate TanStack Virtual for render only visible items in large scrollable lists or grids.
---

# TanStack Virtual

Render only visible items in large scrollable lists or grids.

Use it for: Large lists cause measurable DOM or rendering cost.

Usually unnecessary for: Small lists that render quickly, virtualizing adds scrolling and accessibility complexity.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-virtual
```

Minimal example, paste into an existing React app:

```tsx
import { useRef } from 'react'
import { useVirtualizer } from '@tanstack/react-virtual'
export function List() {
  const parent = useRef<HTMLDivElement>(null)
  const virtual = useVirtualizer({ count: 10000, getScrollElement: () => parent.current, estimateSize: () => 32 })
  return <div ref={parent} style={{ height: 320, overflow: 'auto' }}>
    <div style={{ height: virtual.getTotalSize(), position: 'relative' }}>
      {virtual.getVirtualItems().map(item => <div key={item.key}
        style={{ position: 'absolute', top: 0, height: item.size, transform: `translateY(${item.start}px)` }}>
        Row {item.index + 1}
      </div>)}
    </div>
  </div>
}
```

Use stable item keys when data changes. Measure variable-height rows instead of pretending they are fixed. Test scroll position, resize, keyboard navigation, and access to unloaded items. Virtual supplies no table sorting or data fetching.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/virtual/latest/docs/introduction) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
