---
name: responsive-accessibility
description: Ensure 3D websites stay usable on mobile, by keyboard, with reduced motion, and when WebGL or assets fail.
---

# Responsive, Accessible, and Fast 3D

Use when planning or reviewing mobile/responsive behavior, accessibility, rendering performance, or fallbacks for a 3D website.

## Checklist

1. Preserve all important pages and content across viewports. Compose a deliberate portrait camera view, reduce background detail where needed, and keep controls reachable with touch targets appropriate to the platform.
2. Keep headings, paragraphs, links, forms, and essential controls in semantic HTML. Give canvas scenes an accessible name or short description, and announce meaningful selection changes without narrating every animation frame.
3. Ensure visible keyboard focus, logical tab order, labeled controls, readable contrast, and keyboard/button alternatives for drag, hover, orbit, and material selection.
4. Respect prefers-reduced-motion and in-app motion controls: stop automatic motion, remove nonessential scroll choreography, and preserve navigation and information.
5. Budget assets and GPU work: compress geometry and textures, reuse materials, limit dynamic lights/shadows/postprocessing, select device-appropriate resolution, pause hidden scenes, and unload inactive resources safely.
6. Show truthful asset loading, retry/error states, and useful feedback. If WebGL or a major asset fails, present a complete 2D experience with equivalent pages, portfolio content, links, and forms; never leave a blank canvas or endless loader.
7. Check for mobile scroll trapping, pointer conflicts, layout shifts, text overlap, reduced-motion regressions, and low-end device performance. Do not claim performance targets without measurements on named devices or a documented test profile.

## Output

Provide the tested viewport/device matrix, accessibility controls, reduced-motion behavior, performance evidence, and fallback status. Record unknown or untested device behavior explicitly.

