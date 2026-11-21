# Testing and evidence standard

Statuses: **PASS** (command actually ran and passed), **FAIL**, **PARTIAL**, **BLOCKED**, **NOT RUN**. 'Code looks correct' is not PASS.

## Evidence per task
- Platform/device/runtime/dependencies; exact commands, exit codes and meaningful output; artifact paths and timestamp if available.
- Code build/type/lint, unit, integration, UI E2E, accessibility and visual checks by platform. Report omitted layers.
- For visual QA: screenshot source/reference, rendering viewport/device, compared elements, actual mismatches and fixes. Don't invent screenshot paths.
- Web: browser navigation, keyboard focus, responsive widths, real click flows; PWA offline/install/update behavior.
- iOS/macOS: Xcode build, unit/UI/simulator on Mac; if unavailable mark NOT RUN with exact reason.
- Android: gradle unit tests and instrumented UI tests when SDK/emulator available.
- Cross-platform: evidence for each shipped target. A web preview doesn't validate native.
- Security: authZ, token leaks, data isolation, dependency issues, destructive operations and permission checks.

## Release gate
No release-ready statement with failed required builds, critical authorization problems, data-loss defects, or missing essential main flow. Link work to evidence and disclose limitations. Independent reviewer reports are only independent if executed separately.
