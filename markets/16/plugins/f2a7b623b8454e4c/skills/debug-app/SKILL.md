---
name: debug-app
description: Diagnose and fix actual web, PWA, SwiftUI, macOS, Android or React Native crashes, broken UI, build errors and app state bugs.
---

# Debug App

1. Inspect user's logs, reproduction steps, versions, OS/browser, recent changes and repository. Reproduce failure when tools allow; do not assume the first plausible explanation is the cause.
2. Narrow to minimal failing scenario, instrument safely, and capture baseline command and error. Avoid logging secrets, tokens or user data.
3. Determine root cause and implement smallest justified patch. Keep unrelated behavior unchanged and add a regression check.
4. Run focused test, typecheck/build, then broader related checks; for UI defects inspect relevant viewport/device and expected state.
5. Report reproduction evidence, changed files, test output, and remaining caveats. When environment blocks reproduction, state hypothesis as unverified.
