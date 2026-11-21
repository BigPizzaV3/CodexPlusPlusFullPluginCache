---
name: 3d-scene-architecture
description: Plan a maintainable web architecture for persistent 3D scenes, page content, assets, and graceful rendering fallbacks.
---

# 3D Scene Architecture

Use when designing the technical structure for a 3D website or turning a visual brief into an implementation-ready architecture.

## Process

1. Inspect the existing repository and preserve its framework, package manager, routing, styling, deployment runtime, and test conventions unless the user asks for a migration.
2. Separate semantic routes and content from the renderer, scene registry, camera/animation state, assets, and any server-side preview services. Keep text and essential controls in accessible DOM layers.
3. Recommend a persistent renderer and coordinated camera across sections when the experience benefits from a continuous journey. Use independently loaded scene groups or route-specific scenes where they reduce complexity. Do not require one canvas if the current stack or page behavior makes that unsuitable.
4. Select technologies based on project fit. React Three Fiber/Three.js, a server-rendered React framework, an animation library, and typed state can be useful options, not mandatory requirements. Avoid adding multiple overlapping animation or state systems without a clear need.
5. Define asset loading, compression, texture sizes, material reuse, level of detail, instancing, disposal, visibility pausing, and device-aware rendering. Make loading progress truthful and errors recoverable.
6. Keep public data distinct from secrets. Put service credentials server-side, validate user-supplied URLs, and do not expose tokens or private project data in client bundles.
7. Include route-level rendering behavior, direct deep links, refresh behavior, error boundaries, and a complete semantic 2D fallback for unsupported WebGL, failed assets, or constrained devices.

## Output

Return the project fit and stack rationale, component/scene boundaries, state/data flow, asset strategy, loading/error behavior, and testing requirements. Label unverified runtime or provider assumptions.

