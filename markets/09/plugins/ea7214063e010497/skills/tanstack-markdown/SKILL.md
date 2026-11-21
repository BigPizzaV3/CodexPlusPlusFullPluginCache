---
name: tanstack-markdown
description: Introduce, add, debug, or migrate TanStack Markdown for parse and render Markdown through a shared document model.
---

# TanStack Markdown

Parse and render Markdown through a shared document model.

Use it for: Documentation, user content, or streamed AI text rendered as HTML or framework components.

Usually unnecessary for: Plain text or content that requires MDX execution or every CommonMark edge case.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/markdown
```

Minimal example, run in a browser module:

```ts
import { renderHtml } from '@tanstack/markdown/html'
const article = document.createElement('article')
article.innerHTML = renderHtml('# Hello\n\n**Markdown** works.')
document.body.append(article)
```

Raw HTML is escaped and unsafe URLs are removed by default. Custom ASTs, highlighter output, and HTML hooks are trusted inputs. This is not a general HTML sanitizer. Keep executable MDX separate. Import only the needed renderer. Highlight is an optional companion, not a bundled dependency.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/markdown/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
