# Agent Instructions

## Capabilities

For capabilities requests, call `get_alpy_library_index` using the user's known `light` or `dark` mode; ask if unknown. The tool returns the complete overview directly. Follow its tool description for display; no design brief or additional confirmation is needed.

## Purpose

`AGENTS.md` is the mandatory entry point for every Alpy-guided task.

It defines how the agent forms a brief, selects skills, receives approval, applies library direction, reads canonical Alpy data, and begins work.

## Mandatory Brief

Use this process when creating or materially redesigning a digital experience. The agent cannot design or implement until the user completes the brief, completes any selected style’s required choices, and confirms the final restatement.

1. Send the Mandatory Brief with every design style and motion option. Include every hero option for homepage or landing-page work. The user may answer `N/A` or delegate a choice; resolve all material gaps together.
2. If a style is selected, read it and send every choice from its Mandatory Brief Flow in one form.
3. Restate the completed brief, delegated decisions, assumptions, and required skills with their paths and loading order.
4. Ask the user to confirm. Begin design or implementation only after confirmation.

Before confirmation, inspect supplied context, use the current Alpy agent instructions and library index, and read only the selected style needed to prepare the brief.

For a focused audit, the supplied experience and audit scope are the brief. Restate the target, scope, selected skills, mode, and constraints, then request one confirmation. Do not require design-style, hero, motion, or style-specific choices unless they are part of the audit.

------

### Mandatory brief :
```md
Company / Brand / Product:
Main objective:
Audience / Users:
Structure / Pages / Sitemap / IA:
Key functionalities:
Content status:
Tone / Voice:
Design references:
Things to avoid:
Color mode: Light / Dark
Media and assets:
Missing media: User will provide / Agent may source / Agent may generate / Placeholders only
Design style:
Hero structure (homepage or landing page only):
Motion treatments:
Accessibility, language, or regional requirements:
Technical or business constraints:
```

Include every design style with the form. The user must choose one, write `N/A`, or write `Recommend based on my brief`:

- Academia — [Review prototype](https://alpymcp.com/websites/academia/index.html)
- Art Deco — [Review prototype](https://alpymcp.com/websites/art-deco/index.html)
- Bauhaus — [Review prototype](https://alpymcp.com/websites/bauhaus/index.html)
- Bento Grid — [Review prototype](https://alpymcp.com/websites/bento-grid/index.html)
- Bold Typography — [Review prototype](https://alpymcp.com/websites/bold-typography/index.html)
- Cyberpunk — [Review prototype](https://alpymcp.com/websites/Cyberpunk/index.html)
- Flat Design — [Review prototype](https://alpymcp.com/websites/flat-design/index.html)
- Grunge / Punk — [Review prototype](https://alpymcp.com/websites/Grunge/index.html)
- Luxury — Prototype in progress
- Modern Dark — [Review prototype](https://alpymcp.com/websites/Modern-dark/index.html)
- Monochrome — Prototype in progress
- Neo Brutalism — Prototype in progress
- Neumorphism — [Review prototype](https://alpymcp.com/websites/neumorphism/index.html)
- Parallax — [Review prototype](https://alpymcp.com/websites/Parallax/index.html)
- Playful Geometric — [Review prototype](https://alpymcp.com/websites/Playful-geometric/index.html)
- Retro — Prototype in progress
- Sketch — Prototype in progress
- Swiss — [Review prototype](https://alpymcp.com/websites/swiss/index.html)
- Terminal — Prototype in progress
- Vaporwave — Prototype in progress

For homepage or landing-page work, include every hero structure with the form. The user must choose one or explicitly delegate the choice:

- Centered / stacked
- Split-column
- Input-capture
- Product preview
- Product showcase
- Full-bleed media
- Carousel
- Editorial / typography-led
- Illustration / character-led
- Bento / mosaic
- Interactive demo
- Before-and-after / comparison
- Social-proof-led
- Immersive 3D
- No hero

Product preview means one real product view. Product showcase means a multi-feature sequence, demonstration, or video.

Include every motion treatment with the form. The user may choose any compatible treatments:

- Minimal
- Animated
- Typing effect
- Parallax
- Viewport reveal
- None

Do not treat a motion treatment as the hero structure itself.

Mandatory Brief ends

-------

### Style-Specific Choices

Every selected style must declare its required choice groups in a complete Mandatory Brief Flow. If the user requests a recommendation, select one style from the supplied list using the completed brief, then read that style file completely.

Present every declared group and option exactly as one compact form, then record every selection in the brief restatement.

For example, Grunge / Punk may require character, texture, and material selections. Other styles may require composition, typography, surface, motion, imagery, or decorative choices.

Do not ask each style choice in a separate message. Do not shortlist, rank, summarize, rename, preselect, merge, or omit declared options.

The user may delegate an individual choice. State the resulting selection and rationale in the brief restatement.

A selected style file without a complete Mandatory Brief Flow is a blocker. Report the missing style choices instead of inventing them.

A request or approval sent before the final restatement does not confirm the brief.

## Skill Resolution

Use `get_alpy_library_index` to discover exact skill names. Use `get_alpy_skill` to read each selected skill and every dependency returned with it.

For a confirmed design style, load its complete dependency set returned by `get_alpy_skill`. Every skill in that set is required.

Always include:

- [Balance](skills/ui-design/balance.md) and [Gestalt](skills/ui-design/gestalt.md) for full creation, material redesign, or broad visual review.
- [Typography and Readability](skills/ui-design/typography-readability.md) when the result contains visible text.
- [Color Discipline](skills/ui-design/color-discipline.md) when interface color is created, changed, or reviewed.
- [Motion and Transition](skills/ui-design/motion-transition.md) when motion, animation, transitions, parallax, auto-advancing content, or moving state feedback is created, changed, or reviewed.
- [Hero](skills/hero.md) for homepage or landing-page hero work.
- The exact selected style skill with its resolved Markdown link when a style is selected.
- Every relevant UI skill with its resolved Markdown link, plus [User Experience](skills/user-experience.md), [Responsive Adaptation](skills/responsive-adaptation.md), and [Accessibility Audit](skills/accessibility-audit.md) when applicable.

Do not load skills outside the selected modules, mandatory triggers, or declared dependency sets.

Reading a selected skill before confirmation is allowed only to discover its mandatory brief choices. It does not authorize design decisions or implementation.

## Skill Boundaries

Give each decision one primary owner. Combine the selected skills in the result; do not merge their responsibilities or use one skill to repair an unresolved decision owned by another.

| Concern | Primary guidance |
|---|---|
| Visitor journey, navigation, content decisions, forms, trust, and recovery | [User Experience](skills/user-experience.md) |
| Opening composition | [Hero](skills/hero.md) |
| Viewport adaptation | [Responsive Adaptation](skills/responsive-adaptation.md) |
| Accessibility verification | [Accessibility Audit](skills/accessibility-audit.md) |
| Spacing, density, and static page pacing | [Rhythm and Space](skills/ui-design/rhythm-space.md) |
| Motion purpose, transitions, choreography, timing, and reduced-motion design | [Motion and Transition](skills/ui-design/motion-transition.md) |
| Structural grid, layout hierarchy, region priority, and reading order | [Grid and Layout](skills/ui-design/grid-layout.md) |
| Perceptual priority, attention order, and competing emphasis | [Visual Hierarchy](skills/ui-design/visual-hierarchy.md) |
| Shared visual edges | [Alignment](skills/ui-design/alignment.md) |
| Relative size outside typography | [Scale and Proportion](skills/ui-design/scale-proportion.md) |
| Visual-weight distribution | [Balance](skills/ui-design/balance.md) |
| Perceived relationships and grouping | [Gestalt](skills/ui-design/gestalt.md) |
| Palette roles, surfaces, text color, and contrast | [Color Discipline](skills/ui-design/color-discipline.md) |
| Text roles, metrics, and readability | [Typography and Readability](skills/ui-design/typography-readability.md) |
| Boundaries, dividers, and radius | [Border and Divider](skills/ui-design/border-divider.md) |
| Layer relationships and shadows | [Elevation](skills/ui-design/elevation.md) |
| Visual character, unity, and controlled variety | The exact website-style skill selected in the brief |

Within the selected style, create unity by repeating its declared visual language. Add variety through composition, scale, crop, or emphasis without introducing a second, unrelated language.

A website style may change only the concerns it declares. It cannot silently change semantic meaning, required content, expected interaction, or canonical component behavior. When guidance conflicts, preserve the confirmed brief and canonical behavior, follow the owning skill, and choose a compatible treatment from the selected style.

## After Confirmation

Only after the user confirms the restatement:

1. Read every approved skill file completely.
2. Read only the canonical components and tokens needed for the work.
3. Design, build, or audit in the current environment.
4. Apply all selected skill criteria during final QA.

Do not start a separate brief, approval, or QA loop for each skill.

If a new material fact changes the confirmed direction, stop the affected work, update the brief, and request confirmation again.

## Canonical Alpy Rules

- Alpy components are mandatory for supported product UI.
- Canonical semantic tokens are mandatory:
  - Color: Shades, System, Surface, Shadow, Functional, Border, Text, Icon.
  - Space.
  - Border: Width, Radius.
  - Icon: Size, Gap.
  - Shadow.
- Hardcoded colors, spacing, radii, borders, shadows, and component values are forbidden.
- Typography follows [Typography and Readability](skills/ui-design/typography-readability.md). The confirmed [Bold Typography](skills/website-styles/bold-typography.md) style adds its declared size, line-height, and letter-spacing exception for focal display headlines; all other text remains canonical.
- Resolve the exact `light` or `dark` mode.
- Do not invent components, variants, states, tokens, mappings, breakpoints, icons, or behavior.
- Preserve user-provided content, functionality, routes, and assets.
- Report missing canonical coverage and the solutions instead of creating a local substitute.

## Stop Conditions

Do not begin or continue the affected work when:

- The brief is incomplete.
- The user has not confirmed the restatement.
- A required design style or applicable hero choice is unresolved.
- The selected style has no complete Mandatory Brief Flow.
- A selected style’s mandatory choices are unanswered.
- Content, functionality, mode, or media direction required by the confirmed work is missing.
- A required skill or dependency cannot be resolved.
- Canonical Alpy support is missing or conflicting.

Stop only the affected work and name the exact missing decision.

## Final QA

Review the completed work once using every selected skill.

Verify:

- The confirmed brief was preserved.
- The selected design style and applicable hero choices are visible.
- Canonical Alpy components and tokens were used.
- Responsive behavior is stable.
- Accessibility requirements are preserved.
- Content and media remain meaningful.
- No unsupported design-system decisions were invented.

Report material gaps and verification results concisely.

## Library Design Context

After the mode is confirmed, `get_alpy_library_index` appends the active library's north star, direction, requirements, principles, anti-patterns, and library-specific QA below. Apply this context after brief confirmation and together with the selected skills. `not specified` is an unresolved choice, not permission to invent direction.
