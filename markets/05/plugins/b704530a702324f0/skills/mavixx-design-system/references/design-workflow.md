# Design workflow

## Direction selection

Derive direction from product category, audience, task frequency, emotional goal, content density, accessibility needs, and performance constraints. Marketing pages may justify expressive motion; operational tools usually prioritize clarity, speed, and information density.

## Reference handling

Ask for references only when they materially reduce ambiguity. If browsing is allowed, propose suitable sources. Record which principles are adopted and which distinctive brand elements are excluded. Confirm licensing before using third-party fonts, photos, icons, illustrations, or components.

## System definition

Define semantic color roles, type scale, spacing scale, container/grid rules, radii, borders, elevation, component anatomy, interaction states, content tone, image art direction, icon rules, motion timing/easing, breakpoints, focus, contrast, and reduced motion.

Map the specification into the project's existing implementation: CSS custom properties, theme configuration, utility tokens, component variants, or the closest native equivalent. Avoid introducing a parallel styling system when the current one can express the approved direction.

## Implementation order

Implement global tokens and typography first, followed by the application shell and navigation, shared interactive components, repeated content patterns, and then page-level refinements. Keep working behavior and content intact. Verify each shared change on more than one consuming page before removing legacy styles.

## Existing products and verification

Inventory current tokens and repeated patterns. Consolidate gradually. Preserve recognizable brand equity and working flows unless the approved direction replaces them. Run or preview the product and review representative pages and shared component states at desktop and mobile widths with real content, keyboard focus, contrast, overflow, and reduced motion. Correct observed defects and repeat the inspection. A design document or source-only review is not visual verification.
