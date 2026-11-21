---
name: 3d-motion-interaction
description: Design natural camera choreography, scroll-linked scenes, and usable interactions for 3D websites.
---

# 3D Motion and Interaction

Use when a website needs camera movement, scroll-driven scenes, object interactions, configurators, or input controls.

## Process

1. Map user journeys before animation. Let visitors navigate directly to important routes and sections without being forced through a cinematic intro.
2. Define camera waypoints and transitions from the route/scene matrix. Use restrained acceleration, deceleration, easing, a stable horizon, sensible exposure changes, and explicit clipping limits.
3. Tie scroll progress to animation without hijacking native scrolling. Keep camera travel bounded, reversible, and robust to resize, fast scrolling, reduced motion, and route changes.
4. Give each interaction a clear purpose and visible state: selected project, material choice, room, gallery item, or control state. Provide keyboard, touch, pointer, and visible button alternatives as appropriate.
5. Provide pause/resume for continuous motion and honor reduced-motion preferences by stopping auto-rotation and removing nonessential camera travel. Preserve all content and core actions in the reduced-motion experience.
6. Keep sound muted unless visitors explicitly enable it. Do not use sudden motion, forced audio, or motion as the only way to reveal essential information.
7. For scene transitions, plan preloading and transition cover using plausible occlusion or light changes only where they are observable and tested. Never claim seamless loading when visible pauses or errors remain.

## Deliverable

Provide a state-and-control map: trigger, camera/object response, user-visible state, keyboard/touch alternative, reduced-motion response, and fallback behavior. State what is scroll-controlled and what remains directly navigable.

