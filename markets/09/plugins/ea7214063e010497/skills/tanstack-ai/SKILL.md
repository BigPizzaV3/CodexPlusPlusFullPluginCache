---
name: tanstack-ai
description: Introduce, add, debug, or migrate TanStack AI for provider adapters, streaming, tools, and typed AI application flows.
---

# TanStack AI

Provider adapters, streaming, tools, and typed AI application flows.

Use it for: An application needs model calls or a streaming chat interface while keeping its own framework and backend.

Usually unnecessary for: A product with no AI feature or a plain API call that already meets the requirement.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

```sh
npm install @tanstack/ai @tanstack/ai-openai
```

Minimal example, run in a TypeScript module:

```ts
import { chat, streamToText } from '@tanstack/ai'
import { openaiText } from '@tanstack/ai-openai'
const stream = chat({
  adapter: openaiText('gpt-5.5'),
  messages: [{ role: 'user', content: 'Say hello in one sentence.' }],
})
console.log(await streamToText(stream))
```

Run this in a server module with OPENAI_API_KEY supplied through the environment. Select a model supported by the user's account. Provider calls cost money, use mocks for tests unless a live call is authorized. Never expose provider credentials to the browser. Use TanStack AI chat, not APIs from another AI SDK.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/ai/latest/docs/getting-started/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
