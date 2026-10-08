---
name: compose-ui-theme
description: Compose a coherent application or website color theme from seed colors, an existing palette, a product brief, or light/dark-mode requirements. Use for UI surfaces, text hierarchy, controls, focus states, borders, and semantic feedback colors. Do not use for brand identity alone, interior spaces, or code-only token formatting without theme design.
---

# Compose a UI theme

## Define the interface context

- Determine product type, light or dark mode, density, emotional tone, seed colors, and critical components.
- Preserve explicit brand colors, but distinguish brand expression from colors suitable for text, surfaces, and interaction states.

## Compose the hierarchy

1. Start with canvas, surface, elevated surface, and border values that create clear depth without excessive contrast.
2. Assign primary, secondary, and muted text colors for readable hierarchy.
3. Define action colors and their hover, active, disabled, and focus treatments. Do not encode state through color alone when offering implementation advice.
4. Add success, warning, error, and informational colors only when relevant; keep them distinguishable from the main action color.
5. For dark themes, avoid pure black expanses and over-saturated large surfaces unless the brief calls for them. For light themes, avoid borders too faint to communicate structure.
6. Evaluate likely foreground/background pairings. Clearly label uncalculated contrast as needing verification rather than claiming compliance.
7. Keep the visible editable palette manageable, normally eight to twelve representative colors; describe derived interaction variants separately if necessary.

## Deliver

- Summarize the theme direction and map every displayed color to a UI role.
- Invoke `palette-picker` with representative uppercase `#RRGGBB` colors and a `reason` identifying mode and product context.
- If implementation output is requested, provide semantic mappings after the palette and keep them synchronized with its values.

