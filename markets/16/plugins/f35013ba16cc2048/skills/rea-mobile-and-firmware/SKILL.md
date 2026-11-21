---
name: rea-mobile-and-firmware
description: Route authorized Android APK or firmware investigations to REA's static inspection and extraction workflows, with platform prerequisites and safe output handling.
---

# Android and firmware

## Android APK

- For archive/member inventory, use the general package route; for manifest, classes, methods, or references, use `inspect_android_package` and only advertised focused tools.
- Verify host prerequisites: upstream documents headless JADX and a full JDK for Linux/macOS; exact support varies by release.
- Separate manifest declarations, decompiled code, and inferred behavior. Static APK analysis does not establish device/runtime behavior.
- Do not install or launch the APK, access its services, or bypass signature/account/DRM controls unless the user explicitly authorizes a lawful test in a controlled scope.

## Firmware

- Use `inspect_firmware_regions` first when available. Request extraction only when the user explicitly needs it, using a caller-selected new absolute output directory.
- Upstream documents caller-supplied Binwalk/Unblob on Linux; don't install tools or write to a guessed directory.
- Treat extracted files as untrusted. Avoid launching binaries. Report format recognition/extraction boundaries and resource limits.
- Do not probe or exploit devices on a network. Keep firmware analysis offline unless the user authorizes a specific test device and action.

If required tools are absent, report the missing prerequisite and offer a static/manual alternative; do not fabricate analysis results.
