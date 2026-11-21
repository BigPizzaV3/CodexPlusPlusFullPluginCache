---
name: tanstack-hotkeys
description: Introduce, add, debug, or migrate TanStack Hotkeys for typed shortcuts, key sequences, held-key tracking, and shortcut recording.
---

# TanStack Hotkeys

Typed shortcuts, key sequences, held-key tracking, and shortcut recording.

Use it for: Keyboard commands need consistent platform handling and scopes.

Usually unnecessary for: A page with no shortcut workflow or one native control that already has keyboard behavior.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/react-hotkeys
```

Minimal example, paste into an existing React app:

```tsx
import { useState } from 'react'
import { useHotkey, formatForDisplay } from '@tanstack/react-hotkeys'
export function Save() {
  const [saved, setSaved] = useState(false)
  const save = () => setSaved(true)
  useHotkey('Mod+S', save, { preventDefault: true })
  return <button onClick={save}>{saved ? 'Saved' : 'Save'} <kbd>{formatForDisplay('Mod+S')}</kbd></button>
}
```

Mod maps to Command on macOS and Control elsewhere. Preserve input typing, scope shortcuts to the correct UI, and test browser conflicts. Provide a visible clickable control for each command. Enable shortcuts only when their target action is available.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/hotkeys/latest/docs/framework/react/quick-start) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
