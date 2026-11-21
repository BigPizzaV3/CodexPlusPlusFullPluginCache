# Release handoff gates

Web: correct environment, production build/test, HTTPS/domain handling, auth/cookies, logs, monitoring, rollback and privacy disclosure.
PWA: manifest, icons, service worker cache, offline/update test, platform installation caveats, secure cache/privacy model.
iOS/macOS: Xcode archive, bundle identifier, provisioning profiles, entitlements, app privacy labels, screenshots, accessibility, signing, TestFlight/App Store or notarization as applicable. Require genuine Apple account credentials and approval; don't claim approvals.
Android: Android App Bundle/APK release variant, package identifier, key management, target SDK policy, privacy/data safety declaration, permissions, Play Console approval and staged rollout as appropriate.
Cross-platform: release evidence per target, dependency/native-module audit and install test on each platform.
General: user-approved deployment; change log; licensing of reused code/assets; legal/privacy text is user-owned, not invented; smoke test and rollback plan; security/QA gates all explicitly reported.

Plugin authorship vs app release is different: this builder's OpenAI plugin listing has its own review process documented at https://developers.openai.com/plugins/deploy/submission .
