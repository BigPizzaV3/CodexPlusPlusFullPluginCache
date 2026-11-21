---
name: build-android-app
description: Create or improve native Android apps using Kotlin and Jetpack Compose, modern Android navigation, permissions and Material 3 guidance.
---

# Build Android App

1. Read `../../references/android-native.md`, `../../references/platform-choice.md`, and current repo configuration. Keep Gradle, Kotlin and Compose dependencies compatible; verify versions with docs when possible.
2. Use Compose and suitable architecture such as ViewModel and state flows; structure screen UI, navigation, repositories, persistence and network requests. Honor existing framework if established.
3. Follow Material 3 and Android platform conventions, including system bars, predictive back, permissions, adaptive layouts, accessibility semantics and dynamic color where appropriate.
4. Implement real states, retries, background constraints and offline strategy rather than hiding failures behind loading spinners.
5. Build/test with real Android SDK and emulator/device if available. If tools unavailable, deliver exact commands and clearly mark tests unverified.
6. No automatic Play Console publishing, signing key handling or production permission changes.
