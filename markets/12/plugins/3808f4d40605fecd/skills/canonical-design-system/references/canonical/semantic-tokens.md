# Semantic Tokens

This file carries the package semantic aliases and mode-specific mappings for color intent. Agents should resolve UI color choices through these semantic tokens before reading primitive palette shades.

## Semantic Token Contract

Use this file as the semantic color intent contract.

It answers:

1. What semantic color family matches the UI intent?
2. Which token id is allowed for that intent?
3. Which mode-specific palette target does the token resolve to?
4. When must the agent stop instead of inventing a color?

The guidance sections explain how to choose. The YAML data below is the package truth.

Do not treat these guidance sections as alternate token definitions. If guidance and generated YAML disagree, generated YAML wins.

## Semantic Token Selection Workflow

1. Resolve the explicit mode first: `light` or `dark`.
2. Decide whether the UI is component-owned.
3. If the UI is component-owned, start in `component-tokens.md` and follow its token binding here.
4. If the UI is not component-owned, identify the visual property: text, surface, border, icon, feedback fill, or interaction state.
5. Select the semantic token family by meaning, not by visual similarity.
6. Read the matching token definition and description in this file.
7. Confirm the token exists in `byMode[mode]`.
8. Follow `target.paletteId` and `target.shadeId` to `palette.md`.
9. Stop if the token, mode mapping, palette, shade, or intended semantic family is missing.

## Semantic Intent Chooser

| Intent | Start With | Use For | Do Not Use For |
|---|---|---|---|
| Page or app canvas | `color.surface.canvas` | Page backgrounds and base app surfaces. | Component containers with their own component-token binding. |
| Body text | `color.text.body` | Primary readable content. | Headings, links, disabled text, status text, or text on color. |
| Muted text | `color.text.body.muted` | Secondary copy, metadata, quiet labels. | Critical instructions, errors, or primary actions. |
| Subtle text | `color.text.body.subtle` | Low-emphasis supporting text. | Required labels, validation, or contrast-critical copy. |
| Headings | `color.text.heading`, `color.text.subheading` | Page, section, modal, and content hierarchy. | Body copy or decorative emphasis. |
| Links | `color.text.link.*` | Link default, hover, pressed, visited, disabled, and inverse states. | Buttons, arbitrary brand accents, or non-navigation text. |
| Text on strong color | `color.text.onColor`, `color.text.heading.onColor` | Text placed on strong brand, functional, or dark colored surfaces. | Normal canvas text or low-contrast decorative text. |
| Neutral borders | `color.border.neutral.*` | Dividers, outlines, separators, containers. | Focus rings, brand accents, functional feedback, or input borders. |
| Input borders | `color.border.input` | Form fields and input controls. | Static containers, cards, or status outlines. |
| Icons | `color.icon.default`, `color.icon.subtle`, `color.icon.subtlest` | Neutral icons by emphasis level. | Status icons, brand icons, or interactive state icons. |
| Functional feedback | `color.functional.*`, `color.text.functional.*`, `color.border.functional.*`, `color.icon.*` status tokens | Success, warning, danger, and info feedback across fills, text, borders, and icons. | Decoration, branding, or general emphasis. |
| Interaction states | `color.surface.interaction.*`, `color.border.interaction.*`, `color.icon.interaction.*` | Hover, focused, pressed, selected, and disabled interactive states. | Static content, feedback severity, or brand-only emphasis. |
| Brand emphasis | `color.text.brand.*`, `color.border.brand.*`, `color.icon.brand.*` | Identity, selected brand moments, primary emphasis, and branded accents. | Functional feedback, destructive actions, neutral structure, or dense decoration. |
| On-color or inverse UI | `*.onColor`, `*.inverse` | Foreground elements on strong colored or inverse surfaces. | Normal light/dark canvas decisions. |
| System colors | `color.system.black`, `color.system.white`, `color.system.transparent` | Explicit system-level black, white, or transparent needs. | Semantic UI decisions that have a role-specific token. |

## Status And Severity Rules

Functional color is reserved for meaning.

| Severity | Fill | Text | Border | Icon |
|---|---|---|---|---|
| Danger | `color.functional.danger*` | `color.text.functional.danger*` | `color.border.functional.danger` | `color.icon.danger` |
| Warning | `color.functional.warning*` | `color.text.functional.warning*` | `color.border.functional.warning` | `color.icon.warning` |
| Success | `color.functional.success*` | `color.text.functional.success*` | `color.border.functional.success` | `color.icon.success` |
| Info | `color.functional.info*` | `color.text.functional.info*` | `color.border.functional.info` | `color.icon.info` |

Use the same severity across fill, text, border, and icon when those parts describe one status message.

Do not mix severities in one message unless the product explicitly needs multiple independent statuses.

Do not use functional tokens only to make a screen more colorful.

## Interaction State Rules

Interaction tokens describe user interaction states, not general decoration.

Use:

- `disabled` only when the control is unavailable.
- `hover` only for pointer hover affordance.
- `focused` only for visible focus or focus-related structure.
- `pressed` only for active press state.
- `selected` only when an item is selected, active, checked, or current.

If a state belongs to a component, resolve it through `component-tokens.md` first. The component binding chooses the semantic token.

## Brand And Neutral Rules

Brand tokens communicate identity and intentional emphasis.

Use brand tokens for:

- Primary brand accents.
- Selected branded moments.
- Branded links or highlights when allowed by the UI pattern.
- Brand-owned borders or icons.

Do not use brand tokens for:

- Error, warning, success, or info states.
- Disabled states.
- Generic dividers or layout structure.
- Many competing elements in the same decision area.

Neutral tokens communicate hierarchy and structure.

Use neutral tokens for:

- Body text and secondary copy.
- Quiet icons.
- Dividers, outlines, and containers.
- Non-status, non-brand UI structure.

## Component-Owned Color Rule

When a canonical component owns the UI, do not select semantic tokens directly for that component's styling.

Resolve in this order:

1. `components.md` for component anatomy, allowed variants, states, axes, and content options.
2. `component-tokens.md` for component token slots and mode-specific token bindings.
3. This file for the semantic token target behind the component binding.
4. `palette.md` for the final palette shade.

Only use this file directly for UI that is not owned by a component token slot.

## Helper Description Rule

Every semantic token definition in this file may include a `description`.

Treat `description` as usage guidance text:

- Use it to understand intended usage.
- Use it to identify misuse and anti-patterns.
- Use it to choose between nearby tokens.
- Do not use it to override the token id, category, mode mapping, palette target, or generated package data.

## Stop Conditions

Stop and report a design-system gap when:

- The mode is not explicitly `light` or `dark`.
- The required semantic token id is missing.
- The token exists in one mode but not the active mode.
- The token category does not match the UI property.
- The requested severity, state, emphasis, or on-color relationship is not represented.
- A component-owned color is being styled directly instead of through `component-tokens.md`.
- The token target points to a missing palette or shade.
- The task requires raw color values, palette guesses, opacity tweaks, or local CSS substitutes.

Useful gap language:

- Missing semantic token for `<intent>`.
- Missing `<mode>` mapping for `<tokenId>`.
- Missing functional severity token for `<severity>/<property>`.
- Missing interaction state token for `<state>/<property>`.
- Missing component token binding for `<component>/<variant>/<state>/<slot>`.

## Canonical Semantic Token Data

```yaml
byMode:
  dark:
    "color.border.brand.color-one.strong.one":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.border.brand.color-one.strong.one"
    "color.border.brand.color-one.strong.three":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.border.brand.color-one.strong.three"
    "color.border.brand.color-one.strong.two":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "400"
      tokenId: "color.border.brand.color-one.strong.two"
    "color.border.brand.color-one.subtle.one":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.border.brand.color-one.subtle.one"
    "color.border.brand.color-one.subtle.three":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.border.brand.color-one.subtle.three"
    "color.border.brand.color-one.subtle.two":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "800"
      tokenId: "color.border.brand.color-one.subtle.two"
    "color.border.brand.color-three.strong.one":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.border.brand.color-three.strong.one"
    "color.border.brand.color-three.strong.three":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.border.brand.color-three.strong.three"
    "color.border.brand.color-three.strong.two":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "400"
      tokenId: "color.border.brand.color-three.strong.two"
    "color.border.brand.color-three.subtle.one":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.border.brand.color-three.subtle.one"
    "color.border.brand.color-three.subtle.three":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.border.brand.color-three.subtle.three"
    "color.border.brand.color-three.subtle.two":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "800"
      tokenId: "color.border.brand.color-three.subtle.two"
    "color.border.brand.color-two.strong.one":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.border.brand.color-two.strong.one"
    "color.border.brand.color-two.strong.three":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.border.brand.color-two.strong.three"
    "color.border.brand.color-two.strong.two":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "400"
      tokenId: "color.border.brand.color-two.strong.two"
    "color.border.brand.color-two.subtle.one":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.border.brand.color-two.subtle.one"
    "color.border.brand.color-two.subtle.three":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.border.brand.color-two.subtle.three"
    "color.border.brand.color-two.subtle.two":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "800"
      tokenId: "color.border.brand.color-two.subtle.two"
    "color.border.functional.danger":
      category: "border"
      target:
        paletteId: "palette.danger"
        shadeId: "100"
      tokenId: "color.border.functional.danger"
    "color.border.functional.info":
      category: "border"
      target:
        paletteId: "palette.info"
        shadeId: "100"
      tokenId: "color.border.functional.info"
    "color.border.functional.success":
      category: "border"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.border.functional.success"
    "color.border.functional.warning":
      category: "border"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.border.functional.warning"
    "color.border.input":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.border.input"
    "color.border.interaction.disabled":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.border.interaction.disabled"
    "color.border.interaction.focused":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.border.interaction.focused"
    "color.border.interaction.hover":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.border.interaction.hover"
    "color.border.interaction.pressed":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.border.interaction.pressed"
    "color.border.interaction.selected":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.border.interaction.selected"
    "color.border.neutral.strong.one":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.border.neutral.strong.one"
    "color.border.neutral.strong.three":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.border.neutral.strong.three"
    "color.border.neutral.strong.two":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "400"
      tokenId: "color.border.neutral.strong.two"
    "color.border.neutral.subtle.one":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.border.neutral.subtle.one"
    "color.border.neutral.subtle.three":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.border.neutral.subtle.three"
    "color.border.neutral.subtle.two":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "800"
      tokenId: "color.border.neutral.subtle.two"
    "color.border.onColor":
      category: "border"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.border.onColor"
    "color.functional.danger":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "100"
      tokenId: "color.functional.danger"
    "color.functional.danger.soft":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.functional.danger.soft"
    "color.functional.danger.strong":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "50"
      tokenId: "color.functional.danger.strong"
    "color.functional.danger.subtle":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "300"
      tokenId: "color.functional.danger.subtle"
    "color.functional.info":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "100"
      tokenId: "color.functional.info"
    "color.functional.info.soft":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.functional.info.soft"
    "color.functional.info.strong":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "50"
      tokenId: "color.functional.info.strong"
    "color.functional.info.subtle":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "300"
      tokenId: "color.functional.info.subtle"
    "color.functional.success":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "100"
      tokenId: "color.functional.success"
    "color.functional.success.soft":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.functional.success.soft"
    "color.functional.success.strong":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "50"
      tokenId: "color.functional.success.strong"
    "color.functional.success.subtle":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "300"
      tokenId: "color.functional.success.subtle"
    "color.functional.warning":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "100"
      tokenId: "color.functional.warning"
    "color.functional.warning.soft":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.functional.warning.soft"
    "color.functional.warning.strong":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "50"
      tokenId: "color.functional.warning.strong"
    "color.functional.warning.subtle":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "300"
      tokenId: "color.functional.warning.subtle"
    "color.icon.accent":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.icon.accent"
    "color.icon.brand.color-one.strong.one":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-one.strong.one"
    "color.icon.brand.color-one.strong.three":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-one.strong.three"
    "color.icon.brand.color-one.strong.two":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-one.strong.two"
    "color.icon.brand.color-one.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-one.subtle.one"
    "color.icon.brand.color-one.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-one.subtle.three"
    "color.icon.brand.color-one.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-one.subtle.two"
    "color.icon.brand.color-three.strong.one":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-three.strong.one"
    "color.icon.brand.color-three.strong.three":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-three.strong.three"
    "color.icon.brand.color-three.strong.two":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-three.strong.two"
    "color.icon.brand.color-three.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-three.subtle.one"
    "color.icon.brand.color-three.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-three.subtle.three"
    "color.icon.brand.color-three.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-three.subtle.two"
    "color.icon.brand.color-two.strong.one":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-two.strong.one"
    "color.icon.brand.color-two.strong.three":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-two.strong.three"
    "color.icon.brand.color-two.strong.two":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-two.strong.two"
    "color.icon.brand.color-two.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-two.subtle.one"
    "color.icon.brand.color-two.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-two.subtle.three"
    "color.icon.brand.color-two.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-two.subtle.two"
    "color.icon.danger":
      category: "icon"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.icon.danger"
    "color.icon.default":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.icon.default"
    "color.icon.disabled":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.icon.disabled"
    "color.icon.info":
      category: "icon"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.icon.info"
    "color.icon.interaction.disabled":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.icon.interaction.disabled"
    "color.icon.interaction.focused":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.icon.interaction.focused"
    "color.icon.interaction.hover":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.icon.interaction.hover"
    "color.icon.interaction.pressed":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.icon.interaction.pressed"
    "color.icon.interaction.selected":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.icon.interaction.selected"
    "color.icon.inverse":
      category: "icon"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "black"
      tokenId: "color.icon.inverse"
    "color.icon.onColor":
      category: "icon"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.icon.onColor"
    "color.icon.subtle":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.icon.subtle"
    "color.icon.subtlest":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.icon.subtlest"
    "color.icon.success":
      category: "icon"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.icon.success"
    "color.icon.warning":
      category: "icon"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.icon.warning"
    "color.shades.brand.color-one.strong-one":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-one.strong-one"
    "color.shades.brand.color-one.strong-three":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-one.strong-three"
    "color.shades.brand.color-one.strong-two":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-one.strong-two"
    "color.shades.brand.color-one.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-one.subtle-one"
    "color.shades.brand.color-one.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-one.subtle-three"
    "color.shades.brand.color-one.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-one.subtle-two"
    "color.shades.brand.color-three.strong-one":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-three.strong-one"
    "color.shades.brand.color-three.strong-three":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-three.strong-three"
    "color.shades.brand.color-three.strong-two":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-three.strong-two"
    "color.shades.brand.color-three.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-three.subtle-one"
    "color.shades.brand.color-three.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-three.subtle-three"
    "color.shades.brand.color-three.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-three.subtle-two"
    "color.shades.brand.color-two.strong-one":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-two.strong-one"
    "color.shades.brand.color-two.strong-three":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-two.strong-three"
    "color.shades.brand.color-two.strong-two":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-two.strong-two"
    "color.shades.brand.color-two.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-two.subtle-one"
    "color.shades.brand.color-two.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-two.subtle-three"
    "color.shades.brand.color-two.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-two.subtle-two"
    "color.shades.neutral.strong-one":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.shades.neutral.strong-one"
    "color.shades.neutral.strong-three":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.shades.neutral.strong-three"
    "color.shades.neutral.strong-two":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.shades.neutral.strong-two"
    "color.shades.neutral.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.shades.neutral.subtle-one"
    "color.shades.neutral.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.shades.neutral.subtle-three"
    "color.shades.neutral.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.shades.neutral.subtle-two"
    "color.shadow.deep":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.shadow.deep"
    "color.shadow.medium":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.shadow.medium"
    "color.shadow.soft":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.shadow.soft"
    "color.shadow.strong":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.shadow.strong"
    "color.surface.canvas":
      category: "surface"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "black"
      tokenId: "color.surface.canvas"
    "color.surface.interaction.disabled":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.surface.interaction.disabled"
    "color.surface.interaction.focused":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "800"
      tokenId: "color.surface.interaction.focused"
    "color.surface.interaction.hover":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "800"
      tokenId: "color.surface.interaction.hover"
    "color.surface.interaction.pressed":
      category: "surface"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.surface.interaction.pressed"
    "color.surface.interaction.selected":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.surface.interaction.selected"
    "color.system.black":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "black"
      tokenId: "color.system.black"
    "color.system.transparent":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "transparent"
      tokenId: "color.system.transparent"
    "color.system.white":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.system.white"
    "color.text.body":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.text.body"
    "color.text.body.muted":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.text.body.muted"
    "color.text.body.subtle":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "400"
      tokenId: "color.text.body.subtle"
    "color.text.brand.color-one.accent":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.text.brand.color-one.accent"
    "color.text.brand.color-one.accent.strong":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.text.brand.color-one.accent.strong"
    "color.text.brand.color-one.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "400"
      tokenId: "color.text.brand.color-one.accent.subtle"
    "color.text.brand.color-three.accent":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.text.brand.color-three.accent"
    "color.text.brand.color-three.accent.strong":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "200"
      tokenId: "color.text.brand.color-three.accent.strong"
    "color.text.brand.color-three.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "400"
      tokenId: "color.text.brand.color-three.accent.subtle"
    "color.text.brand.color-two.accent":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.text.brand.color-two.accent"
    "color.text.brand.color-two.accent.strong":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "200"
      tokenId: "color.text.brand.color-two.accent.strong"
    "color.text.brand.color-two.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "400"
      tokenId: "color.text.brand.color-two.accent.subtle"
    "color.text.functional.danger":
      category: "text"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.text.functional.danger"
    "color.text.functional.danger.strong":
      category: "text"
      target:
        paletteId: "palette.danger"
        shadeId: "300"
      tokenId: "color.text.functional.danger.strong"
    "color.text.functional.info":
      category: "text"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.text.functional.info"
    "color.text.functional.info.strong":
      category: "text"
      target:
        paletteId: "palette.info"
        shadeId: "300"
      tokenId: "color.text.functional.info.strong"
    "color.text.functional.success":
      category: "text"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.text.functional.success"
    "color.text.functional.success.strong":
      category: "text"
      target:
        paletteId: "palette.success"
        shadeId: "300"
      tokenId: "color.text.functional.success.strong"
    "color.text.functional.warning":
      category: "text"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.text.functional.warning"
    "color.text.functional.warning.strong":
      category: "text"
      target:
        paletteId: "palette.warning"
        shadeId: "300"
      tokenId: "color.text.functional.warning.strong"
    "color.text.heading":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.text.heading"
    "color.text.heading.onColor":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.heading.onColor"
    "color.text.inverse":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.inverse"
    "color.text.link":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.text.link"
    "color.text.link.disabled":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.text.link.disabled"
    "color.text.link.hover":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.text.link.hover"
    "color.text.link.inverse":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.text.link.inverse"
    "color.text.link.pressed":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "400"
      tokenId: "color.text.link.pressed"
    "color.text.link.visited":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.text.link.visited"
    "color.text.onColor":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.onColor"
    "color.text.subheading":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.text.subheading"
  light:
    "color.border.brand.color-one.strong.one":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.border.brand.color-one.strong.one"
    "color.border.brand.color-one.strong.three":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.border.brand.color-one.strong.three"
    "color.border.brand.color-one.strong.two":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.border.brand.color-one.strong.two"
    "color.border.brand.color-one.subtle.one":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "50"
      tokenId: "color.border.brand.color-one.subtle.one"
    "color.border.brand.color-one.subtle.three":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.border.brand.color-one.subtle.three"
    "color.border.brand.color-one.subtle.two":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "100"
      tokenId: "color.border.brand.color-one.subtle.two"
    "color.border.brand.color-three.strong.one":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.border.brand.color-three.strong.one"
    "color.border.brand.color-three.strong.three":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.border.brand.color-three.strong.three"
    "color.border.brand.color-three.strong.two":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.border.brand.color-three.strong.two"
    "color.border.brand.color-three.subtle.one":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "50"
      tokenId: "color.border.brand.color-three.subtle.one"
    "color.border.brand.color-three.subtle.three":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.border.brand.color-three.subtle.three"
    "color.border.brand.color-three.subtle.two":
      category: "border"
      target:
        paletteId: "palette.tertiary"
        shadeId: "100"
      tokenId: "color.border.brand.color-three.subtle.two"
    "color.border.brand.color-two.strong.one":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.border.brand.color-two.strong.one"
    "color.border.brand.color-two.strong.three":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.border.brand.color-two.strong.three"
    "color.border.brand.color-two.strong.two":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.border.brand.color-two.strong.two"
    "color.border.brand.color-two.subtle.one":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "50"
      tokenId: "color.border.brand.color-two.subtle.one"
    "color.border.brand.color-two.subtle.three":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.border.brand.color-two.subtle.three"
    "color.border.brand.color-two.subtle.two":
      category: "border"
      target:
        paletteId: "palette.secondary"
        shadeId: "100"
      tokenId: "color.border.brand.color-two.subtle.two"
    "color.border.functional.danger":
      category: "border"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.border.functional.danger"
    "color.border.functional.info":
      category: "border"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.border.functional.info"
    "color.border.functional.success":
      category: "border"
      target:
        paletteId: "palette.success"
        shadeId: "300"
      tokenId: "color.border.functional.success"
    "color.border.functional.warning":
      category: "border"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.border.functional.warning"
    "color.border.input":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.border.input"
    "color.border.interaction.disabled":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.border.interaction.disabled"
    "color.border.interaction.focused":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.border.interaction.focused"
    "color.border.interaction.hover":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.border.interaction.hover"
    "color.border.interaction.pressed":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.border.interaction.pressed"
    "color.border.interaction.selected":
      category: "border"
      target:
        paletteId: "palette.primary"
        shadeId: "600"
      tokenId: "color.border.interaction.selected"
    "color.border.neutral.strong.one":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.border.neutral.strong.one"
    "color.border.neutral.strong.three":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.border.neutral.strong.three"
    "color.border.neutral.strong.two":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.border.neutral.strong.two"
    "color.border.neutral.subtle.one":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.border.neutral.subtle.one"
    "color.border.neutral.subtle.three":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.border.neutral.subtle.three"
    "color.border.neutral.subtle.two":
      category: "border"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.border.neutral.subtle.two"
    "color.border.onColor":
      category: "border"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.border.onColor"
    "color.functional.danger":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.functional.danger"
    "color.functional.danger.soft":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "100"
      tokenId: "color.functional.danger.soft"
    "color.functional.danger.strong":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "300"
      tokenId: "color.functional.danger.strong"
    "color.functional.danger.subtle":
      category: "functional"
      target:
        paletteId: "palette.danger"
        shadeId: "50"
      tokenId: "color.functional.danger.subtle"
    "color.functional.info":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.functional.info"
    "color.functional.info.soft":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "100"
      tokenId: "color.functional.info.soft"
    "color.functional.info.strong":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "300"
      tokenId: "color.functional.info.strong"
    "color.functional.info.subtle":
      category: "functional"
      target:
        paletteId: "palette.info"
        shadeId: "50"
      tokenId: "color.functional.info.subtle"
    "color.functional.success":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.functional.success"
    "color.functional.success.soft":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "100"
      tokenId: "color.functional.success.soft"
    "color.functional.success.strong":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "300"
      tokenId: "color.functional.success.strong"
    "color.functional.success.subtle":
      category: "functional"
      target:
        paletteId: "palette.success"
        shadeId: "50"
      tokenId: "color.functional.success.subtle"
    "color.functional.warning":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.functional.warning"
    "color.functional.warning.soft":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "100"
      tokenId: "color.functional.warning.soft"
    "color.functional.warning.strong":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "300"
      tokenId: "color.functional.warning.strong"
    "color.functional.warning.subtle":
      category: "functional"
      target:
        paletteId: "palette.warning"
        shadeId: "50"
      tokenId: "color.functional.warning.subtle"
    "color.icon.accent":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.icon.accent"
    "color.icon.brand.color-one.strong.one":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-one.strong.one"
    "color.icon.brand.color-one.strong.three":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-one.strong.three"
    "color.icon.brand.color-one.strong.two":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-one.strong.two"
    "color.icon.brand.color-one.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-one.subtle.one"
    "color.icon.brand.color-one.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-one.subtle.three"
    "color.icon.brand.color-one.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-one.subtle.two"
    "color.icon.brand.color-three.strong.one":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-three.strong.one"
    "color.icon.brand.color-three.strong.three":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-three.strong.three"
    "color.icon.brand.color-three.strong.two":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-three.strong.two"
    "color.icon.brand.color-three.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-three.subtle.one"
    "color.icon.brand.color-three.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-three.subtle.three"
    "color.icon.brand.color-three.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.tertiary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-three.subtle.two"
    "color.icon.brand.color-two.strong.one":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.icon.brand.color-two.strong.one"
    "color.icon.brand.color-two.strong.three":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.icon.brand.color-two.strong.three"
    "color.icon.brand.color-two.strong.two":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.icon.brand.color-two.strong.two"
    "color.icon.brand.color-two.subtle.one":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "50"
      tokenId: "color.icon.brand.color-two.subtle.one"
    "color.icon.brand.color-two.subtle.three":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.icon.brand.color-two.subtle.three"
    "color.icon.brand.color-two.subtle.two":
      category: "icon"
      target:
        paletteId: "palette.secondary"
        shadeId: "100"
      tokenId: "color.icon.brand.color-two.subtle.two"
    "color.icon.danger":
      category: "icon"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.icon.danger"
    "color.icon.default":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.icon.default"
    "color.icon.disabled":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.icon.disabled"
    "color.icon.info":
      category: "icon"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.icon.info"
    "color.icon.interaction.disabled":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.icon.interaction.disabled"
    "color.icon.interaction.focused":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.icon.interaction.focused"
    "color.icon.interaction.hover":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.icon.interaction.hover"
    "color.icon.interaction.pressed":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.icon.interaction.pressed"
    "color.icon.interaction.selected":
      category: "icon"
      target:
        paletteId: "palette.primary"
        shadeId: "600"
      tokenId: "color.icon.interaction.selected"
    "color.icon.inverse":
      category: "icon"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.icon.inverse"
    "color.icon.onColor":
      category: "icon"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.icon.onColor"
    "color.icon.subtle":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "400"
      tokenId: "color.icon.subtle"
    "color.icon.subtlest":
      category: "icon"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.icon.subtlest"
    "color.icon.success":
      category: "icon"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.icon.success"
    "color.icon.warning":
      category: "icon"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.icon.warning"
    "color.shades.brand.color-one.strong-one":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-one.strong-one"
    "color.shades.brand.color-one.strong-three":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-one.strong-three"
    "color.shades.brand.color-one.strong-two":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-one.strong-two"
    "color.shades.brand.color-one.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-one.subtle-one"
    "color.shades.brand.color-one.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-one.subtle-three"
    "color.shades.brand.color-one.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.primary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-one.subtle-two"
    "color.shades.brand.color-three.strong-one":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-three.strong-one"
    "color.shades.brand.color-three.strong-three":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-three.strong-three"
    "color.shades.brand.color-three.strong-two":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-three.strong-two"
    "color.shades.brand.color-three.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-three.subtle-one"
    "color.shades.brand.color-three.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-three.subtle-three"
    "color.shades.brand.color-three.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.tertiary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-three.subtle-two"
    "color.shades.brand.color-two.strong-one":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.shades.brand.color-two.strong-one"
    "color.shades.brand.color-two.strong-three":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "900"
      tokenId: "color.shades.brand.color-two.strong-three"
    "color.shades.brand.color-two.strong-two":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.shades.brand.color-two.strong-two"
    "color.shades.brand.color-two.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "50"
      tokenId: "color.shades.brand.color-two.subtle-one"
    "color.shades.brand.color-two.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "300"
      tokenId: "color.shades.brand.color-two.subtle-three"
    "color.shades.brand.color-two.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.secondary"
        shadeId: "100"
      tokenId: "color.shades.brand.color-two.subtle-two"
    "color.shades.neutral.strong-one":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "500"
      tokenId: "color.shades.neutral.strong-one"
    "color.shades.neutral.strong-three":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.shades.neutral.strong-three"
    "color.shades.neutral.strong-two":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.shades.neutral.strong-two"
    "color.shades.neutral.subtle-one":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.shades.neutral.subtle-one"
    "color.shades.neutral.subtle-three":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.shades.neutral.subtle-three"
    "color.shades.neutral.subtle-two":
      category: "shades"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.shades.neutral.subtle-two"
    "color.shadow.deep":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.shadow.deep"
    "color.shadow.medium":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "400"
      tokenId: "color.shadow.medium"
    "color.shadow.soft":
      category: "shadow"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.shadow.soft"
    "color.shadow.strong":
      category: "shadow"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "black"
      tokenId: "color.shadow.strong"
    "color.surface.canvas":
      category: "surface"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.surface.canvas"
    "color.surface.interaction.disabled":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "50"
      tokenId: "color.surface.interaction.disabled"
    "color.surface.interaction.focused":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.surface.interaction.focused"
    "color.surface.interaction.hover":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "100"
      tokenId: "color.surface.interaction.hover"
    "color.surface.interaction.pressed":
      category: "surface"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.surface.interaction.pressed"
    "color.surface.interaction.selected":
      category: "surface"
      target:
        paletteId: "palette.neutral"
        shadeId: "200"
      tokenId: "color.surface.interaction.selected"
    "color.system.black":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "black"
      tokenId: "color.system.black"
    "color.system.transparent":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "transparent"
      tokenId: "color.system.transparent"
    "color.system.white":
      category: "system"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.system.white"
    "color.text.body":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.text.body"
    "color.text.body.muted":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "300"
      tokenId: "color.text.body.muted"
    "color.text.body.subtle":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "400"
      tokenId: "color.text.body.subtle"
    "color.text.brand.color-one.accent":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.text.brand.color-one.accent"
    "color.text.brand.color-one.accent.strong":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.text.brand.color-one.accent.strong"
    "color.text.brand.color-one.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "400"
      tokenId: "color.text.brand.color-one.accent.subtle"
    "color.text.brand.color-three.accent":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "500"
      tokenId: "color.text.brand.color-three.accent"
    "color.text.brand.color-three.accent.strong":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "700"
      tokenId: "color.text.brand.color-three.accent.strong"
    "color.text.brand.color-three.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.tertiary"
        shadeId: "400"
      tokenId: "color.text.brand.color-three.accent.subtle"
    "color.text.brand.color-two.accent":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "500"
      tokenId: "color.text.brand.color-two.accent"
    "color.text.brand.color-two.accent.strong":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.text.brand.color-two.accent.strong"
    "color.text.brand.color-two.accent.subtle":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "400"
      tokenId: "color.text.brand.color-two.accent.subtle"
    "color.text.functional.danger":
      category: "text"
      target:
        paletteId: "palette.danger"
        shadeId: "200"
      tokenId: "color.text.functional.danger"
    "color.text.functional.danger.strong":
      category: "text"
      target:
        paletteId: "palette.danger"
        shadeId: "300"
      tokenId: "color.text.functional.danger.strong"
    "color.text.functional.info":
      category: "text"
      target:
        paletteId: "palette.info"
        shadeId: "200"
      tokenId: "color.text.functional.info"
    "color.text.functional.info.strong":
      category: "text"
      target:
        paletteId: "palette.info"
        shadeId: "300"
      tokenId: "color.text.functional.info.strong"
    "color.text.functional.success":
      category: "text"
      target:
        paletteId: "palette.success"
        shadeId: "200"
      tokenId: "color.text.functional.success"
    "color.text.functional.success.strong":
      category: "text"
      target:
        paletteId: "palette.success"
        shadeId: "300"
      tokenId: "color.text.functional.success.strong"
    "color.text.functional.warning":
      category: "text"
      target:
        paletteId: "palette.warning"
        shadeId: "200"
      tokenId: "color.text.functional.warning"
    "color.text.functional.warning.strong":
      category: "text"
      target:
        paletteId: "palette.warning"
        shadeId: "300"
      tokenId: "color.text.functional.warning.strong"
    "color.text.heading":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "900"
      tokenId: "color.text.heading"
    "color.text.heading.onColor":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.heading.onColor"
    "color.text.inverse":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.inverse"
    "color.text.link":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "500"
      tokenId: "color.text.link"
    "color.text.link.disabled":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "200"
      tokenId: "color.text.link.disabled"
    "color.text.link.hover":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "700"
      tokenId: "color.text.link.hover"
    "color.text.link.inverse":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.link.inverse"
    "color.text.link.pressed":
      category: "text"
      target:
        paletteId: "palette.primary"
        shadeId: "900"
      tokenId: "color.text.link.pressed"
    "color.text.link.visited":
      category: "text"
      target:
        paletteId: "palette.secondary"
        shadeId: "700"
      tokenId: "color.text.link.visited"
    "color.text.onColor":
      category: "text"
      target:
        paletteId: "palette.black-and-white"
        shadeId: "white"
      tokenId: "color.text.onColor"
    "color.text.subheading":
      category: "text"
      target:
        paletteId: "palette.neutral"
        shadeId: "700"
      tokenId: "color.text.subheading"
definitions:
  -
    categoryId: "semantics.border.weight"
    defaultValue: 0
    id: "border.width.0"
    label: "0"
    valueType: "number"
  -
    categoryId: "semantics.border.weight"
    defaultValue: 1
    id: "border.width.1"
    label: "1"
    valueType: "number"
  -
    categoryId: "semantics.border.weight"
    defaultValue: 1.5
    id: "border.width.1.5"
    label: "1.5"
    valueType: "number"
  -
    categoryId: "semantics.border.weight"
    defaultValue: 2
    id: "border.width.2"
    label: "2"
    valueType: "number"
  -
    categoryId: "semantics.border.weight"
    defaultValue: 4
    id: "border.width.4"
    label: "4"
    valueType: "number"
  -
    categoryId: "semantics.border.weight"
    defaultValue: 0.5
    id: "border.width.hairline"
    label: "Hairline"
    valueType: "number"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Primary brand border color for focused outlines, selected controls, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Highest-emphasis primary brand border color for maximum-strength branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Strong primary brand border color for high-emphasis branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Lowest-emphasis primary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Medium-emphasis primary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-one"
    description: "Low-emphasis primary brand border color for secondary branded outlines and muted branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-one.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Tertiary brand border color for selected controls, branded focus alternatives, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Highest-emphasis tertiary brand border color for maximum-strength branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Strong tertiary brand border color for high-emphasis branded outlines and prominent branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Lowest-emphasis tertiary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Medium-emphasis tertiary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-three"
    description: "Low-emphasis tertiary brand border color for secondary branded outlines and muted branded strokes. Do not use for text, fills, icons, neutral borders, functional feedback."
    id: "color.border.brand.color-three.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Secondary brand border color for selected controls, branded focus alternatives, and branded emphasis strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Highest-emphasis secondary brand border color for maximum-strength branded outlines, prominent branded strokes, and secondary pressed borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Strong secondary brand border color for high-emphasis branded outlines, prominent branded strokes, and secondary hover borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Lowest-emphasis secondary brand border color for soft branded outlines and quiet branded strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Medium-emphasis secondary brand border color for visible branded outlines and supporting branded strokes. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.brand.color-two"
    description: "Low-emphasis secondary brand border color for secondary branded outlines, muted branded strokes, and secondary disabled borders. Do not use for text, fills, icons, neutral borders, or functional feedback."
    id: "color.border.brand.color-two.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.functional"
    description: "Danger border color for error, destructive, and critical feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    id: "color.border.functional.danger"
    label: "Danger"
    valueType: "color"
  -
    categoryId: "semantics.color.border.functional"
    description: "Info border color for informational feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    id: "color.border.functional.info"
    label: "Info"
    valueType: "color"
  -
    categoryId: "semantics.color.border.functional"
    description: "Success border color for completed, positive, and confirmed feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    id: "color.border.functional.success"
    label: "Success"
    valueType: "color"
  -
    categoryId: "semantics.color.border.functional"
    description: "Warning border color for caution, attention, and recoverable issue feedback outlines, status containers, and alert accents. Do not use for text, fills, icons, brand borders, neutral borders, or interaction states."
    id: "color.border.functional.warning"
    label: "Warning"
    valueType: "color"
  -
    categoryId: "semantics.color.border.input"
    description: "Border color for input fields and form controls. Do not use for text, fills, icons, functional feedback, brand emphasis, or non-input containers."
    id: "color.border.input"
    label: "Input"
    valueType: "color"
  -
    categoryId: "semantics.color.border.interaction"
    description: "Border color for disabled interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    id: "color.border.interaction.disabled"
    label: "Disabled"
    valueType: "color"
  -
    categoryId: "semantics.color.border.interaction"
    description: "Border color for focused interactive elements and focus outlines. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    id: "color.border.interaction.focused"
    label: "Focused"
    valueType: "color"
  -
    categoryId: "semantics.color.border.interaction"
    description: "Border color for hovered interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    id: "color.border.interaction.hover"
    label: "Hover"
    valueType: "color"
  -
    categoryId: "semantics.color.border.interaction"
    description: "Border color for pressed interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    id: "color.border.interaction.pressed"
    label: "Pressed"
    valueType: "color"
  -
    categoryId: "semantics.color.border.interaction"
    description: "Border color for selected interactive elements. Do not use for text, fills, icons, static borders, brand borders, or functional feedback."
    id: "color.border.interaction.selected"
    label: "Selected"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Primary neutral border color for visible outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Highest-emphasis neutral border color for maximum-strength outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Strong neutral border color for high-emphasis outlines, separators, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Lowest-emphasis neutral border color for very quiet dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Medium-emphasis neutral border color for standard dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Low-emphasis neutral border color for quiet dividers, outlines, and container strokes. Do not use for text, fills, icons, brand borders, functional feedback, or interaction states."
    id: "color.border.neutral.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.border.neutral"
    description: "Border color for strokes on strong colored surfaces. Do not use for text, fills, icons, normal neutral borders, brand borders, or functional feedback."
    id: "color.border.onColor"
    label: "On Color"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.danger"
    description: "Danger color for error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.danger"
    label: "Danger"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.danger"
    description: "Soft danger color for medium-emphasis error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.danger.soft"
    label: "Soft"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.danger"
    description: "Strong danger color for high-emphasis error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.danger.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.danger"
    description: "Lowest-emphasis danger color for soft error, destructive, and critical feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.danger.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.info"
    description: "Info color for informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.info"
    label: "Info"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.info"
    description: "Soft info color for medium-emphasis informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.info.soft"
    label: "Soft"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.info"
    description: "Strong info color for high-emphasis informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.info.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.info"
    description: "Lowest-emphasis info color for soft informational feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.info.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.success"
    description: "Success color for completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.success"
    label: "Success"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.success"
    description: "Soft success color for medium-emphasis completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.success.soft"
    label: "Soft"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.success"
    description: "Strong success color for high-emphasis completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.success.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.success"
    description: "Lowest-emphasis success color for soft completed, positive, and confirmed feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.success.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.warning"
    description: "Warning color for caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.warning"
    label: "Warning"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.warning"
    description: "Soft warning color for medium-emphasis caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.warning.soft"
    label: "Soft"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.warning"
    description: "Strong warning color for high-emphasis caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.warning.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.functional.warning"
    description: "Lowest-emphasis warning color for soft caution, attention, and recoverable issue feedback fills and status surfaces. Do not use for text, borders, icons, neutral surfaces, brand colors, system colors, or interaction states."
    id: "color.functional.warning.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Accent icon color for emphasized neutral UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    id: "color.icon.accent"
    label: "Accent"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "Default strong Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "Highest-emphasis Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "High-emphasis Color One brand icon color for primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "Lowest-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "Medium-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-one"
    description: "Low-emphasis Color One brand icon color for subtle primary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-one.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "Default strong Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "Highest-emphasis Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "High-emphasis Color Three brand icon color for tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "Lowest-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "Medium-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-three"
    description: "Low-emphasis Color Three brand icon color for subtle tertiary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-three.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "Default strong Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.strong.one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "Highest-emphasis Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.strong.three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "High-emphasis Color Two brand icon color for secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.strong.two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "Lowest-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.subtle.one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "Medium-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.subtle.three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.brand.color-two"
    description: "Low-emphasis Color Two brand icon color for subtle secondary brand icons and accents. Do not use for text, fills, borders, functional status icons, or neutral icons."
    id: "color.icon.brand.color-two.subtle.two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.functional"
    description: "Danger icon color for error, destructive, and critical status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    id: "color.icon.danger"
    label: "Danger"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Default icon color for standard UI icons. Do not use for text, fills, borders, brand accents, functional status icons, or interaction states."
    id: "color.icon.default"
    label: "Default"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Gray disabled icon color for unavailable UI icons. Use only when a gray disabled icon is required. Do not use for text, fills, borders, enabled icons, brand-disabled icons, functional status icons, or interaction states."
    id: "color.icon.disabled"
    label: "Disabled"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.functional"
    description: "Info icon color for informational status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    id: "color.icon.info"
    label: "Info"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.interaction"
    description: "Icon color for disabled interaction state. Do not use for text, fills, borders, enabled icons, hover icons, pressed icons, selected icons, brand icons, or functional status icons."
    id: "color.icon.interaction.disabled"
    label: "Disabled"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.interaction"
    description: "Icon color for focused interaction state. Do not use for text, fills, borders, default icons, hover icons, pressed icons, selected icons, disabled icons, brand icons, or functional status icons."
    id: "color.icon.interaction.focused"
    label: "Focused"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.interaction"
    description: "Icon color for hover interaction state. Do not use for text, fills, borders, default icons, pressed icons, selected icons, disabled icons, brand icons, or functional status icons."
    id: "color.icon.interaction.hover"
    label: "Hover"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.interaction"
    description: "Icon color for pressed interaction state. Do not use for text, fills, borders, default icons, hover icons, selected icons, disabled icons, brand icons, or functional status icons."
    id: "color.icon.interaction.pressed"
    label: "Pressed"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.interaction"
    description: "Icon color for selected interaction state. Do not use for text, fills, borders, default icons, hover icons, pressed icons, disabled icons, brand icons, or functional status icons."
    id: "color.icon.interaction.selected"
    label: "Selected"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Icon color for icons on inverse or dark neutral surfaces. Do not use for text, fills, borders, brand icons, functional status icons, or normal light surfaces."
    id: "color.icon.inverse"
    label: "Inverse"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Icon color for icons, checkmarks, and dots on strong colored fills. Do not use for text, fills, borders, standalone brand icons, functional status icons, or normal neutral surfaces."
    id: "color.icon.onColor"
    label: "On Color"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Lower-emphasis icon color for secondary UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    id: "color.icon.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.base"
    description: "Lowest-emphasis icon color for decorative or very low-emphasis UI icons. Do not use for text, fills, borders, brand icons, functional status icons, or interaction states."
    id: "color.icon.subtlest"
    label: "Subtlest"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.functional"
    description: "Success icon color for positive, completed, and confirmed status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    id: "color.icon.success"
    label: "Success"
    valueType: "color"
  -
    categoryId: "semantics.color.icon.functional"
    description: "Warning icon color for caution, attention, and recoverable issue status icons. Do not use for text, fills, borders, neutral icons, brand icons, or interaction states."
    id: "color.icon.warning"
    label: "Warning"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Primary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.strong-one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Highest-emphasis primary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.strong-three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Strong primary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.strong-two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Lowest-emphasis primary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.subtle-one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Medium-emphasis primary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.subtle-three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-one"
    description: "Low-emphasis primary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-one.subtle-two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Tertiary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.strong-one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Highest-emphasis tertiary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.strong-three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Strong tertiary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.strong-two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Lowest-emphasis tertiary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.subtle-one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Medium-emphasis tertiary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.subtle-three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-three"
    description: "Low-emphasis tertiary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-three.subtle-two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Secondary brand emphasis shade for filled UI states, accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.strong-one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Highest-emphasis secondary brand shade for maximum-strength fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.strong-three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Strong secondary brand shade for high-contrast fills and prominent accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.strong-two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Lowest-emphasis secondary brand shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.subtle-one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Medium-emphasis secondary brand shade for visible fills, supporting accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.subtle-three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.brand.color-two"
    description: "Low-emphasis secondary brand shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.brand.color-two.subtle-two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Primary neutral emphasis shade for filled UI states, neutral accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.strong-one"
    label: "Strong One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Highest neutral emphasis shade for maximum-strength fills and neutral accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.strong-three"
    label: "Strong Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Strong neutral emphasis shade for high-contrast fills and neutral accents. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.strong-two"
    label: "Strong Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Lowest-emphasis neutral shade for soft fills, quiet accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.subtle-one"
    label: "Subtle One"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Medium-emphasis neutral shade for visible fills, separators-as-fill, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.subtle-three"
    label: "Subtle Three"
    valueType: "color"
  -
    categoryId: "semantics.color.shades.neutral"
    description: "Low-emphasis neutral shade for secondary fills, muted accents, and surfaces when needed. Do not use for text, borders, functional colors, icons, system colors, or interaction tokens."
    id: "color.shades.neutral.subtle-two"
    label: "Subtle Two"
    valueType: "color"
  -
    categoryId: "semantics.color.shadow"
    description: "Deep shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    id: "color.shadow.deep"
    label: "Deep"
    valueType: "color"
  -
    categoryId: "semantics.color.shadow"
    description: "Medium shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    id: "color.shadow.medium"
    label: "Medium"
    valueType: "color"
  -
    categoryId: "semantics.color.shadow"
    description: "Soft shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    id: "color.shadow.soft"
    label: "Soft"
    valueType: "color"
  -
    categoryId: "semantics.color.shadow"
    description: "Strong shadow layer color. Use only through canonical Shadow styles; do not hardcode it into components."
    id: "color.shadow.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.surface"
    description: "Default canvas and component surface color for containers. Do not use for text, borders, functional colors, icons, system colors, or interaction states."
    id: "color.surface.canvas"
    label: "Canvas"
    valueType: "color"
  -
    categoryId: "semantics.color.surface.interaction"
    description: "Surface color for disabled interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    id: "color.surface.interaction.disabled"
    label: "Disabled"
    valueType: "color"
  -
    categoryId: "semantics.color.surface.interaction"
    description: "Surface color for focused interactive areas when the focus state needs a surface treatment. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    id: "color.surface.interaction.focused"
    label: "Focused"
    valueType: "color"
  -
    categoryId: "semantics.color.surface.interaction"
    description: "Surface color for hovered interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    id: "color.surface.interaction.hover"
    label: "Hover"
    valueType: "color"
  -
    categoryId: "semantics.color.surface.interaction"
    description: "Surface color for pressed interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    id: "color.surface.interaction.pressed"
    label: "Pressed"
    valueType: "color"
  -
    categoryId: "semantics.color.surface.interaction"
    description: "Surface color for selected interactive areas. Do not use for text, borders, functional colors, icons, system colors, or static surfaces."
    id: "color.surface.interaction.selected"
    label: "Selected"
    valueType: "color"
  -
    categoryId: "semantics.color.system"
    description: "Absolute black utility color for system-level fallbacks and hard black requirements. Do not use for normal text, fills, borders, icons, brand colors, functional feedback, or interaction states."
    id: "color.system.black"
    label: "Black"
    valueType: "color"
  -
    categoryId: "semantics.color.system"
    description: "Transparent utility color for intentionally invisible fills, borders, or cleared backgrounds. Do not use for text, icons, brand colors, functional feedback, or interaction states."
    id: "color.system.transparent"
    label: "Transparent"
    valueType: "color"
  -
    categoryId: "semantics.color.system"
    description: "Absolute white utility color for system-level fallbacks, hard white requirements, and hard-white inverse surface requirements. Do not use for normal text, normal fills, borders, icons, brand colors, functional feedback, or non-inverse interaction states."
    id: "color.system.white"
    label: "White"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Default text color for readable body copy, labels, and standard UI text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    id: "color.text.body"
    label: "Body"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Muted text color for low-emphasis copy, helper text, placeholders, and disabled-adjacent text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or primary readable text."
    id: "color.text.body.muted"
    label: "Muted"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Lower-emphasis text color for supporting copy and secondary UI text. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    id: "color.text.body.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-one"
    description: "Default Color One brand text for branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-one.accent"
    label: "Accent"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-one"
    description: "High-emphasis Color One brand text for strong branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-one.accent.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-one"
    description: "Low-emphasis Color One brand text for subtle branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-one.accent.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-three"
    description: "Default Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-three.accent"
    label: "Accent"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-three"
    description: "High-emphasis Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-three.accent.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-three"
    description: "Low-emphasis Color Three brand text for tertiary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-three.accent.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-two"
    description: "Default Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-two.accent"
    label: "Accent"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-two"
    description: "High-emphasis Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-two.accent.strong"
    label: "Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.brand.color-two"
    description: "Low-emphasis Color Two brand text for secondary branded labels and accents. Do not use for body text, links, fills, borders, or icons."
    id: "color.text.brand.color-two.accent.subtle"
    label: "Subtle"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Danger text color for error, destructive, and critical status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.danger"
    label: "Danger"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Strong danger text color for high-emphasis error, destructive, and critical status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.danger.strong"
    label: "Danger Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Info text color for informational messages and status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.info"
    label: "Info"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Strong info text color for high-emphasis informational messages and status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.info.strong"
    label: "Info Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Success text color for positive, completed, and confirmed status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.success"
    label: "Success"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Strong success text color for high-emphasis positive, completed, and confirmed status labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.success.strong"
    label: "Success Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Warning text color for caution, attention, and recoverable issue labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.warning"
    label: "Warning"
    valueType: "color"
  -
    categoryId: "semantics.color.text.functional"
    description: "Strong warning text color for high-emphasis caution, attention, and recoverable issue labels. Do not use for fills, borders, icons, brand text, or neutral body text."
    id: "color.text.functional.warning.strong"
    label: "Warning Strong"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Text color for primary headings and high-emphasis titles. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    id: "color.text.heading"
    label: "Heading"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Heading text color for headings on strong colored surfaces. Do not use for fills, borders, icons, links, standalone brand accents, functional text, or normal neutral surfaces."
    id: "color.text.heading.onColor"
    label: "Heading on Color"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Text color for text on inverse or dark neutral surfaces. Do not use for fills, borders, icons, links, functional feedback, brand accents, or normal light surfaces."
    id: "color.text.inverse"
    label: "Inverse"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Default link text color for inline and navigational links. Do not use for body text, fills, borders, icons, or non-link text."
    id: "color.text.link"
    label: "Link"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Disabled link text color. Do not use for enabled links, body text, fills, borders, or icons."
    id: "color.text.link.disabled"
    label: "Disabled"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Link text color for hover state. Do not use for default, pressed, visited, disabled, fills, borders, or icons."
    id: "color.text.link.hover"
    label: "Hover"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Link text color for inverse or on-color surfaces. Do not use for standard surface links, body text, fills, borders, or icons."
    id: "color.text.link.inverse"
    label: "Inverse"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Link text color for pressed state. Do not use for default, hover, visited, disabled, fills, borders, or icons."
    id: "color.text.link.pressed"
    label: "Pressed"
    valueType: "color"
  -
    categoryId: "semantics.color.text.link"
    description: "Link text color for visited links. Do not use for default links, body text, fills, borders, or icons."
    id: "color.text.link.visited"
    label: "Visited"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Text color for readable text on strong colored surfaces. Do not use for fills, borders, icons, links, standalone brand accents, functional text, or normal neutral surfaces."
    id: "color.text.onColor"
    label: "Text on Color"
    valueType: "color"
  -
    categoryId: "semantics.color.text.base"
    description: "Text color for secondary headings and section titles. Do not use for fills, borders, icons, links, functional feedback, brand accents, or disabled text."
    id: "color.text.subheading"
    label: "Subheading"
    valueType: "color"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 16
    id: "icon.gap.lg"
    label: "Large"
    valueType: "number"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 12
    id: "icon.gap.md"
    label: "Medium"
    valueType: "number"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 8
    id: "icon.gap.sm"
    label: "Small"
    valueType: "number"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 20
    id: "icon.gap.xl"
    label: "XLarge"
    valueType: "number"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 4
    id: "icon.gap.xs"
    label: "XSmall"
    valueType: "number"
  -
    categoryId: "semantics.icon.gap"
    defaultValue: 24
    id: "icon.gap.xxl"
    label: "XXLarge"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 9999
    id: "radius.full"
    label: "Full"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 12
    id: "radius.large"
    label: "Large"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 8
    id: "radius.medium"
    label: "Medium"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 0
    id: "radius.none"
    label: "None"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 4
    id: "radius.small"
    label: "Small"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 12
    id: "radius.tile"
    label: "Tile"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 16
    id: "radius.xlarge"
    label: "Xlarge"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 2
    id: "radius.xsmall"
    label: "Xsmall"
    valueType: "number"
  -
    categoryId: "semantics.border.radius"
    defaultValue: 24
    id: "radius.xxlarge"
    label: "Xxlarge"
    valueType: "number"
requiredCategories:
  "color.border.brand.color-one.strong.one": "border"
  "color.border.brand.color-one.strong.three": "border"
  "color.border.brand.color-one.strong.two": "border"
  "color.border.brand.color-one.subtle.one": "border"
  "color.border.brand.color-one.subtle.three": "border"
  "color.border.brand.color-one.subtle.two": "border"
  "color.border.brand.color-three.strong.one": "border"
  "color.border.brand.color-three.strong.three": "border"
  "color.border.brand.color-three.strong.two": "border"
  "color.border.brand.color-three.subtle.one": "border"
  "color.border.brand.color-three.subtle.three": "border"
  "color.border.brand.color-three.subtle.two": "border"
  "color.border.brand.color-two.strong.one": "border"
  "color.border.brand.color-two.strong.three": "border"
  "color.border.brand.color-two.strong.two": "border"
  "color.border.brand.color-two.subtle.one": "border"
  "color.border.brand.color-two.subtle.three": "border"
  "color.border.brand.color-two.subtle.two": "border"
  "color.border.functional.danger": "border"
  "color.border.functional.info": "border"
  "color.border.functional.success": "border"
  "color.border.functional.warning": "border"
  "color.border.input": "border"
  "color.border.interaction.disabled": "border"
  "color.border.interaction.focused": "border"
  "color.border.interaction.hover": "border"
  "color.border.interaction.pressed": "border"
  "color.border.interaction.selected": "border"
  "color.border.neutral.strong.one": "border"
  "color.border.neutral.strong.three": "border"
  "color.border.neutral.strong.two": "border"
  "color.border.neutral.subtle.one": "border"
  "color.border.neutral.subtle.three": "border"
  "color.border.neutral.subtle.two": "border"
  "color.border.onColor": "border"
  "color.functional.danger": "functional"
  "color.functional.danger.soft": "functional"
  "color.functional.danger.strong": "functional"
  "color.functional.danger.subtle": "functional"
  "color.functional.info": "functional"
  "color.functional.info.soft": "functional"
  "color.functional.info.strong": "functional"
  "color.functional.info.subtle": "functional"
  "color.functional.success": "functional"
  "color.functional.success.soft": "functional"
  "color.functional.success.strong": "functional"
  "color.functional.success.subtle": "functional"
  "color.functional.warning": "functional"
  "color.functional.warning.soft": "functional"
  "color.functional.warning.strong": "functional"
  "color.functional.warning.subtle": "functional"
  "color.icon.accent": "icon"
  "color.icon.brand.color-one.strong.one": "icon"
  "color.icon.brand.color-one.strong.three": "icon"
  "color.icon.brand.color-one.strong.two": "icon"
  "color.icon.brand.color-one.subtle.one": "icon"
  "color.icon.brand.color-one.subtle.three": "icon"
  "color.icon.brand.color-one.subtle.two": "icon"
  "color.icon.brand.color-three.strong.one": "icon"
  "color.icon.brand.color-three.strong.three": "icon"
  "color.icon.brand.color-three.strong.two": "icon"
  "color.icon.brand.color-three.subtle.one": "icon"
  "color.icon.brand.color-three.subtle.three": "icon"
  "color.icon.brand.color-three.subtle.two": "icon"
  "color.icon.brand.color-two.strong.one": "icon"
  "color.icon.brand.color-two.strong.three": "icon"
  "color.icon.brand.color-two.strong.two": "icon"
  "color.icon.brand.color-two.subtle.one": "icon"
  "color.icon.brand.color-two.subtle.three": "icon"
  "color.icon.brand.color-two.subtle.two": "icon"
  "color.icon.danger": "icon"
  "color.icon.default": "icon"
  "color.icon.disabled": "icon"
  "color.icon.info": "icon"
  "color.icon.interaction.disabled": "icon"
  "color.icon.interaction.focused": "icon"
  "color.icon.interaction.hover": "icon"
  "color.icon.interaction.pressed": "icon"
  "color.icon.interaction.selected": "icon"
  "color.icon.inverse": "icon"
  "color.icon.onColor": "icon"
  "color.icon.subtle": "icon"
  "color.icon.subtlest": "icon"
  "color.icon.success": "icon"
  "color.icon.warning": "icon"
  "color.shades.brand.color-one.strong-one": "shades"
  "color.shades.brand.color-one.strong-three": "shades"
  "color.shades.brand.color-one.strong-two": "shades"
  "color.shades.brand.color-one.subtle-one": "shades"
  "color.shades.brand.color-one.subtle-three": "shades"
  "color.shades.brand.color-one.subtle-two": "shades"
  "color.shades.brand.color-three.strong-one": "shades"
  "color.shades.brand.color-three.strong-three": "shades"
  "color.shades.brand.color-three.strong-two": "shades"
  "color.shades.brand.color-three.subtle-one": "shades"
  "color.shades.brand.color-three.subtle-three": "shades"
  "color.shades.brand.color-three.subtle-two": "shades"
  "color.shades.brand.color-two.strong-one": "shades"
  "color.shades.brand.color-two.strong-three": "shades"
  "color.shades.brand.color-two.strong-two": "shades"
  "color.shades.brand.color-two.subtle-one": "shades"
  "color.shades.brand.color-two.subtle-three": "shades"
  "color.shades.brand.color-two.subtle-two": "shades"
  "color.shades.neutral.strong-one": "shades"
  "color.shades.neutral.strong-three": "shades"
  "color.shades.neutral.strong-two": "shades"
  "color.shades.neutral.subtle-one": "shades"
  "color.shades.neutral.subtle-three": "shades"
  "color.shades.neutral.subtle-two": "shades"
  "color.shadow.deep": "shadow"
  "color.shadow.medium": "shadow"
  "color.shadow.soft": "shadow"
  "color.shadow.strong": "shadow"
  "color.surface.canvas": "surface"
  "color.surface.interaction.disabled": "surface"
  "color.surface.interaction.focused": "surface"
  "color.surface.interaction.hover": "surface"
  "color.surface.interaction.pressed": "surface"
  "color.surface.interaction.selected": "surface"
  "color.system.black": "system"
  "color.system.transparent": "system"
  "color.system.white": "system"
  "color.text.body": "text"
  "color.text.body.muted": "text"
  "color.text.body.subtle": "text"
  "color.text.brand.color-one.accent": "text"
  "color.text.brand.color-one.accent.strong": "text"
  "color.text.brand.color-one.accent.subtle": "text"
  "color.text.brand.color-three.accent": "text"
  "color.text.brand.color-three.accent.strong": "text"
  "color.text.brand.color-three.accent.subtle": "text"
  "color.text.brand.color-two.accent": "text"
  "color.text.brand.color-two.accent.strong": "text"
  "color.text.brand.color-two.accent.subtle": "text"
  "color.text.functional.danger": "text"
  "color.text.functional.danger.strong": "text"
  "color.text.functional.info": "text"
  "color.text.functional.info.strong": "text"
  "color.text.functional.success": "text"
  "color.text.functional.success.strong": "text"
  "color.text.functional.warning": "text"
  "color.text.functional.warning.strong": "text"
  "color.text.heading": "text"
  "color.text.heading.onColor": "text"
  "color.text.inverse": "text"
  "color.text.link": "text"
  "color.text.link.disabled": "text"
  "color.text.link.hover": "text"
  "color.text.link.inverse": "text"
  "color.text.link.pressed": "text"
  "color.text.link.visited": "text"
  "color.text.onColor": "text"
  "color.text.subheading": "text"
shadowStylesByMode:
  dark:
    -
      layers:
        []
      modeId: "dark"
      name: "None"
      styleId: "shadow-none"
    -
      layers:
        -
          blur: 2.6
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.15
          resolvedColor:
            hex: "#CECECE"
            paletteId: "palette.neutral"
            shadeId: "100"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 1.95
          y: 1.95
      modeId: "dark"
      name: "2XS"
      styleId: "shadow-2xs"
    -
      layers:
        -
          blur: 4
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.16
          resolvedColor:
            hex: "#CECECE"
            paletteId: "palette.neutral"
            shadeId: "100"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 1
      modeId: "dark"
      name: "XS"
      styleId: "shadow-xs"
    -
      layers:
        -
          blur: 8
          colorTokenRef: "color.shadow.medium"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#A1A1A1"
            paletteId: "palette.neutral"
            shadeId: "200"
            tokenId: "color.shadow.medium"
          spread: 0
          x: 0
          y: 2
      modeId: "dark"
      name: "SM"
      styleId: "shadow-sm"
    -
      layers:
        -
          blur: 8
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.24
          resolvedColor:
            hex: "#CECECE"
            paletteId: "palette.neutral"
            shadeId: "100"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 3
      modeId: "dark"
      name: "MD"
      styleId: "shadow-md"
    -
      layers:
        -
          blur: 15
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.35
          resolvedColor:
            hex: "#CECECE"
            paletteId: "palette.neutral"
            shadeId: "100"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 5
      modeId: "dark"
      name: "LG"
      styleId: "shadow-lg"
    -
      layers:
        -
          blur: 24
          colorTokenRef: "color.shadow.soft"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#767676"
            paletteId: "palette.neutral"
            shadeId: "300"
            tokenId: "color.shadow.soft"
          spread: 0
          x: 0
          y: 8
      modeId: "dark"
      name: "XL"
      styleId: "shadow-xl"
    -
      layers:
        -
          blur: 29
          colorTokenRef: "color.shadow.medium"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#A1A1A1"
            paletteId: "palette.neutral"
            shadeId: "200"
            tokenId: "color.shadow.medium"
          spread: 0
          x: 0
          y: 7
      modeId: "dark"
      name: "2XL"
      styleId: "shadow-2xl"
    -
      layers:
        -
          blur: 100
          colorTokenRef: "color.shadow.deep"
          inset: false
          opacity: 0.15
          resolvedColor:
            hex: "#F1F1F1"
            paletteId: "palette.neutral"
            shadeId: "50"
            tokenId: "color.shadow.deep"
          spread: 0
          x: 0
          y: 48
      modeId: "dark"
      name: "3XL"
      styleId: "shadow-3xl"
  light:
    -
      layers:
        []
      modeId: "light"
      name: "None"
      styleId: "shadow-none"
    -
      layers:
        -
          blur: 2.6
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.15
          resolvedColor:
            hex: "#000000"
            paletteId: "palette.black-and-white"
            shadeId: "black"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 1.95
          y: 1.95
      modeId: "light"
      name: "2XS"
      styleId: "shadow-2xs"
    -
      layers:
        -
          blur: 4
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.16
          resolvedColor:
            hex: "#000000"
            paletteId: "palette.black-and-white"
            shadeId: "black"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 1
      modeId: "light"
      name: "XS"
      styleId: "shadow-xs"
    -
      layers:
        -
          blur: 8
          colorTokenRef: "color.shadow.medium"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#5C5C5C"
            paletteId: "palette.neutral"
            shadeId: "400"
            tokenId: "color.shadow.medium"
          spread: 0
          x: 0
          y: 2
      modeId: "light"
      name: "SM"
      styleId: "shadow-sm"
    -
      layers:
        -
          blur: 8
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.24
          resolvedColor:
            hex: "#000000"
            paletteId: "palette.black-and-white"
            shadeId: "black"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 3
      modeId: "light"
      name: "MD"
      styleId: "shadow-md"
    -
      layers:
        -
          blur: 15
          colorTokenRef: "color.shadow.strong"
          inset: false
          opacity: 0.35
          resolvedColor:
            hex: "#000000"
            paletteId: "palette.black-and-white"
            shadeId: "black"
            tokenId: "color.shadow.strong"
          spread: 0
          x: 0
          y: 5
      modeId: "light"
      name: "LG"
      styleId: "shadow-lg"
    -
      layers:
        -
          blur: 24
          colorTokenRef: "color.shadow.soft"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#A1A1A1"
            paletteId: "palette.neutral"
            shadeId: "200"
            tokenId: "color.shadow.soft"
          spread: 0
          x: 0
          y: 8
      modeId: "light"
      name: "XL"
      styleId: "shadow-xl"
    -
      layers:
        -
          blur: 29
          colorTokenRef: "color.shadow.medium"
          inset: false
          opacity: 0.2
          resolvedColor:
            hex: "#5C5C5C"
            paletteId: "palette.neutral"
            shadeId: "400"
            tokenId: "color.shadow.medium"
          spread: 0
          x: 0
          y: 7
      modeId: "light"
      name: "2XL"
      styleId: "shadow-2xl"
    -
      layers:
        -
          blur: 100
          colorTokenRef: "color.shadow.deep"
          inset: false
          opacity: 0.15
          resolvedColor:
            hex: "#151515"
            paletteId: "palette.neutral"
            shadeId: "900"
            tokenId: "color.shadow.deep"
          spread: 0
          x: 0
          y: 48
      modeId: "light"
      name: "3XL"
      styleId: "shadow-3xl"
shadowUsageRules:
  - "Reference canonical shadow IDs only."
  - "Never invent or hardcode shadow layer values."
  - "Resolve light or dark explicitly; never fall back between modes."
  - "Shadow does not control stacking order."
  - "Shadow must not replace focus indicators."
  - "Shadow does not imply component behavior."
tokenCategories:
  -
    id: "semantics.color"
    label: "Color"
    order: 10
  -
    id: "semantics.spacing"
    label: "Space"
    order: 20
  -
    id: "semantics.border"
    label: "Border"
    order: 30
  -
    id: "semantics.icon"
    label: "Icon"
    order: 35
  -
    id: "semantics.shadow"
    label: "Shadow"
    order: 40
  -
    id: "semantics.border.weight"
    label: "Width"
    order: 10
    parentId: "semantics.border"
  -
    id: "semantics.border.radius"
    label: "Radius"
    order: 20
    parentId: "semantics.border"
  -
    id: "semantics.color.shades"
    label: "Shades"
    order: 10
    parentId: "semantics.color"
  -
    id: "semantics.color.system"
    label: "System"
    order: 20
    parentId: "semantics.color"
  -
    id: "semantics.color.surface"
    label: "Surface"
    order: 25
    parentId: "semantics.color"
  -
    id: "semantics.color.shadow"
    label: "Shadow"
    order: 27
    parentId: "semantics.color"
  -
    id: "semantics.color.functional"
    label: "Functional"
    order: 30
    parentId: "semantics.color"
  -
    id: "semantics.color.border"
    label: "Border"
    order: 40
    parentId: "semantics.color"
  -
    id: "semantics.color.text"
    label: "Text"
    order: 50
    parentId: "semantics.color"
  -
    id: "semantics.color.icon"
    label: "Icon"
    order: 60
    parentId: "semantics.color"
  -
    id: "semantics.color.border.input"
    label: "Input"
    order: 10
    parentId: "semantics.color.border"
  -
    id: "semantics.color.border.functional"
    label: "Functional"
    order: 20
    parentId: "semantics.color.border"
  -
    id: "semantics.color.border.brand"
    label: "Brand"
    order: 30
    parentId: "semantics.color.border"
  -
    id: "semantics.color.border.neutral"
    label: "Neutral"
    order: 40
    parentId: "semantics.color.border"
  -
    id: "semantics.color.border.interaction"
    label: "Interaction"
    order: 50
    parentId: "semantics.color.border"
  -
    id: "semantics.color.border.brand.color-one"
    label: "Color One"
    order: 10
    parentId: "semantics.color.border.brand"
  -
    id: "semantics.color.border.brand.color-two"
    label: "Color Two"
    order: 20
    parentId: "semantics.color.border.brand"
  -
    id: "semantics.color.border.brand.color-three"
    label: "Color Three"
    order: 30
    parentId: "semantics.color.border.brand"
  -
    id: "semantics.color.functional.info"
    label: "Info"
    order: 10
    parentId: "semantics.color.functional"
  -
    id: "semantics.color.functional.danger"
    label: "Danger"
    order: 20
    parentId: "semantics.color.functional"
  -
    id: "semantics.color.functional.success"
    label: "Success"
    order: 30
    parentId: "semantics.color.functional"
  -
    id: "semantics.color.functional.warning"
    label: "Warning"
    order: 40
    parentId: "semantics.color.functional"
  -
    id: "semantics.color.icon.base"
    label: "Base"
    order: 10
    parentId: "semantics.color.icon"
  -
    id: "semantics.color.icon.functional"
    label: "Functional"
    order: 20
    parentId: "semantics.color.icon"
  -
    id: "semantics.color.icon.interaction"
    label: "Interaction"
    order: 30
    parentId: "semantics.color.icon"
  -
    id: "semantics.color.icon.brand"
    label: "Brand"
    order: 40
    parentId: "semantics.color.icon"
  -
    id: "semantics.color.icon.brand.color-one"
    label: "Color One"
    order: 10
    parentId: "semantics.color.icon.brand"
  -
    id: "semantics.color.icon.brand.color-two"
    label: "Color Two"
    order: 20
    parentId: "semantics.color.icon.brand"
  -
    id: "semantics.color.icon.brand.color-three"
    label: "Color Three"
    order: 30
    parentId: "semantics.color.icon.brand"
  -
    id: "semantics.color.shades.neutral"
    label: "Neutral"
    order: 10
    parentId: "semantics.color.shades"
  -
    id: "semantics.color.shades.brand"
    label: "Brand"
    order: 20
    parentId: "semantics.color.shades"
  -
    id: "semantics.color.shades.brand.color-one"
    label: "Color One"
    order: 10
    parentId: "semantics.color.shades.brand"
  -
    id: "semantics.color.shades.brand.color-two"
    label: "Color Two"
    order: 20
    parentId: "semantics.color.shades.brand"
  -
    id: "semantics.color.shades.brand.color-three"
    label: "Color Three"
    order: 30
    parentId: "semantics.color.shades.brand"
  -
    id: "semantics.color.surface.interaction"
    label: "Interaction"
    order: 10
    parentId: "semantics.color.surface"
  -
    id: "semantics.color.text.base"
    label: "Base"
    order: 10
    parentId: "semantics.color.text"
  -
    id: "semantics.color.text.link"
    label: "Link"
    order: 20
    parentId: "semantics.color.text"
  -
    id: "semantics.color.text.functional"
    label: "Functional"
    order: 30
    parentId: "semantics.color.text"
  -
    id: "semantics.color.text.brand"
    label: "Brand"
    order: 40
    parentId: "semantics.color.text"
  -
    id: "semantics.color.text.brand.color-one"
    label: "Color One"
    order: 10
    parentId: "semantics.color.text.brand"
  -
    id: "semantics.color.text.brand.color-two"
    label: "Color Two"
    order: 20
    parentId: "semantics.color.text.brand"
  -
    id: "semantics.color.text.brand.color-three"
    label: "Color Three"
    order: 30
    parentId: "semantics.color.text.brand"
  -
    id: "semantics.icon.size"
    label: "Size"
    order: 10
    parentId: "semantics.icon"
  -
    id: "semantics.icon.gap"
    label: "Gap"
    order: 20
    parentId: "semantics.icon"
```

## Resolution Algorithm

1. Resolve the explicit mode first: light or dark.
2. Resolve the semantic token id in byMode[mode].
3. Follow target.paletteId and target.shadeId to palette.md.
4. Use category to preserve UI intent in generated work.
5. Stop if a semantic token, mode mapping, palette, or shade is missing.

## Rules

- Resolve color, text, surface, border, focus, and status intent through semantic token ids.
- Keep light and dark mode mappings explicit.
- Do not replace semantic refs with palette guesses.
- Generated package data contains active semantic mappings with user overrides already materialized.
