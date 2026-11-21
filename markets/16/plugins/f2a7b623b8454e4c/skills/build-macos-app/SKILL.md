---
name: build-macos-app
description: Build or improve native macOS apps with SwiftUI and AppKit integrations, multiple windows, keyboard shortcuts, persistence and Xcode tests.
---

# Build Macos App

1. Read `../../references/apple-native.md` and inspect target/architecture before editing.
2. Respect macOS-specific patterns: menus, commands, focus, toolbar, sidebar/split view, multi-window behavior, document handling, drag-and-drop and native keyboard shortcuts. Do not merely enlarge an iPhone layout.
3. Model autosave/retry, document identity, undo/redo, window restoration and resilient persistence when needed. Preserve existing data and filenames by default.
4. Use SwiftUI for primary UI with AppKit where unavoidable. Handle accessibility, keyboard use, dark mode and dynamic resizing.
5. Run xcodebuild/unit/UI tests on supported macOS host. On other platforms provide source and precise unverified test steps rather than a fake build pass.
6. Packaging, signing and notarization require real Apple tooling/credentials and approval.
