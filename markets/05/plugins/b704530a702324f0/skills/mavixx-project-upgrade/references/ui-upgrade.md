# Existing UI upgrade protocol

Use this protocol when the requested project has a user-facing website or application interface.

## Capture the current product

Run the existing app with its documented command. Inspect representative routes and shared states before editing. At minimum, review one primary page and any changed flow at desktop and mobile widths. Note hierarchy, navigation, typography, color and contrast, spacing, responsive behavior, overflow, interaction feedback, loading, empty, success, error, disabled, and focus states. Keep observed functional defects separate from visual preferences.

If the app cannot run because of a pre-existing issue, diagnose and repair that issue when it is within scope. Otherwise record the blocker and continue with source-level work that can be verified safely. Never claim visual completion without a rendered inspection.

## Choose a coherent direction

Use approved brand assets and explicit user references first, then established product patterns. When the user has authorized an upgrade but supplied no visual reference, recommend one direction derived from the product, audience, content density, and current brand, then proceed with reversible implementation. Offer multiple directions only when the choice would materially change cost or product identity, or when the user asks to compare concepts.

## Implement foundations before decoration

1. Consolidate semantic color, type, spacing, container, radius, border, elevation, and motion tokens in the project's existing styling system.
2. Repair the application shell, navigation, responsive structure, page hierarchy, and common layouts.
3. Upgrade shared buttons, links, forms, cards, tables, feedback, overlays, and their interactive states.
4. Apply the system to representative pages and then every page in the authorized scope. Remove one-off styles only when replacement is verified.
5. Preserve real content, routes, forms, data states, authentication, analytics, and accessibility semantics. Do not substitute fake interactions or static mock data for working behavior.

## Render, interact, correct

After each material phase, reload the running app and inspect changed routes at wide and narrow widths. Exercise navigation and the primary action. Correct overflow, clipping, density, contrast, focus, hover, active, disabled, loading, error, empty, and success states. Respect reduced motion and avoid animation that harms task completion or performance.

UI work is complete only when the new system exists in source code, the changed routes render successfully, important interactions still work, desktop and mobile states have been inspected, and relevant quality checks pass or remaining pre-existing failures are explicitly separated.
