---
name: build-ios-app
description: Build, refactor or debug true native iOS applications in Swift and SwiftUI with Apple navigation, persistence, accessibility and Xcode verification.
---

# Build Ios App

1. Read `../../references/apple-native.md`, `../../references/design-quality.md` and `../../references/execution-model.md`. Inspect existing Xcode project, OS target, Swift language mode, dependencies and capabilities; preserve package signing and current state.
2. Prefer SwiftUI for modern native screens and selectively use UIKit bridges when justified. Use native NavigationStack/navigationSplitView, tabs, sheets, presentation detents, dynamic type, accessibility labels and safe areas appropriately. Do not produce web/CSS-style interfaces inside SwiftUI.
3. Design platform-appropriate loading/empty/errors, permission prompts, state restoration, dark appearance and VoiceOver. Respect user-provided screenshots and HIG constraints.
4. Separate views, observable state, persistence/network clients and test seams. Use SwiftData/Core Data/files as appropriate for the project's OS target; do not choose storage solely by trend.
5. For charts, consult `../../references/apple-native.md` and user-provided Swift Charts Examples when licensed/useful; use Swift Charts for meaningful data with accessible descriptions.
6. Build with real Xcode/xcodebuild, run simulator/UI tests and inspect render when Mac tools are present. In Linux-only or no-Xcode environments, label all Apple builds as **unverified**; never fabricate simulator screenshots.
7. Do not promise App Store approval, provisioning or TestFlight distribution without credentials and user authorization.
