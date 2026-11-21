---
name: tanstack-cli
description: Introduce, add, debug, or migrate TanStack CLI for create TanStack projects and inspect starter capabilities.
---

# TanStack CLI

Create TanStack projects and inspect starter capabilities.

Use it for: Create a new app, discover supported add-ons, or inspect a scaffold plan.

Usually unnecessary for: Adding one library to an existing app, ordinary package installation is enough.

## Install and try

Use the project's framework and package manager. These examples target the current official documentation checked on September 30, 2026. Match installed versions before copying them into an existing project.

Use npx commands below, no global installation is needed.

Minimal example, run from the project directory:

```sh
npx @tanstack/cli@latest create my-app --blank --intent -y
cd my-app
npm run dev
```

Requires a local shell and supported Node.js. Check current create --help and package-manager options before executing. Use the existing package manager. Blank means a minimal app, --intent opts into dependency skill guidance. Discover machine-readable CLI commands through help and use JSON output where supported. The old tanstack mcp command was removed, do not resurrect it. Never pass --force against a nonempty project unless its replacement is explicitly requested.

## Implement, debug, or migrate

Read the project's package manifest and lockfile before changing dependencies. Load version-matched TanStack Intent guidance with `npx @tanstack/intent@latest list`, then `npx @tanstack/intent@latest load` followed by a concrete identifier returned by the list. Do not invent skill names or assume every version includes skills. If no relevant skill is packaged, use the installed version's official docs and source. Current web docs can describe a newer API than the lockfile.

For an existing project, reproduce the failure and change the smallest relevant integration. For migration, read the version-specific migration guide and preserve behavior through a small verified slice before migrating the rest. Run the project's relevant build and checks, then verify the user-visible feature. Do not add unrelated TanStack packages.

In ChatGPT without a shell or repository tools, use the connected documentation tools and provide the code and exact commands for the user to run. Never claim files were edited, packages installed, or checks passed without execution evidence.

[Official docs](https://tanstack.com/cli/latest/docs/overview) · [Version-matched guidance](https://tanstack.com/intent/latest/docs/overview)
