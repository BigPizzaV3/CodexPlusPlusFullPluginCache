---
name: echo-ui
description: Build or change a product's interface with Echo UI, the tactile React design system: a screen, a component, a look from a moodboard, or Echo's check on code. Use it for any interface task on a product that's built, or will be built, with Echo, in a project or in a chat.
---

# Echo UI

Echo UI is a design system for React: components that press, click and move, all on one grammar (the `echo-ui-core` package: theme, sound, motion), with the builder's own style on top. A style changes the look (colours, type, radius, finish, density); the feel stays Echo's.

## Where you are

- **A project with Echo** (an `echo.json` at its root): the project's own Echo skill leads, with the Echo block `init` wrote into the project's agent instructions. They know the project's folder, its style and its checks. Follow them, and leave this one.
- **A project without Echo, with a terminal** (any agent that runs commands in the builder's code): set it up first. `npx echo-ui-cli init`, or `npx echo-ui-cli init --style <name>` when the builder has a style for this product (Echo's `echo-style-fit` skill picks one). `init` writes the project's own skill, `DESIGN.md` and the check, and from then on they lead.
- **A chat, with no terminal** (with Echo's connector): the rest of this skill.

## In a chat: make the style here, build with it in the code tool

1. **A look of their own.** A moodboard goes to Echo's `echo-design-eye` skill, which turns it into a style. Echo's `echo-style-fit` skill picks the style that fits the product, from Echo's and the builder's own. `wear_style` shows the pick: its link makes Echo's whole site wear the style's colours, so the builder can feel it before anything is built.
2. **A screen or a component.** Name the screen's one main action; everything else on it is quieter. Find each part with `search_components` ("a settings toggle", "confirm a delete"), and read it with `get_component` before using it: its anti-patterns are the part a model gets wrong. Style only with `var(--echo-*)`, from `get_tokens`; never a hex, a duration or a shadow by hand.
3. **Check before handing over.** Run `check_code` on every file you write, and fix what it reports the way each finding says. It's the same check the CLI runs in a project.
4. **The handoff.** The code goes into a project in the builder's code tool. End with the commands, in order: `npx echo-ui-cli init --style <name>` (or `npx echo-ui-cli init`, with no style), then `npx echo-ui-cli add <name>` for each component the code uses. A style of the builder's own has to be in their library first, as `wear_style` says.

Echo's components aren't an npm package: `npx echo-ui-cli add` copies each one's source into the project, which owns it from then on. Never write `npm install` for a component; the one package is `echo-ui-core`. The Base UI package is `@base-ui/react` (per-component imports, e.g. `@base-ui/react/dialog`), NOT `@base-ui-components/react` (the old name). Training data may be stale.

The accessibility floor, on every screen: every control has a name: `label`, `aria-label` or `aria-labelledby` (the types require it); a form error goes in words, in the field's `error`; never colour alone; announce with `toast()` from `useToast()`, under one `<Toaster>`; never remove a focus ring, shrink a target below 24×24px, or put `aria-hidden` on something focusable. `get_accessibility` has the rest.
