# UI Design

## Purpose

Coordinate component selection and the UI design skills when creating or materially recomposing an interface. Focused corrections use their owning skill directly.

[Agent Instructions](AGENTS.md) owns the brief, approval, skill loading, and Final QA. [User Experience](user-experience.md) owns tasks, content, behavior, and recovery. This skill coordinates composition and review.

## Required Related Resources

- [Component Tokens](canonical/component-tokens.md) — `alpy/component-tokens.md`: styling slots and bindings.
- [Canonical Components](canonical/components.md) — `alpy/components.md`: supported components, options, and behavior.
- [Semantic Tokens](canonical/semantic-tokens.md) — `alpy/semantic-tokens.md`: semantic roles for non-component areas.
- [Foundations](canonical/foundations.md) — `alpy/foundations.md`: resolved spacing, size, border, radius, and icon values.
- [Palette](canonical/palette.md) — `alpy/palette.md`: mode-specific color values reached through token bindings.
- [Type Scale](canonical/type-scale.md) — `alpy/type-scale.md`: canonical text roles and complete typography tuples.

Read canonical resources through Alpy MCP. Follow the selected skills, declared dependencies, and mandatory triggers in Agent Instructions.

## Component Selection

| Need | Use |
|---|---|
| Button/action | `Button` with the appropriate supported variant. |
| Text entry | `Text Input` for single-line entry; `Textarea` for multiline entry. |
| Date entry | `Date Picker`. |
| Multiple independent choices | `Checkbox`. |
| One choice from a set | `Radio`; `Dropdown` for a supported option picker. |
| Immediate on/off setting | `Toggle`. |
| Data display | `Table` for structured comparisons; `Cell` within tables/lists; `Card` for grouped content; `Badge` for compact status or metadata. |
| Navigation | `Breadcrumb` for hierarchy; `Tabs` for peer views; `Pagination` for result pages. |
| Overlays | `Modal` for blocking focused tasks; `Popover` for anchored contextual content. |
| Feedback | `Alert` for status, notices, and outcomes. |
| Progress | `Progress Bar` for loading or amount; `Progress Indicator` for process steps. |
| Expand/collapse content | `Accordion`. |
| Menus | `Dropdown` with supported menu behavior. |
| Brief contextual help | `Tooltip`; keep required information visible in the task. |
| Media and icons | `Image` with a supported ratio; `Icons` for canonical icon instances. |

### Component Workflow

1. **Check existing components first.** Reuse available canonical implementations. Verify that a component exists in the project before importing it; avoid duplicate implementations.
2. **Read supported usage.** Confirm anatomy, required children, variants, states, content options, and behavior against the canonical definitions. Preserve internal anatomy and component-token bindings.
3. **Use verified project paths.** Follow the project's actual import aliases and canonical icon references; do not assume default paths or substitute icon libraries.
4. **Preview component updates.** Inspect the proposed diff and preserve unrelated project changes.
5. **Review changed files.** Fix missing imports, missing required children, incorrect composition, and unsupported overrides before rendered QA.

Report unsupported needs instead of inventing components or behavior.

## Semantic Tokens for Non-Component Areas

You have to use `semantic-tokens.md` for non-component areas. Don't interpret this rule.

Component-owned UI uses `component-tokens.md`; follow its bindings to the required resources without selecting replacement tokens.

| Category | Includes |
|---|---|
| Color | Shades, System, Surface, Shadow, Functional, Border, Text, Icon |
| Space | Spacing roles |
| Border | Width, Radius |
| Icon | Size, Gap |
| Shadow | Complete shadow styles |

Resolve exact roles and mappings for the explicit `light` or `dark` mode. Report missing coverage; never invent tokens or substitute raw values.

## Compose the Interface

Start from confirmed content, behavior, states, mode, style, and component support. Work outside-in and revisit affected passes when content fit or emphasis changes.

| Pass | Coordination |
|---|---|
| Relationships and attention | [Gestalt](ui-design/gestalt.md) establishes groups; [Visual Hierarchy](ui-design/visual-hierarchy.md) expresses confirmed priority. |
| Structure and fit | [Grid and Layout](ui-design/grid-layout.md) places regions; [Scale and Proportion](ui-design/scale-proportion.md) sizes them around real content. |
| Reading and spacing | Coordinate [Typography and Readability](ui-design/typography-readability.md), [Rhythm and Space](ui-design/rhythm-space.md), and [Alignment](ui-design/alignment.md). |
| Surfaces and separation | Coordinate [Color Discipline](ui-design/color-discipline.md), [Border and Divider](ui-design/border-divider.md), and [Elevation](ui-design/elevation.md). |
| Composition and change | [Balance](ui-design/balance.md) checks combined visual weight; [Motion and Transition](ui-design/motion-transition.md) expresses relevant state changes. |

Apply the confirmed [Hero](hero.md), brand, and website-style direction where relevant. Use [Responsive Adaptation](responsive-adaptation.md) for target contexts, then recheck composition and consistency across screens and states.

## Evaluate the Finished Interface

Within shared Final QA:

1. **Inspect renders:** Check real content across relevant sizes for clear hierarchy, suitable components, confirmed style, consistent spacing/alignment, and wrapping or overflow defects.
2. **Test tasks and states:** Verify completion, interruption, and recovery across supported interaction, loading, empty, error, and success states. Check feedback, data continuity, and applicable inputs.
3. **Verify accessibility:** Use [Accessibility Audit](accessibility-audit.md) and preserve confirmed style-review requirements.
4. **Fix and recheck:** Route issues to their owners and retest affected renders and tasks. Resolve blockers before declaring readiness; report remaining issues and untested conditions.

Token compliance alone is not visual proof; untested conditions are not passes.
