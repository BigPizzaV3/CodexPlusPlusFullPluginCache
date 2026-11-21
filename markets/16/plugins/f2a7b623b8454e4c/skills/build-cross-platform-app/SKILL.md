---
name: build-cross-platform-app
description: Build or maintain a shared-codebase iOS and Android app using Expo/React Native or Flutter, preserving platform-specific behavior and release constraints.
---

# Build Cross Platform App

1. Read `../../references/cross-platform.md` and select Expo/React Native vs Flutter based on existing repository, team capabilities, native modules, UX requirements, web needs and performance.
2. Shared core does **not** imply identical screens. Respect iOS navigation/safe areas and Android back navigation/system UI/Material conventions; use platform-specific components when warranted.
3. Implement coherent navigation, forms, offline/persistence model, accessibility and error states. Do not claim Web, Android and iOS functionality tested because one platform builds.
4. Separate app state, network/adapters and platform permissions; audit third-party native packages, build plugins and secrets.
5. Run available platform tests/builds separately; for iOS signing/simulators require macOS/Apple tooling, Android builds require proper SDK. Clearly mark unrun platforms.
6. Provide actual source, setup instructions, dependency versions, proof of builds and remaining platform risks; request approval for EAS/App Store/Play publishing.
