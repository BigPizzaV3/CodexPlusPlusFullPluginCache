---
name: build-pwa
description: Turn an existing web app into a genuine PWA or build a new installable PWA with manifest, service worker strategy, offline behavior and installation testing.
---

# Build Pwa

1. Read `../../references/web-and-pwa.md`; start with the user's web framework and existing content. Explain that PWA installation and capability vary by browser and OS, especially iOS.
2. Implement a valid manifest (name, icons, start URL, display modes), HTTPS deployment expectations and a versioned service worker when needed. Pick a cache strategy per resource class; avoid caching sensitive authenticated data by default.
3. Define offline UX: shell, data that may be cached, unavailable actions, queued writes only when consistency/replay is safe, conflict behavior and user-facing sync status.
4. Test installability with compatible tools/browsers, simulate offline and cache refresh, update flows and version migration. Validate mobile layouts and app icon sizes when assets are available.
5. Do not claim background sync, push, arbitrary file access or install prompt is universally supported. Record platform/browser constraints and actual tests.
6. Return manifest/service worker source, commands, test log and limitations.
