---
name: test-app
description: Run reproducible functional, UI, accessibility, integration and platform-specific checks on websites, PWAs, native Apple, Android or cross-platform projects before handoff.
---

# Test App

1. Read `../../references/testing-and-evidence.md` and `../../templates/evidence-report.md`; inspect scripts and environment capabilities.
2. Select relevant test layers: formatting/typecheck, unit, API/integration, browser E2E, accessibility, visual screenshots, offline/PWA, Swift tests/Xcode UI tests, Android instrumentation/Compose UI tests.
3. Execute real commands where supported. Store command, platform, dependency versions (when relevant), exit code, count and evidence paths. Never infer passing tests from code review.
4. Distinguish PASS, FAIL, NOT RUN, BLOCKED and PARTIAL. For missing credentials or unavailable macOS simulator, mark appropriately and supply exact follow-up steps.
5. Review security separately; prohibit release claims if critical broken flows, data-loss risk, failed security gates or build failure remain. Do not assert that passing tests proves universal correctness.
6. Provide verification matrix, findings, fix/retest ledger, and honest release readiness statement.
