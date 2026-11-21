---
name: create-design-system
description: Create or adapt a consistent, accessible design system for a web, PWA, iOS/macOS or Android app, including tokens, components, typography, spacing and interaction states.
---

# Create Design System

1. Review the existing project's design tokens/components first; preserve its recognizable identity unless redesign is requested.
2. Read `../../references/design-quality.md` and the relevant platform guide: `../../references/web-and-pwa.md`, `../../references/apple-native.md`, or `../../references/android-native.md`.
3. Define semantic color tokens, typography roles, spacing scale, elevation/borders, radius, icon rules, motion duration/easing, responsive breakpoints or adaptive size classes. Design for content and task, not a single fashionable template.
4. List component states (rest, hover where relevant, pressed, focus, disabled, loading, selected, error, success), light/dark and reduced-motion variants.
5. Implement shared components and tokens rather than repeating hardcoded style fragments. Include examples and usage constraints.
6. Verify contrast/focus, touch target sizing, screen-reader labeling, dynamic content, localization and long text. Follow native platform systems when building native apps.
7. Provide code artifacts and before/after screenshots when implementation tools exist; otherwise a design token/spec file and explicit limits.
