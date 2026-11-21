---
name: design-app-flows
description: Design end-to-end product navigation and interface states for dashboards, editors, commerce, onboarding, forms, mobile apps and complex interactive workflows.
---

# Design App Flows

1. Identify the user task, starting context, necessary permissions and completion signal. Map primary and secondary journeys without inventing business features.
2. Create a screen inventory showing entry, normal, empty, loading, offline, permission denied, error, validation, success, retry and recovery states. Use `../../templates/screen-state-inventory.md`.
3. Design accessible navigation, information hierarchy, keyboard/touch interactions, back behavior and persistence. For native apps, respect safe areas, platform tab/nav conventions, state restoration and OS permissions.
4. Define what each interactive control actually does. Label simulated demo state explicitly, never represent placeholder buttons as production flows.
5. Verify the journey at small and large viewports or device sizes, including long labels, dynamic type and one-hand interactions where relevant.
6. Hand off screen/state requirements to platform implementation and QA skills; include user-visible expected outcomes.
