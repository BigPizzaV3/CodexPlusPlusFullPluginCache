---
name: secure-app
description: Assess and harden app authentication, authorization, data privacy, secret handling, API calls, platform permissions and dependency risks.
---

# Secure App

1. Read `../../references/security-and-privacy.md`; identify assets, users, data classification, trust boundaries, external services and relevant abuse cases.
2. Check server-side authZ on every privileged operation (not only hidden UI controls), tenancy/data isolation, token lifecycle, least-privileged scopes, validated untrusted input, safe output, CSRF/CORS/XSS/SSRF risks as applicable and rate limits.
3. For web/PWA review service worker caching, authentication cookies, environment variables, upload handling, dependency advisories and disclosure of third-party telemetry.
4. For native/mobile review permissions, storage (Keychain/Keystore for secrets), deep links, exported components, ATS/network security, package identifiers, mobile signing secrets and release builds.
5. Never request users paste production secrets into chat or embed server tokens in client bundles. Before destructive writes, publishing, payment or external integration, check authorization and approvals.
6. Provide severity, reproduction or supporting evidence, minimal fix and residual risk; never call an unaudited project 'secure'.
