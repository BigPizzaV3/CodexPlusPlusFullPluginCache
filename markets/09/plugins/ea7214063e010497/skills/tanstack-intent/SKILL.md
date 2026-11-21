---
name: tanstack-intent
description: Introduce, add, debug, or migrate TanStack Intent for discover and load agent guidance shipped with installed package versions.
---

# TanStack Intent

Discover and load agent guidance shipped with installed package versions.

Use it for: Implementing, debugging, or migrating TanStack features in a local project.

Usually unnecessary for: A general explanation with no project or a shell-less chat that cannot inspect installed dependencies.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

Use npx commands below, no global installation is needed.

Minimal example, run from the project directory:

```sh
npx @tanstack/intent@latest list
# Copy a concrete package#skill identifier printed by list, then:
# npx @tanstack/intent@latest load <that-identifier>
```

list is a working read-only discovery command. Do not run the commented illustrative load line literally. list scans installed dependencies, it does not install them. load reads the matching installed package skill. install writes project guidance and hooks install adds supported agent hooks, use only when the user requests that setup. Respect the project allowlist and local package precedence.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/intent/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
