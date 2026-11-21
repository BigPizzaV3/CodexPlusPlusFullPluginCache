---
name: prepare-release
description: Prepare tested web/PWA/iOS/Android applications for deployment, store submission or handoff with accurate platform gates, security findings and user approvals.
---

# Prepare Release

1. Read `../../references/release-and-compliance.md` and `../../references/testing-and-evidence.md`. Determine actual target (preview, staging, production, TestFlight, App Store, Play Console, distributable ZIP).
2. Confirm app identifier, version, environments, signing, legal/privacy copy, runtime secrets, data retention, content policy and platform permissions. Do not invent organization identities, privacy policies or store screenshots.
3. Run available build/test/security/accessibility checks and attach evidence. Provide platform-specific blockers (macOS/Xcode for Apple signing, keystore/Android build tools for Android, HTTPS for PWAs, DNS for web).
4. Prepare deployment checklist, release notes, rollback/backup strategy and known issues. Ask for user approval before deploy, public sharing, purchases, external writes or app-store submission.
5. Return a verified release bundle where tools support it; otherwise a clearly labeled release-readiness report, not a false publication claim.
