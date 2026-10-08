---
name: mavixx-design-system
description: Define and apply a project-specific visual system to a real user interface using approved brand assets, existing product patterns, or an inferred design direction. Use for new UI implementation, substantial UI or UX upgrades, broad redesigns, or inconsistent interfaces; use `$mavixx-project-upgrade` as the orchestrator for a full existing-project upgrade and do not activate for backend-only work.
---

# Mavixx Design System

Create and implement a distinctive, usable visual direction without forcing one aesthetic on every product. Documentation supports the interface; it does not replace the interface.

Read [references/design-workflow.md](references/design-workflow.md). Adapt [assets/DESIGN.template.md](assets/DESIGN.template.md) into the project's root `DESIGN.md` when a durable design source of truth is useful. If the user asked to build or improve the UI, continue by applying the system to the actual source code.

## Inputs and decisions

Inspect existing brand assets and UI first. Classify missing inputs:

- **Blocking:** brand identity conflict, regulated content, required licensed font/assets, or a visual direction with materially different implementation cost.
- **Recommended:** logo, audience, personality, competitor/reference examples, preferred and forbidden styles.
- **Generatable:** initial palette, type pairing, tokens, component language, motion direction, and placeholder imagery.

When references are absent, derive a recommended direction from the product, audience, task frequency, content density, and existing brand. Present multiple directions only when the choice materially changes identity or implementation cost, or when the user requests options. When references are provided, extract principles—hierarchy, rhythm, density, composition, and motion—without copying protected brand elements or content.

## Rules

- When created, `DESIGN.md` must define semantic tokens, typography, spacing, layout, components, states, imagery, motion, responsive behavior, accessibility constraints, and an explicit anti-pattern list.
- Preserve an existing working design unless redesign is requested or inconsistency is part of the task.
- Prefer coherent native components over a collage of unrelated component-library examples.
- Implement foundations in the project's existing styling system, then update shared components and page shells before one-off page decoration.
- Preserve functioning routes, content, data states, forms, and interactions. A visually polished static mock is not a successful upgrade of a working product.
- Treat third-party design skills such as `gpt-taste` as optional specialists. Recommend them only when their strong editorial/GSAP style fits; disclose the source and obtain approval before installation.
- Start or preview the app, inspect representative desktop and mobile states, correct visual and interaction defects, and invoke `$mavixx-quality-gates` after implementation. Do not claim the UI was upgraded from source inspection alone.
