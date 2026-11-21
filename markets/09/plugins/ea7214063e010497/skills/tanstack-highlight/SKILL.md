---
name: tanstack-highlight
description: Introduce, add, debug, or migrate TanStack Highlight for synchronous syntax highlighting with compact HTML and separate theme CSS.
---

# TanStack Highlight

Synchronous syntax highlighting with compact HTML and separate theme CSS.

Use it for: Code examples in docs, editor previews, or Markdown fences need syntax coloring.

Usually unnecessary for: No code display, plain preformatted text, or full editor language services.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/highlight
```

Minimal example, run in a browser module:

```ts
import { createHighlighter } from '@tanstack/highlight/core'
import { ts } from '@tanstack/highlight/languages/ts'
import { createThemeCss } from '@tanstack/highlight/theme'
import { githubLightTheme } from '@tanstack/highlight/themes/github-light'
const highlighter = createHighlighter({ languages: [ts] })
const style = document.createElement('style')
style.textContent = createThemeCss({ light: githubLightTheme })
document.head.append(style)
const output = document.createElement('div')
output.innerHTML = highlighter.highlight('const answer: number = 42', { lang: 'ts' }).html
document.body.append(output)
```

Register only required languages and any delegated embedded languages. Reuse a highlighter instance. Source text is escaped by the renderer, insert HTML returned directly by the highlighter. Themes use CSS and do not require re-highlighting.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/highlight/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
